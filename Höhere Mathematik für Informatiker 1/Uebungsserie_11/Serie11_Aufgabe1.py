import math

#a)
number = 3-11j

def complex_normalform_to_exponential_trigonometisch_form(number):
    x = number.real
    y = number.imag

    r = (x**2 + y**2)**(1/2)
    phi = math.asin(y/r)

    print("R0: " + str(r))
    print("Phi: " + str(phi))
    return r,phi

r, phi = complex_normalform_to_exponential_trigonometisch_form(number)

