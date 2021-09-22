
import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a.shape)
a.shape = (3,2)
print(a)
b = a.reshape(3,2)
print(b)
a = np.arange(5, 24, 2)
print(a)
b = np.arange(24)
print(b[0:10])
print(b[3:])
print(b[:10])

s = slice(5, 24, 2)
print(b[s])

x = np.linspace(10,20,5, endpoint=False)
print (x)
