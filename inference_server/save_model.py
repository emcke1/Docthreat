import torch
from uniform_classifier import UniformClassifier

# Create the model instance
model = UniformClassifier()

# Save the state dictionary (random weights)
torch.save(model.state_dict(), "uniform_classifier.pt")

print("✅ Model saved as uniform_classifier.pt")

