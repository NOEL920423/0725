# 第一份作業，目標:
#                   隨機生成10張三通道影像。
#                   將10張影像轉為灰階(三通道之平均)。
#                   統計每張影像的最大值、最小值、平均以及標準差。
#                   以xlsx格式儲存以上統計數值，如下圖所示。 2025/07/17

# 匯入需要用的套件
import numpy as np      # numpy 用於數值計算和產生隨機陣列。
import matplotlib.pyplot as plt     # matplotlib.pyplot 用於繪圖、顯示影像。
import pandas as pd     # pandas 用於建立和操作表格資料，最後輸出 Excel 檔。
import os   # os 用來操作作業系統相關功能，例如建立資料夾與路徑合併

# 建立要儲存的資料夾
folder_path = r"D:\NEAF暑期培訓\lab"    # r"" 是 raw 字串，避免路徑中反斜線被誤解析。
os.makedirs(folder_path, exist_ok=True) # 建立該資料夾（若資料夾已存在，不會報錯，因為參數 exist_ok=True）。

# 建立統計資料的清單
statistics = []

# 圖像尺寸與圖形畫布
h, w = 10, 10 # 設定影像尺寸為 10x10（高度 h 與寬度 w）。
fig, axes = plt.subplots(2, 5, figsize=(12, 5)) # 使用 plt.subplots() 建立一個 2 行 5 列的繪圖網格，也就是 10 個圖。
                                                # figsize=(12,5) 指定整體圖像的寬高大小（英吋），方便排列。

for i in range(10):
    # 產生灰階影像 (值域 0~255)
    gray = np.random.randint(0, 255, (h, w), dtype=np.uint8)    # 使用 numpy 隨機產生一個 10x10 的二維陣列，元素為 0 到 255（灰階像素值範圍）。
                                                                # dtype=np.uint8 表示每個像素為無號 8 位元整數（標準影像格式）。
    # 統計值
    max_val = gray.max()    # 最大像素值。
    min_val = gray.min()    # 最小像素值。
    mean_val = gray.mean()  # 像素平均值（亮度平均）。
    std_val = gray.std()    # 像素標準差（亮度變化程度）。
    
    # 存入統計資料表
    statistics.append({
        "Image Index": i + 1,   # 影像編號（從 1 開始）。
        "Max": int(max_val),    # Max, Min 強制轉成整數。
        "Min": int(min_val),    
        "Mean": float(f"{mean_val:.2f}"),   # Mean, Std 四捨五入到小數點後 2 位。
        "Std": float(f"{std_val:.2f}")
    })
    
    # 顯示圖像
    ax = axes[i // 5][i % 5]    # 利用整除與取餘數選擇對應圖的位置： i // 5：第幾列（0 或 1）， i % 5：第幾欄（0 到 4）。
    ax.imshow(gray, cmap='gray')    # 將 gray 陣列顯示成灰階影像，cmap='gray' 指定灰階色彩映射。
    ax.set_title(f"Img {i+1}\nMax:{max_val} Min:{min_val}\nMean:{mean_val:.1f} Std:{std_val:.1f}") # 為圖設定標題，內容顯示影像編號與統計數據，數值以小數點一位呈現，換行排版整齊。
    ax.axis('off')  # 關閉該圖的座標軸與刻度，讓圖片視覺更乾淨。

plt.tight_layout()  # 自動調整圖間距，避免標題或圖片重疊。
plt.show()  # 顯示整個包含 10 張圖的視窗。

# 存成 DataFrame
df = pd.DataFrame(statistics)   # 將 statistics 清單轉換為 pandas 的 DataFrame 表格結構，方便後續處理與儲存。

# 儲存為 Excel 檔案 (利用 pandas 將 DataFrame 儲存為 Excel 格式)
save_path = os.path.join(folder_path, "image_statistics.xlsx")  # 使用 os.path.join 產生 Excel 檔案的完整路徑（路徑 + 檔名）。
df.to_excel(save_path, index=False) # index=False 表示不把 DataFrame 的索引（0,1,2...）存入檔案。

print(f"統計結果已儲存在：{save_path}\u2705")   # \u2705 是 Emoji 的 Unicode。
