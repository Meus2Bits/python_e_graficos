
# CONFIGURANDO 
#--------------------------------------------
# %matplotlib inline

import matplotlib as mpl
#mpl.rcParams['figure.dpi'] = 100

# Importando as bibliotecas
import numpy as np
import matplotlib.pyplot as plt

# CRIANDO OS DADOS 
#--------------------------------------------
x = np.linspace(0, 10, 100)
y = np.sin(x)

# REPRESENTANDO GRAFICAMENTE 
#--------------------------------------------
plt.plot(x, y)
plt.show()
