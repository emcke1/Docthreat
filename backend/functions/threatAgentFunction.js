const axios = require("axios");

module.exports = async (req, res) => {
  try {
    const imageUrl = req.body.imageUrl;

    const [yolo, blip, uniform] = await Promise.all([
      axios.post("http://localhost:5000/yolo", { imageUrl }),
      axios.post("http://localhost:5000/blip", { imageUrl }),
      axios.post("http://localhost:5000/uniform", { imageUrl }),
    ]);

    res.json({
      threatScore: "HIGH",
      alertMessage: "Armed individual in military clothing detected near a casualty.",
      detections: yolo.data.detections,
      uniformClass: uniform.data.uniform_class,
      languageExplanation: blip.data.caption,
      timestamp: new Date().toISOString()
    });
  } catch (err) {
    console.error(err);
    res.status(500).send("Error analyzing threat.");
  }
};
