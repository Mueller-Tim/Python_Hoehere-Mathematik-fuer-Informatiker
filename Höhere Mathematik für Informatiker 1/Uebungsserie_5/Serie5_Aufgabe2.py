import math

d = 10
v = 471


def f(h):
    return (math.pi * h ** 2) / 6 * (3*d-2*h)-471


def fab(h):
    return -h ** 2 * math.pi + 10 * math.pi * h


h0 = 9
hn = h0
hn_1 = 0
absolutError = 10 ** (-3)
counter = 0
while abs(hn - hn_1) > absolutError:
    hTemp = hn - f(hn) / fab(hn)
    hn_1 = hn
    hn = hTemp
    counter += 1
    print(hn)

print("Number of Iteration: " + str(counter))
print("Max h after " + str(counter) + " Iterations: " + str(hn))