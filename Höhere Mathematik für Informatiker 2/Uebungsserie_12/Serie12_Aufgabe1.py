import matplotlib.pyplot as plt
import numpy as np


def df(t,y):
    return t ** 2 + 0.1 * y

y0 = 0
n = 5
a = -1.5
b = 1.5

def f(t):
    return -10 * t ** 2 -200 * t -2000 + 1722.5 * np.exp(0.05 * (2 * t + 3))
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
        print("i: ", i)
        print("x" + str(i) + ": ", x[i])
        print("y" + str(i) + ": ", y[i])
        print("k1[" + str(i) + "]: ", k1)
        print("k2[" + str(i) + "]: ", k2)
        print("k3[" + str(i) + "]: ", k3)
        print("k4[" + str(i) + "]: ", k4)
        print("y" + str(i + 1) + ": ", y[i+1])

    return x,y


t, y = vierstufig_runge_kutta_verfahren(df, n, a, b, y0)

t_exact = np.arange(a,b+0.01,0.01)

plt.plot(t, y,label="Vierstufig runge-Kutta Verfahren")
plt.plot(t_exact, f(t_exact), label="exact f(t)")
plt.title("Funktionsvergleich")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.legend()
plt.show()