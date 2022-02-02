def succession(n):
  u0=3/2
  u1=5/3
  if n==0:
    u=u0
  elif n==1:
    u=u1
  else:
    u=2003-(6002/succession(n-1))+(4000/(succession(n-1)*succession(n-2)))
  return u

n=int(input("Escribe el numero de la sucesión que deseas: "))
u=succession(n)
print("El termino ",n," de la sucesión es:",u)
