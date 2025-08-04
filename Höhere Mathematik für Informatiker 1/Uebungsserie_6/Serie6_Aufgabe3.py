3'''
Bei Aufgabe 4.3 hat 4 Rechnungen, ich Empfehle zur besseren Übersicht
alle Aufgaben, welche man gerade nicht anschauen möchte auszukommentieren.
'''
import numpy as np

from muellti3_S6_Aufg2 import muellti3_S6_Aufg2

#A1X

A1 = np.array([[4,-1,-5],
               [-12,4,17],
               [32,-10,-41]])

b1 = np.array([[-5],
               [19],
               [-39]])

b1Alternative = np.array([[6],
               [-12],
               [-48]])

x1 = muellti3_S6_Aufg2(A1, b1Alternative)

print("Task 1")
print("My solution:\nUpper triangle matrix U:\n" + str(x1[0]) + "\nSolution vector:\n"
      + str(x1[2]) + "\nDeterminant of A:\n" + str(x1[1]))

print("Solution of Numpy.linal.solve():\n" + str(np.linalg.solve(A1, b1Alternative)))
print("Difference from my solution and numpy solution:\n" + str(np.linalg.solve(A1, b1Alternative)-x1[2]))

'''
Bei Rechnung 1 hat bei beiden Varianten von b1 keinen Unterschied.
'''


#A2X

A2 = np.array([[2,7,3],
               [-4,-10,0],
               [12,34,9]])

b2 = np.array([[25],
               [-24],
               [107]])

b2Alternative = np.array([[5],
               [-22],
               [42]])

x2 = muellti3_S6_Aufg2(A2, b2Alternative)
print("Task 2")
print("My solution:\nUpper triangle matrix U:\n" + str(x2[0]) + "\nSolution vector:\n"
      + str(x2[2]) + "\nDeterminant of A:\n" + str(x2[1]))

print("Solution of Numpy.linal.solve():\n" + str(np.linalg.solve(A2, b2Alternative)))
print("Difference from my solution and numpy solution:\n" + str(np.linalg.solve(A2, b2Alternative)-x2[2]))

'''
Bei Rechnung 2 hat es bei beiden Varianten von b2 einen kleinen Unterschied. Der Unterschied ist im bereich von e^-15
Numby hat bessere Methoden um Fehlerminimuerung zu erhöhen. Meine hat wahrscheinlich gewisse
Rundungsfehler.
'''


#A3X

A3 = np.array([[-2,5,4],
               [-14,38,22],
               [6,-9,-27]])

b3 = np.array([[1],
               [40],
               [75]])
b3Alternative = np.array([[16],
               [82],
               [-120]])


x3 = muellti3_S6_Aufg2(A3, b3Alternative)

print("Task 3")
print("My solution:\nUpper triangle matrix U:\n" + str(x3[0]) + "\nSolution vector:\n"
      + str(x3[2]) + "\nDeterminant of A:\n" + str(x3[1]))

print("Solution of Numpy.linal.solve():\n" + str(np.linalg.solve(A3, b3Alternative)))
print("Difference from my solution and numpy solution:\n" + str(np.linalg.solve(A3, b3Alternative)-x3[2]))

'''
Gleich wie bei der Rechnung 2 hat Rechnung 3 ei beiden Varianten von b3 einen unterschied im bereich von e^-15
'''


A4 = np.array([[-1, 2, 3, 2, 5, 4, 3, -1],
[3, 4, 2, 1, 0, 2, 3, 8],
[2, 7, 5, -1, 2, 1, 3, 5],
[3, 1, 2, 6, -3, 7, 2, -2],
[5, 2, 0, 8, 7, 6, 1, 3],
[-1, 3, 2, 3, 5, 3, 1, 4],
[8, 7, 3, 6, 4, 9, 7, 9],
[-3, 14, -2, 1, 0, -2, 10, 5]])

b4 = np.array([[-11], [103], [53], [-20], [95], [78], [131], [-26]])

x4 = muellti3_S6_Aufg2(A4, b4)

print("Task 3")
print("My solution:\nUpper triangle matrix U:\n" + str(x4[0]) + "\nSolution vector:\n"
      + str(x4[2]) + "\nDeterminant of A:\n" + str(x4[1]))

print("Solution of Numpy.linal.solve():\n" + str(np.linalg.solve(A4, b4)))
print("Difference from my solution and numpy solution:\n" + str(np.linalg.solve(A4, b4)-x4[2]))

'''
Gleich wie bei der Rechnung 2 hat Rechnung 4 einen unterschied im bereich von e^-15
'''


