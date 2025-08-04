import numpy as np
import matplotlib.pyplot as plt


def euler_verfahren(f, a, b, n, y0):
    h = (b - a) / n

    x = np.zeros(n + 1)
    y = np.zeros(n + 1)

    x[0] = a
    y[0] = y0

    for idx in range(n):
        x[idx + 1] = x[idx] + h
        y[idx + 1] = y[idx] + h * f(x[idx], y[idx])

    return x, y


def mittelpunktsverfahren(f, a, b, n, y0):
    h = (b - a) / n

    x = np.zeros(n + 1)
    y = np.zeros(n + 1)

    x[0] = a
    y[0] = y0

    for idx in range(n):
        x_half = x[idx] + h / 2
        y_half = y[idx] + h / 2 * f(x[idx], y[idx])
        x[idx + 1] = x[idx] + h
        y[idx + 1] = y[idx] + h * f(x_half, y_half)

    return x, y


def modifizierter_euler(f, a, b, n, y0):
    h = (b - a) / n
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    x[0], y[0] = a, y0

    for idx in range(n):
        x_next = x[idx] + h
        x[idx + 1] = x_next
        y_next_euler = y[idx] + h * f(x[idx], y[idx])
        k1 = f(x[idx], y[idx])
        k2 = f(x_next, y_next_euler)
        y[idx + 1] = y[idx] + h * ((k1 + k2) / 2)

    return x, y


def vierstufig_runge_kutta_verfahren(df, n, a, b, y0):
    x0 = a
    h = (b - a) / n
    x = np.zeros(n + 1)
    x[0] = x0
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(n):
        x[i + 1] = x[i] + h
        k1 = df(x[i], y[i])
        k2 = df(x[i] + h / 2, y[i] + h / 2 * k1)
        k3 = df(x[i] + h / 2, y[i] + h / 2 * k2)
        k4 = df(x[i] + h, y[i] + h * k3)
        y[i + 1] = y[i] + h * 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return x, y


f = lambda x, y: x ** 2 / y
a, b = 0, 10
h = 0.1
n_kon_ord_2 = int((b - a) / h)
y0 = 2

f_exakt = lambda x: np.sqrt((2 * x ** 3 / 3) + 4)

x_euler, y_euler = euler_verfahren(f, a, b, n_kon_ord_2, y0)
x_mod, y_mod = modifizierter_euler(f, a, b, n_kon_ord_2, y0)
x_mit, y_mit = mittelpunktsverfahren(f, a, b, n_kon_ord_2, y0)
x_run, y_run = vierstufig_runge_kutta_verfahren(f, n_kon_ord_2, a, b, y0)

plt.plot(x_euler, y_euler, label="Euler-Verfahren")
plt.plot(x_mod, y_mod, label="Modifiziertes Euler-Verfahren")
plt.plot(x_mit, y_mit, label="Mittelpunkt-Verfahren")
plt.plot(x_run, y_run, label="Runge-Kutta-Verfahren")
plt.grid()
plt.legend()
plt.title("Vergleich der Verfahren")
plt.show()

y_exakt = f_exakt(x_euler)
plt.semilogy(x_euler, np.abs(y_euler - y_exakt), label="Euler-Verfahren")
plt.semilogy(x_mod, np.abs(y_mod - y_exakt), label="Modifiziertes Euler-Verfahren")
plt.semilogy(x_mit, np.abs(y_mit - y_exakt), label="Mittelpunkt-Verfahren")
plt.semilogy(x_run, np.abs(y_run - y_exakt), label="Runge-Kutta-Verfahren")
plt.grid()
plt.legend()
plt.title("Fehlervergleich der Verfahren")
plt.show()

a, b = 0, 10
y0 = 2

# Euler muss separat getestet werden, da andere Konsistenzordnung
test_euler = 20  # Euler (da anderes p)
h_kon_ord_1 = 0.1 / 2 ** test_euler
n_kon_ord_1 = int((b - a) / h_kon_ord_1)

test_kon_ord_2 = 6  # Alles außer Euler
h_kon_ord_2 = 0.1 / 2 ** test_kon_ord_2
n_kon_ord_2 = int((b - a) / h_kon_ord_2)

x_euler_test, y_euler_test = euler_verfahren(f, a, b, n_kon_ord_1, y0)
x_mod_test, y_mod_test = modifizierter_euler(f, a, b, n_kon_ord_2, y0)
x_mit_test, y_mit_test = mittelpunktsverfahren(f, a, b, n_kon_ord_2, y0)

# Konsistenzordnung 1
y_exakt_test_euler = f_exakt(x_euler_test)
plt.semilogy(x_euler_test, np.abs(y_euler_test - y_exakt_test_euler), label="Euler-Verfahren")

# Konsistenzordnung 2
y_exakt_kon_ord2 = f_exakt(x_mod_test)
plt.semilogy(x_mod_test, np.abs(y_mod_test - y_exakt_kon_ord2), label="Modifiziertes Euler-Verfahren")
plt.semilogy(x_mit_test, np.abs(y_mit_test - y_exakt_kon_ord2), label="Mittelpunkt-Verfahren")
plt.semilogy(x_run, np.abs(y_run - y_exakt), label="Runge-Kutta-Verfahren")

plt.grid()
plt.legend()
plt.title("Fehlervergleich der Verfahren")
plt.show()
