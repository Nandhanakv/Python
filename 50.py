import matplotlib.pyplot as plt
import numpy as np

x=np.array([20,10,45,50])
mylabels=["banana","orange","grapes","cherry"]
mycolors=["yellow","orange","m","r"]

plt.pie(x,labels=mylabels,colors=mycolors)
plt.legend()
plt.show()