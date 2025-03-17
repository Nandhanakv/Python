import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,3,1)
plt.plot(x,y)

x1 = np.array([0,1,2,3])
y1 = np.array([5,6,7,8])
plt.subplot(2,3,2)
plt.plot(x1,y1)


x2 = np.array([0,1,2,3])
y2 = np.array([3,8,1,10])
plt.subplot(2,3,3)
plt.plot(x2,y2)

x3 = np.array([0,1,2,3])
y3 = np.array([5,6,7,8])
plt.subplot(2,3,4)
plt.plot(x3,y3)


x4 = np.array([0,1,2,3])
y4 = np.array([3,8,1,10])
plt.subplot(2,3,5)
plt.plot(x4,y4)

x5 = np.array([0,1,2,3])
y5 = np.array([5,6,7,8])
plt.subplot(2,3,6)
plt.plot(x5,y5)
plt.show()