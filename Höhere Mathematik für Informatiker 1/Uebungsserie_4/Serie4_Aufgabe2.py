##a)
import matplotlib.pyplot as plt
import numpy as np

'''
Aufgabe 2a)
Wir haben anziehende Fixpunkte für 0<alpha<=3 ('monotone' Kon... 1<alpha<=2).
Für alpha > 3 haben wir keine Fixpunkte mehr und zunehmend chatoischs verhalten.
'''

start = 0.1
nit = 100000
amin = 0.25
amax = 4
step = 0.25
fig = 1

k = np.zeros(nit + 1)
alpha = np.arange(amin, amax+0.25, 0.25)

for a in alpha:
    k[0] = start
    for j in np.arange(0,nit):
        k[j+1] = a * k[j] * (1-k[j])
    plt.figure(fig)
    plt.semilogx(k)
    plt.title('Alpha = ' + str(a))
    plt.xlabel('Number of Iterations')
    plt.ylabel('Iteration value')
    fig += 1
    plt.grid()
    plt.show()


'''
Aufgabe 2b)
Der Fixpunkt entspricht dem (im Unendlichen) konstanten Anteil kranker
Kinder für ein vorgegebens apha für 1<alpha<3
'''

'''
Aufgabe 2c)
Aus der Fixpunktgleichung x = alpha * x * (1-x) folgt durch Auflösung nach
alpha direkt apha = 1/(1-x) bzw. x = (alpha-1)/alpha
'''