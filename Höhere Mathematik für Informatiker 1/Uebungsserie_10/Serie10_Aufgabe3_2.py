import numpy as np


def Single_Jacobi_Iteration(B, c, xn):
    return B @ xn + c


def Single_Gauss_Seidel_Iteration(B, c, xn):
    return B @ xn + c


def A_Priori_Estimation(B, x0, x1, tol):
    return np.log((tol / np.linalg.norm((x1 - x0), np.inf) * (1 - np.linalg.norm(B, np.inf)))) / np.log(
        np.linalg.norm(B, np.inf))


def A_Posteriori_Estimation(B, xn, xn_minus_one):
    return (np.linalg.norm(B, np.inf) / (1 - np.linalg.norm(B, np.inf))) * np.linalg.norm(xn - xn_minus_one)


def muellti3_S10_Aufg3a(A, b, x0, tol, opt):
    A = A.astype("float64")
    b = b.astype("float64")
    x0 = x0.astype("float64")
    x1 = np.copy(x0)
    L = np.tril(A, k=-1)
    D = np.diag(np.diag(A))
    R = np.triu(A, k=1)
    n = 1

    if opt == 0:
        B = -np.linalg.inv(D) @ (L + R)
        c = np.linalg.inv(D) @ b
        x1 = Single_Jacobi_Iteration(B, c, x0)
    elif opt == 1:
        B = -np.linalg.inv(D + L) @ R
        c = np.linalg.inv(D + L) @ b
        x1 = Single_Gauss_Seidel_Iteration(B, c, x0)
    xn = np.copy(x1)
    xn_minus_one = np.copy(x0)
    # a-priori Abschätzung
    n2 = A_Priori_Estimation(B, x0, x1, tol)

    while tol < A_Posteriori_Estimation(B, xn, xn_minus_one):
        xn_minus_one = np.copy(xn)
        if opt == 0:
            xn = Single_Jacobi_Iteration(B, c, xn)
        elif opt == 1:
            xn = Single_Gauss_Seidel_Iteration(B, c, xn)
        n = n + 1
    return (xn, n, n2)


A = np.array([[8, 5, 2], [5, 9, 1], [4, 2, 7]])
b = np.array([[19], [5], [34]])
x0 = np.array([[1], [-1], [3]])
opt = 1  # 0 is Jacobi; 1 is Gauss-Seidel

[xn, n, n2] = muellti3_S10_Aufg3a(A, b, x0, 0.0001, opt)

print("Solution vector xn:")
print(xn)
print("Number of iterations:")
print(n)
print("Used steps with a priori:")
print(n2)