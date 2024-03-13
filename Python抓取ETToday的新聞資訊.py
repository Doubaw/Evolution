#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
url = "https://www.ettoday.net/news/news-list.htm"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
resp = requests.get(url, headers = headers)
soup = BeautifulSoup(resp.text,"lxml")
elem = soup.select(".part_list_2")

title_list = []
date_list = []
cate_list = []
# link_list = []
for e in elem:
    title_list = [title.text for title in e.select("a")]
#     print(title_list)
#     link_list = [i.get('href') for i in e.select("a")]
#     print(link_list)
    date_list = [date.text for date in e.select(".date")]
#     print(date_list)
    cate_list = [cate.text for cate in e.select("em")]
#     print(cate_list)

df = pd.DataFrame()
df["title"]=title_list
df["category"]=cate_list
df["date"]=date_list
# df["link"]=link_list
print(df)


# In[ ]:




