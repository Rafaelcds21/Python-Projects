maior = 0
menor = 99999999
for i in range(1, 7):
    peso = float(input('Insira um peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(maior)
print(menor)
