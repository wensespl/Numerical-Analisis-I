import numpy as np
from numpy import diag, diagflat

#Penadillo Lazares Wenses Johan

def JacobiRichardson(a, b, x, n):
    tol = 1e-8
    max_iter = 300
    cambio_rel = 1
    cont = 0
    y = np.zeros_like(x)
    while (cambio_rel>tol) and (cont<max_iter):
        print("x_"+str(cont)+"=["+(" "*4).join(list(map('{:5.8f}'.format,x)))+"]"+" error: "+str(cambio_rel))
        for i in range(n):
            idx = [j for j in range(n) if j!=i]
            y[i] = (b[i]-np.dot(a[i, idx],x[idx]))/a[i, i]
        cambio_rel = np.linalg.norm(x-y, np.inf)/np.linalg.norm(y, np.inf)
        x[:] = y[:]
        cont += 1
    print("x_"+str(cont)+"=["+(" "*4).join(list(map('{:5.8f}'.format,x)))+"]"+" error: "+str(cambio_rel))
    if cambio_rel <= tol:
        print("Metodo converge")
    else:
        print("Metodo no converge")
    print(f"Metodo terminado en {cont} iteraciones.")
    return x, cont

a = np.array([[10, 1, 2], [4, 6, -2], [-2, 3, 8]], dtype='f4')
n = len(a)
b = np.array([3, 9, 51], dtype='f4')
x = np.array([0.3, 1.5, 6.375], dtype='f4')
#q = np.array([[0, 1], [0.5, 0]], dtype='f4')

JacobiRichardson(a, b, x, n)
q = np.zeros((n,n))
print("Matriz de Jacobi")
for i in range(n):
    for j in range(n):
        if(i!=j):
            q[i][j] = -a[i][j]/a[i][i]
            print(" "+str(-a[i][j]/a[i][i]), end="")
        else:
            q[i][j] = 0.
            print(" "+str(0.0), end="")
    print("\n")

print("||.||1: ",end="")
print(np.linalg.norm(q,1))
print("||.||2: ",end="")
print(np.linalg.norm(q))
print("||.||inf: ",end="")
print(np.linalg.norm(q,np.inf))