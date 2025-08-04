import numpy as np
import matplotlib.pyplot as plt
from muellti3_S9_Aufg2 import muellti3_S9_Aufg2

gesammelte_dxmax = np.array([])
gesammelte_dxobs = np.array([])
verhaeltnis_dxmax_dxobs = np.array([])
indexbereich = np.arange(0, 1000)


for i in indexbereich:
    ZufallsMatrix = np.random.rand(100, 100)
    ZufallsVektor = np.random.rand(100, 1)
    NaherungMatrix = ZufallsMatrix + np.random.rand(100, 100) / 1e5
    NaherungVektor = ZufallsVektor + np.random.rand(100, 1) / 1e5
    [loesung, loesung_approx, max_dx, beob_dx] = muellti3_S9_Aufg2(ZufallsMatrix, NaherungMatrix, ZufallsVektor, NaherungVektor)
    gesammelte_dxmax = np.append(gesammelte_dxmax, max_dx)
    gesammelte_dxobs = np.append(gesammelte_dxobs, beob_dx)
    verhaeltnis_dxmax_dxobs = np.append(verhaeltnis_dxmax_dxobs, max_dx / beob_dx)


plt.figure(1)
plt.semilogy(gesammelte_dxmax, label="Maximale Delta x")
plt.semilogy(gesammelte_dxobs, label="Beobachtete Delta x")
plt.semilogy(verhaeltnis_dxmax_dxobs, label="Verhältnis Max/Beob")
plt.legend()
plt.grid(True)
plt.xlabel("Index")
plt.ylabel("Werte")
plt.title("Analyse der Delta x Werte")
plt.show()

# Kommentar zum Verständnis des Ergebnisses
# Die obere Schranke (maximale Delta x) liegt immer über der beobachteten Delta x,
# was zeigt, dass sie realistisch und korrekt ist. Jedoch ist diese Schranke
# in der Regel um den Faktor 1e3 größer als die beobachtete Delta x.
