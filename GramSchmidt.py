import numpy as np
#Penadillo Lazares Wenses

def gram_schmidt(A):
    Q = np.zeros_like(A)
    cnt = 0
    for a in A.T:
        u = np.copy(a)
        for i in range(0, cnt):
            u -= np.dot(np.dot(Q[:, i].T, a), Q[:, i])  # ​​
        e = u / np.linalg.norm(u)  # Normalizado
        print("q_", cnt, e)
        Q[:, cnt] = e
        cnt += 1
    print("___ GramnSchmidt ___")
    print("Matriz Q")
    print(Q)
    R = np.dot(Q.T, A)
    print("Matriz R = Q^t*A")
    print(R)
    return (Q, R)


np.set_printoptions(precision=8, suppress=True)
A = np.array([[1, 1, 1, 1, 1],
              [2, 3, 4, 5, 6],
              [3, 7, 13, 21, 31],
              [1,2,4,8,16],
              [2,6,16,40,96]], dtype=float)
b = np.array([2, 4, 6, 8, 13])
n = 5

(Q, R) = gram_schmidt(A)

b = np.dot(Q.T, b)

x = np.zeros(n)
for j in range(n-1, -1, -1):
    sum = 0
    for k in range(j+1, n):
        sum += R[j][k]*x[k]
    x[j] = (b[j]-sum)/R[j][j]

print("Solucion: ")
print(x)
# print(Q)
# print(R)
#print(np.dot(Q, R))
