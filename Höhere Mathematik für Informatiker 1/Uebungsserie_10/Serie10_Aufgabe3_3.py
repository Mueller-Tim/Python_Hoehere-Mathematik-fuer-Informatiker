from timeit import default_timer as timer

from muellti3_S6_Aufg2_copie import muellti3_S6_Aufg2
from muellti3_S10_Aufg3a import muellti3_S10_Aufg3a

import numpy as np
import time
import matplotlib.pyplot as plt

#b)
dim = 3000
A = np.diag( np.diag( np.ones( ( dim , dim ) )*4000 ) )+ np.ones( ( dim , dim ) )
dum1 = np.arange( 1 , np.int32( dim /2+1) , dtype = np.float64 ).reshape( ( np.int32( dim / 2 ) , 1 ) )
dum2 = np.arange( np.int32( dim / 2 ) ,0 , -1 , dtype=np.float64 ).reshape( ( np.int32( dim / 2 ) , 1 ) )
x = np.append( dum1 , dum2 , axis=0)
b = A@x
x0 = np.zeros( ( dim , 1 ) )
tol = 1e-4

startLinalgSolve = timer()
x_linalg_solve = np.linalg.solve(A,b)
stoppLinalgSolve = timer()

startJacobi = timer()
[x_jacobi, n, n2] = muellti3_S10_Aufg3a(A,b,x0,tol,0)
stoppJacobi = timer()

startGaussSeidel = timer()
[x_gauss_seidel, n, n2] = muellti3_S10_Aufg3a(A,b,x0,tol,1)
stoppGaussSeidel = timer()

startGauss = timer()
x_gauss = muellti3_S6_Aufg2(A,b)[2]
stoppGauss = timer()

print("***********Time Estimation***********")
print("Time for np.linalg.solve:")
print(stoppLinalgSolve-startLinalgSolve)
print("Time for Jacobi:")
print(stoppJacobi-startJacobi)
print("Time for Gauss-Seidel:")
print(stoppGaussSeidel-startGaussSeidel)
print("Time for Gauss:")
print(stoppGauss-startGauss)



#In this algorithm for Jacobi and Gauss-Seidel is the B calculated every single time
""" Time for np.linalg.solve:
0.6146464347839355
Time for Jacobi:
319.44120621681213
Time for Gauss-Seidel:
307.4256772994995
Time for Gauss:
95.12803220748901 """

#In this algorithm for Jacobi and Gauss-Seidel is the B calculated one time
""" Time for np.linalg.solve:
0.5016989707946777
Time for Jacobi:
18.02965211868286
Time for Gauss-Seidel:
17.64187240600586
Time for Gauss:
105.31756782531738 """

print(x_gauss)
print(np.any(np.abs(x_gauss) > 1e10))

#c)
x_axis = np.arange(dim)

plt.semilogy()
plt.plot(x_axis, x_gauss_seidel-x)
plt.plot(x_axis, x_jacobi-x)
plt.plot(x_axis, x_gauss-x)
plt.plot(x_axis, x_linalg_solve-x)
plt.legend(["Gauss Seidel", "Jacobi", "Gauss", "Linalg"])
plt.show()

#Das Gauss-Verfahren ist genauer wie das Jacobi und Gauss-Seidel Verfahren
