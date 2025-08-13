def detect_weapons(image_url):
    return {
        "detections": [{
            "label": "rifle",
            "confidence": 0.91,
            "bounding_box": [120, 80, 230, 200],
            "proximity": 2.1
        }]
    }
