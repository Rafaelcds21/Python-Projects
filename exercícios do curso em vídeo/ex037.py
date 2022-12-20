numero = int(input('Insira um número inteiro: '))
print('-'*15)
print('Digite:')
print('1 para binário')
print('2 para octal')
print('3 para hexadecimal')
print('-'*15)
base_nova = int(input('Insira a base nova: '))
if base_nova == 1:
    numero = bin(numero)
else:
    if base_nova == 2:
        numero = oct(numero)
    else:
        numero = hex(numero)
print(numero)
