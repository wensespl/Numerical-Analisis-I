# Penadillo Lazares Wenses Johan
import numpy as np

def J(x):
  Jf=np.zeros((2,2))
  Jf[:,0]=np.transpose([x[1],-3.0])
  Jf[:,1]=np.transpose([x[0],2.0])
  return Jf
def f(x):
  ft=np.zeros((2, 1))
  ft[0,0]=x[0]*x[1]-72
  ft[1,0]=(-3*x[0])+(2*x[1])-6
  return ft

def homotopia(f,J,x0,N):
  k=1
  h=1/N;
  a=f(x0)
  b=-1*h*a;
  i = 0
  while k<=N:
    A=J(x0);
    k1=np.transpose(np.dot(np.linalg.inv(A),b))
    C=x0+(1/2*k1)
    C=C.ravel().tolist()
    D=J(C);
    k2=np.transpose(np.dot(np.linalg.inv(D),b))
    E=x0+(1/2*k2);
    E=E.ravel().tolist()
    F=J(E)
    k3=np.transpose(np.dot(np.linalg.inv(F),b))
    G=x0+k3;
    G=G.ravel().tolist()
    I=J(G)
    k4=np.transpose(np.dot(np.linalg.inv(I),b))
    x=x0+(k1+2*k2+2*k3+k4)/6;
    i += 1
    print("Iteracion {}: ".format(i),x[0])
    x0=x.ravel().tolist()
    k=k+1

x0=[3.,6.]
homotopia(f,J,x0,40)
