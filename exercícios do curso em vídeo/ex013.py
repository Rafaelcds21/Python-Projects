salario = float(input('Insira o salário do funcionário: '))
aumento = 0.15
salario_aumentado = salario + aumento * salario
print(f'O salário de R${salario:.2f} aumentado a uma taxa de {100*aumento}% é igual a R${salario_aumentado:.2f}')
