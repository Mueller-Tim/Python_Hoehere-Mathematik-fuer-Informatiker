import matplotlib.pyplot as plt


from muellti3_S1_Aufg2 import polynom

a = [1, -5, -30, 110, 29, -105]
xmin = -10
xmax = 10.01
x, p, dp, pint = polynom(a, xmin, xmax)

plt.plot(x, p, x, dp, x, pint)
plt.xlim(-10, 10)
plt.ylim(-1500, 1500)

plt.legend(['Polynom f(x)', 'Ableitung', 'Stammfunktion'])
plt.title('Darstellung eines Polynoms, der Ableitung und der Stammfunktion')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()