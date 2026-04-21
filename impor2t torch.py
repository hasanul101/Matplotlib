import torch
import torch.nn as nn

model = nn.Linear(2,1)

x = torch.tensor([[1.0,2.0]])
y = model(x)

print(y)