num1 = int(input('Insira um valor inteiro: '))
num2 = int(input('Insira um valor inteiro: '))
if num1 > num2:
    print(f'{num1} é maior que {num2}.')
else:
    if num2>num1:
        print(f'{num2} é maior que {num1}.')
    else:
        print(f'{num1} e {num2} são iguais.')
