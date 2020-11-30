import numpy as np  # numerical Python lib
import matplotlib.pyplot as plt  # plot lib

t = np.arange(0, 1e-2/30, 1e-8)
Vt = 0.2 * np.sin(2 * np.pi * 30000 * t) + 5

plt.plot(t,Vt)
plt.grid()
plt.show()