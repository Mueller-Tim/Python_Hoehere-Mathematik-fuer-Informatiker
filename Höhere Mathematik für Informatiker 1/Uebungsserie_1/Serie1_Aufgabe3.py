'''
y = fact_rec(n) berechnet die Fakultät von n als fact_rec(n) = n * fact_rec(n -1) mit fact_rec(0) = 1
# Fehler, falls n < 0 oder nicht ganzzahlig
'''
import timeit
import math

import numpy as np

def fact_rec(n):
    if n < 0 or np.trunc(n) != n:
        raise Exception('The factorial is defined only for positive integers')
    if n <=1:
        return 1
    else:
        return n*fact_rec(n-1)


def fact_for(n):
    if n < 0 or np.trunc(n) != n:
        raise Exception('The factorial is defined only for positive integers')

    number = 1

    for i in range(1, n+1):
        number *= i

    return number


t1 = timeit.repeat("fact_rec(500)", "from __main__ import fact_rec", number=100)
average_t1 = sum(t1)/len(t1)

print("Time for the recursive formula: " + str(average_t1))


t2 = timeit.repeat("fact_for(500)", "from __main__ import fact_for", number=100)
average_t2 = sum(t2)/len(t2)
print("Time for the direct formula: " + str(average_t2))

if(average_t1 < average_t2):
    print("The recurve formula is faster than the direct formula with the factor: ", average_t2/average_t1)
elif(average_t1 > average_t2):
    print("The recurve formula is slower than the direct formula with the factor: ", average_t2/average_t1)
else:
    print("The recurve formula is as fast as the direct formula.")


for n in range(190, 201):
    result = fact_for(n)
    print(f"{n}! = {result}")

for n in range(170, 172):
    result = fact_for(n)
    result_float = float(result)
    print(f"{n}! = {result_float}")

'''
Die direkte Formel ist 10 mal schneller als die rekursive Formel,
da die rekursive Formel sich immer wieder aufrufen muss, dies braucht Zeit.
Bei der direkten Formel wird immer in der gleichen Schlaufe gerechnet.


Es gibt eine Obergrenzen, beim Typ 'float' ist dieser bei 171 erreicht. Es gibt einen
OverflowError. Bei integer ist dies mit 201 noch nicht erreicht.

'''