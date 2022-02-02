def newton(f, df, x_0, maxiter=100, xtol=1.0e-5, ftol=1.0e-5):
    x = float(x_0) # Se convierte a número de coma flotante
    print("x0: ",x)
    for i in range(maxiter):
        dx = -f(x) / df(x) # ¡Aquí se puede producir una división por cero!
        # También x puede haber quedado fuera del dominio
        x = x + dx
        print("x{}: {:3.6f}  error x: {:3.6f} error f(x): {:3.6f}".format(i+1,x,abs(dx / x),abs(f(x))))
        if abs(dx / x) < xtol and abs(f(x)) < ftol:
            return x
    raise RuntimeError("No hubo convergencia después de {} iteraciones".format(maxiter))

def f(x):
    return x**7 - 17.0859375

def df(x):
    return 7 * x**6

root = newton(f, df, 1, xtol=1.0e-5, ftol=1.0e-5)
print("Raiz f(x): ",root)
