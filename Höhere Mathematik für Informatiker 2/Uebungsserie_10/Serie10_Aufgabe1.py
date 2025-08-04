import numpy as np

def trapezoidal_integration(func, start, end, steps):
    integral = 0
    step_size = (end - start) / steps
    for i in range(1, steps):
        integral += func(start + i * step_size)
    return step_size * ((func(start) + func(end)) / 2 + integral)

def romberg_integration(target_function, lower_bound, upper_bound, depth):
    size = depth + 1
    R = np.zeros((size, size))

    for i in range(size):
        R[i, 0] = trapezoidal_integration(target_function, lower_bound, upper_bound, 2 ** i)

    for j in range(1, size):
        for i in range(depth - j, -1, -1):
            R[i, j] = (4 ** j * R[i + 1, j - 1] - R[i, j - 1]) / (4 ** j - 1)

    return R[0, depth]

x0 = 0
t0 = 0
v0 = 100
vE = 0
m = 97000


##a)

def time(v):
    return m / (-5*v**2-570000)

tE = romberg_integration(time,v0,vE,4)
print("Gebrauchte Zeit in Sekunden: ", tE)

##b)

def position(v):
    return (m * v) / (-5 * v **2-570000)

xE = romberg_integration(position, v0,vE,4)

print("Gebrauchte Stecke in Meter: ", xE)