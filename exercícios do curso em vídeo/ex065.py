soma = 0

contador = 0

maior = 0
menor = 9999999

flag = True

while flag:
    num = int(input("Digite um número: "))
    soma += num
    contador += 1

    continuar = str(input("Quer continuar? ")).lower()

    if continuar == 'sim':
        if num > maior:
            maior = num

    else:
        flag = False

media = soma/contador

print(f"Média: {media}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")

