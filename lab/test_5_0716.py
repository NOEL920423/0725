import numpy as np
import pandas as pd
# 生成線性數列
sequence_1 = np.linspace(1, 3, 10)
sequence_2 = np.linspace(1, 10, 10)

# 寫成字典型態，後面可以是 list 或 numpy array
d = {'s1': sequence_1, 
     's2': sequence_2,
    }

# 以字典型態寫入xlsl檔案
df = pd.DataFrame(data=d)
df.to_excel(f'test.xlsx')
#excel會存在 C:\Users\姜陳昊> 裡
