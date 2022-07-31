#!/usr/bin/env python
# coding: utf-8

# # Auto-scraper
# 
# We will build an automatic scraper that emails me every morning.
# 
# Website: https://www.nytimes.com/news-event/roe-v-wade-supreme-court-abortion?name=styln-abortion-us&region=TOP_BANNER&block=storyline_menu_recirc&action=click&pgtype=LegacyCollection&variant=show
# 
# ### Inspiration credits: 
# - https://github.com/jsoma/autoscraper-history
# - https://github.com/jsoma/autoscraper-changes 
# - https://github.com/jsoma/autoscraper-mailer
# - https://github.com/jsoma/auto-covid-map
# 

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


response = requests.get("https://www.nytimes.com/news-event/roe-v-wade-supreme-court-abortion?name=styln-abortion-us&region=TOP_BANNER&block=storyline_menu_recirc&action=click&pgtype=LegacyCollection&variant=show")
doc = BeautifulSoup(response.text)
doc


# # 1. Collect highlight articles on the top of the page

# In[4]:


tops =[]

articles = doc.select("#collection-highlights-container")

for article in articles:
    for article in article.select(".css-1lktipf"):
        title = article.text
        url = "https://www.nytimes.com" + article.find("a")["href"]
        
        article_dict = {
            "title": title,
            "url" : url,
        }
        
        tops.append(article_dict)

df1 = pd.DataFrame(tops)
df1


# # 2. Collect articles from Opinion column

# In[5]:


opinions = []

articles = doc.select(".css-k6p1hl")

for article in articles:
    for article in article.select(".css-10p9jve"):
        title = article.text
        url = "https://www.nytimes.com" + article.find("a")["href"]
        
        article_dict = {
            "title": title,
            "url" : url,
        }
        
        opinions.append(article_dict)

df2 = pd.DataFrame(opinions)
df2


# # 3. Collect the rest of articles on page

# In[6]:


rest = []

articles = doc.select(".css-1l4spti")

for article in articles:
    url = "https://www.nytimes.com" + article.find("a")["href"]
    for article in article.select("h2"):
        title = article.text
        
        article_dict = {
            "title": title,
            "url":url,
        }
        
        rest.append(article_dict)
        
df3 = pd.DataFrame(rest)
df3


# # 4. Merge your dataframes

# In[8]:


frames = [df1, df2, df3]
df_merged = pd.concat(frames)
df_merged


# # 5. Save it as a csv file

# In[10]:


df_merged.to_csv("abortion_nyt.csv",index=False)


# In[ ]:





# In[ ]:





# # Try selenium to scrape the data!
# 
# - okay selenium doesn't work either!!
# - so wait til Jessie gets back to you about how nyt block you with 10 articles limits
# 

# In[22]:


import pandas as pd

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from webdriver_manager.chrome import ChromeDriverManager


# In[23]:


driver = webdriver.Chrome(ChromeDriverManager().install())


# In[24]:


driver.get("https://www.nytimes.com/news-event/roe-v-wade-supreme-court-abortion?name=styln-abortion-us&region=TOP_BANNER&block=storyline_menu_recirc&action=click&pgtype=LegacyCollection&variant=show")


# In[25]:


doc = BeautifulSoup(driver.page_source)
doc


# In[26]:


rest = []

articles = doc.select(".css-1l4spti")

for article in articles:
    url = "https://www.nytimes.com" + article.find("a")["href"]
    for article in article.select("h2"):
        title = article.text
        
        article_dict = {
            "title": title,
            "url":url,
        }
        
        rest.append(article_dict)
        
df3 = pd.DataFrame(rest)
df3


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




