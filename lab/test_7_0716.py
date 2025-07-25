import matplotlib.pyplot as plt
import numpy as np

# 設置隨機種子以確保結果可重現
np.random.seed(0)

# 生成10張隨機的三通道影像
images = np.random.randint(0, 256, size=(64, 64, 3), dtype=np.uint8)

# 轉換為灰階
gray_images = np.mean(images, axis=2).astype(np.uint8)

# 顯示選中的灰階影像
plt.figure(figsize=(6, 8)) # 視窗尺寸
plt.imshow(gray_images, cmap='gray')
plt.title(f"Gray Image")
plt.axis('off')
plt.show()

# 顯示選中的彩色影像
plt.figure(figsize=(12, 6))
plt.imshow(images)
plt.title(f"Color Image")
plt.axis('off')
plt.show()
