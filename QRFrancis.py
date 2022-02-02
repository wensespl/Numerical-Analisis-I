import numpy as np
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
        #print("H_", cnt)
        # print(Q_cnt)
        R = np.dot(Q_cnt, R)  # R=H(n-1)*...*H(2)*H(1)*A
        #print("R_", cnt)
        # print(R)
        # Q = H (n-1) * ... * H (2) * H (1) H es la matriz autoversa
        Q = np.dot(Q, Q_cnt)
        #print("Q_", cnt)
        # print(Q)
        # print("_______________________________")
    return (Q, R)


def QRFrancis(A, eps=1.0e-6):
    Ai = np.copy(A)
    (r, c) = np.shape(A)
    maxabs = 0.0
    cont = 0
    (rows, cols) = np.tril_indices(r, -1, c)
    for (row, col) in zip(rows, cols):
        if(maxabs < abs(Ai[row, col])):
            maxabs = abs(Ai[row, col])
    while(maxabs > eps):
        Q, R = householder_reflection(Ai)
        Ai = np.dot(R, Q)
        print("**************************************************")
        print("Matriz A_"+str(cont))
        print(Ai)
        maxabs = 0.0
        for (row, col) in zip(rows, cols):
            if(maxabs < abs(Ai[row, col])):
                maxabs = abs(Ai[row, col])
        cont += 1
    return np .diag(Ai)


np.set_printoptions(precision=8, suppress=True)

A = np.array([[4, 0, 1, 3],
              [0, -4, 2, 1],
              [1, 2, -2, 0],
              [3, 1, 0, -4]], dtype=float)

auto_vals = QRFrancis(A, eps=1.0e-4)

print("\nAutovalores")
print(auto_vals)

print(np.linalg.eigvals(A))
