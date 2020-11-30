import numpy as np
import matplotlib.pyplot as plt

R = 1000  # 1000 Ohms
r = 10  # 10 Ohms

V = np.linspace(-10, 10, 11)
I = []
V1 = []
V2 = []
counter = 0

for i in V:
    I.append(i / (R + r))

    V1.append(I[counter] * R)
    V2.append(I[counter] * r)

    counter += 1

plt.plot(I, V1)
plt.grid()
plt.xlabel("Current A")
plt.ylabel("Voltage V")
plt.show()

print((V1[0] - V1[len(V1) - 1]) / (I[0] - I[len(V1) - 1]))
