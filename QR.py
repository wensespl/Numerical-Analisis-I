import numpy as np


def gram_schmidt(A):
    Q = np.zeros_like(A)
    cnt = 0
    for a in A.T:
        u = np.copy(a)
        for i in range(0, cnt):
            u -= np.dot(np.dot(Q[:, i].T, a), Q[:, i])  # ​​
        e = u / np.linalg.norm(u)  # Normalizado
        Q[:, cnt] = e
        cnt += 1
    R = np.dot(Q.T, A)
    return (Q, R)


def givens_rotation(A):
    (r, c) = np.shape(A)
    Q = np.identity(r)
    R = np.copy(A)
    (rows, cols) = np.tril_indices(r, -1, c)
    for (row, col) in zip(rows, cols):
        if R[row, col] != 0:  # Q = 1, s = 0, r, q sin cambios
            r_ = np.hypot(R[col, col], R[row, col])  # d
            c = R[col, col]/r_
            s = -R[row, col]/r_
            G = np.identity(r)
            G[[col, row], [col, row]] = c
            G[row, col] = s
            G[col, row] = -s
            R = np.dot(G, R)  # R=G(n-1,n)*...*G(2n)*...*G(23,1n)*...*G(12)*A
            # Q=G(n-1,n).T*...*G(2n).T*...*G(23,1n).T*...*G(12).T
            Q = np.dot(Q, G.T)
    return (Q, R)


# Penadillo Lazares Wenses
def householder_reflection(A):
    (r, c) = np.shape(A)
    Q = np.identity(r)
    R = np.copy(A)
    for cnt in range(r - 1):
        x = R[cnt:, cnt]
        e = np.zeros_like(x)
        e[0] = np.linalg.norm(x)
        u = x - e
        v = u / np.linalg.norm(u)
        Q_cnt = np.identity(r)
        Q_cnt[cnt:, cnt:] -= 2.0 * np.outer(v, v)
        print("H_", cnt)
        print(Q_cnt)
        R = np.dot(Q_cnt, R)  # R=H(n-1)*...*H(2)*H(1)*A
        print("R_", cnt)
        print(R)
        # Q = H (n-1) * ... * H (2) * H (1) H es la matriz autoversa
        Q = np.dot(Q, Q_cnt)
        print("Q_", cnt)
        print(Q)
        print("_______________________________")
    return (Q, R)


np.set_printoptions(precision=8, suppress=True)
A = np.array([[3, -1],
              [1, -1],
              [0, 3],
              [2, 1]], dtype=float)

(Q, R) = householder_reflection(A)
print("_____ Householder ____")
print("Matriz Q")
print(Q)
print("Matriz R")
print(R)

b = np.array([1, 2, 0, 3]).T
n = 4
b = np.dot(Q.T, b)

x = np.zeros(n)
for j in range(n-1, -1, -1):
    sum = 0
    for k in range(j+1, n):
        sum += R[j][k]*x[k]
    x[j] = (b[j]-sum)/R[j][j]

print("Solucion: ")
print(x)
#print(np.dot(Q, R))
