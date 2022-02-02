import math

def x(k):
  if k!=0:
    return 1/k - 5 * x(k-1)
  else:
    return math.log(1.2)

for i in range(20):
  print(x(i))