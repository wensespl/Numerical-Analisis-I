# Penadillo Lazares Wenses Johan

import math
import numpy as np

def newton(f, J, x_0, maxiter=100, xtol=1.0e-2):
    #x = float(x_0) # Se convierte a número de coma flotante
    x = np.array([x_0[0], x_0[1]])
    x = x.T
    print("x0: ",x)
    for i in range(maxiter):
        Jx = np.dot(np.linalg.inv(J(x)),f(x))
        x = x - Jx
        print("x{}: ".format(i+1),x)
        if abs(Jx[0] / x[0]) < xtol and abs(Jx[1] / x[1]) < xtol:
            return x
    raise RuntimeError("No hubo convergencia después de {} iteraciones".format(maxiter))

def f(x):
    f = np.array([x[0]*x[1]-42,(x[0]+5)*(x[1]+5)-132])
    return f.T

def J(x):
    J = np.array([[x[1], x[0]],
                [x[1]+5, x[0]+5]])
    return J
x0 = np.array([3,4])

root1 = newton(f, J, x0)
print("Raiz f(x): ",root1)
