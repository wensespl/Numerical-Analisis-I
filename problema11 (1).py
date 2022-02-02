def succession(n):
  u0=3/2
  u1=5/3
  if n==0:
    u=u0
  elif n==1:
    u=u1
  else:
    aux1=succession(n-1)
    aux2=succession(n-2)
    u=2003-(6002/aux1)+(4000/(aux1*aux2))
  return u
def successionReal(n):
  u=(2**(n+1)+1)/(2**(n)+1)
  return u
for n in range(0,15):
  u=succession(n)
  print("El termino ",n," de la sucesión en python es:",u)
print("Aca vemos como el error se propaga tanto que diverge")
for n in range (0,55):
  u=successionReal(n)
  print("El termino ",n," de la sucesión 2 en python es:",u)
print("En esta ultima sucesion vemos que error a disminuido y es mas cercano al resultado teorico.")