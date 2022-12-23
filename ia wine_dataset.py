import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier

# Carrega o arquivo
arquivo = pd.read_csv("wine_dataset.csv")

# Muda as variáveis para números
arquivo['style'] = arquivo['style'].replace('red', 0)
arquivo['style'] = arquivo['style'].replace('white', 1)

# Divide em duas partes
y = arquivo['style']
x = arquivo.drop('style', axis=1)

# Divide as duas partes anteriores em partes de teste e partes de treino
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

# Modelo de árvore de decisões
modelo = ExtraTreesClassifier()

# Treina a IA
modelo.fit(x_treino, y_treino)

# Compara o treino com o teste
resultado = modelo.score(x_teste, y_teste)

print(resultado)
