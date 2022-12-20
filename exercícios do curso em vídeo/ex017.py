import numpy as np
cateto_oposto = float(input('Insira o valor do cateto oposto: '))
cateto_adjacente = float(input('Insira o valor do cateto adjacente: '))
hipotenusa = np.sqrt(cateto_oposto**2+cateto_adjacente**2)
print(f'O valor da hipotenusa é {hipotenusa}')

