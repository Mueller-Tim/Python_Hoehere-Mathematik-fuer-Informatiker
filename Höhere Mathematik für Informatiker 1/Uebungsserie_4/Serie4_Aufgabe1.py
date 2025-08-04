def fn_1(x):
    return ((230*x**4+18*x**3+9*x**2-9)/221)

def fn_1Ableitung(x):
    return ((4*230*x**3)/221+(3*18*x**2)/221+(2*9*x)/221)

x01 = -1
x02 = 1
tolerance = 10**(-6)

def iteration(nullstelle, tolerance, xn, index):
    xn1 = fn_1(xn)

    if abs(xn - xn1) < tolerance:
        print("Nullstelle für: " + str(nullstelle) + ", Iteration: " + str(index) + ", Lösung: " + str(xn1))
    else:
        index += 1
        iteration(nullstelle, tolerance, xn1, index)


def aufgabeA(x0, tolerance):
    if(fn_1Ableitung(x0) < 1):
        iteration(x0, tolerance, x0, 1)
    else:
        print("Nullstelle für: " + str(x0) + " ist abstossend")


aufgabeA(x01, tolerance)
aufgabeA(x02, tolerance)

