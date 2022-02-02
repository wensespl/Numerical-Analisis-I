import numpy as np

def CuasiNewton(A,f,x,tol):
    k=0
    while np.linalg.norm(f(x))>=tol:
        s=np.transpose(np.linalg.solve(A,-f(x)))
        #s=-1*np.transpose(np.dot(np.linalg.inv(A),f(x)))
        aux=x
        x=x+s
        y=f(x)-f(aux)
        A=A+np.dot((y-np.dot(A,np.transpose(s))),s)/(np.linalg.norm(s)**2)
        k+=1
        print("Para iteracion "+str(k)+" el x es: ",x)
    print("El metodo termino con "+str(k)+" iteraciones")


def f(x):
    x = np.transpose(x)
    ft=np.zeros((2, 1))
    ft[0,0]=x[0]*x[1]-42
    ft[1,0]=(x[0]+5)*(x[1]+5)-132
    return ft

#x0 = np.array([0., 1.])
x0 = np.array([3., 4.])
A0=np.diag([1.,1.])
CuasiNewton(A0,f,x0,1E-5)
'''
print("-------------------------")
x0 = np.array([0., 1.])
CuasiNewton(A0,f,x0,1E-6)
'''