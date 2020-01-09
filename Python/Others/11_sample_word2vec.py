import numpy as np
import matplotlib.pyplot as plt

#sample = np.linspace(0,10,100)
z = np.linspace(0,10,10000)
y = (np.sqrt(z / 0.001) + 1) * (0.001 / z)
y1 = (np.sqrt(z / 0.000001) + 1) * (0.0000001 / z)
plt.axis([0,10,0,10])
#print (y)

plt.plot(z, y, c="r")
plt.plot(z, y1, c="b")
plt.show()