import matplotlib.pyplot as plt
import numpy as np


def df(x,y):
    return x ** 2 / y

y0 = 2
n = 2
a = 0
b = 1.4

def f(x):
    return (2 * x **3 / 3 + 4) ** (1/2)
def euler_verfahren(df, n, a, b, y0):
    x0 = a
    h = (b-a)/n
    x = np.zeros(n + 1)
    x[0] = x0
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(0,n):
        x[i + 1] = x[i] + h
        y[i + 1]= y[i] + h * df(x[i],y[i])
    return x,y

def mittelpunkt_verfahren(df, n, a, b, y0):
    x0 = a
    h = (b-a)/n
    x = np.zeros(n + 1)
    x[0] = x0
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(0,n):
        x[i + 1] = x[i] + h
        y[i + 1]= y[i] + h * df(x[i] + h/2,y[i] + h/2 * df(x[i],y[i]))
    return x,y

def modifiziertes_euler_verfahren(df, n, a, b, y0):
    x0 = a
    h = (b-a)/n
    x = np.zeros(n + 1)
    x[0] = x0
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(0,n):
        x[i+1] = x[i] + h
        k1 = df(x[i],y[i])
        k2 = df(x[i+1], y[i] + h * df(x[i],y[i]))
        y[i+1] = y[i] + h * (k1 + k2) / 2
    return x,y

def plot_euler_mittelpunkt_modifiziertEuler_exakt(df,n,a,b,y0):
    x, y_euler = euler_verfahren(df,n,a,b,y0)
    x, y_mittelpunkt = mittelpunkt_verfahren(df,n,a,b,y0)
    x, y_modeuler = modifiziertes_euler_verfahren(df,n,a,b,y0)
    plt.plot(x, y_euler, label="Euler")
    plt.plot(x, y_mittelpunkt, label="Mittelpunkt")
    plt.plot(x, y_modeuler, label="Mod. Euler")
    Xres = np.arange(a, b + 0.1, 0.1)
    Yres = f(Xres)
    plt.plot(Xres, Yres, label="exakt")
    plt.legend(["Euler", "Mittelpunkt", "Mod. Euler", "exakt"])
    plt.show()

plot_euler_mittelpunkt_modifiziertEuler_exakt(df,n,a,b,y0)

