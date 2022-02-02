""" x = 2
for i in range(2000):
  x = x/2
  if x + 0 == 0:
    print(2**x)
    print(i)
    break """

import numpy as np

a = np.zeros((2,2))
a[0][0] = 1
a[1][0] = 2


print(a)

t = a[0]
a[0] = a[1]
a[1] = t

print(a)