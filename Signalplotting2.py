# created by Enes for the circuit theory preliminary work
# the code can be reach from the my github account
# question 1 part a
import numpy as np  # numerical Python lib
import matplotlib.pyplot as plt  # plot lib

t = np.arange(0, 1e-3, 1e-6)  # time interval
Vt = 3.5 * np.sin(2 * np.pi * 10000 * t)  # sinusoidal signal

plt.plot(t, Vt)
plt.grid()
plt.show()
# plotting the signal
