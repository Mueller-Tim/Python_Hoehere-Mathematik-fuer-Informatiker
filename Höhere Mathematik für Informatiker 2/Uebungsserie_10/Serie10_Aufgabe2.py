import matplotlib.pyplot as plt
import numpy as np

g = 9.81

tA = 0
tE = 190

vRel = 2_600

mA = 300_000
mE = 80_000

massenstrom = (mA - mE) / tE


def a(t):
    return vRel * massenstrom / (mA - massenstrom * t) - g


n = tE * 10
t = np.linspace(tA, tE, n)


def muellti3_S8_Aufg3a(x, y):
    x_a = x.copy()
    y_a = y.copy()
    n = x.size

    Tf_neq = 0
    for i in range(0, n - 1):
        Tf_neq += ((y_a[i] + y_a[i + 1]) / 2 * (x_a[i + 1] - x_a[i]))
    return Tf_neq


a = a(t)

##a und b)

plt.figure(0)
plt.plot(t, a)
plt.title("Beschleunigung über Zeit a(t)")
plt.xlabel("Zeit [s]")
plt.ylabel("Beschleuningung [m/s²]")

v = np.zeros(n)
for i in range(1, n):
    v[i] = muellti3_S8_Aufg3a(t[0:i + 1], a[0:i + 1])

h = np.zeros(n)
for i in range(1, n):
    h[i] = muellti3_S8_Aufg3a(t[0:i + 1], v[0:i + 1])


def geschwindigkeit(t):
    return vRel * np.log(mA / (mA - massenstrom * t)) - g * t


plt.figure(1)
plt.title('v(t)')
plt.plot(t, v, label='numerisch')
plt.plot(t, geschwindigkeit(t), label='analytisch')
plt.xlabel('t')
plt.ylabel('v')
plt.legend()


def strecke(t):
    return -((vRel * (mA - massenstrom * t)) / massenstrom) * np.log(
        mA / (mA - massenstrom * t)) + vRel * t - 0.5 * g * t ** 2

plt.figure(2)
plt.title('h(t)')
plt.plot(t, h, label='numerisch')
plt.plot(t, strecke(t), label='analytisch')
plt.xlabel('t')
plt.ylabel('h')
plt.legend()
plt.show()

print('g_max:', a[n - 1] / g)
print('v_max:', v[n - 1])
print('h_max:', h[n - 1])
