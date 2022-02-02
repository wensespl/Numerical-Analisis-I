import numpy as np


def Krylov(A, n):
    a = np.zeros(n)
    y0 = np.array([1.0, 0.0, 0.0, 1.0]).T
    y = []
    y.append(y0)
    for i in range(n):
        y.append(np.dot(A, y[i]))
    for j in range(n):
        sum = 0
        for k in range(j):
            sum += y[n-k-1][n-j-1]*a[k]
        a[j] = (-(y[-1][n-j-1])-sum)/(y[n-j-1][n-j-1])
    return a


A = np.array([[4, 0, 1, 3],
              [0, -4, 2, 1],
              [1, 2, -2, 0],
              [3, 1, 0, -4]])

coeffA = Krylov(A, 4)
coeffA = np.append([1.],coeffA)
print(coeffA)
eigvA = np.roots(coeffA)
for eig in eigvA:
    print(type(eig), end=" ,")

B = np.array([[1, 0, -1, 1],
              [2, 2, -1, 1],
              [0, 1, 3, -2],
              [1, 0, 1, 4]])

print("\n")

coeffB = Krylov(B, 4)
coeffB = np.append([1.],coeffB)
print(coeffB)
eigvB = np.roots(coeffB)
for eig in eigvB:
    print(type(eig), end=" ,")
