#!/usr/bin/env python
# coding: utf-8

# In[79]:


#MSError
#https://www.geeksforgeeks.org/python-mean-squared-error/
#https://clay-atlas.com/blog/2019/10/19/machine-learning-chinese-sigmoid-function/
#溢位
#https://www.delftstack.com/zh-tw/howto/python/sigmoid-function-python/


# In[ ]:


#Sgn Function


# In[2]:


import time
import numpy as np
import matplotlib.pyplot as plt

w=np.array([0,0,0,0])
x=np.array([[-1,0,-2,1],[-1,-0.5,1.5,0],[-1, 0.5, -1.5, 0.5],[-1, 0.5, 2, 1],[-1.5, -0.5, 1.5, -1.5],[2, -0.5, 1.5, 0.5]])
d=np.array([1,-1,1,-1,1,1])
mse=[]

number=int(input("輸入執行多少次迴圈"))
n=float(input("輸入n值"))
# print("------------------------------------------")
answer=[[0,0,0,0]]
def test1(wa):
    for i in range(number):
        f=np.dot(wa,x[i%6].T) #矩陣相乘
#         print(f)
        fans=1 if f>=0 else -1 #比較sgn function 大於等於0 回傳 1 小於0回傳 -1
        ans=wa+(n**i)*(d[i%6]-fans)*x[i%6] #帶入公式 沒有T次方會導致 值"沒有"收縮 呈現波浪
        wa=ans
        answer.append(wa)
# minans=(d[i%6]-answer[-1])**2
# min.append(minans)
test1(w)

print("------------------------------------------")
print("沒有平方 導致值沒有收縮 呈現波浪")
labe=['w1','w2','w3','w4']
plt.plot(answer)
plt.legend(labe)
plt.show()
print(answer[-1])

print("------------------------------------------")
sum=0
for i in range(len(x)):
    b=np.dot(x[i],answer[-1].T) 
    ms=(d[i]-b)**2
    sum+=ms
print("MS Error",sum)
print("------------------------------------------")


# In[ ]:





# In[1]:


import time
import numpy as np
import matplotlib.pyplot as plt

w=np.array([0,0,0,0])
x=np.array([[-1,0,-2,1],[-1,-0.5,1.5,0],[-1, 0.5, -1.5, 0.5],[-1, 0.5, 2, 1],[-1.5, -0.5, 1.5, -1.5],[2, -0.5, 1.5, 0.5]])
d=np.array([1,-1,1,-1,1,1])
mse=[]

number=1000
n=0.95
print("------------------------------------------")
answer=[[0,0,0,0]]
def test1(wa):
    for i in range(number):
        f=np.dot(wa,x[i%6].T) #矩陣相乘
#         print(f)
        fans=1 if f>=0 else -1 #比較sgn function 大於等於0 回傳 1 小於0回傳 -1
        ans=wa+(n**i)*(d[i%6]-fans)*x[i%6] #帶入公式 沒有T次方會導致 值"沒有"收縮 呈現波浪
        minans=(d[i%6]-answer[-1])**2
        mse.append(minans)
#         b=np.dot(x[i%6],ans.T) 
# #       print("d",d[i%6],"b",b)
#         MSE = np.square(np.subtract(d[i%6],b)).mean()
        wa=ans
        answer.append(wa)

test1(w)

print("------------------------------------------")
print("沒有平方 導致值沒有收縮 呈現波浪")
labe=['w1','w2','w3','w4']
plt.plot(answer)
plt.legend(labe)
plt.show()
print(answer[-1])

print("------------------------------------------")
sum=0
for i in range(len(x)):
    b=np.dot(x[i],answer[-1].T) 
    ms=(d[i]-b)**2
    sum+=ms
print("MS Error",sum)
print("------------------------------------------")


# In[ ]:





# In[ ]:





# In[5]:


import time
import numpy as np
import matplotlib.pyplot as plt

w=np.array([0,0,0,0])
x=np.array([[-1,0,-2,1],[-1,-0.5,1.5,0],[-1, 0.5, -1.5, 0.5],[-1, 0.5, 2, 1],[-1.5, -0.5, 1.5, -1.5],[2, -0.5, 1.5, 0.5]])
d=np.array([1,-1,1,-1,1,1])
mserr=[]

