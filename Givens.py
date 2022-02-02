import numpy as np
#Penadillo Lazares Wenses

def givens_rotation(A):
    (r, c) = np.shape(A)
    Q = np.identity(r)
    R = np.copy(A)
    k = 0
    print("Matriz A_"+str(k))
    print(A)
    print("\n")
    (Is, Js) = np.tril_indices(r, -1, c)
    for (i, j) in zip(Is, Js):
        if R[i, j] != 0:  # Q = 1, s = 0, r, q sin cambios
            r_ = np.hypot(R[j, j], R[i, j])  # d
            c = R[j, j]/r_
            s = -R[i, j]/r_
            G = np.identity(r)
            G[[j, i], [j, i]] = c
            G[i, j] = s
            G[j, i] = -s
            print("G("+str(i)+","+str(j)+")")
            print(G)
            R = np.dot(G, R)  # R=G(n-1,n)*...*G(2n)*...*G(23,1n)*...*G(12)*A
            k += 1
            print("Matriz A_"+str(k))
            print(R)
            # Q=G(n-1,n).T*...*G(2n).T*...*G(23,1n).T*...*G(12).T
            Q = np.dot(Q, G.T)
            print("Matriz Q_"+str(k))
            print(Q)
            print("\n")
    return (Q, R)


""" def Givens(A, b):
    m, n = A.shape
    for i in range(n):
        for k in range(i+1, m):
            if(A[k][i] != 0.0):
                if(abs(A[k][i]) >= abs(A[i][i])):
                    t = A[i][i]/A[k][i]
                    s = 1/np.sqrt(1+pow(t, 2))
                    c = s*t
                else:
                    t = A[k][i]/A[i][i]
                    c = 1/np.sqrt(1+pow(t, 2))
                    s = c*t
                A[i][i] = c*A[i][i] + s*A[k][i]
                for j in range(i+1, n):
                    aux = c*A[i][j] + s*A[k][j]
                    A[k][j] = -s*A[i][j] + c*A[k][j]
                    A[i][j] = aux
                aux = c*b[i] + s*b[k]
                b[k] = -s*b[i] + c*b[k]
                b[i] = aux

    x = np.zeros(n)
    for j in range(n-1, -1, -1):
        sum = 0
        for k in range(j+1, n):
            sum += A[j][k]*x[k]
        x[j] = (b[j]-sum)/A[j][j]
    R2 = 0
    for k in range(n, m):
        R2 += pow(b[k], 2)
    print("Residuos al cuadrado: ", R2)
    return A, b, x """

n = 3
A = np.array([[1, 1, 1],
              [12, 10, 9],
              [2, -1, 0]], dtype=float)
b = np.array([44, 436, 0])

np.set_printoptions(precision=8, suppress=True)
Q, R = givens_rotation(A)

print("Matriz Q")
print(Q)
print("Matriz R")
print(R)
b = np.dot(Q.T, b)

#print("Verificacion")
#print(np.dot(Q, R))

x = np.zeros(n)
for j in range(n-1, -1, -1):
    sum = 0
    for k in range(j+1, n):
        sum += R[j][k]*x[k]
    x[j] = (b[j]-sum)/R[j][j]

print("Solucion: ")
print(x)
