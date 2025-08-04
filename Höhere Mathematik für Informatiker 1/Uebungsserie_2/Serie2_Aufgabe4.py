##a)
verkleinerungsfaktor = 0.99999  # Faktor um den epsilon sukessiv verkleinert wird
epsilon = 1  # Startwert für epsilon

while (1 + epsilon > 1):
    epsilon = epsilon * verkleinerungsfaktor

print('Die Machinengenaugkeit beträgt:', epsilon)

'''
Die Machinengenaugkeit beträgt: 1.1102195668629618e-16 das entspricht dem binären Wert 2^-53
Also rechnet der Rechner im Dualsystem. Er rechnet mit der Stellenzahl 52 (aus 2^-52 abgeleitet).
'''


##b)
qMax = float(1.9999999999 * 2**52)
step = float(1)
while True:
    if float(qMax) != float(qMax + 1):
        print("Die maximal grosse Zahl lautet:", qMax)
        break
    qMax += float(step)

'''
Resultat
Wenn die Maschinengenauigkeit 2^53 beträgt, dann ist die grösste darstellbare Zahl in 2s Complement (2^52)-1
Die grösste Zahl ist genau der Kehrwert von eps. Desto genauer ein Algorithmus an diesen Kehrwert kommt, desto besser
oder eher genauer ist der Algorithmus.
'''