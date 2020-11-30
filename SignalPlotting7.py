import numpy as np  # numerical Python lib
import matplotlib.pyplot as plt  # plot lib
from scipy import signal

t = np.linspace(0, 0.0008, 1001)
Vt1 = 3 * signal.square(2 * np.pi * 4e3 * t) + 2

plt.plot(t, Vt1)
plt.grid()
plt.show()
