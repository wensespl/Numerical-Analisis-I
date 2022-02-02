import numpy as np
import scipy
import scipy.linalg

def plu(A):

    n = len(A)

    U = A.copy()
    L = np.eye(n, dtype=np.double)
    P = np.eye(n, dtype=np.double)

    for i in range(n):
        for k in range(i, n):
            if ~np.isclose(U[i, i], 0.0):
                break
            U[[k, k + 1]] = U[[k + 1, k]]
            P[[k, k + 1]] = P[[k + 1, k]]

        factor = U[i + 1:, i] / U[i, i]
        L[i + 1:, i] = factor
        U[i + 1:] -= factor[:, np.newaxis] * U[i]

    return P, L, U

A = np.array([[0.0, 2.0, 1.0, 4.0, -1.0, 3.0],
           [1.0, 2.0, -1.0, 3.0, 4.0, 0.0],
           [0.0, 1.0, 1.0, -1.0, 2.0, -1.0],
           [2.0, 3.0, -4.0, 2.0, 0.0, 5.0],
           [1.0, 1.0, 1.0, 3.0, 0.0, 2.0],
           [-1.0, -1.0, 2.0, -1.0, 2.0, 0.0]], dtype=np.double)
A2 = np.array([[0.0, 2.0, 1.0, 4.0, -1.0, 3.0],
           [1.0, 2.0, -1.0, 3.0, 4.0, 0.0],
           [0.0, 1.0, 1.0, -1.0, 2.0, -1.0],
           [2.0, 3.0, -4.0, 2.0, 0.0, 5.0],
           [1.0, 1.0, 1.0, 3.0, 0.0, 2.0],
           [-1.0, -1.0, 2.0, -1.0, 2.0, 0.0]], dtype=np.double)

P, L, U = plu(A)
P2, L2, U2 = scipy.linalg.lu(A)

