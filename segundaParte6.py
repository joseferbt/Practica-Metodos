import matplotlib.pylab as p 
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D 
from numpy import *
import numpy as np

#Constantes
h = 0.1
wa=1
presion = 1
Nxmax =30#36
Nymax = 30#36
limite = Nxmax*(Nxmax+2)
H = (Nxmax//2)-2
L = Nymax//2
ite=0

#u
uInicial= zeros((Nxmax + 1, Nymax + 1), float )
u= zeros((limite +1, limite + 1), float )
matrizUfinal = zeros((Nxmax + 1, Nymax + 1), float )
Ux= zeros((Nxmax + 1, Nymax + 1), float )
auxInicial = zeros((Nymax + 1, Nxmax + + 1), float )
bVector = zeros((limite + 1,1 ), float )
bVectorAux = salida =[0 for i in range(limite+1)]

# w
wInicial = zeros((Nxmax + 1, Nymax + 1), float )
w = zeros((limite +1, limite + 1), float )
matrizWfinal = zeros((Nxmax + 1, Nymax + 1), float )
W = zeros((Nxmax + 1, Nymax + 1), float )
bVectorW = zeros((limite + 1,1 ), float )
bVectorAuxW = salida =[0 for i in range(limite+1)]



#Barra

def borders():
 for i in range(Nxmax+1):
     for j in range(Nymax+1): 
        uInicial[i][j] = j
        wInicial = 0

borders()
#print(uInicial)
for i in range(Nxmax+1):
    b = Nymax
    for j in range(Nymax+1):
       auxInicial[b][i] = uInicial[i][j]
       b -=1


def llenarMatrix(auxInicial,wInicial):
    aux=2
    i1=0
    j1=0
    ancho =0
    largo =2
    ancho2=0
    largo2=2
    #count = 0
    for i in range(limite+1):

        for j in range(limite+1):
            if(i<=Nxmax+1 or i>=limite-(Nxmax+1) or (i>=((Nxmax+1)*aux)-1 and i<=((Nxmax+1)*aux))):
                if(i==j):
                    u[i][j]=1 
            else:
                if(i>= ((limite)/2)+ancho and i<= ((limite)/2)+ ancho+6):
                  if(i==j):
                    #count += 1
                    u[i][j] =1
                    #print("[]",i,"  ", j)
                    #print(largo, "   " , ancho)
                    largo +=1 
                    if(largo ==5):
                      largo = 2
                      ancho += Nxmax+1                  
                else:
                 if(i==j):
                   u[i][j]=1
                   u[i][j-1]= (-1/4)-((h/8)*wInicial[i1][j1]) #wInicial[i1][j1]
                   u[i][j+1]= (-1/4)+((h/8)*wInicial[i1][j1]) #wInicial[i1][j1]
                   u[i][j-3]= (-1/4)-((h/8)*auxInicial[i1][j1])
                   u[i][j+3]= (-1/4)+((h/8)*auxInicial[i1][j1])     
                  #print(auxInicial[i1][j1])
        if(i==((Nxmax+1)*aux)):
            aux += 1
        if(j1==Nymax):
            j1=0
            i1 += 1
        else :  j1 += 1

    aux2=2
    i2=0
    j2=0
    for i in range(limite+1):

        for j in range(limite+1):
            if(i<=Nxmax+1 or i>=limite-(Nxmax+1) or (i>=((Nxmax+1)*aux2)-1 and i<=((Nxmax+1)*aux2))):
                if(i==j):
                    w[i][j]=1 
            else:
                if(i>= ((limite)/2)+ancho2 and i<= ((limite)/2)+ ancho2+6):
                    if(i==j):
                     #count += 1
                     w[i][j] =1
                     #print("[]",i,"  ", j)
                     #print(largo, "   " , ancho)
                     largo2 +=1 
                     if(largo2 ==5):
                       largo2 = 2
                       ancho2 += Nxmax+1                  
                else:
                 if(i==j):
                   w[i][j]=1
                   w[i][j-1]= (-1/4)-((h/8)*auxInicial[i2][j2]) #auxInicial[i2][j2]
                   w[i][j+1]= (-1/4)+((h/8)*auxInicial[i2][j2]) #auxInicial[i2][j2]
                   w[i][j-3]= (-1/4)-((h/8)*wInicial[i2][j2])
                   w[i][j+3]= (-1/4)+((h/8)*wInicial[i2][j2])
        if(i==((Nxmax+1)*aux2)):
            aux2 += 1
        if(j2==Nymax):
            j2=0
            i2 += 1
        else :  j2 += 1

llenarMatrix(auxInicial,wInicial)


def llenarB():
    aux2=2
    i2=0
    j2=0
    ancho =0
    largo = 2

    for i in range(limite+1):
        for j in range(1):
            if(i<=Nxmax+1 or i>=limite-(Nxmax+1) or (i>=((Nxmax+1)*aux2)-1 and i<=((Nxmax+1)*aux2))):
                bVector[i][j] = auxInicial[i2][j2]
            else : 
                if(i>= ((limite)/2)+ancho and i<= ((limite)/2)+ ancho+6):
                    bVector[i][j] =0
                    largo +=1
                    if(largo ==5 ):
                        largo = 0
                        ancho += Nxmax+1 
                else:
                 if(i==j):
                     bVector[i][j]=auxInicial[i2][j2] #uInicial
                 else: bVector[i][j] =(h/2)*presion
        if(i==((Nxmax+1)*aux2)):
           aux2 += 1
        if(j2==Nymax):
            j2=0
            i2 += 1
        else :  j2 += 1

def llenarBW():
    aux2=2
    i2=0
    j2=0
    ancho2=0
    largo2=2
    for i in range(limite+1):
        for j in range(1):
            if(i<=Nxmax+1 or i>=limite-(Nxmax+1) or (i>=((Nxmax+1)*aux2)-1 and i<=((Nxmax+1)*aux2))):
                bVectorW[i][j] = wInicial[i2][j2]
            else :
                if(i>= ((limite)/2)+ancho2 and i<= ((limite)/2)+ ancho2+6):
                    bVectorW[i][j] =-1
                    largo2 +=1
                    if(largo2 ==5 ):
                        largo2 = 0
                        ancho2 += Nxmax+1 
                else:
                  if(i==j):
                      bVectorW[i][j]=wInicial[i2][j2] #uInicial
                  else: bVectorW[i][j] =(h/2)*presion
        if(i==((Nxmax+1)*aux2)):
           aux2 += 1
        if(j2==Nymax):
            j2=0
            i2 += 1
        else :  j2 += 1

llenarB()
#print(bVector)
llenarBW()

def voltear():
    for i in range(limite+1):
        for j in range(1):
            bVectorAux[i] = bVector[i][j]
    for i in range(limite+1):
        for j in range(1):
            bVectorAuxW[i] = bVectorW[i][j]



voltear()

"""
                u[i][j]=1
                u[i][j-1]= (-1/4)-((h/8)*wInicial[1][1])
                u[i][j+1]= (-1/4)+((h/8)*wInicial[1][1])
                u[i][j-3]= (-1/4)-((h/8)*uInicial[1][1])
                u[i][j+3]= (-1/4)+((h/8)*uInicial[1][1])
                (i>=(Nxmax*aux)-2 and i<=(Nxmax*aux)-1)):
                or i==(Nxmax+1*aux)-1 or i==(Nxmax+1*aux)
"""      

def Jacobi(A, b, N, M):
    x = np.zeros(N)
    xp = np.zeros(N)
    Q = np.zeros((N,M))
    Qminus1 = np.zeros((N,M))
    I = np.identity(N)
    
    #Set Qminus1
    for i in range(N):
        for j in range(M):
            if i == j:
                Qminus1[i][j] = 1/A[i][j]
                Q[i][j] = A[i][j]
    

    for _ in range(25): #40
        x = np.add(np.matmul(np.subtract(I, np.matmul(Qminus1, A)), xp), np.matmul(Qminus1, b))
        xp = x
    return x


A = u
b = bVectorAux

Aw = w
bw = bVectorAuxW
matrizAvoltear = Jacobi(A, b, limite+1, limite+1)
matrizAvoltearW = Jacobi(Aw, bw, limite+1, limite+1)

def formar(matrizAvoltear,matrizAvoltearW):
    aux =0
    for i in range(Nxmax+1):
        for j in range(Nymax+1):
            matrizUfinal[i][j] = matrizAvoltear[aux]
            aux +=1
    aux2 =0
    for i in range(Nxmax+1):
        for j in range(Nymax+1):
            matrizWfinal[i][j] = matrizAvoltearW[aux2]
            aux2 +=1

formar(matrizAvoltear,matrizAvoltearW)

def frontera(u,w):
  H = len(u)//2
  L = len(u)//2
  for j in range(L,len(u)):
    w[j][H] =  -2*(u[j][H-1])/h*h  #black
    w[j][H+2] = -2*(u[j][H+1+2])/h*h  #front
  for i in range(H,H+2):
       w[L][i] = -2*(u[L-1][i])/h*h#top
  for i in range(H, len(u)):
       for j in range(H,H+2):
         u[i][j] =0
         w[i][j]


def relajacion(inicial,inicial2):
    llenarMatrix(inicial,inicial2)
    A = u
    b = bVectorAux
    Aw = w
    bw = bVectorAuxW
    matrizAvoltear = Jacobi(A, b, limite+1, limite+1)
    matrizAvoltearW = Jacobi(Aw, bw, limite+1, limite+1)
    formar(matrizAvoltear,matrizAvoltearW )
    #print(matrizUfinal)
    for i in range(0,Nxmax+1):
        for j in range(0,Nymax+1):
          r1= wa*(matrizUfinal[i][j]-Ux[i][j])
          Ux[i][j] = Ux[i][j]+r1

    for i in range(0,Nxmax+1):
        for j in range(0,Nymax+1):
          r2= wa*(matrizWfinal[i][j]-W[i][j])
          W[i][j] = W[i][j]+r2 


def variasIteraciones(ite):
    while(ite <= 5):

      if(ite==0):
       relajacion(auxInicial,wInicial)
      else:
        frontera(Ux, W)
        relajacion(Ux,W)
      if(ite%10==0):
        pass

      #print(Ux)
      ite += 1
       

variasIteraciones(ite)
X=np.random.randint(256, size=(10, 10))

fig = p.figure(figsize=(8,6))
p.imshow(Ux,cmap="inferno")
p.title("Plot 2D array")
p.colorbar()
p.show()
"""
                  u[i][j]=1
                  u[i][j-1]= (-1/4)-((h/8)*uInicial[i1][j1]) #w
                  u[i][j+1]= (-1/4)+((h/8)*uInicial[i1][j1]) #w
                  u[i][j-3]= (-1/4)-((h/8)*uInicial[i1][j1])
                  u[i][j+3]= (-1/4)+((h/8)*uInicial[i1][j1])
"""
