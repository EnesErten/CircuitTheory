import numpy as np  # numerical Python lib
import matplotlib.pyplot as plt  # plot lib

t = np.arange(0, 1e-2/5, 1e-6)
Vt = np.sin(2 * np.pi * 1000 * t)
Vt1 = 3 * np.sin(2 * np.pi * 1000 * t)


plt.plot(t,Vt)
plt.plot(t,Vt1)
plt.grid()
plt.show()