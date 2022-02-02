import numpy as np


def traza(A, n):
    tr = 0
    for i in range(n):
        tr += A[i][i]
    return tr


def Leverrier(A, n):
    a = np.zeros(n)
    s = np.zeros(n)
    t_A = A
    for i in range(n):
        s[i] = traza(t_A, n)
        t_A = np.dot(t_A, A)

    for i in range(n):
        sum = s[i]
        k = 0
        for j in range(i-1, -1, -1):
            sum += s[j]*a[k]
            k += 1
        a[i] = -sum/(i+1)
    return a


A = np.array([[4, 0, 1, 3],
              [0, -4, 2, 1],
              [1, 2, -2, 0],
              [3, 1, 0, -4]])

coeffA = Leverrier(A, 4)
coeffA = np.append([1.], coeffA)
print("Coeficientes del polinomio carateristico")
print(coeffA)
print("Autovalores")
print(np.roots(coeffA))

print("\n")

B = np.array([[1, 0, -1, 1],
              [2, 2, -1, 1],
              [0, 1, 3, -2],
              [1, 0, 1, 4]])

coeffB = Leverrier(B, 4)
coeffB = np.append([1.], coeffB)
print("Coeficientes del polinomio carateristico")
print(coeffB)
print("Autovalores")
print(np.roots(coeffB))
