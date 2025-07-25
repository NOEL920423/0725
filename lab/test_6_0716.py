import matplotlib.pyplot as plt

# 折線線圖
x = [1, 2, 3, 4, 5]
y = [2, 4, 3, 8, 9]

plt.plot(x, y, "--o")
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# 散佈圖
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
