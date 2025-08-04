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

x_exact = np.arange(a,b+0.01,0.01)



##a)
x_euler,y_euler = euler_verfahren(df,n,a,b,y0)
y_exact = f(x_euler)
absoluterFehler_euler = np.abs(y_euler-y_exact)
print("Die Lösung für das Euler-Verfahren ist: ", y_euler)
print("Die exakte Lösung ist: ", y_exact)
print("Der Absulute Fehler für das Euler-Verfahren ist: ", absoluterFehler_euler)


##b)
x_mittelpunkt,y_mittelpunkt = mittelpunkt_verfahren(df,n,a,b,y0)
y_exact = f(x_mittelpunkt)
absoluterFehler_mittelpunkt = np.abs(y_mittelpunkt-y_exact)

print("Die Lösung für das Mittelpunkt-Verfahren ist: ", y_mittelpunkt)
print("Die exakte Lösung ist: ", y_exact)
print("Der Absulute Fehler für das Mittelpunkt-Verfahren ist: ", absoluterFehler_mittelpunkt)

##c)
x_modifiziertes_euler,y_modifiziertes_euler = modifiziertes_euler_verfahren(df,n,a,b,y0)
y_exact = f(x_modifiziertes_euler)
absoluterFehler_modifiziertes_euler = np.abs(y_modifiziertes_euler-y_exact)

print("Die Lösung für das modifizierte Euler-Verfahren ist: ", y_modifiziertes_euler)
print("Die exakte Lösung ist: ", y_exact)
print("Der Absulute Fehler für das modifizierte Euler-Verfahren ist: ", absoluterFehler_modifiziertes_euler)
