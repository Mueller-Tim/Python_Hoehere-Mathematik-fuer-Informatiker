import math


def muellti3_S5_Aufg3(f,x0,x1,tol):
    xn = x1
    xn_1 = x0
    while abs(xn-xn_1) > tol:
        temp = xn - (xn - xn_1) / (f(xn) - f(xn_1)) * f(xn)
        xn_1 = xn
        xn = temp
        print(xn)

    print(f(xn))

'''
Beim Newtonverfahren müsste man die Ableitung noch mitliefern,
dies wäre einfach möglich wenn man die mullti3_S5_Aufg3() funktion anpassen würde
'''


'''
Überprüfung Aufgabe 1
Achtung, mit dem Sekantenverfahren springt X sprungfahrt auf eine sehr kleine Zahl
Diese Zahl kann man ignorieren. Man nimmt die Zahl kurz vor dem sprung.
'''


def f(x):
    return math.e ** (x ** 2) + x ** (-3) - 10


x0 = 2.0
x1 = 1.795040766664155
tol = 10 ** (-3)
print("Startwert x0 = 2 und x1 = 1.7")
muellti3_S5_Aufg3(f, x0, x1, tol)

x0 = 0.5
x1 = 0.4846738810503588
print("Startwert x0 = 0.5 und x1 = 0.48")
muellti3_S5_Aufg3(f, x0, x1, tol)


x0 = -1.0
x1 = -1.2
print("Startwert x0 = -1 und x1 = -1.2")
muellti3_S5_Aufg3(f, x0, x1, tol)

'''
Überprüfung Aufgabe 2
'''
d = 10
v = 471


def f(h):
    return (math.pi * h ** 2) / 6 * (3*d-2*h)-471


x0 = 9
x1 = 7.658217376951714
print("Startwert x0 = 9 und x1 = 7.68")
muellti3_S5_Aufg3(f, x0, x1, tol)