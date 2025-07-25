# 先安裝matplotlib
# 紅色10x10雜訊方塊
import numpy as np
import matplotlib.pyplot as plt
one = np.random.randint(0, 255, size=(10, 10), dtype=np.uint8)
zero = np.zeros((10, 10), dtype=np.uint8)
img = np.stack((one, zero, one), axis=-1)
plt.imshow(img)
# 是綠色 img = np.stack((zero, one, zero), axis=-1)
# 是藍色 img = np.stack((zero, zero, one), axis=-1)
# (r,g,b)
# 數值0~255
plt.show()

