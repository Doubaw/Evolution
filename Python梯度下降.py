#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

x_data = [ 9,  4,  7 , 3 , 10  , 7 , 4 ,  3 , 1,  9]
y_data = [  45  , 24 ,  59  , 28  , 91 , 28  ,  42 ,  18 , 14, 82]

# 建立網格資料
x = np.arange(0,10,0.05)
y = np.arange(0,10,0.05)
Z =  np.zeros((len(x), len(y)))
X, Y = np.meshgrid(x, y)

for i in range(len(x)):
    for j in range(len(y)):
        b = x[i]
        a = y[j]
        Z[j][i] = 0
        for n in range(len(x_data)):
            Z[j][i] = Z[j][i] +  (y_data[n] - b - a*x_data[n])**2
        Z[j][i] = Z[j][i]/len(x_data)
        
# 決定 a 與 b 的起始點
b = 0
a = 0

# 決定 learning rate
lr = 0.00005

# 決定 iteration 的次數
iteration = 10000

# 儲存每一次 iterate 後的結果
b_history = [b]
a_history = [a]

# 執行梯度下降
for i in range(iteration):
    b_grad = 0.0
    a_grad = 0.0
    
    # 計算損失函數分別對 a 和 b 的偏微分
    for n in range(len(x_data)):
        b_grad = b_grad  - 2.0*(y_data[n] - b - a*x_data[n])*1.0
        a_grad = a_grad  - 2.0*(y_data[n] - b - a*x_data[n])*x_data[n]
        
    # 更新 a, b 位置 
    b = b - lr * b_grad
    a = a - lr * a_grad
    
    # 紀錄 a, b 的位置 
    b_history.append(b)
    a_history.append(a)

# 建立等高線圖
plt.contourf(x,y,Z, 50, alpha=0.5, cmap=plt.get_cmap('jet'))

# 繪製目標點
plt.plot([1.97], [7.22], 'x', ms=12, markeredgewidth=3, color='red')

# 繪製 a,b iteration 的結果
plt.plot(b_history, a_history, 'o-', ms=3, lw=1.5, color='black')

# 定義圖形範圍
plt.xlim(0,5)
plt.ylim(0,10)

# 繪製 x 軸與 y 軸的標籤
plt.xlabel(r'$b$', fontsize=16)
plt.ylabel(r'$a$', fontsize=16)
plt.show()


# In[ ]:




