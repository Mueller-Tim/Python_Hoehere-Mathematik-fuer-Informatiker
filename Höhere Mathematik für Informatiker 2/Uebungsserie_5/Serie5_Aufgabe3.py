import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import CubicSpline

##a)

t = np.array([1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000,2010])
pt = np.array([75.995,91.972,105.711,123.203,131.669,150.697,179.323,203.212,226.505,249.633,281.422,308.745])

tt = np.arange(1900, 2010+0.1,0.1)

def spline_interpolation(x,y,xx):
    n = len(x) - 1
    a = np.zeros(n)
    b = np.zeros(n)
    c = np.zeros(n+1)
    d = np.zeros(n)
    h = np.zeros(n)




    for i in range(n):
        a[i] = y[i]
        h[i] = x[i+1] - x[i]


    c[0] = 0
    c[n] = 0
    A = np.zeros((n-1, n-1))

    for i in range(n-1): #0,1
        A[i,i] = 2 * (h[i] + h[i+1])
        if i != 0:
            A[i,i-1] = h[i]
        if i < n-2:
            A[i,i+1] = h[i+1]
    z = np.zeros((n-1,1))

    for i in range(z.size):
        z[i] = ((3 * (y[i+2]-y[i+1]) / h[i+1]) - (3 * (y[i+1]-y[i]) / h[i]))


    c_vec = np.linalg.solve(A,z)

    for i in range(len(c_vec)):
        c[i+1] = c_vec[i,0]


    for i in range(n):
        b[i] = (y[i+1]-y[i]) / h[i] - (h[i] / 3) * (c[i+1] + 2 * c[i])
        d[i] = (1/(3 * h[i])) * (c[i+1]-c[i])

    yy = np.zeros(xx.shape)
    for i in range(0,n):
        idx, = np.where((xx >= x[i]) & (xx <= x[i+1]))
        dx = xx[idx] - x[i]
        yy[idx] = a[i] + dx * b[i] + c[i] * dx ** 2 + d[i] * dx**3

    return yy


ptt = spline_interpolation(t,pt,tt)

plt.figure(0)
plt.scatter(t,pt, label="Stützpunkte", color="red")
plt.plot(tt,ptt, label="kubische Splinefunktion")
plt.title("Meine Rechung")



##b)
cs = CubicSpline(t,pt)
plt.figure(1)
plt.scatter(t,pt, label="Stützpunkte", color="red")
plt.plot(tt,cs(tt), label="kubische Splinefunktion")
plt.title("Pyton CubicSpline Rechung")

'''
Aufgabe a und b sehen sehr ähnlich aus
'''

##c)

coefficients = np.polyfit(t,pt,11)

plt.figure(2)
plt.scatter(t,pt, label="Stützpunkte", color="red")
plt.plot(tt,np.polyval(coefficients, tt), label="kubische Splinefunktion")
plt.title("Pyton polyfit und polyval Rechung")
plt.show()

'''
Polynom 11 grades da es 12 Stützpunkte sind

Im Gegensatz zu a und b geht die funktion nicht durch alle Punkte
Dafür würde sie genauer für neue testobjekte sind.
'''



