
### Lagrange-Interpolation
def lagrange_int(x,y,x_int):

    if(len(x) != len(y)):
        raise ValueError("Length of x and y must be equal!")

    n = len(x)
    y_int = 0

    for i in range(n):

        li = 1

        for j in range(n):

            if i != j:
                li *= (x_int-x[j]) / (x[i]-x[j])

        y_int += y[i] * li

    return y_int

### Werte aus aufgabe 1

x = [0,2500,5000,10000]
y = [1013,747,540,226]

x_int = 3750

y_int = lagrange_int(x,y,x_int)

print("Y_int:", y_int)
