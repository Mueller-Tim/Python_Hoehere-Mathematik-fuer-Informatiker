import numpy as np

printAFlag = 1
printBFlag = 1
printCFlag = 1

print("************************Task A************************")
k = 100
A = np.array([[1, -2, 0],
              [2, 0, 1],
              [0, -2, 1]])


def muellti3_S12_Aufg4(A, k):
    P = np.identity(np.size(A, axis=0))
    for i in range(k):
        [Q, R] = np.linalg.qr(A)
        A = R @ Q
        P = P @ Q
    return [A, P]


[Ak, Pk] = muellti3_S12_Aufg4(A, k)

if(printAFlag):
    print(Ak)
    print("****************")
    print(Pk)

print("************************Task B************************")
A = np.array([[6, 1, 2, 1, 2],
              [1, 5, 0, 2, -1],
              [2, 0, 5, -1, 0],
              [1, 2, -1, 6, 1],
              [2, -1, 0, 1, 7]])

[Ak, Pk] = muellti3_S12_Aufg4(A, k)

if(printBFlag):
    # Folgende Berechunung erzeugt die Einheitsmatrix
    with np.printoptions(precision=2):
        print(Pk @ np.linalg.inv(Pk))
        print("****************")
        print(Ak)
        print("****************")
        print(Pk)
        print("Die Eigenvektoren sind:")
        print(Ak.diagonal())
        print("Zuordnung der Eigenvektoren & Eigenwerte")
        for i in np.arange(0,np.shape(Ak)[0]):
            print(Ak[i,i], Pk[:,i])


print("************************Task C************************")
[W, V] = np.linalg.eig(A)


if(printCFlag):
    with np.printoptions(precision=2):
        print("Eigenwerte:")
        print(W)
        print("Eigenvektoren:")
        print(V)
        for i in np.arange(0,np.shape(Ak)[0]):
            print(W[i], V[:,i])

#Der Vorteil ist, np.linalg.eig kann mit komplexen Eigenwerten umgehen