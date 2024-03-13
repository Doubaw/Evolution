#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import time
import sys

date = time.strftime("%Y-%m-%d", time.localtime())
for i in range(20):
    url = 'https://tw.stock.yahoo.com/q/h?s=2330&pg=' 
    j = i+1
    url_news = url+str(j) 
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
    res = requests.get(url_news, header)
    res.encoding = 'utf-8'
    bs = BeautifulSoup(res.content, 'lxml')
    news = bs.find('table', {'class':'yui-text-left'})
    url_text = news.find_all('a')
    with open(r"C:\Users\admin\Python\NewsData\ "+date+'-news.txt','a',encoding='utf-8') as file:
            for new in url_text:
                file.write(new.text)
                print(new.text)
                file.write('\n')


# In[ ]:




