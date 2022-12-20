flag = True
contador = 0
soma = 0
while flag:
    num = int(input("Insira um input: "))
    if num == 99:
        flag = False
        soma -= 99
        contador -= 1
    soma += num
    contador += 1
print(f"Soma: {soma}")
print(f"Quantidade de números: {contador}")
