import numpy as np
import scipy.linalg

A = np.array([[0.8, 2.2, 3.6],
              [2.0, 3.0, 4.0],
              [1.2, 2.0, 5.8]])

P, L, R = scipy.linalg.lu(A)

print("Untere Dreicksmatrix L:\n" + str(L))

print("Obere Dreiecksmatrix R:\n" + str(R))

print("Permutationsmatrix P:\n" + str(P))

