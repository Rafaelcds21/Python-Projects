num1 = float(input('Insira um número: '))
num2 = float(input('Insira mais um número: '))
num_novo = 0
while True:
    operacao = int(input('Insira o código da operação: '))

    if operacao == 1:
        soma = num1 + num2 + num_novo
        print(soma)

    elif operacao == 2:
        multiplicacao = num1 * num2
        print(multiplicacao)

    elif operacao == 3:
        maior = 0
        if num1 > maior:
            maior = num1
            if num2 > maior:
                maior = num2
                if num_novo > maior:
                    maior = num_novo
        print(maior)

    elif operacao == 4:
        num_novo = float(input('Insira um novo numero: '))
        num_novo = num_novo

    elif operacao == 5:
        break

