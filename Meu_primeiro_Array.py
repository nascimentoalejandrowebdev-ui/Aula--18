import numpy as np

dados_vendas = np.array([12, 15, 17, 20, 22, 25, 28, 30, 35, 150])

print(dados_vendas)

#Calculando a Média (sensível a extremos)
media_vendas = np.mean(dados_vendas)

print(media_vendas)

#Calculando a Mediana (robusta a extremos)
mediana_vendas = np.median(dados_vendas)

print(mediana_vendas)
