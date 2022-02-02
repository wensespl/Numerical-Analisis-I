# successive over-relaxation (SOR)

f1 = lambda x,y: (32+3*y)/5
f2 = lambda x,y: (16-x)

#Penadillo Lazares Wenses Johan

x0 = 0
y0 = 0
count = 1


e = 1.0e-8

w = 0.5

print('\nCount\tx\ty\terr1\terr2\n')

condition = True

while condition:
    x1 = (1-w) * x0 + w * f1(x0,y0)
    y1 = (1-w) * y0 + w * f2(x1,y0)
    e1 = abs(x0-x1)
    e2 = abs(y0-y1)
    print('%d\t%0.8f\t%0.8f\t%0.8f\t%0.8f\n' %(count, x1,y1, e1, e2))
    
    count += 1
    x0 = x1
    y0 = y1

    condition = e1>e and e2>e

print('\nSolucion: x = %0.8f, y = %0.8f\n'% (x1,y1))