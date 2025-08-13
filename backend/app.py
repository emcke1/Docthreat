from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend is running."

@app.route("/analyze", methods=["POST"])
def analyze_image():
    image = request.files.get("image")
    if not image:
        return jsonify({"error": "No image uploaded"}), 400

    try:
        response = requests.post("http://127.0.0.1:5000/uniform", files={"image": image})
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=7000, debug=True)
