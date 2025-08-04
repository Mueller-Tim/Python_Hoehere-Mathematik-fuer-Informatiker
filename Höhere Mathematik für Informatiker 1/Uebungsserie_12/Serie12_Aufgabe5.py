import numpy as np
import math


def eigenvector_iteration(A, v_k):
    return ((A @ v_k) / (np.linalg.norm(A @ v_k)))


def eigenvalue_iteration(A, v_k):
    return (v_k.T @ A @ v_k) / (v_k.T @ v_k)


A = np.array([[1, 1, 0],
              [3, -1, 2],
              [2, -1, 3]])

v = np.array([[1],
              [0],
              [0]])

v_k = v
v_k_plus_one = eigenvector_iteration(A, v_k)
iteration = 1

while (np.linalg.norm(v_k_plus_one - v_k,2)) >= (1e-4):
    v_k = v_k_plus_one
    v_k_plus_one = eigenvector_iteration(A, v_k)
    iteration = iteration + 1


print("Eigenvektor:")
print(v_k_plus_one)
print("Eigenwert:")
print(eigenvalue_iteration(A, v_k_plus_one))
print("Number of iterations")
print(iteration)

print("Calculated with np.linalg.eig:")
[W, V] = np.linalg.eig(A)
print("Eigenvektor:")
print(V)
print("Eigenwert:")
print(W)