# %%
import torch
import numpy as np

# %%
# 0維tensor (scalar)
t1 = torch.tensor(1, dtype=torch.int16)
print(t1.shape)
print(t1)

# %%
# 1維tensor (vector)
t2 = torch.tensor([1,2,3], dtype=torch.float32)
print(t2.shape)
print(t2)

# %%
# 2維tensor (matrix)
t3 = torch.tensor([[1.,2],[3,4]])
print(t3.shape)
print(t3)

# %%
# 3維tensor (n-dimensional array)
t4 = torch.tensor([[[1, 2, 3], [3, 4, 5]],
									 [[5, 6, 7], [7, 8 ,9]]])
print(t4.shape)
print(t4)

# %% [markdown]
# 除了使用 torch.tensor 的方式建立張量外，我們也可以使用下列方式，建立給定形狀的張量。
# 1. torch.randn：
# 由常態分佈中抽取組成張量

# %%
# torch.randn: 由平均值為0，標準差為1的常態分佈中，抽樣元素組成給定形狀的張量
t5 = torch.randn((2,3,5))
print(t5.shape)
print(t5)

# %% [markdown]
# 2. torch.randint：
# 由上下界抽取組成張量

# %%
# torch.randint: 在給定的上下界(預設下界為0)中抽樣"整數"元素組成給定形狀的張量
t6 = torch.randint(low=0, high=100, size=(3,2,5))
print(t6.shape)
print(t6)

# %% [markdown]
# 3. torch.ones：
# 產生給定形狀，元素全為 1 的張量

# %%
# torch.ones: 產生給定形狀，元素全為1的張量
t7 = torch.ones((2,3))
print(t7.shape)
print(t7)

# %% [markdown]
# 4. torch.ones_like：
# 產生與給定張量相同形狀，但元素全為 1 的張量

# %%
# torch.ones_like: 產生與給定張量相同形狀，但元素全為1的張量
t8 = torch.ones_like(t6)
print(t8.shape)
print(t8)

# %% [markdown]
# 張量與陣列轉換
# 先前提及 tensor 與 numpy 的 array 是很相像的資料型態，我們可以由 array 來生成 tensor，也可以將 tensor 轉換為 array。
# 1. 生成 numpy array

# %%
# 產生numpy ndarray
x = np.array([[1.,2],[3,4]])
print(x.shape)
print(x)

# %% [markdown]
# 2. 由numpy array生成torch tensor

# %%
# 由numpy ndarray產生pytorch tensor
y = torch.from_numpy(x)
# y = torch.tensor(x) 也可以達到同樣效果
print(y.shape)
print(y)

# %% [markdown]
# 3. 由tensor轉換為array

# %%
# 將tensor轉換為array
z = y.numpy()
print(z.shape)
print(z)
