import math
import numpy as np

def det(A):
  l = len(A)
  if(l == 1):
    return math.abs(A)
  elif(l == 2):
    return (A[0][0]*A[1][1])-(A[0][1]*A[1][0])
  else:
    d = 0
    for j in range(l):
      d+=(-1)**(0+j)*det(subMat(A,0,j))
    return d

def subMat(A, I, J):
  l = len(A)
  M = np.zeros((l-1,l-1))
  K = 0
  for i in range(l):
    L = 0
    for j in range(l):
      if(j != J):
        M[K][L] = A[i][j]
        L+=1
    if(i != I):
      K+=1
  return M

"""
A = np.array([[1,1],[1,2]])
print(det(A))
B = np.array([[1,0,0],[0,1,0],[0,0,1]])
print(det(B))
"""

#Penadillo Lazares Wenses Johan
A = np.array([[2/9,1/4,2/9],
              [1/3,1/3,5/18],
              [4/9,5/12,1/2]])
B = np.array([[34],
              [46],
              [67]])
#Calculando la inversa
AI = np.linalg.inv(A)
print("Matriz inversa de A")
print(AI)
#Calculando las normas
NAI = np.linalg.norm(AI)
NA = np.linalg.norm(A)
print("Norma de A^-1: ",NAI)
print("Norma de A: ",NA)
#numero de condicion
print("cond(A): ",NAI*NA)
#Solucion
print("Solucion")
print(np.linalg.solve(A,B))

C = np.array([[4,1],
              [0,4]])

print(np.linalg.inv(C))