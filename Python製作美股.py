#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


#用 Python 打造自己的股市資料庫 — 美股篇
#https://medium.com/ai%E8%82%A1%E4%BB%94/%E7%94%A8-python-%E6%89%93%E9%80%A0%E8%87%AA%E5%B7%B1%E7%9A%84%E8%82%A1%E5%B8%82%E8%B3%87%E6%96%99%E5%BA%AB-%E7%BE%8E%E8%82%A1%E7%AF%87-e3e896659fd6


# In[2]:


#Yahoo Finance python API
# pip install yfinance 
#FRED python API
# pip install fredapi 
#Google Trends python API
# pip install pytrends 
# pip install requests


# In[4]:


import requests
import pandas as pd
# 貼上連結
url = 'https://www.slickcharts.com/sp500'
headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
request = requests.get(url, headers = headers)

data = pd.read_html(request.text)[0]
# 欄位『Symbol』就是股票代碼
stk_list = data.Symbol
# # 用 replace 將符號進行替換
stk_list = data.Symbol.apply(lambda x: x.replace('.', '-'))
print(stk_list)


# In[4]:


import yfinance as yf
import time

# # 取得個股公司資料的語法，先測試一檔看看
stk_basic_data = yf.Ticker('AAPL').info
stk_basic_data

# 將 yfinance 有提供的數據項目取出存在 info_columns，它將會成為 stk_info_df 這張總表的欄位項目
info_columns = list(stk_basic_data.keys())

# 創立一個名為 stk_info_df 的總表，用來存放所有股票的基本資料！其中 stk_list 是我們先前抓到的股票代碼喔！
stk_info_df = pd.DataFrame(index = stk_list.sort_values(), columns = info_columns)

# 創立一個紀錄失敗股票的 list
failed_list = []

# 開始迴圈抓資料囉！
for i in stk_info_df.index:
    try:
        # 打印出目前進度
        print('processing: ' + i)
        # 抓下來的資料暫存成 dictionary
        info_dict = yf.Ticker(i).info
        # 由於 yahoo finance 各檔股票所提供的欄位項目都不一致！所以這邊要針對每一檔股票分別取出欄位項目
        columns_included = list(info_dict.keys())
        # 因為在別檔公司裡有著 AAPL 裡所沒有的會計科目，因此要取兩家公司會計科目的交集
#         intersect_columns = [x for x in info_columns if x in columns_included]
        # 有了該股欄位項目後，就可順利填入總表中相對應的位置
        stk_info_df.loc[i,columns_included] = list(pd.Series(info_dict)[columns_included].values,dtype=object)
        # 停一秒，再抓下一檔，避免對伺服器造成負擔而被鎖住
        time.sleep(1)
    except:
        failed_list.append(i)
        continue

# 查看一下資料內容，然後儲存下來吧！
stk_info_df.to_csv(r'C:\Users\admin\Python\股市\US-stocks.csv')


# In[5]:


import yfinance as yf
import time

# 取得個股公司資料的語法，先測試一檔看看
stk_basic_data = yf.Ticker('AAPL').info
stk_basic_data

# 將 yfinance 有提供的數據項目取出存在 info_columns，它將會成為 stk_info_df 這張總表的欄位項目
info_columns = list(stk_basic_data.keys())

# 創立一個名為 stk_info_df 的總表，用來存放所有股票的基本資料！其中 stk_list 是我們先前抓到的股票代碼喔！
stk_info_df = pd.DataFrame(index = stk_list.sort_values(), columns = info_columns)

# 創立一個紀錄失敗股票的 list
failed_list = []

# 開始迴圈抓資料囉！
for i in stk_info_df.index:
    try:
        # 打印出目前進度
        print('processing: ' + i)
        # 抓下來的資料暫存成 dictionary
        info_dict = yf.Ticker(i).info
        # 由於 yahoo finance 各檔股票所提供的欄位項目都不一致！所以這邊要針對每一檔股票分別取出欄位項目
        columns_included = list(info_dict.keys())
        # 因為在別檔公司裡有著 AAPL 裡所沒有的會計科目，因此要取兩家公司會計科目的交集
        intersect_columns = [x for x in info_columns if x in columns_included]
        # 有了該股欄位項目後，就可順利填入總表中相對應的位置
        stk_info_df.loc[i,intersect_columns] = list(pd.Series(info_dict)[intersect_columns].values)
        # 停一秒，再抓下一檔，避免對伺服器造成負擔而被鎖住
        time.sleep(1)
    except:
        failed_list.append(i)
        continue

