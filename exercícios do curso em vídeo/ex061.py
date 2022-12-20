primeiro_termo = float(input('Insira o 1° termo da PA: '))
razao = int(input('Insira a razão da PA: '))
print(f'1° termo: {primeiro_termo}')
for i in range(1, 10):
    termo = primeiro_termo+i*razao
    print(f'{i+1}° termo: {termo}')
