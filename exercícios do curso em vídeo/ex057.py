sexo = str(input('Insira o seu sexo (M ou F): '))
flag = True
while flag:
    if sexo == 'M' or sexo == 'F':
        flag = False
    else:
        print('Refaça')
        sexo = str(input('Insira o seu sexo (M ou F): '))
