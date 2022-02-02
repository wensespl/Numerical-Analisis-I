import math
import numpy as np
# Penadillo Lazares Wenses Johan

def gradienteConjugado(A, B, tol):
    n = len(A)
    x = np.transpose([-5.05,80.05,0.])
    r = B
    d = (np.linalg.norm(r))**n
    k = 1
    while math.sqrt(d) > tol*np.linalg.norm(B) and k<300:
        if k == 1:
            p = r
        else:
            b = d/auxD2
            p = r+b*p
        w = np.dot(A, p)
        a = d/(np.dot(np.transpose(p), w))
        x = x+a*p
        r = r-a*w
        auxD2 = d
        d = (np.linalg.norm(r))**n
        print("La matriz X", (k), " es: ", end="")
        print(x[:], end="")
        print(" error: ", math.sqrt(d))
        k += 1

A = np.array([
    [ 256., 16., 1.],
    [ 64., 8., 1.],
    [ 0., 0., 1.]])
B = np.transpose([0.,320.,0.])
eps = 1.0e-5
gradienteConjugado(A, B, eps)
