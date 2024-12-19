import numpy as np

#matrices
m = np.array([[5,12,96],[1,2,-5]])
print(m.T)
print("##########")

#scalar
s = np.array([5])
print(s.T)
print("##########")

#vectors
v = np.array([1,2,3])
print(v.T)
print("##########")
v1 = v.reshape(1,3)
print(v1.T)