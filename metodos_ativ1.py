from math import *
import numpy as np
import matplotlib.pyplot as plt

# f(x) = sen(x)/x**3

erro_absoluto_progressivo = []
erro_absoluto_regressivo = []
erro_absoluto_central = []

# Derivada exata da função no ponto x = 4.
derivada_exata = np.round((cos(4)/(4**3))-(sin(4)*(3/(4**4))), 4)

def diferenca_progressiva(x, h):
    result = ((sin(x+h)/(x+h)**3)-(sin(x)/x**3))/h
    return np.round(result, 4)


def diferenca_regressiva(x, h):
    result = ((sin(x)/x**3)-(sin(x-h)/(x-h)**3))/h
    return np.round(result, 4)


def diferenca_central(x, h):
    result = ((sin(x + h)/(x+h)**3)-(sin(x-h)/(x-h)**3))/h
    return np.round(result, 4)

array_h = np.arange(0.01, 1.00, 0.01)

for i in array_h:
    erro_absoluto_progressivo.append(np.absolute(
        derivada_exata - diferenca_progressiva(4, i)))
    erro_absoluto_regressivo.append(np.absolute(
        derivada_exata - diferenca_regressiva(4, i)))
    erro_absoluto_central.append(np.absolute(
        derivada_exata - diferenca_central(4, i)))

plt.plot(array_h, erro_absoluto_progressivo, "r")
plt.plot(array_h, erro_absoluto_regressivo, "g")
plt.plot(array_h, erro_absoluto_central, "b")
plt.legend(["Diferença Progressiva", "Diferença Regressiva", "Diferença Central"])
plt.xlabel("$h$")
plt.ylabel("$| f'(x)_{exata} - f'(x)_{aproximada} |$")
plt.show()

