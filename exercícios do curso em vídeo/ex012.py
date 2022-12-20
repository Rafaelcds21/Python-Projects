preco = float(input('Insira o valor do preço do produto: '))
desconto = 0.05
preco_ajustado = preco - desconto * preco
print(f'O valor de R${preco:.2f} com um desconto a uma taxa de {100*desconto}% é igual a R${preco_ajustado:.2f}')
