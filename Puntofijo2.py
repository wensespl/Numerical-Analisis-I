import numpy as np


def puntofijo(f, x0):
    eps = 1E-5
    maxIter = 100
    f0 = f(x0)
    i = 0
    while i < maxIter and abs(f0-x0) >= eps:
        x0 = f0
        f0 = f(x0)
        i += 1
        print(f'x0={x0:5.8f} f(x0)={f0:5.8f}')
    if abs(f0-x0) >= eps:
        print(f'Metodo no converge')
    else:
        print(f'Solucion c={x0}')
        print(f'Numero de iteraciones={i}')


puntofijo(f=lambda x: np.cbrt(3*x-4), x0=0.)
