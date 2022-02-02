import numpy as np
import time
from matplotlib import pyplot as plt

def croutU1(a):
    n = len(a)
    l = np.zeros((n,n))
    u = np.zeros((n,n))
    s1 = 0
    s2 = 0
    for i in range(n):
        l[i][0] = a[i][0]
        u[i][i] = 1
    for j in range(1, n):
        u[0][j] = a[0][j] / l[0][0]
    for k in range(1, n):
        for i in range(k, n):
            for r in range(k): s1 += l[i][r] * u[r][k]
            l[i][k] = a[i][k] - s1
            s1 = 0
        for j in range(k+1, n):
            for r in range(k): s2 += l[k][r] * u[r][j]
            u[k][j] = (a[k][j] - s2) / l[k][k]
            s2 = 0
    return l, u

def croutL1(a):
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

A = {'a1': np.zeros((1,1))}
for i in range(3,16):
    name = 'a'+str(i)
    M1 = np.random.randint(1,10,(i,i))
    M2 = np.random.randint(1,10,(i,i))
    L = np.tril(M1)
    U = np.triu(M2)
    for j in range(i):
        for k in range(i):
            if j == k:
                L[j][k] = 1
    B = {name: np.dot(L,U)}
    A.update(B)

T = np.zeros((1,16))
for i in range(3,16):
    name = 'a'+str(i)
    start = time.time()
    croutU1(A[name])
    finish = time.time()
    T[0][i] = finish-start

'''
for i in range(3,16):
    name2 = 'sol'+str(i)
    print("L"+str(i))
    print(sol[name2][0])
    print("U"+str(i))
    print(sol[name2][1])
'''

y = [3,4,5,6,7,8,9,10,11,12,13,14,15]
x = [T[0][3], T[0][4], T[0][5], T[0][6], T[0][7], T[0][8], T[0][9], T[0][10], T[0][11], T[0][12], T[0][13], T[0][14], T[0][15]]
plt.plot(x,y,marker="o",color="blue")
plt.show()