import torch
import torch.nn as nn
import torch.optim as optim
from model import MLQSTModel

def train_model(X, y, epochs=100, lr=0.001):

    model = MLQSTModel(X.shape[1], y.shape[1])
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    for epoch in range(epochs):
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()

        if epoch % 10 == 0:
            print(f"Epoch {epoch}, Loss: {loss.item()}")

    return model

