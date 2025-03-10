import math
import numpy as np
def cost(x):
    return (2 * np.expm1(x) - 2/np.expm1(x))*(2 * np.expm1(x) - 2/np.expm1(x))

def grad(x):
    return 2*(2* np.expm1(x) - 2/np.expm1(x))*(2 * np.expm1(x) + 2/np.expm1(x))

def myGD1(alpha, x0, gra=1e-3, loop=5000):
    x = [x0]
    for i in range(loop):
        x_new = x[-1] - alpha*grad(x[-1])
        if abs(grad(x_new)) < gra:
            break
        x.append(x_new)
    return (x, i)

(x1, it1) = myGD1(0.01, -1)
print('Solution x1 = %f, cost = %f, obtained after %d iterations' %
(x1[-1], cost(x1[-1]), it1))