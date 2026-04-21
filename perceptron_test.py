import torch
import torch.nn as nn

model = nn.Linear(2, 1)

x1 = torch.tensor([[1.0, 2.0]])
x2 = torch.tensor([[3.0, 4.0]])

print(model(x1))
print(model(x2))


print(model.weight)
print(model.bias)
