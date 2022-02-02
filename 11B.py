import numpy as np

def potEscalado(x, A):
    eps = 1E-5
    maxIter = 100
    i = 0
    x0 = x
    lambda0 = 0
    lambdak = max(x)

    while i<maxIter and abs(lambdak-lambda0)>=eps:
        xk1 = np.dot(A,x0)
        lambda0 = lambdak
        lambdak = max(xk1)
        xk = xk1/lambdak
        x0 = xk
        i+=1
        print(f'lambdak = {lambdak[0]:<8.5f} x{i} = {xk[0][0]:<8.5f}{xk[1][0]:<8.5f}{xk[2][0]:<8.5f}{xk[3][0]:<8.5f}')

    if(abs(lambdak-lambda0)>=eps):
        print(f'Metodo no converge')
    else:
        print(f'Solucion c={xk[0][0]:<8.5f}{xk[1][0]:<8.5f}{xk[2][0]:<8.5f}{xk[3][0]:<8.5f}')
        print(f'Numero de iteraciones = {i}')


x0 = np.array([[1,0,0,0]]).T
A = np.array([[2, 1, 3, 4],
            [1, -3, 1, 5],
            [3, 1, 6, -2],
            [4, 5, -2, -1]])

potEscalado(x0,A)