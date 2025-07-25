import pandas as pd

# 創建 DataFrame
data = {
    'Name': ['John', 'Emma', 'Alex'],
    'Age': [28, 32, 24],
    'City': ['New York', 'London', 'Paris']
}
df = pd.DataFrame(data)
print(df)

# 數據選擇
print("\nSelect 'Name' column:")
print(df['Name'])

# 數據過濾
print("\nFilter age > 25:")
print(df[df['Age'] > 25])

# 基本數據操作
print("\nSort by Age:")
print(df.sort_values('Age'))
