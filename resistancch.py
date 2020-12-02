import numpy as np  # numerical Python lib
import matplotlib.pyplot as plt  # plot lib

V = np.linspace(-10, 10 , 11)
V2 = np.linspace(-0.1,0.1,11)
V1 = V - V2
i = np.linspace(-10,10,11)

plt.plot(V2,V1)
plt.grid()
plt.xlabel('V1')
plt.ylabel('V2')
plt.show()

plt.plot(V1,i)
plt.grid()
plt.xlabel('Current (mA)')
plt.ylabel('Voltage (V)')
plt.show()

slope = (V1[0] - V1[len(V) - 1]) / (1e-3 * (i[0] - i[len(i) - 1]))
print("the slope of the figure 7a", str(slope))

avrg = np.mean()