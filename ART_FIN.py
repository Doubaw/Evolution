#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Part 01完成


# In[2]:


import numpy as np
from matplotlib import pyplot as plt
#net=a/b
#neta=比較完1的個數(test)
#netb=儲存值1的個數(save)
#=================================================================
#v=a/b
#va=比較完1的個數(test)
#vb=要比較的值1的個數(data)
#=================================================================
#data 初始值
data=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
      [1,0,0,0,1,1,1,1,1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,1],
      [1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,1,1,1,1],
      [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]]

ldata=len(data)
#計有幾次一樣model
count=0
#空陣列 儲存model
save=[]
#警戒值
p=0.7
#=================================================================
#初始第一個資料
#Input值有幾個1,m分子
data1=data[0]
m=data1.count(1)
#原本model有幾個1,d分母
d=data1.count(1)
#net & v
net=m/37
v=m/d
#儲存到save
save.append(data1)

count+=1

print("net",net)
print("v",v)
#================================================================= 
print(save)
print("count",count)
print("=========================================================")
#=================================================================    
#比較第二到後續    
def funv():
    global count
    #儲存save陣列(迴圈數)
    numb=[]
    #儲存比較完的陣列
    netv=[]
    #net & v陣列
    netvsv=[]
    #目前儲存陣列的大小(有幾個數)
    n=count
    #抓取儲存陣列的資料(0~目前儲存陣列大小)
    for i in range(len(save)):
        #test初始值
        test=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        #netb=儲存值1的個數(save)
        netb=save[i].count(1)
        #vb=要比較的值1的個數(data)
        vb=data[n].count(1)
        #抓取儲存陣列中第一陣列的第一個元素 vs 下一位陣列的第一個元素 比較
        for j in range(36):
            if(save[i][j]==data[n][j]):
                if(save[i][j]!=0 and data[n][j]!=0):
                    #比較兩個陣列相比 元素不等於0但是相通的值 記錄下來(j)
                    test[j]=1
                    continue
        #在i=0時，test是多少
        #儲存比較完的值
        netv.append(test)
        #儲存save陣列(迴圈數)
        numb.append(i)
        m=netv[i].count(1)
        v=m/vb
        #儲存v值
        netvsv.append(v)
    #最大的v值
    maxv=max(netvsv)
    #將v值與比較完的值做成字典( 0.6:[0,1,0] )
    sumv=dict(zip(netvsv,netv))
    #將v值與迴圈數做成字典( 0.6:1 ) ( 在第1迴圈時，v值是0.6 )
    vs=dict(zip(netvsv,numb))
    for i in range(len(save)):
        #最大值大於警戒值，進行更換
        if(maxv>p):
            print("not new, so neet to change")
            one=vs.get(maxv)
            sec=sumv.get(maxv)
            save[one]=sec
            break
        #小於警戒值，添加項目
        else:
            print("new, insert data")
            save.append(data[n])  
            break

    count+=1
    print(save) 
    print("count",count)
    print("=========================================================")    
       
for i in range(ldata-1):
    funv()
print("=========================================================")     
print(save)
print("=========================================================") 
for i in range(len(save)):
    print("No.",i+1)
    for j in range(9):
        print("-----------------")
        print("|",save[i][j],"|",save[i][j+9],"|",save[i][j+18],"|",save[i][j+27],"|")
    print("-----------------")
    print(" ")
print("=========================================================")

def funimage():
    for i in range(len(save)):
        image=np.transpose(np.array(save[i]).reshape(4,9)).tolist()
        plt.subplot(2, 4, i+1)
        plt.imshow(image,cmap='gray')
funimage()


# In[ ]:


1 234 567 89


# In[ ]:


#Part 02添加亂數


# In[56]:


import numpy as np
import random
from matplotlib import pyplot as plt

#net=a/b
#neta=比較完1的個數(test)
#netb=儲存值1的個數(save)
#=================================================================
#v=a/b
#va=比較完1的個數(test)
#vb=要比較的值1的個數(data)
#=================================================================

#data 初始值
data=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
      [1,0,0,0,1,1,1,1,1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,1],
      [1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,1,1,1,1],
      [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]]

#=================================================================
#亂數
rand_list=[]
for i in range(36):
    n=random.randint(0,1)
    rand_list.append(n)

data.append(rand_list)
print("=========================================================")
print("Random list",rand_list)
print("=========================================================")

#=================================================================
#data有幾個
ldata=len(data)
#計有幾次一樣model
count=0
#空陣列 儲存model
save=[]
#警戒值
p=0.5
#=================================================================
#初始第一個資料
#Input值有幾個1,m分子
data1=data[0]
m=data1.count(1)
#原本model有幾個1,d分母
d=data1.count(1)
#net & v
net=m/37
v=m/d
#儲存到save
save.append(data1)

count+=1

print("net",net)
print("v",v)
#================================================================= 
print(save)
print("count",count)
print("=========================================================")
#=================================================================    
#比較第二到後續    
def funv():
    global count
    #儲存save陣列(迴圈數)
    numb=[]
    #儲存比較完的陣列
    netv=[]
    #net & v陣列
    netvsv=[]
    #目前儲存陣列的大小(有幾個數)
    n=count
    #抓取儲存陣列的資料(0~目前儲存陣列大小)
    for i in range(len(save)):
        #test初始值
        test=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        #netb=儲存值1的個數(save)
        netb=save[i].count(1)
        #vb=要比較的值1的個數(data)
        vb=data[n].count(1)
        #抓取儲存陣列中第一陣列的第一個元素 vs 下一位陣列的第一個元素 比較
        for j in range(36):
            if(save[i][j]==data[n][j]):
                if(save[i][j]!=0 and data[n][j]!=0):
                    #比較兩個陣列相比 元素不等於0但是相通的值 記錄下來(j)
                    test[j]=1
                    continue
        #在i=0時，test是多少
        #儲存比較完的值
        netv.append(test)
        #儲存save陣列(迴圈數)
        numb.append(i)
        m=netv[i].count(1)
        v=m/vb
        #儲存v值
        netvsv.append(v)
    #最大的v值
    maxv=max(netvsv)
    #將v值與比較完的值做成字典( 0.6:[0,1,0] )
    sumv=dict(zip(netvsv,netv))
    #將v值與迴圈數做成字典( 0.6:1 ) ( 在第1迴圈時，v值是0.6 )
    vs=dict(zip(netvsv,numb))
    for i in range(len(save)):
        #最大值大於警戒值，進行更換
        if(maxv>p):
            print("not new, so neet to change")
            one=vs.get(maxv)
            sec=sumv.get(maxv)
            save[one]=sec
            break
        #小於警戒值，添加項目
        else:
            print("new, insert data")
            save.append(data[n])  
            break

    count+=1
    print(save) 
    print("count",count)
    print("=========================================================")    
       
for i in range(ldata-1):
    funv()
print("=========================================================")     
print(save)
print("=========================================================") 
for i in range(len(save)):
    print("No.",i+1)
    for j in range(9):
        print("-----------------")
        print("|",save[i][j],"|",save[i][j+9],"|",save[i][j+18],"|",save[i][j+27],"|")
    print("-----------------")
    print(" ")
print("=========================================================")

def funimage():
    for i in range(len(save)):
        image=np.transpose(np.array(save[i]).reshape(4,9)).tolist()
        plt.subplot(2, 4, i+1)
        plt.imshow(image,cmap='gray')
funimage()


# In[ ]:




