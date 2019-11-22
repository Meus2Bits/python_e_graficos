# CONFIGURANDO
# -------------------------------------------
# %matplotlib inline

import matplotlib as mpl
#mpl.rcParams['figure.dpi'] = 100

import numpy as np
import matplotlib.pyplot as plt

# CRIANDO DADOS
# -------------------------------------------
x = np.linspace(0, 10, 100)
y = np.sin(x)

# COR E ESPESSURA 
# -------------------------------------------
plt.plot(x, y, color='orange', linewidth=6)
plt.show()

# MARCADOR
# -------------------------------------------
plt.plot(x, y,  marker='*', markersize=8)
plt.legend(['sin(x)'])
plt.show()

# ESTILO DE LINHA 
# -------------------------------------------
plt.plot(x, y, linestyle='-.', color='indigo')
plt.show()

# TRANSPARÊNCIA
# -------------------------------------------
plt.plot(x, y, linestyle='', alpha=0.5, marker='o', markersize=12)
plt.show()

# PREENCHIMENTO
# -------------------------------------------
plt.plot(x, y, color='orange')
plt.fill_between(x, 0, y, color='wheat')
plt.show()
