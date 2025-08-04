import numpy as np

"""
Input:
- a ist ein Array mit den Koeffizienten in absteigender Riehenfolgen
- xmin ist das untere Intervall-Limit
- xmax ist dsd obere Intervall-Limit.

Output:
- x ist ein Array mit den x-Werten im Intervall (xmin zu xmax)
- p ist ein Array mit den Funktionswerten des Polynoms
- dp ist ein Array mit den Y-Werten der Ableitung des Polynoms
- pint ist ein Array mit den Y-Werten der Stammfunktion des Polynoms
"""

def polynom(a, xmin, xmax):

    if np.shape(a)[0] == 0 or len(np.shape(a)) > 1 and np.shape(a)[1]:
        raise Exception('Input a must be a row or column vector')

    step = np.abs(xmax- xmin) / 10000
    x = np.arange(xmin,xmax, step, dtype= 'float64')

    n = len(a)-1
    p = 0
    dp = 0
    pint = 0
    for i in range(n+1):
        p = p + a[i] * x ** (n-i)
        dp = dp + a[i] * (n-i) * x ** (n-i-1)
        pint = pint + a[i]/(n-i+1) * x ** (n-i+1)

    return (x, p, dp, pint)
