import matplotlib.pyplot as plt
import numpy as np

# Dados
x = [0.387, 0.447, 0.500, 0.633, 0.671, 0.707, 0.775, 1.000, 1.095, 1.183]
y = [0.759, 0.901, 1.056, 1.272, 1.355, 1.425, 1.564, 2.013, 2.208, 2.373]
desvio_padrão = [0.014, 0.001, 0.021, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.002]

# Reta de ajuste
reta_ajuste = lambda x: 0.018 + 1.994 * x

# Criando o scatter plot
plt.scatter(x, y, label='Pontos experimentais')
plt.plot(x, [reta_ajuste(xi) for xi in x], color='red', label='Reta de Ajuste: y = 0.018 + 1.994 * x')
plt.errorbar(x, y, yerr=desvio_padrão, fmt='none', ecolor='black', capsize=5)

# Configurando o gráfico
plt.xlabel('L (m**0.5)')
plt.ylabel('T (s)')
plt.title('Gráfico de dispersão LxT')
plt.legend()

# Exibindo o gráfico
plt.show()
