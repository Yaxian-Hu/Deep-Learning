import torch
a = torch.arange(3).reshape((3, 1, 1))
b = torch.arange(4).reshape((1, 2, 2))
print(a,b)

print(a + b)

print((a + b).shape)

print((a + b).numel())
