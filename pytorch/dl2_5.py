import torch

x = torch.arange(4.0)
print(x)
x.requires_grad_(True)  # �ȼ��� `x = torch.arange(4.0, requires_grad=True)`
