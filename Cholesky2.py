import numpy as np
import math

def cholesky(A):
    n = len(A)
    L=np.zeros((n,n))
    D = np.zeros((n, n))
    for i in range(n):
        for k in range(i+1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))
            if (i == k):
                L[i][k] = math.sqrt(A[i][i] - tmp_sum)
            else:
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
        Lt = np.transpose(L)

    for j in range(n):
        D[j][j] = L[j][j]
        for k in range(n):
            L[k][j]=L[k][j]/D[j][j]

    return L, D, Lt


A=np.reshape(np.array([6,2,1,-1,2,4,1,0,1,1,4,-1,-1,0,-1,3],dtype=float),(4,4))

print(cholesky(A))