#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import numpy as np
import matplotlib.pyplot as plt
import math

w=np.array([0,0,0,0])
x=np.array([[-1,0,-2,1],[-1,-0.5,1.5,0],[-1, 0.5, -1.5, 0.5],[-1, 0.5, 2, 1],[-1.5, -0.5, 1.5, -1.5],[2, -0.5, 1.5, 0.5]])
d=np.array([1,-1,1,-1,1,1])

number=100
n=0.95

answer=[]

def test1(wa):
    for i in range(number):
        f=np.dot(wa,x[i%6].T) 
        net=f+0
        rf=round(net,5)
        fx=(1 / (1 + math.exp(-rf))) if f>=0  else (1 / (1 + math.exp(rf))) 
        lm=((lambda x,y:x-y)(d[i%6],fx))
        ans=wa+((n**i)*(lm*fx*(1-fx)*x[i%6]))
        
        wa=ans
        answer.append(wa)
        

test1(w)

plt.plot(answer)
labe=['w1','w2','w3','w4']
plt.legend(labe)
plt.show()
print(answer[-1])


# In[ ]:




