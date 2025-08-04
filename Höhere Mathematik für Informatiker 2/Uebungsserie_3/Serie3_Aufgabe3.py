import numpy as np
import sympy as sp

accuracy = 10 ** -5

x1,x2,x3 = sp.symbols('x1 x2 x3')

f1 = x1 + x2 ** 2 - x3 ** 2 -13
f2 = sp.log(x2 / 4) + sp.exp(0.5 * x3 - 1) - 1
f3 = (x2 - 3) ** 2 - x3 ** 3 + 7

x0 = np.array([[1.5],[3],[2.5]])

f = sp.Matrix([f1, f2, f3])

def gedaenftes_newton(f,x0, accuracy, k_max, n_max):
    fn_norm = accuracy + 1
    x_n = x0

    x1, x2, x3 = sp.symbols("x1 x2 x3")
    X = sp.Matrix([x1, x2, x3])
    Df = f.jacobian(X)
    f_n = sp.lambdify([[[x1], [x2], [x3]]], f, "numpy")
    Df_n = sp.lambdify([[[x1], [x2], [x3]]], Df, "numpy")

    n = 0
    while fn_norm > accuracy and n < n_max:
        f_val = f_n(x_n)
        Df_val = Df_n(x_n)
        fn_norm = np.linalg.norm(f_val, 2)
        delta_n = np.linalg.solve(Df_val, -f_val)
        k = 1
        while k < k_max:
            x_temp = x_n + delta_n / (2 ** k)
            f_temp = f_n(x_temp)
            fn_temp_norm = np.linalg.norm(f_temp, 2)

            if fn_temp_norm < fn_norm:
                x_n = x_temp
                fn_norm = fn_temp_norm
                break
            k += 1

        n += 1

    print("Endpunkt für Startwert " + str(x0) + " nach " + str(n) + "Wiederhollung :\n", x_n)

k_max = 20
n_max = 1000
gedaenftes_newton(f, x0, accuracy,k_max, n_max)