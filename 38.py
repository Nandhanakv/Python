import matplotlib.pyplot as plt
import numpy as np

x= np.array([4,6,12,3,4,7,8,12,34,55])
y= np.array([44,23,44,1,78,23,98,7,55,4])
sizes = np.array([0,20,30,1000,50,60,70,800,90,100])
colors = np.array([0,20,30,40,50,60,70,80,90,100])

plt.scatter(x,y,s=sizes,c=colors,alpha=0.4)
plt.colorbar()
plt.show()
