import numpy as np
# Penadillo Lazares Wenses Johan

def qr(A):
    m, n = A.shape
    Q = np.eye(m)
    for i in range(n - (m == n)):
        H = np.eye(m)
        H[i:, i:] = make_householder(A[i:, i])
        print("H_", i)
        print(H)
        Q = np.dot(Q, H)
        print("Q_", i)
        print(Q)
        A = np.dot(H, A)
        print("R_", i)
        print(A)
        print("_________________________________________________")
    return Q, A


def make_householder(a):
    v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    v[0] = 1
    H = np.eye(a.shape[0])
    H -= (2 / np.dot(v, v)) * np.dot(v[:, None], v[None, :])
    return H


np.set_printoptions(precision=8, suppress=True)
a = np.array([[3, -1],
              [1, -1],
              [0, 3],
              [2, 1]], dtype=float)

q, r = qr(a)
print('\nMatriz A:\n', a)
print('\nMatriz Q:\n', q)
print('\nMatriz R:\n', r)

b = np.array([1, 2, 0, 3]).T
n = 2
b = np.dot(q.T, b)
print('\nMatriz b:\n', b)

x = np.zeros(n)
for j in range(n-1, -1, -1):
    sum = 0
    for k in range(j+1, n):
        sum += r[j][k]*x[k]
    x[j] = (b[j]-sum)/r[j][j]

print("\nSolucion: ")
print(x)
