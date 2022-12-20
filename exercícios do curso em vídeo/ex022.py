nome = str(input('Insira o seu nome: '))
nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
nome_junto = nome.replace(' ', '')
print(nome_junto)
print(f'O nome em letras maiúsculas é {nome_maiusculo}, o nome em letras minúsculas é {nome_minusculo} e o nome tem '
      f'{len(nome_junto)} letras.')
