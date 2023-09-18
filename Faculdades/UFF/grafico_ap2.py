import matplotlib.pyplot as plt

lista_dados = []

num = float(input("Digite um número: "))
lista_dados.append(num)

while True:
  num = float(input("Digite um número: "))
  if num == -1.0:
      break
  lista_dados.append(num)

plt.hist(lista_dados)
plt.title("Histograma de períodos de um pêndulo")
plt.xlabel("Intervalo")
plt.show()
