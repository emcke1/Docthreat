import ssl_patch  # auto-sets SSL_CERT_FILE for you
import torch
import torchvision.transforms as T
from PIL import Image
from flask import Flask, request, jsonify
from flask_cors import CORS  # for cross-origin requests
from uniform_classifier import UniformClassifier
from blip_model import generate_caption  # only if you’re using BLIP


app = Flask(__name__)
CORS(app)

# ─── Instantiate & load weights ───────────────────────────────────────────────
model = UniformClassifier()
model.load_state_dict(torch.load("uniform_classifier.pt"))
model.eval()

# ─── Image preprocessing ────────────────────────────────────────────────────
transform = T.Compose([
    T.Resize((224, 224)),
    T.ToTensor()
])

# ─── Uniform classification endpoint ─────────────────────────────────────────
@app.route("/uniform", methods=["POST"])
def classify_uniform():
    file = request.files["image"]
    image = Image.open(file).convert("RGB")
    img_tensor = transform(image).unsqueeze(0)  # add batch dim

    with torch.no_grad():
        output = model(img_tensor)
        _,pred = torch.max(output, dim=1)
        class_map = {0: "Civilian", 1: "Military", 2: "Emergency"}
        label = class_map[pred.item()]

    return jsonify({ "uniform_class": label })

# ─── Image captioning endpoint (BLIP) ────────────────────────────────────────
@app.route("/caption", methods=["POST"])
def caption_image():
    file = request.files["image"]
    image = Image.open(file).convert("RGB")
    caption = generate_caption(image)
    return jsonify({ "caption": caption })

if __name__ == "__main__":
    app.run(debug=True)
