# Este programa calcula a soma de N números quaisquer. Qualquer dúvida ou sugestão é só comentar.

# inserir a quantidade de dados
dado_inicial = int(input('Insira o número inicial: '))
dado_final = int(input('Insira o número final: '))

# fazer a soma
soma = (dado_final-dado_inicial+1)*(dado_inicial+dado_final)/2

# printar o resultado
print(soma)
