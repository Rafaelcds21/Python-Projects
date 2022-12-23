import pandas as pd

arquivo = pd.read_csv('C:/Users/Rafael Campos/Downloads/municipios.csv')
arquivo['área'] = 'arquivo01'
print(arquivo)

arquivo2 = pd.read_html('https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_brasileiros_por_%C3%A1rea_decrescente')
print(arquivo2[0][['Município', 'Código do IBGE', 'Área (km²)']])

nome1 = arquivo['nome']
nome2 = arquivo2[0]['Município']

for i in range(0, len(arquivo)):
    for j in range(0, len(arquivo2[0])):
        if nome1[i] == nome2[j]:
            arquivo['área'][i] = arquivo2[0]['Área (km²)'][j]

print(arquivo)
