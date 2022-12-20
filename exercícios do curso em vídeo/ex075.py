num1 = int(input("Digite um número entre 0 e 10: "))
num2 = int(input("Digite um número entre 0 e 10: "))
num3 = int(input("Digite um número entre 0 e 10: "))
num4 = int(input("Digite um número entre 0 e 10: "))

tupla_numeros = (num1, num2, num3, num4)

cont_9 = 0
pos_3 = 0
qtde_pares = 0

for i in range(0, 4):
    if tupla_numeros[i] == 9:
        cont_9 += 1

    if tupla_numeros[i] == 3:
        pos_3 = i

    if tupla_numeros[i] % 2 == 0:
        qtde_pares += 1

cond = 3 is tupla_numeros
if cond == False:
    pos_3 = 'não há número 3'

if 0 and 2 and 4 and 6 and 8 and 10 is not tupla_numeros:
    qtde_pares = 'não há'

print(f"Tiveram {cont_9} números 9, a posição do número 3 é {pos_3}, e tivemos {qtde_pares} números pares")
