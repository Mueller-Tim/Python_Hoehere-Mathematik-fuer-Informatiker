## a)
import matplotlib.pyplot as plt
import numpy as np


def f1(x):
    return x**7 - 14*x**6 + 84*x**5 - 280*x**4 + 560*x**3 - 672*x**2 + 448*x - 128


def f2(x):
    return (x-2)**7


x = np.arange(1.99, 2.01004, 0.00004)

plt.plot(x, f1(x), x, f2(x))

plt.xlim(1.99, 2.01)

plt.legend(["f1", "f2"])
plt.title("Darstellung von zwei analytische gleichen Funktionen")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

'''
Auslöschung führt bei f1 dazu, dass Werte ungleich 0 berechnet werden schlechte Konditionierung der Subtraktion). 
Dagegen wird f2 nummerisch stabiler berechnet
'''

## b)
limit = 1e-14
stepwidth = 1e-17
x = np.arange(-limit, limit, stepwidth)

def g(x):
    return x / (np.sin(1+x)-np.sin(1))
plt.plot(x, g(x))
plt.xlabel('x')
plt.ylabel('g(x)')
plt.show()

'''
Offensichtlich ist die nummerische Berechnung von g(x) für x nahe bei 0
nicht stabil. Auslöschung im Nenner führt dazu, dass die Berechnung des Bruches
x -> 0 fast beliebig grosse Werte annehmen kann.
'''

## c)

def gNew(x):
    return x /(2*np.cos(1+x/2)*np.sin(x/2))

plt.plot(x, g(x), x, gNew(x))
plt.xlabel('x')
plt.ylabel('g_{new}(x)')
plt.show()

'''
Offensichtlich ist die numerische Berechnung von gNew(x) für x nahe bei
0 stabel, d.h. der Grenzwert für x -> 0 ist 1.8508. Durch die Umformung
des Nenners werden keine fast gleiche grosse Zahlen voneinander subtrahiert, also
findet auch keine Auslöschung mehr statt.
'''