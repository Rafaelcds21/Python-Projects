from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Salvar uma imagem (ou um conjunto de imagens) como referência
x = 'Banco de dados com as fotos que servirão de base de comparação'
y = 'Fotos novas que eu quero comparar com as que eu tenho de modelo'

# Treinar uma IA para reconhecer uma nova imagem a partir do banco de dados
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)
modelo_arvoredecisao = RandomForestRegressor()
modelo_arvoredecisao.fit(x_treino, y_treino)

# Testar o modelo para checar a eficiência
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)
print(r2_score(y_teste, previsao_arvoredecisao))
