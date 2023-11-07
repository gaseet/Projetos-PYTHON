import numpy as np
from scipy.interpolate import interp1d

def descobrir_funcao(y2, y3, y4, y5):
    x = np.array([0, 0.2, 0.4, 0.6, 0.8, 1])
    y = np.array([0, y2, y3, y4, y5, 1])

    f = interp1d(x, y, kind='cubic')

    return f

y2 = float(input("Informe Y para [0.2, Y]: "))
y3 = float(input("Informe Y para [0.4, Y]: "))
y4 = float(input("Informe Y para [0.6, Y]: "))
y5 = float(input("Informe Y para [0.8, Y]: "))

f = descobrir_funcao(y2, y3, y4, y5)

x = np.array([0, 0.2, 0.4, 0.6, 0.8, 1])

coeficientes = np.polyfit(x, f(x), 5)

polinomio = np.poly1d(coeficientes)

integral = np.polyint(polinomio)

integralTotal = integral(1) - integral(0)

Gini = (0.5 - integralTotal) * 2

GiniPorcentagem = Gini * 100
print(polinomio)
print(f"O coeficiente de Gini para a curva informada é: {Gini:.4f} ({GiniPorcentagem:.2f}%).")