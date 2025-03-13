#enumerate iteration using ndenumerate()
#enumeration means mentioning sequence number of somthing one by one
#somthing requred corresponding index of the element while iterating
#the enmerating () method can be used for usecases
#enumerator on following 1 D arrays elements


import numpy as np
arr=np.array([1,2,3,4,5])
for idx, x  in np.ndenumerate(arr):
    print(idx,x)
    