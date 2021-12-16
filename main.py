import numpy as np

Nx = 10
Ny = 10
vy = np.zeros((Nx, Ny))
r = np.zeros((Nx, Ny))
vx = []
itera = 100
pMasI = 1
PMenosI = 1
h = 1
w = 1
a = " "

for i in range(Nx):
    vx.append([])
    for j in range(Ny):
        vx[i].append(((j + 1)))


def prueba1r(h):
    for i in range(1, len(vx) - 1):
        for j in range(1, len(vx) - 1):
            r[i][j] = ((1 / 4) * vx[i + 1][j] +
                       (1 / 4) * vx[i - 1][j]
                       + (1 / 4) * vx[i][j + 1]
                       + (1 / 4) * vx[i][j - 1]
                       - ((1 / 4) * (h / 2) * vx[i][j] * vx[i + 1][j]) + (
                                   (1 / 4) * (h / 2) * vx[i][j] * vx[i - 1][j])  # es cero
                       - ((1 / 4) * (h / 2) * vx[i][j] * vx[i][j + 1]) + ((1 / 4) * (h / 2) * vx[i][j] * vx[i][j - 1])
                       - ((1 / 4) * (h / 2) * pMasI) + ((1 / 4) * (h / 2) * PMenosI)) - vx[i][j]


prueba1r(h)
# Se imprime r
print(r)


def pruebavx(w):
    for i in range(Nx):
        for j in range(Ny):
            vx[i][j] = vx[i][j] + w * r[i][j]


pruebavx(w)


def imprimir(vx, a):
    for i in range( Nx):
        for j in range(Ny):
            a = a + "  " + str(vx[i][j])
        a += "\n"
    return a

#Flujo constante durante n iteraciones n = itera

for i in range(5):
    pruebavx(w)
    print("[",i,"]")
    print(imprimir(vx, a))

# Se imprime la velocidad x

