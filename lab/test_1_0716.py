import numpy as np

# 創建 NumPy 數組
arr = np.array([1, 2, 3, 4, 5])
print("1D array:", arr)

# 2D 數組
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", arr_2d)

# 基本操作
print("Array shape:", arr_2d.shape)
print("Array dimension:", arr_2d.ndim)
print("Array size:", arr_2d.size)

# 數學運算
print("Mean:", np.mean(arr_2d))
print("Sum:", np.sum(arr_2d))

print("Add 1 to all elements:\n", arr_2d + 1)