number=1000
n=0.95
print("------------------------------------------")
answer=[[0,0,0,0]]
def test1(wa):
    for i in range(number):
        f=np.dot(wa,x[i%6].T) #矩陣相乘
#         print(f)
        fans=1 if f>=0 else -1 #比較sgn function 大於等於0 回傳 1 小於0回傳 -1
        ans=wa+(n**i)*(d[i%6]-fans)*x[i%6] #帶入公式 沒有T次方會導致 值"沒有"收縮 呈現波浪
#         minans=(d[i%6]-answer[-1])**2
#         mse.append(minans)
        b=np.dot(x[i%6],ans.T) 
#       print("d",d[i%6],"b",b)
        mse = np.square(np.subtract(d[i%6],b)).mean()
        wa=ans
        answer.append(wa)
        mserr.append(mse)    
test1(w)

# print("------------------------------------------")
# print("沒有平方 導致值沒有收縮 呈現波浪")
# labe=['w1','w2','w3','w4']
plt.plot(mserr)
# plt.legend(labe)
plt.show()
# print(answer[-1])

# print("------------------------------------------")
# sum=0
# for i in range(len(x)):
#     b=np.dot(x[i],answer[-1].T) 
#     ms=(d[i]-b)**2
#     sum+=ms
# print("MS Error",sum)
# print("------------------------------------------")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#有做溢位處裡(有MS Error略為調整)


# In[48]:


import time
import numpy as np
import matplotlib.pyplot as plt
import math

w=np.array([1,1,1,1])
x=np.array([[-1,0,-2,1],[-1,-0.5,1.5,0],[-1, 0.5, -1.5, 0.5],[-1, 0.5, 2, 1],[-1.5, -0.5, 1.5, -1.5],[2, -0.5, 1.5, 0.5]])
d=np.array([1,-1,1,-1,1,1])

# number=int(input("輸入執行多少次迴圈"))
# n=float(input("輸入n值"))

number=10000
n=0.95

print("------------------------------------------")
answer=[[0,0,0,0]]

def test1(wa):
    for i in range(number):
        f=np.dot(wa,x[i%6].T) #矩陣相乘
        rf=round(f,5)
        fans=(1 / (1 + math.exp(-rf))) if f>=0  else (1 / (1 + math.exp(rf)))
        ans=wa+(n**i)*(d[i%6]-fans)*x[i%6] #帶入公式 沒有T次方會導致 值"沒有"收縮 呈現波浪
        wa=ans
        answer.append(wa)
test1(w)

print("------------------------------------------")
print("沒有平方 導致值沒有收縮 呈現波浪")
labe=['w1','w2','w3','w4']
plt.plot(answer)
plt.legend(labe)
plt.show()
print(answer[-1])

print("------------------------------------------")

db=[]
for i in range(len(x)):
    b=np.dot(x[i],answer[-1].T) 
    db.append(b)

MSE = np.square(np.subtract(d,db)).mean()    
    
print("MS Error",MSE)
print("------------------------------------------")


# In[ ]:


#有做溢位處裡(沒有做處理MS Error)


# In[82]:


import time
import numpy as np
import matplotlib.pyplot as plt
import math

w=np.array([0,0,0,0])
x=np.array([[-1,0,-2,1],[-1,-0.5,1.5,0],[-1, 0.5, -1.5, 0.5],[-1, 0.5, 2, 1],[-1.5, -0.5, 1.5, -1.5],[2, -0.5, 1.5, 0.5]])
d=np.array([1,-1,1,-1,1,1])

number=int(input("輸入執行多少次迴圈"))
n=float(input("輸入n值"))
print("------------------------------------------")
answer=[[0,0,0,0]]

def test1(wa):
    for i in range(number):
        f=np.dot(wa,x[i%6].T) #矩陣相乘
        rf=round(f,5)
        fans=(1 / (1 + math.exp(-rf))) if f>=0  else (1 / (1 + math.exp(rf)))
        ans=wa+(n**i)*(d[i%6]-fans)*x[i%6] #帶入公式 沒有T次方會導致 值"沒有"收縮 呈現波浪
        wa=ans
        answer.append(wa)
test1(w)

