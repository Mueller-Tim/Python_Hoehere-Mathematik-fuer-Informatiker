import matplotlib.pyplot as plt
import numpy
import numpy as np
from muellti3_S7_Aufg3_Gaus import muellti3_S6_Aufg2

##a)
A = np.array([[0**3, 0**2, 0, 1],
              [2**3, 2**2, 2, 1],
              [9**3, 9**2, 9, 1],
              [13**3, 13**2, 13, 1]])

b = np.array([[150],
              [104],
              [172],
              [152]])

A_Triangle, a_determinate, xa = muellti3_S6_Aufg2(A, b)
print(A)
print(a_determinate)

def polynomPower3(xValue, x):
    a = x[0][0]
    b = x[1][0]
    c = x[2][0]
    d = x[3][0]
    return a * (xValue ** 3) + b * (xValue ** 2) + c * xValue + d

def calculateDaysForYears(years, x):
    days = polynomPower3(years, x)
    return days

stepSize = 0.1
years = np.arange(0, 20+stepSize, stepSize)

plt.figure(1)
plt.plot(years + 1997, calculateDaysForYears(years, xa), label="Aufgabe a")
plt.ylim(60,200)
plt.xlim(1996, 2013)
plt.scatter([1997, 1999, 2006, 2010], [150, 104, 172, 152], color='red', label="Jahreswerte")  # Rote Punkte für die spezifischen Daten
plt.xlabel("years")
plt.ylabel("days with uv rays")
plt.title("days with uv rays")
plt.grid()


##b)
year2003 = 2003-1997
year2004 = year2003 + 1
print("Annahme für Jahr 2003 in gerundeten Anzahl Tage mit meiner Rechnung: " + str(calculateDaysForYears(year2003, xa)))

print("Annahme für Jahr 2004 in gerundeten Anzahl Tage mit meiner Rechnung: " + str(calculateDaysForYears(year2004, xa)))


##c)
yearPolyfit = np.array([1997, 1999, 2006, 2010])
yearPolyfit = yearPolyfit - yearPolyfit[0]



daysPolyfit = np.array([[150],
                        [104],
                        [172],
                        [152]])

grad = 3
coefficientPolyfit = np.polyfit(yearPolyfit, daysPolyfit, grad)


plt.plot(years + 1997, calculateDaysForYears(years, coefficientPolyfit), label="Aufgabe b")
plt.legend("Aufgabe b")
plt.show()

print("Annahme für Jahr 2003 in gerundeten Anzahl Tage mit polyfit: " + str(calculateDaysForYears(year2003, coefficientPolyfit)))

print("Annahme für Jahr 2004 in gerundeten Anzahl Tage mit polyfit: " + str(calculateDaysForYears(year2004, coefficientPolyfit)))

print("Unterschied im Jahr 2003: " + str(abs(calculateDaysForYears(year2003, coefficientPolyfit)-calculateDaysForYears(year2003, xa))))

print("Unterschied im Jahr 2004: " + str(abs(calculateDaysForYears(year2004, coefficientPolyfit))-calculateDaysForYears(year2004, xa)))