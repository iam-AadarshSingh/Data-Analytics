import numpy as np

x = np.array([2,8,-4])
y = np.array([1,7,3])
print(np.dot(x,y))
print("##########")

#scalar*scalar
print(np.dot(4,6))
print(np.dot(10,-20))
print("##########")

#scalar*vector
print(x)
print(5*x)