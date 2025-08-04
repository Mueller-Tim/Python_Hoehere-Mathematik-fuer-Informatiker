import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import scipy.optimize

sp.init_printing()

x = np.array([2., 2.5, 3., 3.5, 4., 4.5, 5., 5.5, 6., 6.5, 7., 7.5, 8.,
              8.5, 9., 9.5])

y = np.array([159.57209984, 159.8851819, 159.89378952, 160.30305273,
              160.84630757, 160.94703969, 161.56961845, 162.31468058,
              162.32140561, 162.88880047, 163.53234609, 163.85817086,
              163.55339958, 163.86393263, 163.90535931, 163.44385491])

##a)

p = sp.symbols('p:{n:d}'.format(n=4))


def f(x, p):
    return (p[0] + p[1] * 10 ** (p[2] + p[3] * x)) / (1 + 10 ** (p[2] + p[3] * x))


lam0 = np.array([100, 120, 3, -1])

tol = 1e-5
max_iter = 30
pmax = 4
damping = 1

g = sp.Matrix([y[k] - f(x[k], p) for k in range(len(x))])

Dg = g.jacobian(p)

g = sp.lambdify([p], g, 'numpy')
Dg = sp.lambdify([p], Dg, 'numpy')


def gauss_newton_d(g, Dg, lam0, tol, max_iter, pmax, damping):
    k = 0
    lam = np.copy(lam0)
    increment = tol + 1
    err_func = np.linalg.norm(g(lam)) ** 2

    while k < max_iter and increment > tol:
        # QR-Zerlegung von Dg(lam)
        [Q, R] = np.linalg.qr(Dg(lam))
        delta = np.linalg.solve(R, -Q.T @ g(
            lam)).flatten()  # Achtung: flatten() braucht es, um aus dem Spaltenvektor delta wieder
        # eine "flachen" Vektor zu machen, da g hier nicht mit Spaltenvektoren als Input umgehen kann
        # hier kommt die Däfmpfung, falls damping = 1
        p = 0

        while damping == 1 and p < pmax and np.linalg.norm(g(lam + delta / (2 ** p))) ** 2 >= err_func:
               p += 1


        # Update des Vektors Lambda
        lam = lam + delta / (2 ** p)
        err_func = np.linalg.norm(g(lam)) ** 2
        increment = np.linalg.norm(delta)
        k = k + 1
        print('Iteration: ', k)
        print('lambda = ', lam)
        print('Inkrement = ', increment)
        print('Fehlerfunktional =', err_func)
    return (lam, k)

print("Gedämpfter Gauss Newton")
[lam_with, n] = gauss_newton_d(g, Dg, lam0, tol, max_iter, pmax, damping)

plt.figure(0)
t = sp.symbols('t')
F = f(t, lam_with)
F = sp.lambdify([t], F, 'numpy')
t = np.linspace(x.min(), x.max(),200)
y_pred = F(t)
plt.plot(x, y, 'o', label="Points")
plt.plot(t, y_pred, '-', label="Prediction")
plt.xlabel('x')
plt.ylabel('y')
plt.title('gedämpfter Gauss Newton')


##b)
def gauss_newton(g, Dg, lam0, tol, max_iter):
       k = 0
       lam = np.copy(lam0)
       increment = tol + 1
       err_func = np.linalg.norm(g(lam)) ** 2

       while k < max_iter and increment > tol:  # Hier kommt Ihre Abbruchbedingung, die tol und max_iter berücksichtigen muss#

              # QR-Zerlegung von Dg(lam) und delta als Lösung des lin. Gleichungssystems
              [Q, R] = np.linalg.qr(Dg(lam))
              delta = np.linalg.solve(R, -Q.T @ g(
                     lam)).flatten()  # Achtung: flatten() braucht es, um aus dem Spaltenvektor delta wieder
              # eine "flachen" Vektor zu machen, da g hier nicht mit Spaltenvektoren als Input umgehen kann

              # Update des Vektors Lambda
              lam = lam + delta
              err_func = np.linalg.norm(g(lam)) ** 2
              increment = np.linalg.norm(delta)
              k = k + 1
              print('Iteration: ', k)
              print('lambda = ', lam)
              print('Inkrement = ', increment)
              print('Fehlerfunktional =', err_func)
       return (lam, k)

print("ungedämpfter Gauss Newton")
lam0 = np.array([100, 120, 3, -1])
##[lam_without,n] = gauss_newton(g, Dg, lam0, tol, max_iter)

'''
Der ungedämpfte Gauss Newton konvertiert nicht.
Bei der Iteration 11 ist das Inkrement 449 und die Fehlerfunktional nan.
Nacher gibt es einen Error: RuntimeWarning: overflow encountered in scalar power
'''

##c)



def err_func(x):
    return np.linalg.norm(g(x)) ** 2

xopt = scipy.optimize.fmin(err_func, lam0)

print("Lamda: ",xopt)

'''
Das Fehlerfunktional ist das Gleiche.
Es wir einfach erst nach 333 Iterationen gefunden.
'''