import numpy as np
import sys

# Leer numero de incognitas
n = int(input('Ingrese numero de incognitas: '))

# Creamos matriz de n x n+1 para guardar la matriz aumentada
# Inicializado son 0s
a = np.zeros((n, n+1))

# Creamos vector de tamaño n para guardar las soluciones.
# Inicializado son 0s
x = np.zeros(n)

# Leemos los coeficientes de la matriz aumentada
print('Ingrese coeficientes de la matriz aumentada:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input('a['+str(i)+'][' + str(j)+'] = '))

print("\nMatriz Ingresada")
print(a)

# Aplicando eliminacion gausiana
for i in range(n):
    if a[i][i] == 0.0:
        print(a)
        sys.exit('No hay solucion!')

    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]

        print("\nCalculando F"+str(j)+str(i)+"(-"+str(a[j][i])+"/"+str(a[i][i])+")")
        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]
        print(a)

print("\nMatriz despues de eliminacion gausiana")
print(a)

# Sustitucion regresiva
x[n-1] = a[n-1][n]/a[n-1][n-1]

for i in range(n-2, -1, -1):
    x[i] = a[i][n]

    for j in range(i+1, n):
        x[i] = x[i] - a[i][j]*x[j]

    x[i] = x[i]/a[i][i]

# Mostrando soluciones
print('\nSolucion requerida: ')
for i in range(n):
    print("X%d = %0.4f" % (i, x[i]), end='\t')
