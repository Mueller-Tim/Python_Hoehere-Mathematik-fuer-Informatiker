import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**5 - 5 * x**4 - 30 * x**3 + 110 * x**2 + 29 * x - 105

def df(x):
    return 5 * x**4 - 20 * x**3 - 90 * x ** 2 + 220 * x + 29

def F(x):
    return (1/6) * x**6 - x**5 - 30/4 * x**4 + 110/3 * x**3 + 29/2 * x**2 - 105 * x

x = np.arange(-10, 10.01, 0.01, dtype = 'float64')

plt.plot(x, f(x), x, df(x), x, F(x))
plt.xlim(-10, 10)
plt.ylim(-1500, 1500)

plt.legend(['Polynom f(x)', 'Ableitung', 'Stammfunktion'])
plt.title('Darstellung eines Polynoms, der Ableitung und der Stammfunktion')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()