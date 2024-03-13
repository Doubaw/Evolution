#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Python抓取台股證交所每日股價資料
#https://sites.google.com/site/zsgititit/home/python-cheng-shi-she-ji/shi-yongpython-zhua-qu-tai-gu-zheng-jiao-suo-mei-ri-gu-jia-zi-liao-yu-shi-yongpandas-jin-xing-fen-xi


# In[1]:


import numpy as np
import requests
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

def get_stock_history(date, stock_no):
    url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?date='+date+'&stockNo='+stock_no
    r = requests.get(url)
    data = r.json()
    return transform(data['data'])  #進行資料格式轉換

def transform_date(date):
    y, m, d = date.split('/')
    return str(int(y)+1911) + '/' + m  + '/' + d  #民國轉西元
    
def transform_data(data):
    data[0] = datetime.datetime.strptime(transform_date(data[0]), '%Y/%m/%d')
    data[1] = int(data[1].replace(',', ''))  #把千進位的逗點去除
    data[2] = int(data[2].replace(',', ''))
    data[3] = float(data[3].replace(',', ''))
    data[4] = float(data[4].replace(',', ''))
    data[5] = float(data[5].replace(',', ''))
    data[6] = float(data[6].replace(',', ''))
    data[7] = float(0.0 if data[7].replace(',', '') == 'X0.00' else data[7].replace(',', ''))  # +/-/X表示漲/跌/不比價
    data[8] = int(data[8].replace(',', ''))
    return data

def transform(data):
    return [transform_data(d) for d in data]

def create_df(date,stock_no):
    s = pd.DataFrame(get_stock_history(date, stock_no))
    s.columns = ['date', 'shares', 'amount', 'open', 'high', 'low', 'close', 'change', 'turnover']
                #"日期","成交股數","成交金額","開盤價","最高價","最低價","收盤價","漲跌價差","成交筆數" 
    stock = []
    for i in range(len(s)):
        stock.append(stock_no)
    s['stockno'] = pd.Series(stock ,index=s.index)  #新增股票代碼欄，之後所有股票進入資料表才能知道是哪一張股票
    datelist = []
    for i in range(len(s)):
        datelist.append(s['date'][i])
    s.index = datelist  #索引值改成日期
    s2 = s.drop(['date'],axis = 1)  #刪除日期欄位
    mlist = []
    for item in s2.index:
        mlist.append(item.month)
    s2['month'] = mlist  #新增月份欄位
    return s2
        
listDji = ['2330']
#   time = datetime.datetime.now().strftime("%Y%m%d")
for i in range(len(listDji)):
    result = create_df('20210310', listDji[i])
    print(result)
    
print(result.groupby('month').close.count())  #每個月幾個營業日
print(result.groupby('month').shares.sum())  #每個月累計成交股數



import talib
import pandas as pd
stock_file = pd.read_csv(r'D:\0050.TW.csv')
df['Date'] = pd.to_datetime(df['Date'])

df.set_index("Date", inplace=True)

print(df.head(5))


import numpy as np
K,D = talib.STOCH(high = np.array(df['high']), 
                low = np.array(df['low']), 
                close = np.array(df['close']),
                fastk_period=9,
                slowk_period=3,
                slowk_matype=0,
                slowd_period=3,
                slowd_matype=0)



import mpl_finance as mpf
get_ipython().run_line_magic('matplotlib', 'inline')

fig = plt.figure(figsize=(24, 20))
ax = fig.add_axes([0,0.3,1,0.4])
ax2 = fig.add_axes([0,0.2,1,0.1])

ax.set_xticks(range(0, len(df.index), 10))
ax.set_xticklabels(df.index[::10])
mpf.candlestick2_ochl(ax, df['open'], df[' close'], df['high'], df['low'], width=0.6, colorup='r', colordown='g', alpha=0.75)

ax2.plot(K, label='K值')
ax2.plot(D, label='D值')
ax2.set_xticks(range(0, len(df.index), 10))
ax2.set_xticklabels(df.index[::10])


# In[ ]:




