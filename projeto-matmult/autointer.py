import math as m
import numpy as np

def f(b, k):
    return (-14 * m.cos(((-2*m.pi * k)/10) * m.sin(b/2)) - (6 * m.cos(3*((-2*m.pi*k)/5)) * m.sin(3*b)))

valores_k = [-1, -2, -3, -4, -5]

intervalo_t = np.arange(0,2*m.pi,0.0001)

tol = 0.001

inter = []

for b in intervalo_t:
    for k in valores_k:
        func = f(b,k)
        if (func == 0) or (func <= 0 + tol and func >= 0 - tol):
            y = ((-2*m.pi*k/5) - b) / 2
            x = (-2*m.pi*k/5) - y

            if x != y:
                inter.append([x,y])


for valor in inter:
    print(valor)
