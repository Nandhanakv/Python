import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3,4,5])
y = np.array([0,2,4,8,16,25])



plt.plot(x,y,'s--r')
plt.title("plot of x vs y square")
plt.xlabel('input values(x)')
plt.ylabel('squared value(y)')



plt.grid()
plt.show()

