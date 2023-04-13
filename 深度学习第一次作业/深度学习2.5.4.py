import torch

def f(a, x):
    if x<=0:
        b=torch.sqrt(a)
    else:
        b=torch.square(a)
    return b

a = torch.randn(size=(), requires_grad=True)
c = f(a,1)
c.backward()

a.grad == c / a

print(a.grad)
