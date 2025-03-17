#format string fmt
#you can also use the shortcut string notation parameter to specify the marker
#marker line color

import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([3,8,1,10,])

plt.plot(ypoints,'*:c')
plt.show()