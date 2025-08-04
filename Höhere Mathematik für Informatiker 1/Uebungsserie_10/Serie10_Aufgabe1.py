import math

import numpy as np

A = np.array([[8,5,2],
              [5,9,1],
              [4,2,7]])

print("A: " + str(A))

D = np.diag(np.diag(A))

print("D: " + str(D))

L = np.tril(A, k=-1)

print("L: " + str(L))

R = np.triu(A, k=1)

print("R: " + str(R))

b = np.array([[19],
              [5],
              [34]])

print("b: " + str(b))

x = np.array([[1],
              [-1],
              [3]])

D_invert = np.linalg.inv(D)

print("D^(-1): " + str(D_invert))

'''
a)
'''
def is_diagonally_dominant(matrix):
    # Check for square matrix
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square.")

    # Initialize dominance checks
    n = matrix.shape[0]
    row_dominant = [False] * n
    col_dominant = [False] * n

    # Check row-wise and column-wise dominance
    for i in range(n):
        row_elements = np.abs(matrix[i, :])
        col_elements = np.abs(matrix[:, i])

        row_sum = np.sum(row_elements) - row_elements[i]
        col_sum = np.sum(col_elements) - col_elements[i]

        row_dominant[i] = row_elements[i] > row_sum
        col_dominant[i] = col_elements[i] > col_sum

    # Overall dominance check
    if all(row_dominant) or all(col_dominant):
        print("Das Jacobi und Gauss-Seidel Verfahren konvergiert, A ist eine Diagonaldominantmatrize\nund x hat ein anziehender Fixpunkt")
        # Print all rows and columns
        for i in range(n):
            if all(row_dominant):
                row_condition = " + ".join(map(str, np.abs(matrix[i, np.arange(n) != i]))) + " < " + str(np.abs(matrix[i, i]))
                print(f"Zeile {i + 1}: {row_condition} ist dominant")
            if all(col_dominant):
                col_condition = " + ".join(map(str, np.abs(matrix[np.arange(n) != i, i]))) + " < " + str(np.abs(matrix[i, i]))
                print(f"Spalte {i + 1}: {col_condition} ist dominant")
        return True
    else:
        print("Das Jacobi und Gauss-Seidel Verfahren konvergiert nicht, A ist keine Diagonaldominantmatrize\nund x hat ein abstossender Fixpunkt")
        # Print only non-dominant rows and columns
        for i in range(n):
            if not row_dominant[i]:
                row_condition = " + ".join(map(str, np.abs(matrix[i, np.arange(n) != i]))) + " >= " + str(np.abs(matrix[i, i]))
                print(f"Zeile {i + 1}: {row_condition} ist nicht dominant")
            if not col_dominant[i]:
                col_condition = " + ".join(map(str, np.abs(matrix[np.arange(n) != i, i]))) + " >= " + str(np.abs(matrix[i, i]))
                print(f"Spalte {i + 1}: {col_condition} ist nicht dominant")

        return False

is_diagonally_dominant(A)

'''
b)
'''
def Jacobi_Verfahren_Matrix(x, k):
    counter = 0
    print("x^(" + str(counter) + "): " + str(x))
    while counter < k:
        counter += 1
        x = - D_invert@(L+R)@x + D_invert@b
        print("x^(" + str(counter) + "): " + str(x))
    return x
k_3 = 3
k_2 = 2
x_2 = Jacobi_Verfahren_Matrix(x, k_2)
x_3 = Jacobi_Verfahren_Matrix(x, k_3)

'''
c)
'''

def B_Jacobi_Verfahren(D, L, R):
    return -np.linalg.inv(D) @ (L + R)

B = B_Jacobi_Verfahren(D,L, R)

print("B: " + str(B))

def unendlich_Norm_Matrix(A):
    return np.max(np.sum(np.abs(A), axis=1))

def unendlich_Norm_Vektr(b):
    return np.max(np.abs(b))

def A_Posteriori_Abschätzung_Unendlich(B, x_n, x_n_1):
    B_unendlich = unendlich_Norm_Matrix(B)
    print("B_unendliche_norm: " + str(B_unendlich))
    x_n_minus_x_n_1_unendlich = unendlich_Norm_Vektr(x_n-x_n_1)
    a_posterori_abschätzung = (B_unendlich / (1-B_unendlich)) * x_n_minus_x_n_1_unendlich
    print("x_n_minus_x_n_1_unendlich: " + str(x_n_minus_x_n_1_unendlich))
    print("a_posterori_abschätzung: " + str(a_posterori_abschätzung))
    return a_posterori_abschätzung

a_posterori_abschätzung = A_Posteriori_Abschätzung_Unendlich(B, x_3, x_2)

'''
d)
'''

k_1 = 1
x_1 = Jacobi_Verfahren_Matrix(x, k_1)
a_priori = 1e-4

def A_Prorio_Abschätzung_Unendlich_Anzahl_Iterationen(B, x1, x0, a_priori):
    B_unendlich = unendlich_Norm_Matrix(B)
    print("B_unendlich: " + str(B_unendlich))
    x1_minus_x0_unendlich = unendlich_Norm_Vektr(x1 - x0)
    print("x1_minus_x0_unendlich: " + str(x1_minus_x0_unendlich))
    Eins_Minus_B_unendlich = 1-B_unendlich
    print("Eins_Minus_B_unendlich: " + str(Eins_Minus_B_unendlich))
    Alles_Ohne_N = (Eins_Minus_B_unendlich * a_priori) / x1_minus_x0_unendlich
    print("Alles_Ohne_N: " + str(Alles_Ohne_N))
    '''
    Logaritmus ziehen => grösser gleich zeichen wird umgedreht! also von <= zu >=
    '''
    Log_B_unendlich = math.log(B_unendlich)
    print("Log_B_unendlich: " + str(Log_B_unendlich))
    Log_Alles_Ohne_N = math.log(Alles_Ohne_N)
    print("Log_Alles_Ohne_N: " + str(Log_Alles_Ohne_N))
    n = Log_Alles_Ohne_N / Log_B_unendlich
    print("n: " + str(n))
    return n

A_Prorio_Abschätzung_Unendlich_Anzahl_Iterationen(B, x_1, x, a_priori)

'''
e)
'''

A_Prorio_Abschätzung_Unendlich_Anzahl_Iterationen(B, x_3, x_2, a_priori)