print("------------------------------------------")
print("沒有平方 導致值沒有收縮 呈現波浪")
labe=['w1','w2','w3','w4']
plt.plot(answer)
plt.legend(labe)
plt.show()
print(answer[-1])

print("------------------------------------------")
sum=0
for i in range(len(x)):
    b=np.dot(x[i],answer[-1].T) 
    ms=(d[i]-b)**2
    sum+=ms
print("MS Error",sum)
print("------------------------------------------")


# In[ ]:


#沒有做溢位處裡


# In[81]:


import time
import numpy as np
import matplotlib.pyplot as plt
import math

w=np.array([0,0,0,0])
x=np.array([[-1,0,-2,1],[-1,-0.5,1.5,0],[-1, 0.5, -1.5, 0.5],[-1, 0.5, 2, 1],[-1.5, -0.5, 1.5, -1.5],[2, -0.5, 1.5, 0.5]])
d=np.array([1,-1,1,-1,1,1])

number=int(input("輸入執行多少次迴圈"))
n=float(input("輸入n值"))
print("------------------------------------------")
answer=[[0,0,0,0]]
def test1(wa):
    for i in range(number):
        f=np.dot(wa,x[i%6].T) #矩陣相乘
        rf=round(f,5)
        fans=1/(1+np.exp(-rf))
        ans=wa+(n**i)*(d[i%6]-fans)*x[i%6] #帶入公式 沒有T次方會導致 值"沒有"收縮 呈現波浪
        wa=ans
        answer.append(wa)
test1(w)

print("------------------------------------------")
print("沒有平方 導致值沒有收縮 呈現波浪")
labe=['w1','w2','w3','w4']
plt.plot(answer)
plt.legend(labe)
plt.show()
print(answer[-1])

print("------------------------------------------")
sum=0
for i in range(len(x)):
    b=np.dot(x[i],answer[-1].T) 
    ms=(d[i]-b)**2
    sum+=ms
print("MS Error",sum)
print("------------------------------------------")


# In[1]:


#更改公式


# In[3]:


import time
import numpy as np
import matplotlib.pyplot as plt
import math

w=np.array([1,1,1,1])
x=np.array([[-1,0,-2,1],[-1,-0.5,1.5,0],[-1, 0.5, -1.5, 0.5],[-1, 0.5, 2, 1],[-1.5, -0.5, 1.5, -1.5],[2, -0.5, 1.5, 0.5]])
d=np.array([1,-1,1,-1,1,1])

number=1000
n=0.95
# print("------------------------------------------")
answer=[[0,0,0,0]]
mserror=[]

def test1(wa):
    for i in range(number):
        f=np.dot(wa,x[i%6].T) #矩陣相乘
        
        rf=round(f,5)
        fx=(1 / (1 + math.exp(-rf))) if f>=0  else (1 / (1 + math.exp(rf))) 
#         print(fx)
        ans=wa+(n**i)*fx*(1-fx)*x[i%6]
#         print(ans)
        
        b=np.dot(x[i%6],ans.T) 
#       print("d",d[i%6],"b",b)
        MSE = np.square(np.subtract(d[i%6],b)).mean()
#       ans=wa+(n**i)*fans*(d[i%6]-fans)*x[i%6]
        
#         print("MS Error",MSE)
        
        wa=ans
        answer.append(wa)
        mserror.append(MSE)
test1(w)




# print("------------------------------------------")
# print("沒有平方 導致值沒有收縮 呈現波浪")
# labe=['w1','w2','w3','w4']
plt.plot(mserror)
# plt.legend(labe)
plt.show()
# print(answer[-1])







# print("------------------------------------------")

# db=[]
# for i in range(len(x)):
#     b=np.dot(x[i],answer[-1].T) 
#     db.append(b)
# print(db)
# MSE = np.square(np.subtract(d,db)).mean()    
    
# print("MS Error",MSE)
# print("------------------------------------------")


# In[ ]:


#測試


# In[24]:


import time
import numpy as np
import matplotlib.pyplot as plt
import math

w=np.array([0,0,0,0])
x=np.array([[-1,0,-2,1],[-1,-0.5,1.5,0],[-1, 0.5, -1.5, 0.5],[-1, 0.5, 2, 1],[-1.5, -0.5, 1.5, -1.5],[2, -0.5, 1.5, 0.5]])
d=np.array([1,-1,1,-1,1,1])

