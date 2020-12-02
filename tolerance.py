import numpy as np  # numerical Python lib
import matplotlib.pyplot as plt  # plot lib

V = np.linspace(-10, 10 , 11)
i = np.linspace(-10,10,11)

i1 = np.linspace(-9.5,9.5,11)
i2 = np.linspace(-10.5,10.5,11)

plt.plot(V,i,'r')
plt.plot(V,i1,'b')
plt.plot(V,i2,'g')
plt.grid()
plt.show()

i = [-4.5,-3.6,-2.7,-1.8,-0.9,0,0.9,1.8,2.7,3.6,4.5,]
i1 = [-4.725,-3.78,-2.835,-1.89,-0.945,0,0.945,1.89,2.835,3.78,4.725]
i2 = [-4.275,-3.42,-2.565,-1.71,-0.855,0,0.855,1.71,2.565,3.42,4.275]
plt.plot(V,i,'r')
plt.plot(V,i1,'b')
plt.plot(V,i2,'g')
plt.grid()
plt.show()
