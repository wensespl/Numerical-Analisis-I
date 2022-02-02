import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,3,5,8,13])
a = np.array([0,225,383,623,993])

#x = np.array([1,2,3])
#a = np.array([2,3,5])

n = 4 #2 #4
FPO = 75 # 2 #75
FPN = 72 # 1 # 72

h = np.zeros((n,1))

for i in range(0,n):
    h[i]=x[i+1] - x[i]
    
alpha = np.zeros((n+1,1))
alpha[0] = 3*(a[1] - a[0])/h[0] - 3*FPO 
alpha[n] = 3*FPN - 3*(a[n] - a[n-1])/h[n-1]

for i in range(1,n):
    alpha[i] = 3*(a[i+1] - a[i])/h[i] - 3*(a[i] - a[i-1])/h[i-1]

l = np.zeros((n+1,1))
u = np.zeros((n,1))
z = np.zeros((n+1,1))

l[0] = 2*h[0]
u[0] = 0.5
z[0] = alpha[0]/l[0]

for i in range(1,n):
    l[i] = 2*(x[i+1] - x[i-1]) - h[i-1]*u[i-1]
    u[i] = h[i]/l[i]
    z[i] = (alpha[i] - h[i-1]*z[i-1])/l[i]

l[n] = h[n-1]*(2 - u[n-1])
z[n] = (alpha[n] - h[n-1]*z[n-1])/l[n]

c = np.zeros((n+1,1)) 
b = np.zeros((n,1))
d = np.zeros((n,1))
c[n] = z[n]

for j in range(n-1,-1,-1):
    c[j] = z[j] - u[j]*c[j+1]
    b[j] = (a[j+1] - a[j])/h[j] - h[j]*(c[j+1] + 2*c[j])/3
    d[j] = (c[j+1] - c[j])/(3*h[j])
    
print('Coeficientes:')
coeficientes = np.zeros((n,4))
for j in range(0,n):
    coeficientes[j,0] = a[j]
    coeficientes[j,1] = b[j]
    coeficientes[j,2] = c[j]
    coeficientes[j,3] = d[j]
    print(f"S({j}): {a[j]} + {b[j]}*(x - x({j})) + {c[j]}*(x - x({j}))^2 + {d[j]}*(x - x({j}))^3") 
#Guardando los coeficientes
encabezado = '$a_j$  $b_j$  $c_j$  $d_j$'
np.savetxt('Coeficientes.csv', coeficientes, fmt='%8.3f', header=encabezado) 


for j in range(0,n):
    print('S({0:d}): {1:.3f} + {2:.3f}(x - x({3:d})) + {4:.3f}(x - x({5:d}))^2 + {6:.3f}(x - x({7:d}))^3'.format(j,a[j],float(b[j]),j,float(c[j]),j,float(d[j]),j))


for j in range(0,n):
    xx = np.linspace(x[j],x[j+1],20)
    Sjx = a[j] + b[j]*(xx - x[j]) + c[j]*(xx - x[j])**2 + d[j]*(xx - x[j])**3
    plt.plot(xx,Sjx)
    
print('Calculo de velocidades:\n')
velocidades = np.zeros((n,3))
for j in range(0,n):          
        print(f"En S{j} se tiene que:")
        xs = x[j] - c[j]/(3*d[j])
        vxs = b[j] + 2*c[j]*(xs - x[j]) + 3*d[j]*(xs - x[j])**2
        print("Analizamos la velocidad en los extremos")
        x1 = x[j]
        vx1 = b[j] + 2*c[j]*(x1 - x[j]) + 3*d[j]*(x1 - x[j])**2
        x2 = x[j+1]
        vx2 = b[j] + 2*c[j]*(x2 - x[j]) + 3*d[j]*(x2 - x[j])**2
        velocidades[j,0] = vx1
        velocidades[j,1] = vxs
        velocidades[j,2] = vx2
        print(f"En el punto en x({j}) = {x[j]} la velocidad (feet/s) es v({j}) = {vx1} y en (milla/h) es = {3600*vx1/5280}")
        print(f"En el punto en x({j+1}) = {x[j+1]} la velocidad (feet/s) es v({j+1}) = {vx2} y en (milla/h) es = {3600*vx2/5280}")
        print(f"En el punto en xe = {xs} la velocidad (feet/s) es vxe = {vxs} y en (milla/h) es = {3600*vxs/5280}")

encabezado = '$V_{j}$ $V(x)$  $V_{j+1}$ '
np.savetxt('Velocidades.csv', velocidades, fmt='%8.3f', header=encabezado)
np.savetxt('Velocidades2.csv', 3600*velocidades/5280.0, fmt='%8.3f') 
        
    #print(f'La velocidad maxima en S{j} es = {}')
    


xx= 10
j = 3
Sjx = a[j] + b[j]*(xx - x[j]) + c[j]*(xx - x[j])**2 + d[j]*(xx - x[j])**3
print(f"Para t = {xx} la posición ocurre en S({j}) = {Sjx}")

plt.plot(x,a,'ok')
plt.savefig('SplineCubicoClamped.png')
plt.xlabel("x")
plt.ylabel("S(x)")


plt.semilogx(x,a,'ok')
plt.savefig('SplineCubicoClamped2.png')
plt.xlabel("x")
plt.ylabel("S(x)")













