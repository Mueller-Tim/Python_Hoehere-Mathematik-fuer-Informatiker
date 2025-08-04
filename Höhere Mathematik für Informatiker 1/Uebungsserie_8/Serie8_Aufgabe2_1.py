# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:26:09 2020

Höhere Mathematik 1, Serie 8, Gerüst für Aufgabe 2

Description: calculates the QR factorization of A so that A = QR
Input Parameters: A: array, n*n matrix
Output Parameters: Q : n*n orthogonal matrix
                   R : n*n upper right triangular matrix            
Remarks: none
Example: A = np.array([[1,2,-1],[4,-2,6],[3,1,0]]) 
        [Q,R]=Serie8_Aufg2(A)

@author: knaa
"""
import time

import numpy as np

##a)
def Serie8_Aufg2(A):
    
    import numpy as np
    
    A = np.copy(A)                       #necessary to prevent changes in the original matrix A_in
    A = A.astype('float64')              #change to float
    
    n = np.shape(A)[0]
    
    if n != np.shape(A)[1]:
        raise Exception('Matrix is not square') 
    
    Q = np.eye(n)
    R = A



    for j in np.arange(0,n-1):
        a = np.copy(R[j:,j]).reshape(n-j,1)
        e = np.eye(n-j)[:,0].reshape(n-j,1)
        length_a = np.linalg.norm(a)
        if a[0] >= 0: sig = 1
        else: sig = -1
        v = a + sig * length_a * e
        u = (1 / np.linalg.norm(v)) * v
        H = np.eye(n-j) - 2 * u * u.T
        Qi = np.eye(n)
        Qi[j:,j:] = H[:,:]
        R = Qi@R
        Q = Q@Qi.T

    return(Q,R)

##b)

As= np.array([[1,-2,3],
               [-5,4,1],
               [2,-1,3]])

A = np.array([[19.9,29.9,9.9],
              [9.9,16.9,5.9],
              [1.9,2.9,1.9]])

b = np.array([[5820],
             [3400],
              [936]])

Q,R=Serie8_Aufg2(A)

print("Q: " + str(Q))
print("R: " + str(R))
'''
Q und R sind die gleichen, wie wenn ich es von hand gelöst habe.
'''

sb = np.array([[1],
              [9],
              [5]])

'''
R@x = Q.T@b
nach x aufgelöst
'''
def reverse_insertion(Q, R, b):
    n = np.shape(A)[0]
    solution = np.zeros(n, dtype="float")
    left_side = Q.T @ b

    print("Q.T@b: " + str(left_side))

    for index in reversed(range(n)):
        value = left_side[index]
        for p in range(n - index - 1):
            value -= R[index][index + p + 1] * solution[index + p + 1]
        solution[index] = value / R[index][index]

    print("x: " + str(solution.reshape(-1, 1)))


reverse_insertion(Q,R,b)

'''
X ist gleich, wie wenn ich es von hand gelöst habe.
'''

##c)

repetition = 100

startMyCalculation = time.time()
for i in range(repetition):
    Serie8_Aufg2(A)

endMyCalculation = time.time()

startLinalgQR = time.time()
for i in range(repetition):
    np.linalg.qr(A)

endLinalgQR = time.time()

timeMyCalculation = (endMyCalculation - startMyCalculation) / repetition
timeLinalgQR = (endLinalgQR - startLinalgQR) / repetition

print("The time from my Calculation: " + str(timeMyCalculation) + " seconds")
print("The time from linalgQr: " + str(timeLinalgQR) + " seconds")
print("LinalgQr is: " + str(timeMyCalculation / timeLinalgQR) + " times faster than my calculation")


##d)

TestMatrix = np.random.rand(100,100)


startMyCalculation = time.time()
for i in range(repetition):
    Serie8_Aufg2(TestMatrix)

endMyCalculation = time.time()

startLinalgQR = time.time()
for i in range(repetition):
    np.linalg.qr(TestMatrix)

endLinalgQR = time.time()

timeMyCalculation = (endMyCalculation - startMyCalculation) / repetition
timeLinalgQR = (endLinalgQR - startLinalgQR) / repetition
print("Now with a random 100x100 testmatrix:")
print("The time from my Calculation: " + str(timeMyCalculation) + " seconds")
print("The time from linalgQr: " + str(timeLinalgQR) + " seconds")
print("LinalgQr is: " + str(timeMyCalculation / timeLinalgQR) + " times faster than my calculation")

'''

Je grösser die Matrize, desto grösser ist der unterschied zwischen beiden Zeiten.
Dies liegt daran, dass meine Rechnung bei weitem nicht so optimiert ist wie die von Linalg.
Und je grösser die Matrix desto prozentual länger braucht meine Rechnung.
'''








