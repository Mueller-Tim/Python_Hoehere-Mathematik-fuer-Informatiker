
import numpy as np

import matplotlib.pyplot as plt

from matplotlib import cm

def plotten_wireframe(x,y,z, title, xLabel, yLabel, zLabel):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(x, y, z, rstride=5, cstride=5)
    plt.title(title + " 3d mit Wireforum")
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    ax.set_zlabel(zLabel)
    plt.show()

def plotten_surface(x,y,z, title, xLabel, yLabel, zLabel):
    fig = plt.figure(1)
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.title(title + " 3d mit surface und Colormap")
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    ax.set_zlabel(zLabel)
    plt.show()

def plotten_contour(x,y,z, title, xLabel, yLabel):
    fig = plt.figure()
    cont = plt.contour(x, y, z, cmap=cm.coolwarm)
    fig.colorbar(cont, shrink=0.5, aspect=5)
    plt.title(title + "2d mit Höhenlinien")
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.show()

##a)

g = 9.81
[v0,a] = np.meshgrid(np.linspace(0,100), np.linspace(0+0.1,np.pi / 2-0.1));

def W(v0, a):
    return (v0**2 * np.sin(2 * a)) / g

w = W(v0, a)

weitwurf = 'Weitwurf'
weitwurf_xLabel = 'Anfangsgeschwindigkeit (m/s)'
weitwurf_yLabel = 'Winkel in PI'
weitwurf_zLabel = 'Distanz'

plotten_wireframe(v0,a,w,weitwurf,weitwurf_xLabel,weitwurf_yLabel,weitwurf_zLabel)

plotten_surface(v0,a,w,weitwurf,weitwurf_xLabel,weitwurf_yLabel,weitwurf_zLabel)

plotten_contour(v0,a,w,weitwurf,weitwurf_xLabel,weitwurf_yLabel)


##b)

r = 8.31

def P(v,t):
    return (r * t) / v

[v,t] = np.meshgrid(np.linspace(0,0.2), np.linspace(0,10 ** 4));

p = P(v, t)

druckTitel = 'Druckgleichung'
volumen = 'Volumen m^2'
temperatur = 'Absolute Temperatur in K'
druck = 'Druck in N/m^2'


plotten_wireframe(v,t,p,druckTitel,volumen,temperatur,druck)
plotten_surface(v,t,p,druckTitel,volumen,temperatur,druck)
plotten_contour(v,t,p,druckTitel,volumen,temperatur)

def V(p,t):
    return r * t / p

[p,t] = np.meshgrid(np.linspace(1e4,1e5), np.linspace(0,1e4));

v = V(p, t)

volumenTitel = 'Volumengleichung'

plotten_wireframe(p,t,v,volumenTitel,druck,temperatur,volumen)
plotten_surface(p,t,v,volumenTitel,druck,temperatur,volumen)
plotten_contour(p,t,v,volumenTitel,druck,temperatur)


def T(p,v):
    return p * v / r

[p,v] = np.meshgrid(np.linspace(1e4,1e6), np.linspace(0,10));

t = T(p, v)


temperaturTitel = 'Temperaturgleichung'

plotten_wireframe(p,v,t,temperaturTitel,druck,volumen,temperatur)
plotten_surface(p,v,t,temperaturTitel,druck,volumen,temperatur)
plotten_contour(p,v,t,temperaturTitel,druck,volumen)