# CONFIGURANDO
# -------------------------------------------
# %matplotlib inline

import numpy as np
import matplotlib.pyplot as plt

# CRIANDO DADOS
# -------------------------------------------
x = np.linspace(0, 10, 100)
y = np.sin(x)

# REPRESENTANDO GRAFICAMENTE
# -------------------------------------------
plt.plot(x, y)
plt.show()
