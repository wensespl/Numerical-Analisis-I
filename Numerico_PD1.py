import math

N = 10

numero = 1/8

print("Usando la funcion f(x): ")

for i in range(1,N):
    fx = math.sqrt(numero*numero + 1) - 1
    numero = numero*numero
    print(fx)

numero = 1/8

print("Usando la funcion g(x): ")

for i in range(1,N):
    gx = numero*numero/(math.sqrt(numero*numero + 1) + 1)
    numero = numero*numero
    print(gx)