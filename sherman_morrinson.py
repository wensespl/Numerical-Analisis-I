import numpy as np
import scipy.linalg as la
n = 5
A = np.random.randn(n, n)
u = np.random.randn(n)
v = np.random.randn(n)

b = np.random.randn(n)

Ahat = A + np.outer(u, v)

LU, piv = la.lu_factor(A)
print(LU)
print(piv)

def solveA(b):
    return la.lu_solve((LU, piv), b)

print(la.norm(np.dot(A, solveA(b)) - b))

xhat = la.solve(Ahat, b)

xhat2 = solveA(b) - solveA(u)*np.dot(v, solveA(b))/(1+np.dot(v, solveA(u)))

print(la.norm(xhat - xhat2))