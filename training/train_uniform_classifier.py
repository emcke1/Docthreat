import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from inference_server.uniform_classifier import UniformClassifier

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms

# 1. Data preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# 2. Simulated training data
train_dataset = datasets.FakeData(transform=transform, size=1000, num_classes=3)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=32, shuffle=True)

# 3. Initialize model, loss, optimizer
model = UniformClassifier()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 4. Training loop
for epoch in range(5):
    for images, labels in train_loader:
        outputs = model(images)
        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f"✅ Epoch {epoch+1}, Loss: {loss.item():.4f}")

# 5. Save the entire model (so no mismatches later)
torch.save(model.state_dict(), "inference_server/uniform_classifier.pt")
print("✅ Model saved to inference-server/uniform_classifier.pt")
