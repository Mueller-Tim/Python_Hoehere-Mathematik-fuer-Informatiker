import sympy as sp


sp.init_printing()

##a)

x1,x2 = sp.symbols('x1 x2')

fa1 = 5 * x1 * x2
fa2 = x1 ** 2 * x2 ** 2 + x1 + 2 * x2

fa = sp.Matrix([fa1,fa2])

Dfa = fa.jacobian(sp.Matrix([x1,x2]))

Dfa_loesung = Dfa.subs([(x1,1),(x2,2)])

print("Lösung für Teilaufgabe 1: " + str(Dfa_loesung.evalf()))

##b)

x3 = sp.symbols('x3')

fb1 = sp.log(x1 ** 2 + x2 ** 2) + x3 ** 2
fb2 = sp.exp(x2 ** 2 + x3 ** 2) + x1 ** 2
fb3 = 1/(x3 ** 2 + x1 ** 2) + x2 ** 2

fb = sp.Matrix([fb1, fb2, fb3])

Dfb = fb.jacobian(sp.Matrix([x1,x2,x3]))

Dfb_loesung = Dfb.subs([(x1,1),(x2,2),(x3,3)])

print("Lösung für Teilaufgabe 2: " + str(Dfb_loesung.evalf()))


