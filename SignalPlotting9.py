import numpy as np  # numerical Python lib
import matplotlib.pyplot as plt  # plot lib
from scipy import signal

t = np.arange(0, 1e-2/10, 1e-8)
Vt = 0.5 * signal.square(2 * np.pi * 4000 * t) + 12

plt.plot(t,Vt)
plt.grid()
plt.show()