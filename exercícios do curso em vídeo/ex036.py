valor_casa = float(input('Insira o valor da casa: '))
salario = float(input('Insira o valor do salário: '))
anos = int(input('Insira por quantos anos a dívida será paga:'))
meses = 12 * anos
prestacao = valor_casa / meses
if prestacao <= 0.3*salario:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado!')
