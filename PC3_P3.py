import numpy as np

def printMatriz(a):
  n = len(a)
  for i in range(n):
    for j in range(n):
      print("{:^10.4f}".format(a[i][j]), end="")
    print("\n")

def leerMatriz(a):
  n = len(a)
  print('Ingrese coeficientes de la matriz:')
  for i in range(n):
    for j in range(n):
      a[i][j] = float(input('a['+str(i)+'][' + str(j)+'] = '))
  print("\nMatriz Ingresada")
  printMatriz(a)
  return a

def gaussJordan(a):
  n = len(a)
  inv = np.identity(n)
  for i in range(n):
    if a[i][i] == 0.0:
      for j in range(i+1, n):
        if a[j][i] != 0.0:
          print("\nCalculando F"+str(i)+str(j))
          for k in range(n):
            t = a[i][k]
            t2 = inv[i][k]
            a[i][k] = a[j][k]
            inv[i][k] = inv[j][k]
            a[j][k] = t
            inv[j][k] = t2
          printMatriz(a)
          print("\nInversa")
          printMatriz(inv)
        else:
          print('No hay solucion!')

    for j in range(n):
      if i != j:
        ratio = a[j][i]/a[i][i]
        print("\nCalculando F"+str(j)+str(i)+"(-"+str(a[j][i])+"/"+str(a[i][i])+")")
        for k in range(n):
          a[j][k] = a[j][k] - ratio * a[i][k]
          inv[j][k] = inv[j][k] - ratio * inv[i][k]
        printMatriz(a)
        print("\nInversa")
        printMatriz(inv)
      else:
        ratio = a[i][i]
        print("\nCalculando F"+str(i)+"(1/"+str(a[i][i])+")")
        for k in range(n):
          a[i][k] = a[i][k]/ratio
          inv[i][k] = inv[i][k]/ratio
        printMatriz(a)
        print("\nInversa")
        printMatriz(inv)
  return inv

# Leer tamaño de matriz
n = int(input('Ingrese orden de la matriz: '))

# Creamos matriz de n x n para guardar la matriz
a = np.zeros((n, n))
#a = leerMatriz(a)

a[0][0] = -0.9987
a[0][1] = 1.3600*10**-3
a[1][0] = 1.3600*10**-3
a[1][1] = -0.9987

inv2 = np.linalg.inv(a)

inv = gaussJordan(a)
print("\nMatriz inversa por GaussJordan")
printMatriz(inv)

print("\nMatriz inversa")
printMatriz(inv2)
