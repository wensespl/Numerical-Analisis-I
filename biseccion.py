# Penadillo Lazares Wenses Johan

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import root


def biseccion(f, a, b, tol=1.0e-6):
    if a > b:
        raise ValueError("Intervalo mal definido")
    if f(a) * f(b) >= 0.0:
        raise ValueError("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
        raise ValueError("La cota de error debe ser un número positivo")
    c = (a + b) / 2.0
    i = 0
    err = b - a
    while True:
        print("Iteracion ",i)
        print(f'[a,b] = [{a:5.8f} , {b:5.8f}] c = {c:5.8f}  err = {err:5.8f}')
        print(f'f(a) = {f(a):5.8f} f(c) = {f(c):5.8f} f(b) = {f(b):5.8f}')
        print("\n")
        i += 1
        if err <= tol:
            print("Numero de iteraciones: ", i)
            return c
        # Utilizamos la función signo para evitar errores de precisión
        elif np.sign(f(a)) * np.sign(f(c)) > 0:  # se escoge [c,b]
            a = c
        else:  # se escoge [a,c]
            b = c
        c = (a + b) / 2.0
        err = b - a


def func(x):
    return pow(x,3) - pow(x,2) - 4*x + 4

# Metodo de Biseccion
sol1 = biseccion(func, -3.0, 0.0, 1.0e-3)
print("Por Biseccion: ", sol1)
print("Por Root: ", root(func, 0.5).x)
