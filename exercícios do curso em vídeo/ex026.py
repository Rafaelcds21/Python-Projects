frase = str(input('Insira uma frase: ')).lower()
contador = 0
for i in range(0, len(frase)):
    if frase[i] == 'a':
        contador += 1
print(f'A letra "A" aparece {contador} vezes.')
