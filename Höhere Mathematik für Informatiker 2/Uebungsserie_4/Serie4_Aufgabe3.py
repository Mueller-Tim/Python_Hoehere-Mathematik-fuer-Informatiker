import numpy as np
import matplotlib.pyplot as plt

##a)

plt.figure(0)
x = np.array([1981,1984,1989,1993,1997,2000,2001,2003,2004,2010])

y = np.array([0.5,8.2,15,22.9,36.6,51,56.3,61.8,65,76.7])

coefficients = np.polyfit(x, y, len(x)-1)

x_extended = np.arange(1975,2020,0.1)

y_extended = np.polyval(coefficients, x_extended)

plt.plot(x,y,"ro")
plt.scatter(x_extended,y_extended)
plt.title("Aufgabe a)")
plt.ylabel("Jahr")
plt.xlabel("Haushalte mit Computer [%]")
plt.ylim(-100,250)

for i in range(len(x)):
    y_approx = np.polyval(coefficients, x[i])
    if y[i] == y_approx:
        print("Yes for "+ str(x[i]) +"is the same")
    else:
        print("no, the real value is " + str(y[i]) + " and the aproximated value is ", y_approx)

'''
Nein der Wert ist nur gerundet.
'''

##b)





plt.figure(1)

x_b = x-x.mean()
coefficients = np.polyfit(x_b, y, len(x_b)-1)
x_extended_b = x_extended - x.mean()
y_extended = np.polyval(coefficients, x_extended_b)

plt.plot(x,y,"ro")
plt.scatter(x_extended,y_extended)
plt.title("Aufgabe b)")
plt.ylabel("Jahr")
plt.xlabel("Haushalte mit Computer [%]")
plt.ylim(-100,250)


'''
b) geht zwar durch alle punkte geht aber links und rechts unnatürlich schnell in die Höhe.
Ist also zimlich nutzlos abgsehen vo diesen Punkten.
'''

##c)

'''
Der Schätzwert ist nicht mehr im Bereich von minus 100 und 250.
Da es nur Prozentzahlen bei der Y werte sind, machen alles über 100% und unter 0% keinen Sinn.
Solche Werte mit Polynomen höheren Ordnung können ausherhalb des Intervalls nicht benutzt werden. 
'''

##d)

plt.figure(2)

def lagrange_int(x,y,x_vec):
    if (len(x) != len(y)):
        raise ValueError("Length of x and y must be equal!")

    y_vec = []

    for x_int in x_vec:

        n = len(x)
        y_int = 0

        for i in range(n):

            li = 1

            for j in range(n):

                if i != j:
                    li *= (x_int - x[j]) / (x[i] - x[j])

            y_int += y[i] * li

        y_vec.append(y_int)

    return y_vec

xc = np.arange(1981,2010,0.1)

yc = lagrange_int(x,y,xc)

plt.plot(x,y,"ro")
plt.scatter(xc,yc, color="blue", label="Aufgabe d)")
plt.scatter(x_extended,y_extended, color="green", label="Aufgabe b)")
plt.title("Aufgabe d)")
plt.ylabel("Jahr")
plt.xlabel("Haushalte mit Computer [%]")
plt.ylim(-100,250)
plt.legend()
plt.show()

'''
Die Methoden b) und d) sind sehr ähnlich aus.
Wahrscheinlich nutzt polifit und polival eine ähnliche funktion wie die von mir.
'''