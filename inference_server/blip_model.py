import os
import certifi
os.environ["SSL_CERT_FILE"] = certifi.where()  # Ensure certs are trusted

from PIL import Image
import requests
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load the BLIP model and processor from Hugging Face (with SSL fix)
MODEL_ID = "Salesforce/blip-image-captioning-base"

processor = BlipProcessor.from_pretrained(MODEL_ID)
model = BlipForConditionalGeneration.from_pretrained(MODEL_ID)
model.eval()

def generate_caption(image):
    """
    Accepts a PIL Image and returns the generated caption string.
    """
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        out = mod
