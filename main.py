import numpy as np
#import pip pip.main(["install","matplotlib"])
import matplotlib.pylab as p

Nx = 10
Ny = 10
vy = np.zeros((Nx + 1, Ny + 1), float)
vx = np.zeros((Nx + 1, Ny + 1), float)
iter = 0
pMasI = 1
PMenosI = 1
h = 1.0
w = 1.0
vo = 1.0
a = " "

for i in range(Nx):
    for j in range(Ny):
        if j == 0:
            vx[i][j] = 0
        else:
            vx[i][j] = j


def prueba1r(w, h):
    for i in range(1, Nx):
        for j in range(1, Ny):
            r1 = w * (((1 / 4) * vx[i + 1][j] +
                       (1 / 4) * vx[i - 1][j]
                       + (1 / 4) * vx[i][j + 1]
                       + (1 / 4) * vx[i][j - 1]
                       - ((1 / 4) * (h / 2) * vy[i][j] * vx[i + 1][j]) + (
                                   (1 / 4) * (h / 2) * vy[i][j] * vx[i - 1][j])  # es cero
                       - ((1 / 4) * (h / 2) * vx[i][j] * vx[i][j + 1]) + ((1 / 4) * (h / 2) * vx[i][j] * vx[i][j - 1])
                       - ((1 / 4) * (h / 2) * pMasI) + ((1 / 4) * (h / 2) * PMenosI)) - vx[i][j])
            vx[i][j] = vx[i][j] + r1


while (iter <= 6):
    iter += 1
    if iter % 10 == 0: print(iter)
    prueba1r(w, h)

for i in range(0, Nx + 1):
    for j in range(0, Ny + 1): vx[i][j] = vx[i][j] / vo * h

# print(vx)

x = range(0, Nx - 1);
y = range(0, Ny - 1)
X, Y = p.meshgrid(x, y)


def functz(u):
    z = u[X, Y]
    return z


Z = functz(vx)

fig, ax = p.subplots()

ax.pcolormesh(X, Y, Z, vmin=-0.5, vmax=1.0)

p.show()
"""
1
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

# Se imprime la velocidad x
print(imprimir(vx, a))

2
import numpy as np
Nx = 10
Ny = 10
velx = np.zeros((Nx,Ny))
auxVx = []
p = 1
h=1
w=1
for i in range(Nx):
    auxVx.append([])
    for j in range(Ny):
        if(j==0):
            velx[i][j]=1
        auxVx[i].append(((j+1)))


print(velx)

for i in range(1,Nx-1):
    for j in range(1,Ny-1):
        velx[i][j] = velx[i][j] + w * 1/4*(auxVx[i+1][j]+auxVx[i-1][j]+auxVx[i][j+1]+auxVx[i][j-1]
                                       -(h/2)*velx[i][j]*(auxVx[i+1][j]-auxVx[i-1][j])
                                       -(h/2)*velx[i][j]*(auxVx[i][j+1]-auxVx[i][j-1])
                                       -(h/2)*p*p)-velx[i][j]

for i in range(5):
    pruebavx(w)
    print("[",i,"]")
    print(imprimir(vx, a))


# Se imprime la velocidad x """

