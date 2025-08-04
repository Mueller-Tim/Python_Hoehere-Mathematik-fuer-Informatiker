import numpy as np


def f_2(x):
    return -2 * x ** (-2)


def f_4(x):
    return -12 * x ** (-4)


x = np.linspace(1, 2, 10000)

max_f_2 = np.max(np.abs(f_2(x)))
max_f_4 = np.max(np.abs(f_4(x)))

print("max_f_2: ", max_f_2)
print("max_f_4: ", max_f_4)
