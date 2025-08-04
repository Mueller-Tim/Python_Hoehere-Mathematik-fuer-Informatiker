import numpy as np

A = np.array([[1,0,2],
              [0,1,0],
              [10**(-4), 0, 10**(-4)]])

b = np.array([[1],
              [1],
              [0]])

##a)

A_inv = np.linalg.inv(A)

print("A: " + str(A))
print("b: " + str(b))
print("A^(-1): " + str(A_inv))


## Zeilensummennorm mit gegebener matrix

A_infinity_norm = np.max(np.sum(np.abs(A), axis=1))

print("A_infinity_norm: " + str(A_infinity_norm))

A_inv_infinity_norm = np.max(np.sum(np.abs(A_inv), axis=1))

print("A^(-1)_infinity_norm: " + str(A_inv_infinity_norm))

konditionzahl = A_infinity_norm * A_inv_infinity_norm

print("Konditional: " + str(konditionzahl))

##b)
b_infinity_norm = np.max(np.abs(b))

print("b_infinity_norm: " + str(b_infinity_norm))

#nach Epsilon = ||b-b~|| auflösen

max_relativer_fehler = 0.01
epsilon = b_infinity_norm * max_relativer_fehler / konditionzahl
print("Epsilon: " + str(epsilon))


##c)

b_mit_fehler = b.copy()
b_mit_fehler = b_mit_fehler + epsilon
x_ohne_fehler = np.linalg.solve(A, b)
x_mit_fehler = np.linalg.solve(A,b_mit_fehler)
relativer_fehler = np.max(np.abs(x_ohne_fehler - x_mit_fehler)) / np.max(np.abs(x_ohne_fehler))
print("Relativer Fehler wenn nur b falsch ist: " + str(relativer_fehler))



##d)


A_mit_fehler = A.copy()
A_mit_fehler = A_mit_fehler + 1e-7
A_fehlerblock = np.max(np.sum(np.abs(A-A_mit_fehler), axis=1)) / A_infinity_norm
b_fehlerblok = np.max(np.abs(b - b_mit_fehler)) / b_infinity_norm
relativer_fehler = (konditionzahl / (1- konditionzahl * A_fehlerblock)) * (A_fehlerblock + b_fehlerblok)
print("Relativer Fehler wenn A und b falsch ist: " + str(relativer_fehler))
