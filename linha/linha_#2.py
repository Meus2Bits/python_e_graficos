#%matplotlib inline

import matplotlib as mpl
%mpl.rcParams['figure.dpi'] = 100

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.title('Função de Onda')
plt.ylabel('f(x)')
plt.xlabel('x')

plt.plot(x, y)
plt.show()
