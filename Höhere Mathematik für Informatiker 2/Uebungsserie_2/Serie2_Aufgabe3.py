import sympy as sp

sp.init_printing()

x1,x2,x3 = sp.symbols('x y z')

f1 = x1 + x2 ** 2 - x3 ** 2 - 13
f2 = sp.log(x2 / 4) + sp.exp(0.5 * x3 -1) - 1
f3 = (x2 - 3) ** 2 - x3 ** 3 + 7

x01 = 1.5
x02 = 3
x03 = 2.5

f = sp.Matrix([f1,f2,f3])

Df = f.jacobian(sp.Matrix([x1,x2,x3]))

Df0 = Df.subs([(x1,x01),(x2,x02),(x3,x03)])

f0 = f.subs([(x1,x01),(x2,x02),(x3,x03)])

linealisiert = f0 + Df0@(sp.Matrix([x1-x01,x2-x02,x3-x03]))

print(linealisiert.evalf())