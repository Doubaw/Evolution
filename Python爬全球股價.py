#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python新手教學(Part 1)：用爬蟲爬全球股價!
#https://www.finlab.tw/%E7%94%A8%E7%88%AC%E8%9F%B2%E7%88%AC%E5%85%A8%E4%B8%96%E7%95%8C%E8%82%A1%E5%83%B9/

import json
import numpy as np
import pandas as pd
import requests

site = "https://query1.finance.yahoo.com/v8/finance/chart/2330.TW?period1=0&period2=1549258857&interval=1d&events=history&=hP2rOschxO0"
response = requests.get(site)
print(response.text)

data = json.loads(response.text)
df = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0], index=pd.to_datetime(np.array(data['chart']['result'][0]['timestamp'])*1000*1000*1000))
df.head()
df.close.plot()


# In[ ]:




