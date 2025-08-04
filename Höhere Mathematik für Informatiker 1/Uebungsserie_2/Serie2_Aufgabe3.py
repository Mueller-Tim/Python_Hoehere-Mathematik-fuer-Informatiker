import math

import matplotlib.pyplot as plt
import numpy as np


##a)

s = 1
n = 6


number_of_rotation = 28

##a)
def s2n(s):
    return np.sqrt(2-2*np.sqrt(1-((s**2)/4)))

x = [n]
fxa = [s * n]

for value in range(number_of_rotation):
    s = s2n(s)
    n = n * 2
    x = np.append(x, n)
    fxa = np.append(fxa, n * s)


#plt.xlim(6, 80)
plt.plot(x, fxa)
plt.xlabel("2n")
plt.ylabel("2n * s2n")
plt.xscale('log')
plt.title("Anäherung des n-Vielecken an einen Kreis (2PI)")
plt.grid()
plt.show()


'''
Zeigt bei hohen Werten ein starkes Ansteigen und anschließendes starkes Abfallen in den Berechnungen.
Dieses Verhalten tritt auf, weil die Berechnung in der Nähe von 1 aufgrund des Verlusts von Genauigkeit in der 
Maschinengenauigkeit eps ungenau wird.
Es basiert auf mathematischen Operationen, die zur Genauigkeitsverschlechterung führen.


'''

##b)

def s2nV2(s):
    return math.sqrt(s**2/(2*(1+math.sqrt(1-(s**2/4)))))

s = 1
n = 6

fxb = [s * n]

for value in range(number_of_rotation):
    s = s2nV2(s)
    n = n * 2
    fxb = np.append(fxb, n * s)



plt.plot(x, fxb)
plt.xlabel("2n")
plt.ylabel("2n * s2n2")
plt.title("Anäherung des n-Vielecken an einen Kreis (2PI)")
plt.xscale('log')
plt.grid()
plt.show()

'''
Zeigt ein stabileres Verhalten und vermeidet das starke Ansteigen und Abfallen der Berechnungen bei hohen Werten.
Dies wird durch eine geschickte Umformulierung der Berechnung erreicht, die den Verlust von Genauigkeit minimiert und 
die Maschinengenauigkeit besser berücksichtigt.
Es umgeht mathematische Operationen, die zur Genauigkeitsverschlechterung führen.
'''

