import numpy as np
#decalre scalars, vectors and matrices

#scalars
s = 5
print(s)

#vectors
v = np.array([5,-2, 75])
print(v)

#matrices
m = np.array([[5,12,6],[-3,0,14]])
print(m)

print(type(s))
print(type(v))
print(type(m))

print(m.shape)

print(v.reshape(1,3))
print(v.reshape(3,1))