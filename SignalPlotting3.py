# created by Enes for the circuit theory preliminary work
# the code can be reach from the my GitHub account
# question 1 part c
import numpy as np  # numerical Python lib
import matplotlib.pyplot as plt  # plot lib

t = np.arange(0, 1e-2 / 2, 1e-6)
Vt = 3 * np.sin(2 * np.pi * 2400 * t)

plt.plot(t, Vt)
plt.grid()
plt.show()
