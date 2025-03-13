import numpy as np
arr=np.array([[[1,2],[3,4]],[[6,7],[8,9]]])
for x in np.nditer(arr):
    print(x)
    #iteraying array using nditer()
    #iterating through the 3d array?
