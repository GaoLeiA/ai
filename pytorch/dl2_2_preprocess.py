import torch
import torchvision
from torch import nn
from d2l import torch as d2l
import os, sys

#print("当前工作目录 : %s",os.path.split(os.path.realpath(__file__))[0])

x = torch.arange(4)
x[3]
len(x)
x.shape
A = torch.arange(20).reshape(5, 4)
B= torch.arange(20).reshape(4, 5)

print(torch.mm(A, B))
u = torch.tensor([3.0, -4.0])
print(torch.norm(u))