import numpy as np
array3D = np.array([[[10,20],[30,40]],[[50,60],[70,80]]])
for i in np.nditer(array3D):
    print(i)
