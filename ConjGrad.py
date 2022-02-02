import numpy as np

def conjgrad(A, b, x):
    r = b - np.dot(A, x)
    p = r
    rsold = np.dot(np.transpose(r), r)

    for i in range(len(b)):
        Ap = np.dot(A, p)
        alpha = rsold / np.dot(np.transpose(p), Ap)
        x = x + np.dot(alpha, p)
        r = r - np.dot(alpha, Ap)
        rsnew = np.dot(np.transpose(r), r)
        if np.sqrt(rsnew) < 1e-8:
            break
        p = r + (rsnew/rsold)*p
        rsold = rsnew
    return x


n = 16
a = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        #if(j+1 == 1 and (i+1 >= 1 and i+1 <= 16)):
        if(j==i):
            a[i][j] = 4
        elif((j == i+1 and (i+1 in [1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15]))
             or (j == i-1 and (i+1 in [2, 3, 4, 6, 7, 8, 10, 11, 12, 14, 15, 16]))
             or (j == i+4 and (i in range(12)))
             or (j == i-4 and (i in range(16)))):
            a[i][j] = -1
        else:
            a[i][j] = 0
print(a)
b = np.array([1.902207, 1.051143, 1.175689, 3.480083, 0.819600, -0.264419, -0.412789, 1.175689,
             0.913337, -0.150209, -0.264419, 1.051143, 1.966694, 0.913337, 0.819600, 1.902207], dtype='f4')
x = np.zeros(n)
print(conjgrad(a, b, x))
