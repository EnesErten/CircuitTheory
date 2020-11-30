# created by Enes for the circuit theory preliminary work
# the code can be reach from the my GitHub account
# question 1 part d
import numpy as np  # numerical Python lib
import matplotlib.pyplot as plt  # plot lib
from scipy import signal

t = np.linspace(0, 0.0040, 1001)
Vt = (1 / 500) * signal.sawtooth(2 * np.pi * 1250 * t)

plt.plot(t, Vt)
plt.grid()
plt.show()
