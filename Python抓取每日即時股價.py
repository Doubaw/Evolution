#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#https://mis.twse.com.tw/stock/fibest.jsp?stock=2330


# In[1]:


#每日即時股價
#https://medium.com/renee0918/python%E7%88%AC%E8%9F%B2-%E6%AF%8F%E6%97%A5%E5%8D%B3%E6%99%82%E8%82%A1%E5%83%B9-1382bc4d38d3

from IPython.display import display, clear_output
from urllib.request import urlopen
import pandas as pd
import datetime
import requests
import sched
import time
import json

s = sched.scheduler(time.time, time.sleep)
print(s)
def tableColor(val):
    if val > 0:
        color = 'red'
    elif val < 0:
        color = 'green'
    else:
        color = 'white'
    return 'color: %s' % color
def stock_crawler(targets):
    
    clear_output(wait=True)
    
    # 組成stock_list
    stock_list = '|'.join('tse_{}.tw'.format(target) for target in targets) 
    
    #　query data
    query_url = "http://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch="+ stock_list
    url = "http://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch="+ stock_list
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}
    re = requests.get(url, headers=headers) 
    re.encoding = 'utf8'
    str1=re.text
    str2 = str1.replace(' ', '')
    data = json.loads(str2)
    
    # 過濾出有用到的欄位
    columns = ['c','n','z','tv','v','o','h','l','y']
    df = pd.DataFrame(data['msgArray'], columns=columns)
    df.columns = ['股票代號','公司簡稱','當盤成交價','當盤成交量','累積成交量','開盤價','最高價','最低價','昨收價']
    df.insert(9, "漲跌百分比", 0.0) 
    
    # 新增漲跌百分比
    for x in range(len(df.index)):
        if df['當盤成交價'].iloc[x] != '-':
            df.iloc[x, [2,3,4,5,6,7,8]] = df.iloc[x, [2,3,4,5,6,7,8]].astype(float)
            df['漲跌百分比'].iloc[x] = (df['當盤成交價'].iloc[x] - df['昨收價'].iloc[x])/df['昨收價'].iloc[x] * 100
    
    # 紀錄更新時間
    time = datetime.datetime.now()  
    print("更新時間:" + str(time.hour)+":"+str(time.minute))
    
    # show table
    df = df.style.applymap(tableColor, subset=['漲跌百分比'])
    display(df)
    
    start_time = datetime.datetime.strptime(str(time.date())+'9:30', '%Y-%m-%d%H:%M')
    end_time =  datetime.datetime.strptime(str(time.date())+'13:30', '%Y-%m-%d%H:%M')
    
    # 判斷爬蟲終止條件
    if time >= start_time and time <= end_time:
        s.enter(1, 0, stock_crawler, argument=(targets,))
        
# 欲爬取的股票代碼
stock_list = ['1101','1102','1103','2330']

# 每秒定時器
s.enter(1, 0, stock_crawler, argument=(stock_list,))
s.run()


# In[ ]:


# In[ ]:




