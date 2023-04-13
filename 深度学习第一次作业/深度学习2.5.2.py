import torch

x = torch.arange(4.0)
x.requires_grad_(True)
x.grad
y = 2 * torch.dot(x, x)
y.backward()
x.grad
y.backward()
