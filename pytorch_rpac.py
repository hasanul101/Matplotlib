
import torch.nn as nn
import torch
import numpy as np
import pandas as pd

# 20 samples, 10 genes
np.random.seed(42)
data = np.random.randint(100, 1000, (20, 10))

df = pd.DataFrame(data, columns=[f"Gene_{i}" for i in range(10)])

print(df.head())

# Mean expression per sample
df["mean_expr"] = df.mean(axis=1)

# Create binary labels
df["label"] = (df["mean_expr"] > 500).astype(int)

print(df[["mean_expr", "label"]].head())


X = torch.tensor(df.iloc[:, 0:10].values, dtype=torch.float32)
y = torch.tensor(df["label"].values, dtype=torch.float32).unsqueeze(1)

print(X.shape)  # (20, 10)
print(y.shape)  # (20, 1)


class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(10, 5)  # input → hidden
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(5, 1)   # hidden → output
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.sigmoid(x)
        return x


model = SimpleNN()
print(model)


criterion = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

epochs = 100

for epoch in range(epochs):
    outputs = model(X)
    loss = criterion(outputs, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

with torch.no_grad():
    preds = model(X)
    predicted = (preds > 0.5).int()

print("Predictions:\n", predicted.squeeze())
print("Actual:\n", y.squeeze())
