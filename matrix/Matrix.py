import numpy as np
from  numpy.linalg import inv

x = np.array([[1,2],[3,4]])
y = np.array([[1]]);
z = x * y
print x

e21 = np.array([[1,0,0],[-2,1,0],[0,0,1]],dtype=int)
inve21 = inv(e21)
print inve21
e32 = np.array([[1,0,0],[0,1,0],[0,-5,1]],dtype=int);
inve32 = inv(e32)
print inve32
L = np.dot(inve21, inve32)
print L