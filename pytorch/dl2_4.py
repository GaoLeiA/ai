import numpy as np
from IPython import display
from d2l import torch as d2l


def f(x):
    return 3 * x ** 2 - 4 * x

def numerical_lim(f, x, h):
    return (f(x+h) - f(x))/h
h = 0.1 
for i in range(5):
    print(f'h={h:.5f}, numerical limit = {numerical_lim(f,1,h):.5f}')
    h *= 0.1

def set_figszie(figsize=(3.5, 2.5)):
    use_svg_display()
    d21.plt.rcParams['figure.figsize'] = figsize
x = np.arange(0, 3, 0.1)
d2l.plt.plot(x, [f(x), 2 * x - 3], 'x', 'f(x)', legend=['f(x)', 'Tangent line (x=1)'])
