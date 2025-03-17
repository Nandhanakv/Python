import matplotlib.pyplot as plt
import numpy as np

x=np.array([20,10,45,50])
mylabels=["banana","orange","grapes","cherry"]
plt.pie(x,labels=mylabels)
plt.show()