import numpy as np
import matplotlib.pyplot as plt


# Dados fornecidos
x = np.array([78.00, 75.15, 45.70, 32.00, 27.05, 24.50])
y = np.array([244.50, 258.00, 155.65, 111.05, 86.00, 74.50])

# Calcula a linha de tendência (uma reta) usando polyfit
coefficients = np.polyfit(x, y, 1)  # Grau 1 para uma reta
a, b = coefficients

# Cria um conjunto de pontos para a linha de tendência
x_trend = np.linspace(0, 80, 100)  # Usei um intervalo de 0 a 80 para melhor visualização
y_trend = np.polyval(coefficients, x_trend)  # Calcula os valores de y correspondentes

# Plota o gráfico de dispersão e a linha de tendência
plt.scatter(x, y, label='Dados de dispersão')

plt.plot(x_trend, y_trend, 'r', label="Linha de tendência")

plt.xlabel('D (mm)')
plt.ylabel('C (mm)')

plt.legend()
plt.grid(True)

plt.title('CxD')

plt.xlim(0, 80)  # Ajusta os limites do eixo x para melhor visualização
plt.ylim(0, 280)  # Ajusta os limites do eixo y para melhor visualização

plt.show()
