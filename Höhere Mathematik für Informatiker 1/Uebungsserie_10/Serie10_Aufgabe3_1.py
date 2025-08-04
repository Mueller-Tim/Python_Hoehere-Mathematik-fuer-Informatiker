import numpy as np

def Jacobi_Step(B, c, x_prev):
    return np.dot(B, x_prev) + c

def GaussSeidel_Step(B, c, x_prev):
    return np.dot(B, x_prev) + c

def Estimate_A_Priori(B, initial_x, next_x, tolerance):
    return np.log(tolerance / (np.linalg.norm(next_x - initial_x, np.inf) * (1 - np.linalg.norm(B, np.inf)))) / np.log(np.linalg.norm(B, np.inf))

def Estimate_A_Posteriori(B, current_x, previous_x):
    return (np.linalg.norm(B, np.inf) / (1 - np.linalg.norm(B, np.inf))) * np.linalg.norm(current_x - previous_x)

def muellti3_S10_Aufg3a(A, b, initial_x, tolerance, method):
    A = A.astype("float64")
    b = b.astype("float64")
    initial_x = initial_x.astype("float64")
    next_x = np.copy(initial_x)
    Lower = np.tril(A, -1)
    Diagonal = np.diag(np.diag(A))
    Upper = np.triu(A, 1)
    iteration_count = 1

    if method == 0:
        B = -np.linalg.inv(Diagonal) @ (Lower + Upper)
        c = np.linalg.inv(Diagonal) @ b
        next_x = Jacobi_Step(B, c, initial_x)
    elif method == 1:
        B = -np.linalg.inv(Diagonal + Lower) @ Upper
        c = np.linalg.inv(Diagonal + Lower) @ b
        next_x = GaussSeidel_Step(B, c, initial_x)

    current_x = np.copy(next_x)
    previous_x = np.copy(initial_x)
    a_priori_estimate = Estimate_A_Priori(B, initial_x, next_x, tolerance)

    while tolerance < Estimate_A_Posteriori(B, current_x, previous_x):
        previous_x = np.copy(current_x)
        if method == 0:
            current_x = Jacobi_Step(B, c, current_x)
        elif method == 1:
            current_x = GaussSeidel_Step(B, c, current_x)
        iteration_count += 1

    return current_x, iteration_count, a_priori_estimate

# Beispielverwendung
A = np.array([[8, 5, 2], [5, 9, 1], [4, 2, 7]])
b = np.array([[19], [5], [34]])
initial_x = np.array([[1], [-1], [3]])
method = 1  # 0 für Jacobi, 1 für Gauss-Seidel

solution_x, iterations, steps_apriori = muellti3_S10_Aufg3a(A, b, initial_x, 0.0001, method)

print("Lösungsvektor xn:")
print(solution_x)
print("Anzahl der Iterationen:")
print(iterations)
print("Mit a priori geschätzte Schritte:")
print(steps_apriori)