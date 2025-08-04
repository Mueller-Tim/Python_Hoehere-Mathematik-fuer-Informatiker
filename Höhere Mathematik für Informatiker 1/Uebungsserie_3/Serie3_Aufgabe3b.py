import math

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0001, 100.01, 0.01)
f = 5/((2 * x ** 2)**(1/3))
plt.figure(1)
plt.loglog(x,f)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()

g = 10**5 * 2 * 10**(-x/100)
plt.figure(2)
plt.semilogy(x, g)
plt.xlabel("x")
plt.ylabel("g(x)")
plt.grid()
plt.show()

h = ((10)**(2*x)/(2**(5*x))**2)
plt.figure(2)
plt.semilogy(x, h)
plt.xlabel("x")
plt.ylabel("h(x)")
plt.grid()
plt.show()