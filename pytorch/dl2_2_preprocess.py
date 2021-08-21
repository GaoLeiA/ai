import torch
import torchvision
from torch import nn
from d2l import torch as d2l
import os, sys

import numpy as np
from keras.datasets import mnist
(X_train,y_train),(X_test,y_test) = mnist.load_data()
from matplotlib import pyplot as plt
plt.imshow(X_train[0])
plt.show()
plt.imshow(X_train[1])
plt.show()