number=100
n=0.95
# print("------------------------------------------")
answer=[[0,0,0,0]]
mserror=[]

def test1(wa):
    for i in range(number):
        f=np.dot(wa,x[i%6].T) #矩陣相乘 + b
        
#         net=np.dot(wa,x[i%6].T)+w[i%4]

        rf=round(f,5)
        fx=(1 / (1 + math.exp(-rf))) if f>=0  else (1 / (1 + math.exp(rf))) 
#         print(fx)
        ans=wa+(n**i)*fx*(1-fx)*x[i%6]
        
        b=np.dot(x[i%6],ans.T) 
        
        
#         MSE = np.square(np.subtract(d[i%6],b)).mean()
        
        wa=ans
        answer.append(wa)
        mserror.append(MSE)
test1(w)

plt.plot(mserror)
plt.show()


# In[ ]:


net(0)=w[0]*x[0]+w[0]
net(1)=w[1]*x[1]+w[1]


# In[34]:


import time
import numpy as np
import matplotlib.pyplot as plt
import math

w=np.array([0,0,0,0])
x=np.array([[-1,0,-2,1],[-1,-0.5,1.5,0],[-1, 0.5, -1.5, 0.5],[-1, 0.5, 2, 1],[-1.5, -0.5, 1.5, -1.5],[2, -0.5, 1.5, 0.5]])
d=np.array([1,-1,1,-1,1,1])

number=10
n=0.95

answer=[]
# mserror=[]

def test1(wa):
    for i in range(number):
        f=np.dot(wa,x[i%6].T) #矩陣相乘 + b
#         print(f,w[i%4])
        net=f+w[i%4]
#         print(f+w[i%4])
#         net=np.dot(wa,x[i%6].T)+w[i%4]
#         print(net)
        rf=round(net,5)
        fx=(1 / (1 + math.exp(-rf))) if f>=0  else (1 / (1 + math.exp(rf))) 
# #         print(fx)
        ans=wa+fx*(1-fx)*x[i%6]
#         ans=wa+(n**i)*fx*(1-fx)*x[i%6]
        
#         b=np.dot(x[i%6],ans.T) 
        
        
#         MSE = np.square(np.subtract(d[i%6],b)).mean()
        
        wa=ans
        answer.append(wa)
#         mserror.append(MSE)
test1(w)

plt.plot(answer)
labe=['w1','w2','w3','w4']
plt.legend(labe)
plt.show()


# In[ ]:


#可能可以


# In[10]:


import time
import numpy as np
import matplotlib.pyplot as plt
import math

w=np.array([0,0,0,0])
x=np.array([[-1,0,-2,1],[-1,-0.5,1.5,0],[-1, 0.5, -1.5, 0.5],[-1, 0.5, 2, 1],[-1.5, -0.5, 1.5, -1.5],[2, -0.5, 1.5, 0.5]])
d=np.array([1,-1,1,-1,1,1])

number=1000000
n=0.95

answer=[]
# mserror=[]

def test1(wa):
    for i in range(number):
        f=np.dot(wa,x[i%6].T) 
#         net=f+w[i%4]  #矩陣相乘 + b
        net=f+0
        rf=round(net,5)
        fx=(1 / (1 + math.exp(-rf))) if f>=0  else (1 / (1 + math.exp(rf))) 
        ans=wa+(d[i%6]-fx)*fx*(1-fx)*x[i%6]
        
        wa=ans
        answer.append(wa)
        

test1(w)

plt.plot(answer)
labe=['w1','w2','w3','w4']
plt.legend(labe)
plt.show()
print(answer[-1])


# In[1]:


import time
import numpy as np
import matplotlib.pyplot as plt
import math

w=np.array([0,0,0,0])
x=np.array([[-1,0,-2,1],[-1,-0.5,1.5,0],[-1, 0.5, -1.5, 0.5],[-1, 0.5, 2, 1],[-1.5, -0.5, 1.5, -1.5],[2, -0.5, 1.5, 0.5]])
d=np.array([1,-1,1,-1,1,1])

number=10000
n=0.95

answer=[]


