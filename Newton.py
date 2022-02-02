from math import sqrt
import numpy as np
import matplotlib.pyplot as plt


def grafico_iteracionesVSx(gx, gy):
    plt.plot(gx, gy, 'blue')
    plt.title("Metodo de Newton")
    plt.xlabel("Numero de iteraciones")
    plt.ylabel('Valor de X')
    plt.show()


def Fs(x1, x2):
    f1 = x1*x2-42
    f2 = x1*x2+5*x1+5*x2-107
    return np.matrix([[f1], [f2]])


def Jinv(x1, x2):
    J = np.matrix([[x2, x1], [x2+5, x1+5]])
    JV = np.linalg.inv(J)
    return [J, JV]


P0 = [3, 4]
k = 0
x1, x2 = P0
ax = []
ay = []
ai = []
TOL = 1.0e-5
print("k \t\t x1 \t\t x2 \t\t ||x(k)-x(k-1||")
print("{0:1d} \t {1:1.6f} \t {2:1.6f} \t".format(k, x1, x2))
while k < 10:
    ax.append(x1)
    ay.append(x2)
    ai.append(k)
    J, JI = Jinv(x1, x2)
    F = Fs(x1, x2)
    Y = -JI*F
    X = np.matrix(P0).T+Y
    x1, x2 = float(X[0][0]), float(X[1][0])
    eps = sqrt((x1-P0[0])**2+(x2-P0[1])**2)
    P0 = [x1, x2]
    k += 1
    print("{0:1d} \t {1:1.6f} \t {2:1.6f} \t {3:1.6f}".format(k, x1, x2, eps))
    if sqrt(Y[0][0]**2+Y[1][0]**2) < TOL:
        print("Respuestas: x = {0:1.6f} , y = {1:1.6f}".format(x1, x2))
        grafico_iteracionesVSx(ai, ax)
        grafico_iteracionesVSx(ai, ay)
        break
