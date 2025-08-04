import math


def complex_wurzel_exponentialform(n, r0, phi):
    k = 0
    r = r0 ** (1/n)
    print("r: " + str(r))
    while k < n:
        phi_k = (phi + k * 2 * math.pi) / n
        print("phi_" + str(k) + ": " + str(phi_k))
        zk = r * (math.cos(phi_k) + 1j * math.sin(phi_k))
        print("z_" + str(k) + ": " + str(zk))
        k +=1

'''
Z^n = x+y*j
'''

n = 2
number = -2 - math.sqrt(3) * 2j

def complex_normalform_to_exponentialform(number):
    x = number.real
    y = number.imag

    r = (x**2 + y**2)**(1/2)
    phi = math.atan2(y,x)

    print("R0: " + str(r))
    print("Phi: " + str(phi))
    return r,phi

r,phi = complex_normalform_to_exponentialform(number)

complex_wurzel_exponentialform(n, r, phi)