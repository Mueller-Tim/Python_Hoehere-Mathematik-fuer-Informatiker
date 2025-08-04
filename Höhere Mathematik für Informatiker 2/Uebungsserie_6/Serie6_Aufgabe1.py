import numpy as np
import matplotlib.pyplot as plt

##a)
x = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
y = np.array([999.9, 999.7, 998.2, 995.7, 992.2, 988.1, 983.2, 977.8, 971.8, 965.3, 958.4])

def f1(x):
    return x ** 2


def f2(x):
    return x

def f3(x):
    return 1

def f(x, lam):
    return lam[0] * f1(x) + lam[1] * f2(x) + lam[2] * f3(x)

def fehlerfunktionale(y,x,lam):
    summe = 0
    for i in range(x.size):
        summe += (y[i]-f(x[i],lam))**2
    return summe

A = np.zeros([11,3])
A[:,0] = f1(x)
A[:,1] = f2(x)
A[:,2] = f3(x)

x_fine = np.arange(x[0], x[-1] + 0.1, 0.1)

## ohne QR zerlegung
lamda = np.linalg.solve(A.T @ A, A.T @ y)
print(lamda)
plt.figure(0)
plt.plot(x, y, 'o', color="red", label='data')
plt.plot(x_fine,f(x_fine,lamda), color="blue", label='f(x)=a*x²+b*x+c')
plt.xlabel('x')
plt.ylabel('y=f(x)')
plt.legend()
plt.title("Ohne QR-Zerlegung")

## mit QR zerlegung

[Q,R] = np.linalg.qr(A)

lamda = np.linalg.solve(R,Q.T@y)
print(lamda)

fehlerfunktionale_a = fehlerfunktionale(y,x,lamda)

plt.figure(1)
plt.plot(x, y, 'o', color="red", label='data')
plt.plot(x_fine,f(x_fine,lamda), color="blue", label='f(x)=a*x²+b*x+c')
plt.xlabel('x')
plt.ylabel('y=f(x)')
plt.legend()
plt.title("Mit QR-Zerlegung")

##b)
konditionszahl_ohne_qr = np.linalg.cond(A.T@A)
konditionszahl_mit_qr = np.linalg.cond(R)
print(konditionszahl_ohne_qr)
print(konditionszahl_mit_qr)

'''
Die Konditizionszahl mit QR-Zerlegung ist viel kleiner, also besser als ohne QR Zerlegung.
'''

##c)

lamda = np.polyfit(x,y,2)
print(lamda)
fehlerfunktionale_c = fehlerfunktionale(y,x,lamda)
plt.figure(2)
plt.plot(x, y, 'o', color="red", label='data')
plt.plot(x_fine,f(x_fine,lamda), color="blue", label='f(x)=a*x²+b*x+c')
plt.xlabel('x')
plt.ylabel('y=f(x)')
plt.legend()
plt.title("Mit polyfit")
plt.show()

##d)

print("fehlerfunktionale_a", fehlerfunktionale_a)
print("fehlerfunktionale_c", fehlerfunktionale_c)
'''
in schnellform
fehlerfunktionale = np.linal.norm(y-ya)**2

sie sind sehr ähnlich
fehlerfunktionale_a 1.5393379953382047
fehlerfunktionale_c 1.5393379953380506
'''

