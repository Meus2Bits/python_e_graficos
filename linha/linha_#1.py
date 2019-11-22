# CONFIGURANDO
# -------------------------------------------
# %matplotlib inline

# Importando as bibliotecas
import numpy as np
import matplotlib.pyplot as plt

# Criando os dados
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Representando graficamente os pontos
plt.plot(x, y)
plt.show()
