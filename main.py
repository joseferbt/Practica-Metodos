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



for i in range(1,Nx-1):
    for j in range(1,Ny-1):
        velx[i][j] = velx[i][j] + w * 1/4*(auxVx[i+1][j]+auxVx[i-1][j]+auxVx[i][j+1]+auxVx[i][j-1]
                                       -(h/2)*velx[i][j]*(auxVx[i+1][j]-auxVx[i-1][j])
                                       -(h/2)*velx[i][j]*(auxVx[i][j+1]-auxVx[i][j-1])
                                       -(h/2)*p*p)-velx[i][j]


print(velx)
""""
vx = [[1,0,0,0],
      [1,0,0,0],
      [1,0,0,0],
      [1,0,0,0]]

r = [[0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]]
pMasI = 5
PMenosI = 9

def prueba1r(h):
    for i in range(0,len(vx)-1):
        for j in range(0,len(vx)-1):
          r[i][j]=  ((1/4)*vx[i+1][j]+
            (1/4)*vx[i-1][j]
            +(1/4)*vx[i][j+1]
            +(1/4)*vx[i][j-1]
            -((1/4)*(h/2)*vx[i][j]*vx[i+1][j])+((1/4)*(h/2)*vx[i][j]*vx[i-1][j])
            -((1/4)*(h/2)*vx[i][j]*vx[i][j+1])+((1/4)*(h/2)*vx[i][j]*vx[i][j-1])
            -((1/4)*(h/2)*pMasI)+((1/4)*(h/2)*PMenosI))   - vx[i][j]

prueba1r(1)

def pruebavx(w):
    for i in range(0,len(vx)):
        for j in range(0,len(vx)):
          vx[i][j]=  vx[i][j]   + w*r[i][j]        

pruebavx(2)

print(vx)
"""

