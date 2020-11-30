import numpy as np  # numerical Python lib
import matplotlib.pyplot as plt  # plot lib

time_list = []
Vt1 = []

for i in range(6):
    time_list.append(np.linspace(0, 0.0008, 1001) + i * 0.0008)

for i in time_list[0]:
    if i < 0.0004:
        Vt1.append(4000 * i + 1)

    else:
        Vt1.append(-4000 * i + 4.2)

for i in time_list:
    plt.plot(i, Vt1)

plt.grid()
plt.show()
