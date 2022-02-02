#Penadillo Lazares Wenses Johan
X0 = 0.5

n = 120
X = X0
"""
if (X>0.5):
    print("Sentido de agujas de reloj")
else:
  print("Sentido opuesto de agujas de reloj")
"""
c1=0
c2=0
for i in range(n):
  X = 3.9*X*(1-X)
  if(X>0.5):
    c1 += 1
  if(X<0.5):
    c2 += 1
  print(X)
  """
  if (X>0.5):
    print("Sentido de agujas de reloj")
  else:
    print("Sentido opuesto de agujas de reloj")
  """
print(c1/n,c2/n)