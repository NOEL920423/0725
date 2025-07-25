import numpy as np
import matplotlib.pyplot as plt

# 設置隨機種子
np.random.seed(0)

# 隨機生成三通道影像
images = np.random.randint(0, 255, size=(64, 64, 3), dtype=np.uint8)

# 轉換為灰階並計算統計數據
gray_images = np.mean(images, axis=2).astype(np.uint8)

# 計算統計數據
max_values = np.max(gray_images, axis=(0, 1))

# show出統計結果
print(max_values)

#plt.imshow(images)    # 隨機三通道影像(彩色圖片)
plt.imshow(gray_images,cmap="gray")    # 灰階圖片
plt.show()

