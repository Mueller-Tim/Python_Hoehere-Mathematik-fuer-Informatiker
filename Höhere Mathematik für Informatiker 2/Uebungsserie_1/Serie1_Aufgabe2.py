import numpy as np

import matplotlib.pyplot as plt
def plotten_wireframe(x,y,z, title, xLabel, yLabel, zLabel):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(x, y, z, rstride=5, cstride=5)
    plt.title(title + " 3d mit Wireforum")
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    ax.set_zlabel(zLabel)
    plt.show()

c = 1

def wF(x,t):
    return np.sin(x + c * t)


def vF(x,t):
    return wF(x,t) + np.cos(2 * x + 2 * c * t)

[x,t] = np.meshgrid(np.linspace(0,np.pi * 2), np.linspace(0,np.pi * 2));

w = wF(x,t)

v = vF(x,t)

auslenkung = "Auslenkung"
ort = "Ort"
zeit = "Zeit"

plotten_wireframe(x,t,w,"w(x,t)", ort, zeit, auslenkung)
plotten_wireframe(x,t,v,"v(x,t)", ort, zeit, auslenkung)