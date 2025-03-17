import matplotlib.pyplot as plt
import numpy as np

x= np.array([4,6,12,3,4,7,8,12,34,55])
y= np.array([44,23,44,1,78,23,98,7,55,4])
colors = np.array(['r','k','m','g','b','hotpink','brown','y','gray','cyan'])

plt.scatter(x,y,c=colors)
plt.show()
