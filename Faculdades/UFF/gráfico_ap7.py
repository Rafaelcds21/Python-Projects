import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Dados fornecidos
x = [0.387, 0.447, 0.500, 0.633, 0.671, 0.707, 0.775, 1.000, 1.095, 1.183]
y = [0.759, 0.901, 1.056, 1.272, 1.355, 1.425, 1.564, 2.013, 2.208, 2.373]
desvio_padrão = [0.014, 0.001, 0.021, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.002]

# Ajuste linear
def linear_fit(x, m, b):
    return m * x + b

# Realiza o ajuste considerando o desvio padrão como peso
params, covariance = curve_fit(linear_fit, x, y, sigma=desvio_padrão, absolute_sigma=True)

# Parâmetros da reta
m, b = params

# Gera pontos para a reta ajustada
x_fit = np.linspace(min(x), max(x), 100)
y_fit = linear_fit(x_fit, m, b)

# Gera o scatterplot
plt.scatter(x, y, label='Pontos Experimentais')

# Adiciona a reta ajustada ao scatterplot
plt.plot(x_fit, y_fit, label=f'Reta de Ajuste: y = {m:.3f}x + {b:.3f}', color='red')

# Adiciona barras de erro aos pontos experimentais
plt.errorbar(x, y, yerr=desvio_padrão, fmt='none', ecolor='gray', capsize=5)

# Adiciona rótulos e legenda
plt.xlabel('L (m**0.5)')
plt.ylabel('T (s)')
plt.title('Gráfico de dispersão LxT')
plt.legend()

# Exibe o gráfico
plt.show()
