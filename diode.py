import numpy as np
import matplotlib.pyplot as plt

V = np.linspace(-5, 5, 11)
Vdiode = [-0.65, -0.64, -0.62, -0.6, -0.53, 0, 0.53, 0.6, 0.62, 0.64, 0.65]
Vr = V - Vdiode
i = [-4.4, -3.4, -2.4, -1.4, -0.88, 0, 0.9, 1.4, 2.4, 3.4, 4.4]

plt.plot(Vr,i)
plt.grid()
plt.xlabel('i')
plt.ylabel('Vr')
plt.show()

plt.plot(Vdiode, i)
plt.grid()
plt.xlabel('Current (mA)')
plt.ylabel('Voltage (V)')
plt.show()
