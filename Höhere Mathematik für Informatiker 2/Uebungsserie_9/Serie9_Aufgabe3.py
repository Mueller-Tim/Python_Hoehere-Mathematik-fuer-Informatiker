import numpy as np

def trapezoidal_integration(func, start, end, steps):
    integral = 0
    step_size = (end - start) / steps
    for i in range(1, steps):
        integral += func(start + i * step_size)
    return step_size * ((func(start) + func(end)) / 2 + integral)

def advanced_romberg_integration(target_function, lower_bound, upper_bound, depth):
    size = depth + 1
    R = np.zeros((size, size))

    for i in range(size):
        R[i, 0] = trapezoidal_integration(target_function, lower_bound, upper_bound, 2 ** i)

    for j in range(1, size):
        for i in range(depth - j, -1, -1):
            R[i, j] = (4 ** j * R[i + 1, j - 1] - R[i, j - 1]) / (4 ** j - 1)

    return R[0, depth]

def example_function(x):
    return np.cos(x ** 2)


print(advanced_romberg_integration(example_function, 0, np.pi, 4))
