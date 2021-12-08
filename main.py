import math





def segundaDerivadaX(y,x,x1,x2,h):
    return [(x2-2(x1)+y)/h**2,0]

def segundaDerivadaY(x,y,y1,y2,h):
    return [0,(y2-2(y1)+y)/h**2]

def primeraDerivadaY(x,y,y1,h):
    return [0,(y1+y)/h**2]

def primeraDerivadaX(y,x,x1,h):
    return [(x1+x)/h**2,0]

def presionX(x,x1,y,h):
    return [(x1-x)/h**2,0]

def presionY(y,y1,x,h):
    return [0,(y1-y)/h**2]






"""
def euler(t0, y0, h, n):
    ts = [t0]
    ys = [y0]
    for i in range(n):


aux_y = ys[-1] + round(h * ((ts[-1]) + ys[-1], 15))
aux_t = ts[-1] + h
ys.append(aux_y)
ts.append(aux_t)

return ys

if __name__ == '__main__':
    print(euler(0, 0, 0.1, 5))
"""
#""""
def segundaDerivadaParcialDe(funcion,x,y,h,derivar):
    if(derivar == "X"):
        return (funcion(x+2*h,y)-2*funcion(x+h,y)+funcion(x,y))/h**2
    else:
        return (funcion(x,y+2*h)-2*funcion(x,y+h)+funcion(x,y))/h**2

"""