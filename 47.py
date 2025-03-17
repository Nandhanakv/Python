import matplotlib.pyplot as plt
import numpy as np

x=np.array([20,10,45,50])
mylabels=["banana","orange","grapes","cherry"]
myexplode=[0.2,0,0,0]
plt.pie(x,labels=mylabels,explode=myexplode)
plt.show()