'''Gerar 1000 pontos seguindo a distribuição normal
com média de 20 e desvio padrão de 2, exibir em um
histograma'''
from idlelib.colorizer import color_config

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
dados = np.random.normal(20, 2, 1000)
print(dados)
plt.hist(dados, color='lightblue', ec='red')
plt.show()