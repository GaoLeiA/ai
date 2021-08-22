import torch

x = torch.arange(4.0)
print(x)
x.requires_grad_(True)  # µÈ¼ÛÓÚ `x = torch.arange(4.0, requires_grad=True)`
