'''
kubische Splinefunktion S(x)
'''
import matplotlib.pyplot as plt
import numpy as np

'''
x = Vektor mit den (n + 1) gegebenen Stützstellen (aufsteigend sortiert)
y = analoge Vektor mit den bekannten Stützwerten
xx = Vektor mit defnierten Werten
'''
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

'''
Test mit Daten von Aufgabe 1
'''

x = np.array([4,6,8,10]).T
y = np.array([6,3,9,0]).T
xx = np.arange(x[0],x[-1]+0.1, 0.1)

yy = spline_interpolation(x,y,xx)

plt.scatter(x,y, label="Stützpunkte", color="red")
plt.plot(xx,yy, label="kubische Splinefunktion")
plt.show()
