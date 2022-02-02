# Algoritmo de punto fijo
# [a,b] intervalo de búsqueda
# error = tolera

import matplotlib.pyplot as plt
import numpy as np


def puntofijo(gx, a, tolera, iteramax=15):
    i = 1  # iteración
    b = gx(a)
    tramo = abs(b-a)
    while(tramo >= tolera and i <= iteramax):
        a = b
        b = gx(a)
        tramo = abs(b-a)
        i = i + 1
    respuesta = b

    # Validar respuesta
    if (i >= iteramax):
        respuesta = np.nan
    return(respuesta)

# PROGRAMA ---------


# INGRESO
def fx(x): return pow(x,3) - 3.0*x + 4.0
def gx(x): return np.exp(-x)


a = 0       # intervalo
b = 1
tolera = 0.001
iteramax = 15  # itera máximo
muestras = 51  # gráfico
tramos = 50

# PROCEDIMIENTO
respuesta = puntofijo(gx, a, tolera)

# SALIDA
print(respuesta)

# GRAFICA
# calcula los puntos para fx y gx
xi = np.linspace(a, b, muestras)
fi = fx(xi)
gi = gx(xi)
yi = xi


plt.plot(xi, fi, label='f(x)')
plt.plot(xi, gi, label='g(x)')
plt.plot(xi, yi, label='y=x')

if (respuesta != np.nan):
    plt.axvline(respuesta)
plt.axhline(0, color='k')
plt.title('Punto Fijo')
plt.legend()
plt.show()
