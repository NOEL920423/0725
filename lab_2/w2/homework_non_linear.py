import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 讀取數據
data = pd.read_csv(r"D:\NEAF暑期培訓\lab_2\dataset.csv")

# 分割特徵和目標變量
X = data[['Runtime']]  # 注意：保持為 DataFrame（2D）
y = data['faults']     # 目標變量

# 分割數據集為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 創建並訓練多項式回歸模型
degree = 5
polyreg = make_pipeline(PolynomialFeatures(degree), LinearRegression())
polyreg.fit(X_train, y_train)

# 預測測試集結果
y_pred = polyreg.predict(X_test)

# 模型評估
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# 輸出性能指標
print(f'Mean Squared Error: {mse:.4f}')
print(f'R^2 Score: {r2:.4f}')

# 繪圖
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='black', label='Actual')

# 產生平滑的曲線資料點並預測
X_fit = np.linspace(X.min().values[0], X.max().values[0], 100).reshape(-1, 1)
X_fit_df = pd.DataFrame(X_fit, columns=['Runtime'])
y_fit = polyreg.predict(X_fit_df)


plt.plot(X_fit, y_fit, color='red', linewidth=2, label='Predicted Curve')
plt.title('Polynomial Regression (degree=5)')
plt.xlabel('Runtime')
plt.ylabel('Faults')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
