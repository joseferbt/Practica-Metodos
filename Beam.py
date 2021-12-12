import matplotlib.pylab as p 
from mpl_toolkits.mplot3d import Axes3D 
from numpy import *

print("Working, look for figure window after 100 iterations")
Nxmax = 70
Nymax = 20
IL = 10
H = 8
T = 8
h = 1
u= zeros((Nxmax + 1, Nymax + 1), float )
# Stream
w = zeros((Nxmax + 1, Nymax + 1), float )
# Vorticity
V0 = 1
omega = 0.1
nu = 1.
iter = 0
R = V0*h / nu  # R e n o l d #


def borders():
    for i in range(0, Nxmax + 1):
        for j in range(0, Nymax + 1):
            w[i, j] = 0
            u[i, j] = j * V0          
    for i in range(0, Nxmax + 1):
        u[i, Nymax] = u[i, Nymax-1]+ V0*h
        w[i, Nymax - 1] = 0
    for j in range(0, Nymax + 1):
        u[1, j] = u[0, j]
        w[0, j] = 0
    for i in range(0, Nxmax + 1):
        if i <= IL and i >= IL + T:
            u[i, 0] = 0
            w[i, 0] = 0
    for j in range(1, Nymax):
        w[Nxmax, j] = w[Nxmax-1, j]
        u[Nxmax, j] = u[Nxmax-1, j]

def beam():
    for j in range(0, H + 1):
        w[IL, j] = -2 * u[IL-1,j]/(h*h)
        w[IL + T, j] = -2*u[IL+T+1,j]/(h*h)
    for i in range(IL, IL + T + 1):w[i,H-1]= -2 * u[i,H]/(h*h)
    for i in range(IL, IL + T + 1):
        for j in range(0, H + 1):
            u[IL, j] = 0
            u[IL + T, j] = 0
            u[i, H] = 0


# top
def relax():
    beam()
    for i in range(1, Nxmax): 
        for j in range(1, Nymax):
            r1 = omega * ((u[i + 1, j] + u[i -1, j] + u[i, j +1]+ u[i, j -1] + h*h*w[i, j]) *0.25-u[i, j])
            u[i, j] += r1
    for i in range(1, Nxmax):
        for j in range(1, Nymax):
            a1 = w[i + 1, j] + w[i -1, j] + w[i, j + 1] + w[i, j -1]
            a2 = (u[i, j + 1] - u[i, j -1]) *(w[i + 1, j] - w[i - 1, j])
            a3 = (u[i + 1, j] - u[i -1, j]) *(w[i, j + 1] - w[i, j - 1])
            r2 = omega *((a1 - ( R / 4.) *( a2 - a3) ) / 4.0 - w[i, j] )
            w[i, j]+= r2
borders()
while(iter <= 100 ):
    iter += 1
    if iter % 10 == 0: print(iter)
    relax()
    for i in range(0, Nxmax + 1):
        for j in range(0, Nymax + 1): u[i, j] = u[i, j] / (V0*h)  # V0h u n i t s
x = range(0, Nxmax - 1 )
y = range(0, Nymax-1)
X, Y = p.meshgrid(x, y)


def functz(u):
    z = u[X, Y]
    return z
# r e t u r n s stream flow to p l o t
# for several i t e r a t i o n s
Z = functz(u)
# here the function i s called
fig = p.figure()
# creates the figure
ax = Axes3D(fig )# plots the axis for the figure
ax.plotwireframe(X, Y, Z, color = 'r' )
# s u r f a c e of wireframe in red

ax.setxlabel( 'X' )# l a b e l the t h r e e axes
ax.setylabel( 'Y' )
ax.setzlabel( 'StreamFunction' )
p.show()