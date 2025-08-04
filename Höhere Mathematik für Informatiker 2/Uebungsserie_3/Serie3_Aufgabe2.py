import sympy as sp
import numpy as np

##a)
x, y = sp.symbols('x y')

f1 = x**2 / 186 ** 2 - y ** 2 / (300 **2 -186 ** 2) -1
f2 = (y-500) ** 2 / 279 ** 2 - (x-300) ** 2 / (500 ** 2 -279 ** 2) -1

p1 = sp.plot_implicit(sp.Eq(f1,0),(x,-2000,2000),(y,-2000,2000))
p2 = sp.plot_implicit(sp.Eq(f2,0),(x,-2000,2000),(y,-2000,2000))

p1.append(p2[0])
p1.show()



##b)



accuracy = 10 ** -5
f = sp.Matrix([f1,f2])

def newton(f,x_n):
    x1, x2 = sp.symbols("x y")
    X = sp.Matrix([x1,x2])
    Df = f.jacobian(X)
    f_n = sp.lambdify((x1, x2), f, "numpy")
    Df_n = sp.lambdify((x1, x2), Df, "numpy")
    f_val = f_n(x_n[0, 0], x_n[1, 0])
    Df_val = Df_n(x_n[0, 0], x_n[1, 0])

    delta_n = np.linalg.solve(Df_val, -f_val)
    x_n_1 = x_n + delta_n
    fn_norm = np.linalg.norm(f_val, 2)
    return x_n_1, fn_norm





def newton_accuracy(f, x0, accuracy):
    fn_norm = accuracy + 1
    x_n = x0
    while fn_norm > accuracy:
        x_n, fn_norm = newton(f, x_n)

    print("Endpunkt für Startwert " + str(x0) + ":\n", x_n)

##Schnittpunkt oben links
x0 = np.array([[-1500], [2000]])

newton_accuracy(f, x0, accuracy)


##Schnittpunkt unten links
x0 = np.array([[-500], [500]])

newton_accuracy(f, x0, accuracy)


##Schnittpunkt unten rechts
x0 = np.array([[500], [300]])

newton_accuracy(f, x0, accuracy)


##Schnittpunkt oben rechts
x0 = np.array([[1000], [1000]])

newton_accuracy(f, x0, accuracy)