import numpy as np

arr1d = np.array([10, 20, 30, 40, 50])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

zeros = np.zeros((2, 3))
ones = np.ones((3, 2))
seq = np.arange(0, 10, 2)
lin = np.linspace(0, 1, 5)

print("Array 1D:\n", arr1d)
print("Array 2D:\n", arr2d)
print("Zeros:\n", zeros, zeros.dtype)
print("Ones:\n", ones, ones.dtype)
print("Arange:\n", seq, seq.dtype)
print("Linspace:\n", lin, lin.dtype)
