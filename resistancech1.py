import numpy as np  # numerical Python lib
import matplotlib.pyplot as plt  # plot lib

V = np.linspace(10, -10 , 11)
V1 = [9.95,7.96,5.98,3.99,1.99,0,-1.99,-3.99,-5.98,-7.96,-9.95]
V2 = V - V1
i = [4.5,3.6,2.7,1.8,0.9,0,-0.9,-1.8,-2.7,-3.6,-4.5,]

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
print("the slope of the figure 7b",str(slope))
