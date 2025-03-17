#plotting lines without line
#to plot only the marker
#you can use shortcut


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,8])
ypoints = np.array([3,10])

plt.plot(xpoints,ypoints,'*')
plt.show()

