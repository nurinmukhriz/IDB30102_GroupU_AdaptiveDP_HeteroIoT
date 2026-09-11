import torch.nn as nn


# Step 1: Define the IoT classification model
class IoTClassifier(nn.Module):

    # Step 2: Define the model layers
    def __init__(self, input_size, num_classes):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(input_size, 64),
            nn.ReLU(),
            nn.Linear(64, num_classes)
        )

    # Step 3: Define the forward pass
    def forward(self, x):
        return self.network(x)
