# Penadillo Lazares Wenses Johan

import math
import numpy as np
from numpy.core.fromnumeric import transpose

def RDescensoRapido(A,B):
    #eps = np.finfo(float).eps
    eps = 1.0e-5
    x = np.transpose([-5.05,80.05,0.])
    r = B
    i = 0
    while math.sqrt(np.dot(np.transpose(r),r)) >= eps and i < 300:
        t = np.dot(np.transpose(r),r)/np.dot(np.transpose(r),np.dot(A,r))
        x = x+t*r
        r=B-np.dot(A,x)
        print("La matriz X",(i)," es: ",end="")
        print(x,end="")
        print(" erro: ",math.sqrt(np.dot(np.transpose(r),r)))
        i += 1
A = np.array([
    [ 256., 16., 1.],
    [ 64., 8., 1.],
    [ 0., 0., 1.]])
B = np.transpose([0.,320.,0.])
RDescensoRapido(A,B)