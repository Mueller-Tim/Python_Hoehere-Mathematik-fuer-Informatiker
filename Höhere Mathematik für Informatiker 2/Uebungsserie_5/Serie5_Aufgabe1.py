import numpy as np

A = np.array([[8,2],
             [2,8]])

z = np.array([[13.5],
             [-22.5]])

c= np.linalg.solve(A,z)
print(c)