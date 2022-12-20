salario = float(input('Insira um salário: '))
if salario <= 1250.00:
    juros = 0.15
    salario_reajustado = salario+juros*salario
else:
    juros = 0.10
    salario_reajustado = salario+juros*salario
print(f'Dado o salário de R${salario:.2f}, com um juros de {100*juros}%, o salario reajustado vai passar a ser de '
      f'R${salario_reajustado:.2f}')