def test1(wa):
    for i in range(number):
        f=np.dot(wa,x[i%6].T) 
        
        net=f+0
        rf=round(net,5)
        fx=(1 / (1 + math.exp(-rf))) if f>=0  else (1 / (1 + math.exp(rf))) 
        lm=((lambda x,y:x-y)(d[i%6],fx))

        ans=wa+(lm*fx*(1-fx)*x[i%6])
        
        wa=ans
        answer.append(wa)
        

test1(w)

plt.plot(answer)
labe=['w1','w2','w3','w4']
plt.legend(labe)
plt.show()
print(answer[-1])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[7]:


import time
import numpy as np
import matplotlib.pyplot as plt

w=np.array([0,0,0,0])
x=np.array([[-1,0,-2,1],[-1,-0.5,1.5,0],[-1, 0.5, -1.5, 0.5],[-1, 0.5, 2, 1],[-1.5, -0.5, 1.5, -1.5],[2, -0.5, 1.5, 0.5]])
d=np.array([1,-1,1,-1,1,1])
mserr=[]

number=1000
n=0.95
print("------------------------------------------")
answer=[[0,0,0,0]]
def test1(wa):
    for i in range(number):
        f=np.dot(wa,x[i%6].T) #矩陣相乘
        
        fans=1 if f>=0 else -1 #比較sgn function 大於等於0 回傳 1 小於0回傳 -1
        ans=wa+(n**i)*(d[i%6]-fans)*x[i%6] #帶入公式 沒有T次方會導致 值"沒有"收縮 呈現波浪

        b=np.dot(x[i%6],ans.T) 
        mse = np.square(np.subtract(d[i%6],b)).mean()
        wa=ans
        answer.append(wa)
        mserr.append(mse)    
test1(w)

plt.plot(mserr)
plt.show()
print(mserr[-1])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[4]:


import time
import numpy as np
import matplotlib.pyplot as plt

w=np.array([0,0,0,0])
x=np.array([[-1,0,-2,1],[-1,-0.5,1.5,0],[-1, 0.5, -1.5, 0.5],[-1, 0.5, 2, 1],[-1.5, -0.5, 1.5, -1.5],[2, -0.5, 1.5, 0.5]])
d=np.array([1,-1,1,-1,1,1])
mserr=[]

number=1000
n=0.95
print("------------------------------------------")
answer=[]
def test1(wa):
    for i in range(number):
        f=np.dot(wa,x[i%6].T) #矩陣相乘
        
        fans=1 if f>=0 else -1 #比較sgn function 大於等於0 回傳 1 小於0回傳 -1
        ans=wa+(n**i)*(d[i%6]-fans)*x[i%6] #帶入公式 沒有T次方會導致 值"沒有"收縮 呈現波浪

        b=np.dot(x[i%6],ans.T) 
        mse = np.square(np.subtract(d[i%6],b)).mean()
        wa=ans
        answer.append(wa)
        mserr.append(mse)    
test1(w)

plt.plot(mserr)
plt.show()


# In[8]:


import time
import numpy as np
import matplotlib.pyplot as plt
import math

w=np.array([0,0,0,0])
x=np.array([[-1,0,-2,1],[-1,-0.5,1.5,0],[-1, 0.5, -1.5, 0.5],[-1, 0.5, 2, 1],[-1.5, -0.5, 1.5, -1.5],[2, -0.5, 1.5, 0.5]])
d=np.array([1,-1,1,-1,1,1])

number=1000
n=0.95

answer=[]
mserr=[]

def test1(wa):
    for i in range(number):
        f=np.dot(wa,x[i%6].T) 
        net=f+0
        rf=round(net,5)
        fx=(1 / (1 + math.exp(-rf))) if f>=0  else (1 / (1 + math.exp(rf))) 
        lm=((lambda x,y:x-y)(d[i%6],fx))
        ans=wa+((n**i)*(lm*fx*(1-fx)*x[i%6]))
        
        b=np.dot(x[i%6],ans.T) 
        mse = np.square(np.subtract(d[i%6],b)).mean()
        
        wa=ans
        answer.append(wa)
        mserr.append(mse) 
        

test1(w)

plt.plot(answer)
labe=['w1','w2','w3','w4']
plt.legend(labe)
plt.show()
print(answer[-1])
# print(mserr)
# plt.plot(mserr)
# plt.show()


# In[ ]:




