import numpy as np

def Crout(a):
    n = len(a)
    l = np.zeros((n,n))
    u = np.zeros((n,n))
    s1 = 0
    s2 = 0
    for i in range(n):
        l[i][i] = 1
        u[0][i] = a[0][i]
    for j in range(1, n):
        l[j][0] = a[j][0] / u[0][0]
    for k in range(1, n):
        for i in range(k, n):
            for r in range(k): s1 += l[k][r] * u[r][i]
            u[k][i] = a[k][i] - s1
            s1 = 0
        for j in range(k+1, n):
            for r in range(k): s2 += l[j][r] * u[r][k]
            l[j][k] = (a[j][k] - s2) / u[k][k]
            s2 = 0
    return l, u