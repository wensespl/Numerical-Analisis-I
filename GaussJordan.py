import numpy as np
import sys

""" # Leer numero de incognitas
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
print(a) """

""" # Aplicando Gauss Jordan
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('No hay solucion!')

    for j in range(n):
        if i != j:
            ratio = a[j][i]/a[i][i]

            print("\nCalculando F"+str(j)+str(i)+"(-"+str(a[j][i])+"/"+str(a[i][i])+")")
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]
            print(a) """

#print("\nMatriz despues de eliminacion por Gauss Jordan")
#print(a)

a = np.array([[3,2,1],
           [2,3,1],
           [1,2,3]])
b = np.array([[39],
           [34],
           [26]])

sol = np.linalg.solve(a,b)

print(sol)

# Obteniendo soluciones
#for i in range(n):
#    x[i] = a[i][n]/a[i][i]

# Mostrando soluciones
#print('\nSolucion requerida: ')
#for i in range(n):
#    print('X%d = %0.2f' % (i, x[i]), end='\t')

