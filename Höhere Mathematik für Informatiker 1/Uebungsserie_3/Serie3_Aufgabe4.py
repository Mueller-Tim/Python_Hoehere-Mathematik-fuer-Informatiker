import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2, 0.01)
h = np.sqrt(100*x**2-200*x+99)
plt.figure(1)
plt.plot(x,h)
plt.xlabel("x")
plt.ylabel("h(x)")
plt.grid()
plt.show()

'''
Beim Plot sieht man, dass ca. 0.9 bis 1.1 keine Werte angezeigt werden.
Es gibt einen Verlist bei der gleitkommazahl, da 1.1 eine Nullstelle ist.
In der Wurzel würde ca 200-200 gerechnet und wurzel von null gezogen.
'''

xa = 1.1

print(100*xa**2-200*xa+99)

#b)

x = np.arange(1.1, 1.3+1e-7, 1e-7)
h = np.abs(np.sqrt(200*x-200)) *np.abs(x) / np.abs(np.sqrt(100*x**2-200*x+99))
plt.figure(2)
plt.semilogy(x, h)
plt.xlabel("x")
plt.ylabel("h(x)")
plt.grid()
plt.show()

'''
Hier sieht man die abbrubte Nustelle sehr gut.
'''


##c) Konditionszahl (falls y sehr gross => kann nicht vermieden werden)
## aber Reduktion ider der Auslöschung möglich: ~h(x) = 10 * wurzel((x-1.1)(x-0.9)) => plot von ~h

x = np.arange(1.1, 1.3+1e-7, 1e-7)
h2 = np.sqrt((x-1.1)*(x-0.9))*10
plt.figure(3)
plt.semilogy(x, h2)
plt.xlabel("x")
plt.ylabel("h2(x)")
plt.grid()
plt.show()

x = np.arange(0, 2,0.01)
h2 = np.sqrt((x-1.1)*(x-0.9))*10
plt.figure(4)
plt.plot(x, h2)
plt.xlabel("x")
plt.ylabel("h2(x)")
plt.grid()
plt.show()

'''
mit dieser FOrmel kann man die reduktion vergleichnern: ~h(x) = 10 * wurzel((x-1.1)(x-0.9))
Wiiisooo???
'''