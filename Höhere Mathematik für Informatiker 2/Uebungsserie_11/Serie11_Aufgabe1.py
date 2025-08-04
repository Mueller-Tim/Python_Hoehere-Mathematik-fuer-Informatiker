import numpy as np
import matplotlib.pyplot as plt

def differentialgleichung_richtungsfeld(f, xmin, xmax, ymin, ymax, hx, hy):

    #i
    X,Y = np.meshgrid(np.arange(xmin,xmax,hx), np.arange(ymin,ymax,hy))

    #ii
    Ydiff = f(X,Y)

    #iii
    plt.figure(1)
    plt.quiver(X,Y,1,Ydiff)
    plt.grid()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Richtungsfeld")
    plt.show()