num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
num4 = int(input("Digite um número: "))
num5 = int(input("Digite um número: "))
lista = []
lista.append(num1)
lista.append(num2)
lista.append(num3)
lista.append(num4)
lista.append(num5)
menor = 9999999999
maior=0
for i in range(0,len(lista)):
    if lista[i] > maior:
        maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]
print(f"maior: {maior}, menor: {menor}")
