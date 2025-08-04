import math

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return math.e ** (x ** 2) + x ** (-3) - 10

def fab(x):
    return 2*x*math.e ** (x**2) - 3 * x ** (-4)

def newton(x):
    return x - f(x) / fab(x)

def easyNewton(x, x0):
    return x - f(x) / fab(x0)

def sekanten(xn, xn_1):
    return xn - (xn - xn_1) / (f(xn) - f(xn_1)) * f(xn)

x = np.arange(-3, 3.01, 0.01)

plt.ylim(-10,10)

plt.plot(x, f(x))

plt.legend(["f(x)"])
plt.title("Darstellung von einer Funktionen")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

#newton
x0 = 2
xn = x0
n = 0
while n < 4:
    xn = newton(xn)
    print("Newtonverfahren: x" + str(n+1) + " = " + str(xn))
    n += 1


#vereinfacht newton
x0 = 0.5
xn = x0
n = 0
while n < 4:
    xn = easyNewton(xn, x0)
    print("Vereinfachtes Newtonverfahren: x" + str(n+1) + " = " + str(xn))
    n += 1


#sekanten

x0 = -1.0
x1 = -1.2
xn = x1
xn_1 = x0
n = 0
while n < 3:
    xtemp = sekanten(xn, xn_1)
    xn_1 = xn
    xn = xtemp
    print("Sekantenverfahren: x" + str(n+2) + " = " + str(xn))
    n += 1