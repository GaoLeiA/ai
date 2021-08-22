import torch
from torch import nn
net = nn.Sequential(
    nn.Conv2d(1,96,kernel_size=11, stride=4,padding=1),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=3, stride=2),
    
    )
print(net.cpu)