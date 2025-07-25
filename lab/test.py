import numpy as np
import matplotlib.pyplot as plt
import pandas as pd  # 新增匯入
import os

# 建立要儲存的資料夾
folder_path = r"D:\NEAF暑期培訓\lab"
os.makedirs(folder_path, exist_ok=True)

# 建立統計資料的清單
statistics = []

# 圖像尺寸與圖形畫布
h, w = 10, 10
fig, axes = plt.subplots(2, 5, figsize=(12, 5))

for i in range(10):
    # 產生灰階影像 (值域 0~255)
    gray = np.random.randint(0, 256, (h, w), dtype=np.uint8)
    
    # 統計值
    max_val = gray.max()
    min_val = gray.min()
    mean_val = gray.mean()
    std_val = gray.std()
    
    # 存入統計資料表
    statistics.append({
        "Image Index": i + 1,
        "Max": int(max_val),
        "Min": int(min_val),
        "Mean": float(f"{mean_val:.2f}"),
        "Std": float(f"{std_val:.2f}")
    })
    
    # 顯示圖像
    ax = axes[i // 5][i % 5]
    ax.imshow(gray, cmap='gray')
    ax.set_title(f"Img {i+1}\nMax:{max_val} Min:{min_val}\nMean:{mean_val:.1f} Std:{std_val:.1f}")
    ax.axis('off')

plt.tight_layout()
plt.show()

# 存成 DataFrame
df = pd.DataFrame(statistics)

# 儲存為 Excel 檔案
save_path = os.path.join(folder_path, "image_statistics.xlsx")
df.to_excel(save_path, index=False)

print(f"統計結果已儲存在：{save_path}✅")
