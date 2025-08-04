import numpy as np
import matplotlib.pyplot as plt

data=np.array([
    [1971, 2250.],
    [1972, 2500.],
    [1974, 5000.],
    [1978, 29000.],
    [1982, 120000.],
    [1985, 275000.],
    [1989, 1180000.],
    [1989, 1180000.],
    [1993, 3100000.],
    [1997, 7500000.],
    [1999, 24000000.],
    [2000, 42000000.],
    [2002, 220000000.],
    [2003, 410000000.],
    ])

##1)

def f1(x):
    return 1

def f2(x):
    return x-1970

def f(x, lam):
    return lam[0] * f1(x) + lam[1] * f2(x)

x = data[:,0]
y = np.log10(data[:,1])

A = np.zeros([x.size,2])
A[:,0] = f1(x)
A[:,1] = f2(x)

[Q,R] = np.linalg.qr(A)
lamda = np.linalg.solve(R,Q.T@y)
x_fine = np.arange(x[0], x[-1] + 0.1, 0.1)
plt.plot(x, y, 'o', color="red", label='real Data')
plt.plot(x_fine,f(x_fine,lamda), color="blue", label='predicted Data')
plt.xlabel('Jahr')
plt.ylabel('Transistoren pro Chip in $10^y$')
plt.legend()
plt.title("Transistoren")
plt.show()

##2)

y_2015 = f(2015,lamda)
print("predicted value for 2015 is 10^(" + str(y_2015) + str(")"))
print("Real value was 4 * 10⁹")

'''
Der erwartete Wert war mit 10¹⁰ höher als 10⁹
'''
##3)

print("Theta 0 (y-verschiebung in log10) = ", lamda[0])
print("Theta 1 (steigung in log10) = ", lamda[1])

'''
Die Steigung ist 10⁰·¹⁵⁴ was 1.4, was bedeutet das jedes jahr es um 1.4 wächst
Das heisst nach mit verdoppelt es sich alle 1.4 jahre
'''