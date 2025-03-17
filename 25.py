import matplotlib.pyplot as plt
import numpy as np

x= np.array([0,1,3,5,7,9])
y= np.array([6,7,8,9,10,11])

plt.title("sports watch data")
plt.xlabel("average pules")
plt.ylabel("calorie burnage")
plt.plot(x,y)
plt.grid(color='r',ls='--')
plt.show()

