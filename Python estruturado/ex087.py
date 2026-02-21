import numpy as np
import matplotlib.pyplot as plt

#Criar os vetores que contêm os dados
x = np.array(['A', 'B', 'C', 'D'])
y = np.array([3, 8, 1, 10])

#Gráfico de barras usando x para as categorias e y para os valores das barras
plt.bar(x, y)

#Renderiza e exibe a janela com o gráfico
plt.show()