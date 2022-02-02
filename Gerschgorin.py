import numpy as np
from matplotlib import pyplot as plt
#Penadillo Lazares Wenses Johan

def greschgorin(A):
    angulo = np.linspace(0, 2*np.pi, 201)
    R, C = np.shape(A)
    for r in range(R):
        if(type(A[r][r]) == np.complex_):
            cyi = A[r][r].imag
            cxi = A[r][r].real
        else:
            cyi = 0.0
            cxi = A[r][r]
        ri = 0.0
        for c in range(C):
            if (r != c):
                if(type(A[r][c]) == np.complex_):
                    ri += np.sqrt(pow(A[r][c].real, 2) + pow(A[r][c].imag, 2))
                else:
                    ri += abs(A[r][c])
        x = ri * np.cos(angulo) + cxi
        y = ri * np.sin(angulo) + cyi
        plt.plot(x, y, color="red", markersize=1)
    eigenvalue, featurevector = np.linalg.eig(A)
    for eig in eigenvalue:
        if(type(eig) == np.complex_):
            plt.plot(eig.real, eig.imag, "b.")
        else:
            plt.plot(eig, 0.0, "b.")
    plt.gca().set_aspect("equal")
    plt.savefig("img.png")
    plt.show()

M = np.array([[1+1j, 1j, 2],
              [-3, 2+1j, 1],
              [1, 1j, 6]])
greschgorin(M)
print(M)


""" A = np.array([[4, 0, 1, 3],
              [0, -4, 2, 1],
              [1, 2, -2, 0],
              [3, 1, 0, -4]])
greschgorin(A)
print(A)
print("Auto valores de matriz A")
eigenvalue, featurevector = np.linalg.eig(A)
for value in eigenvalue:
    print(value, end=" ,")
print("\n") """

""" B = np.array([[1, 0, -1, 1],
              [2, 2, -1, 1],
              [0, 1, 3, -2],
              [1, 0, 1, 4]])
greschgorin(B)
print(B)
print("Auto valores de matriz B")
eigenvalue, featurevector = np.linalg.eig(B)
for value in eigenvalue:
    print(value, end=" ,") """