# 查看一下資料內容，然後儲存下來吧！
stk_info_df.to_csv(r'C:\Users\admin\Python\股市\TEST.csv')


# In[6]:


import yfinance as yf
import time

# 先測試一檔試看看
stock = yf.Ticker('AAPL')

# 取得損益表，執行看看結果
stock.financials
import yfinance as yf
import time

# 先測試一檔試看看
stock = yf.Ticker('AAPL')

# 取得損益表，執行看看結果
stock.financials

# 取得資產負債表，執行看看結果
stock.balance_sheet

# 取得現金流量表，執行看看結果
stock.cashflow

# 開始迴圈抓資料囉！
for i in stk_list:
    try:
        # 打印出目前進度
        print('processing: ' + i)
        # 填入股票代碼後直接下載成 csv 格式
        stock = yf.Ticker(i)
        stock.financials.to_csv(r'C:\Users\admin\Python\股市\美股-價量資料\profit_loss_account_'+i+'.csv')
        stock.balance_sheet.to_csv(r'C:\Users\admin\Python\股市\美股-價量資料\balance_sheet_'+i+'.csv')
        stock.cashflow.to_csv(r'C:\Users\admin\Python\股市\美股-價量資料\cash_flow_'+i+'.csv')
        # 停一秒，再抓下一檔，避免對伺服器造成負擔而被鎖住
        time.sleep(1)
    except :
        failed_list.append(i)
        continue


# In[7]:


import yfinance as yf
import time

# 先測試一檔試看看
stock = yf.Ticker('AAPL')

# 取得價量資料＋股利發放資料＋股票分割資料
stock.history(period = 'max')

# 創立一個紀錄失敗股票的 list
failed_list = []

# 開始迴圈抓資料囉！
for i in stk_list:
    try : 
        # 打印出目前進度
        print('processing: ' + i)
        # 填入股票代碼後直接下載成 csv 格式
        stock = yf.Ticker(i)
        stock.history(period = 'max').to_csv(r'C:\Users\admin\Python\股市\美股-基本面資料\price_'+i+'.csv')
        # 停一秒，再抓下一檔，避免對伺服器造成負擔而被鎖住
        time.sleep(1)
    except :
        failed_list.append(i)
        continue


# In[ ]:


#ae729f2f20b20391dae9b44bfe620434


# In[2]:


from fredapi import Fred
import requests
import numpy as np
import pandas as pd
import datetime as dt

# 填入專屬 API，讓 fredapi 核准會員通過
api_key = 'ae729f2f20b20391dae9b44bfe620434'
fred = Fred(api_key)

# 先取得 FRED 大分類的完整資訊
r = requests.get('https://api.stlouisfed.org/fred/releases?api_key='+api_key+'&file_type=json', verify = True)
full_releases = r.json()['releases']

# 轉成 DataFrame，來看看這份完整資料長怎樣
full_releases = pd.DataFrame.from_dict(full_releases)
print(full_releases)
# # 將『大分類 ID』放在 index，方便後面的搜尋作業
# full_releases = full_releases.set_index('id')

# # 提供一個從大分類表中進行關鍵字搜尋的程式碼，方便大家查詢需要的大分類，我們以『gdp』作為示範
# search_keywords = 'gdp'
# search_result = full_releases.name[full_releases.name.apply(lambda x: search_keywords in x.lower())]

# # 創造一個以季為更新單位總表
# econ_data = pd.DataFrame(index = pd.date_range(start = '2020-01-01', end = dt.datetime.today(), freq = 'QS'))

# # 開始迴圈爬資料：
# #  第一層迴圈（大分類）：
# #   每個大分類底下，篩選出『最熱門的前三子項目』，以及相對應的『子項目英文代碼』
# #   (當然也可以整個 FRED 所有項目內容都爬取下來，這邊僅做示範)
# # 第二層迴圈（子項目）：
# #  陸續將每一個項目放入該總表裡面，完成你的經濟數據庫！
# for release_id in search_result.index:
#     release_topic = search_result[release_id]
#     series_df = fred.search_by_release(release_id, limit = 3, order_by = 'popularity', sort_order = 'desc')
#     for topic_label in series_df.index:
#         econ_data[series_df.loc[topic_label].title] = fred.get_series(topic_label, observation_start = '2020-01-01', observation_end = dt.datetime.today())


