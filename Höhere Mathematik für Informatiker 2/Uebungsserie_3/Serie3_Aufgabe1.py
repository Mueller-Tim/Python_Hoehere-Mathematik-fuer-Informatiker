import numpy as np
import sympy as sp

sp.init_printing()

x1, x2 = sp.symbols("x1 x2")

f1 = 20 - 18 * x1 - 2 * x2 ** 2

f2 = - 4 * x2 * (x1 - x2 ** 2)

x0 = np.array([[1.1], [0.9]])

f = sp.Matrix([f1, f2])
print("f: ", f)

def newton(f,x_n, n):
    x1, x2 = sp.symbols("x1 x2")
    X = sp.Matrix([x1,x2])
    Df = f.jacobian(X)
    print("Df: ", Df)
    f_n = sp.lambdify((x1, x2), f, "numpy")
    Df_n = sp.lambdify((x1, x2), Df, "numpy")
    f_n = f_n(x_n[0, 0], x_n[1, 0])
    print("f" + str(n) + ": ", f_n)
    Df_n = Df_n(x_n[0, 0], x_n[1, 0])
    print("Df" + str(n) + ": ", Df_n)

    delta_n = np.linalg.solve(Df_n, -f_n)
    print("Delta: ", delta_n)
    x_n_1 = x_n + delta_n
    print("x" + str(n+1) + ": ", x_n_1)
    print("||f(x^"+ str(n+1) + ")||_2: ", np.linalg.norm(f_n, 2))
    return x_n_1


max_iteration = 2


x_n = x0

for counter in range(max_iteration):
    x_n_1 = newton(f, x_n, counter)
    print("||x^" + str(counter+1) + "-x^" + str(counter+1-1) + "||_2: ", np.linalg.norm(x_n_1-x_n, 2))
    x_n = x_n_1