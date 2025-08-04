import matplotlib.pyplot as plt
import numpy as np


def df(x,y):
    return 1 - y / x

y0 = 5
a = 1
b = 6
n = 500

def f(x):
    return x/2+9/(2*x)
def vierstufig_runge_kutta_verfahren(df, n, a, b, y0):
    x0 = a
    h = (b-a)/n
    x = np.zeros(n + 1)
    x[0] = x0
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(0,n):
        x[i + 1] = x[i] + h
        k1 = df(x[i],y[i])
        k2 = df(x[i] + h/2, y[i] + h/2 * k1)
        k3 = df(x[i] + h / 2, y[i] + h / 2 * k2)
        k4 = df(x[i] + h, y[i] + h * k3)
        y[i + 1]= y[i] + h * 1/6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return x,y

##a)
x, y = vierstufig_runge_kutta_verfahren(df, n, a, b, y0)

x_exact = np.arange(a,b+0.001,0.001)
'''
plt.plot(t, y,label="Vierstufig runge-Kutta Verfahren")
plt.plot(t_exact, f(t_exact), label="exact f(t)")
plt.title("Funktionsvergleich")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.legend()
plt.show()
'''

##c)

def eigenes_kutta_verfahren(f, a, b, n, y0):
    h = (b - a) / n

    x = np.zeros(n+1)
    y = np.zeros(n+1)
    k1 = np.zeros(n)
    k2 = np.zeros(n)
    k3 = np.zeros(n)
    k4 = np.zeros(n)
    x[0] = a
    y[0] = y0

    for idx in range(0, n):
        k1[idx] = df(x[idx], y[idx])
        k2[idx] = df(x[idx] + h/4, y[idx]+ h/4 * k1[idx])
        k3[idx] = df(x[idx] + h/2, y[idx]+ h/2 * k2[idx])
        k4[idx] = df(x[idx] + h/2, y[idx] + h/2 * k3[idx])
        x[idx+1] = x[idx] + h
        y[idx+1] = y[idx] + h * (1 / 10) * (2* k1[idx] + 3 * k2[idx] + 3 * k3[idx] + 2* k4[idx])
    return x, y

##d)


x_eig, y_eig = eigenes_kutta_verfahren(f, a, b, n, y0)

plt.plot(x, y, label="Runge Kutta")
plt.plot(x_eig, y_eig, label="Eigenes Runge Kutta")
plt.plot(x_exact, f(x_exact), label="Exakte Funktion", linestyle="dotted")
plt.title("Alle Verfahren")
plt.legend()
plt.grid()
plt.show()