# In[ ]:


from pytrends.request import TrendReq
import pandas as pd
import numpy as np
import datetime as dt

# 填入美國時區資訊
pytrends = TrendReq(hl = 'en-US', tz = 360)

# 如果想要知道現在美國地區的人都在搜尋什麼，可以這樣查詢
pytrends.trending_searches(pn = 'united_states')

# kw_list 就是 keyworld list 的意思，我們這邊有興趣的是股票代碼被搜尋的熱度變化，以 AAPL 為例
kw_list = ['AAPL']

# 然後就可以透過 build_payload 建立查詢作業，再用 interest_over_time() 呈現數據
# 其中的　timeframe 參數很重要！它會改變你的數據格式
#  填入 'all' 就是全期資料，資料會以月頻率更新；
#  填入 'today 5-y' 就是至今的五年，只能設定 5 年，資料會以週頻率更新；
#  填入 'today 3-m' 就是至今的三個月，只能設定 1,2,3 月，資料會以日頻率更新；
#  填入 'now 7-d' 就是至今的七天，只能設定 1,7 天，資料會以小時頻率更新；
#  填入 'now 1-H' 就是至今的一小時，只能設定 1,4 小時，資料會以每分鐘頻率更新；
#  填入 '2015-01-01 2019-01-01' 就是 2015 年初至 2019 年初
pytrends.build_payload(kw_list, timeframe = 'today 3-m')
pytrends.interest_over_time()

# 如果需要長期間的高頻的資料，可以這樣查詢
# 但建議做大樣本查詢的時候，sleep 參數最好設定一下！否則流量的問題有可能查詢作業會被中斷喔！
pytrends.get_historical_interest(kw_list, 
                                 year_start = 2018, month_start = 1, day_start = 1, hour_start = 0,
                                 year_end = 2019, month_end = 2, day_end = 1, hour_end = 0, sleep = 0)
pytrends.interest_over_time()

# 建立一個 DataFrame 存放所有股票代碼的搜尋熱度數據，這裡以日頻率資料作為示範
# 剛剛的高頻查詢方式可以滿足這裡日頻率的要求，但如果要查滿多年的高頻資料，可能要等上很久
# 偏偏 timeframe 的設定有諸多限制，我希望資料是日頻率的話，只能選擇 'today 3-m' 的查詢方式
# 但我想要建一份長期資料例如 10 年資料表，該怎麼辦呢？
# 有一個取巧方式就是用日期對日期的方式查詢，日期之間的差距不要超過 270 天，回傳的資料就會是日頻率
# 所以用迴圈，每 270 天推進，抓到的資料就會是日頻率
trend_data = pd.DataFrame(index = pd.date_range(start = '2008-01-01', end = dt.datetime.today(), freq = 'D'))

# 還記得 stk_list 嗎？沒錯就是我們上面從 slickchart 抓下來的 S&P 500 成份股喔，我們稍微做一個排序
stk_list = stk_list.sort_values()

# 開始迴圈爬搜尋熱度資料吧！
for rnd in range(int(np.ceil(len(trend_data) / 270))):
    # 打印出目前的回合
    print('processing round :' + str(rnd))
    # 設定目前這回合 270 天的日期資訊
    date_list = list(trend_data.index[270*rnd:270*(rnd+1)])
    start_date = date_list[0].strftime('%Y-%m-%d')
    end_date = date_list[-1].strftime('%Y-%m-%d')
    
    # 第二層迴圈，在這個日期區間，查詢每一檔股票的日頻搜尋熱度資料，並填入表格
    for stk in stk_list:
        kw_list = [stk]
        pytrends.build_payload(kw_list, timeframe = start_date + ' ' + end_date)
        try : 
            trend_data.loc[date_list, stk] = pytrends.interest_over_time()[stk]
        except : 
            trend_data.loc[date_list, stk] = np.nan
    time.sleep(5)
trend_data


# In[ ]:

