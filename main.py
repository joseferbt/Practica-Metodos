
def next(h,x,y,n):
    vx = [0]
    vy = [0]
    px = [0]
    py = [0]
    for i in range(n):
        aux_y = ys[-1] + round(h*((ts[-1]) + ys[-1] , 15))
        aux_t = ts[-1] + h
        ys.append(aux_y)
        ts.append(aux_t)

    return ys



import math


def euler(t0, y0, h, n):
    ts = [t0]
    ys = [y0  ]
          for i in range(n):
        aux_y = ys[-1] + round(h*((ts[-1]) + ys[-1] , 15))
        aux_t = ts[-1] + h
        ys.append(aux_y)
        ts.append(aux_t)

    return ys


if __name__ == '__main__':
    print(euler(0, 0, 0.1, 5))