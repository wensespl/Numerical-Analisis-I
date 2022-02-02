import numpy as np

def verificar(A):
  m, n = A.shape
  if (m !=n ):
    print("La matriz no es cuadrada")
    return False
  return True

def matrizE(A):
	n=len(A)
	E=np.zeros((n,n))
	for i in range(n):
		for j in range(n):
			if i>j:
				E[i][j]=-A[i][j]
	return E

def iterativo(M,c,tol=1E-6):
  x=np.zeros_like(c)
  aux=x
  print("El x en la iteracion 0  es: ",x)
  x=np.dot(M,x)+c
  i=1
  while np.linalg.norm(x-aux, np.inf)/ np.linalg.norm(x, np.inf)>tol:
    print("El x en la iteracion",i," es: ",x)
    aux=x
    x=np.dot(M,x)+c
    i=i+1
  print("El numero de iteraciones es: ", i)
  print("La respuesta en la iteración ",i," es:",x)


def GaussSeidel(A,b):
  D=np.diag(np.diag(A))
  E= matrizE(A)
  aux=D-E
  F=aux-A
  inv=np.linalg.inv(aux)
  G=np.dot(inv,F)
  c=np.dot(inv,b)
  iterativo(G,c)


def Richardson(A,b):
  n=len(A)
  I=np.identity(n)
  M=I-A
  iterativo(M,b)

def Jacobi(A,b):
  n=len(A)
  I=np.identity(n)
  D=np.diag(np.diag(A))
  print(D)
  invD=np.linalg.inv(D)
  J=I-np.dot(invD,A)
  c=np.dot(invD,b)
  iterativo(J,c)


A = np.array([[2, 3], [5, 4]],float)
b = np.array([8.8, 16.4])
b=np.transpose(b)

Jacobi(A,b)
