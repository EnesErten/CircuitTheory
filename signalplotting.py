# created by Enes for the circuit theory preliminary work
# the code can be reach from the my github account
# question 1 part a
import numpy as np  # numerical Python lib
import matplotlib.pyplot as plt  # plot lib

t = np.arange(0, 1e-2, 1e-6)  # the interval of the time
Vt = 2.5 * np.sin(2 * np.pi * 1000 * t)
# the sinusoidal signal
# amplitude is 2.5 Volts
# frequency is 1 kHz
# period is 1/1000 second 1 ms in engineering notation
# offset is 0

plt.plot(t, Vt)
plt.grid()
plt.show()
# plotting the signal
