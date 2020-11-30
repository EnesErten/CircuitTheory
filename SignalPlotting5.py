import numpy as np  # numerical Python lib
import matplotlib.pyplot as plt  # plot lib

t = np.arange(0, 1e-2/5, 1e-6)
Vt = 1 + 2 * np.sin(2 * np.pi * 3500 * t)

plt.plot(t, Vt)
plt.grid()
plt.show()
