import numpy as np

def Richardson(a, b, x, n):
    tol = 1e-5
    max_iter = 300
    cambio_rel = 1
    cont = 0
    y = np.zeros_like(x)
    while (cambio_rel>tol) and (cont<max_iter):
        print("x_"+str(cont)+"=["+(" "*4).join(list(map('{:5.8f}'.format,x)))+"]"+" error: "+str(cambio_rel))
        for i in range(n):
            y[i] = x[i] + b[i] - np.dot(a[i,:],x[:])
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

a = np.array([[0.05, -0.05], [0.05, -0.1]], dtype='f4')
n = len(a)
b = np.array([1, -0.5], dtype='f4')
x = np.array([0, 0], dtype='f4')

Richardson(a, b, x, n)
print("||.||1: ",end="")
print(np.linalg.norm(np.identity(n)-a,1))
print("||.||2: ",end="")
print(np.linalg.norm(np.identity(n)-a))
print("||.||inf: ",end="")
print(np.linalg.norm(np.identity(n)-a,np.inf))
