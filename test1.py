def f(x):
    return x**4 - 4*x**2 + 4

def df(x):
    return 4*x**3 - 8*x

def newton(f, df, x0, eps, itmax):
    L = range(1, itmax+1)
    iteracao = 0
    a = x0
    for i in L:
      raiz = a
      if df(raiz) != 0:
          raiz = raiz - f(raiz) / df(raiz)
          erro = raiz - a
          a = raiz
          iteracao = i
      else:
          iteracao = itmax + 1
          break
      if abs(erro) <= eps:
          break
    if iteracao > itmax:
      iteracao = 0.25
    elif iteracao == itmax:
      iteracao = 0.75
      return [raiz, erro, iteracao]

x0 = 1.8
eps = 10**-7
itmax = 1000

resultado = newton(f, df, x0, eps, itmax)
print("Root:", resultado[0])  # Approximated root
print("Error:", resultado[1])  # Error in approximation
print("Number of iterations:", resultado[2])  # Number of iterations taken