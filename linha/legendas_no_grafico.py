# CONFIGURANDO
# -------------------------------------------
#%matplotlib inline

import matplotlib as mpl
#%mpl.rcParams['figure.dpi'] = 100

import numpy as np
import matplotlib.pyplot as plt

# CRIANDO DADOS
# -------------------------------------------
x = np.linspace(0, 10, 100)
y = np.sin(x)

# TÍTULOS E LEGENDAS
# -------------------------------------------
plt.title('Função de Onda')
plt.ylabel('f(x)')
plt.xlabel('x')

# REPRESENTANDO GRAFICAMENTE
# -------------------------------------------
plt.plot(x, y)
plt.show()
