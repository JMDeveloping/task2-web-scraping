#!/usr/bin/env python
# coding: utf-8

# In[11]:


import os
import requests
import re
import sys
from bs4 import BeautifulSoup


# In[ ]:





# In[12]:


# Global URL to scrape


# In[13]:


url = 'https://medium.com/@subashdangol7/papa-what-is-a-neural-network-c8c5e0cc27cf'


# In[ ]:





# In[14]:


# Function to get the html source text of the medium article


# In[15]:


def get_page():
    if not re.match(r'^https://medium.com/', url):
        print("Please enter a valid Medium URL.")
        sys.exit(1)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup


# In[ ]:





# In[16]:


# Function to remove all the html tags and replace some with specific strings


# In[17]:


def clean(text):
    rep = {"<br>": "\n", "<br/>": "\n", "<li>":  "\n"}
    rep = dict((re.escape(k), v) for k, v in rep.items()) 
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
    text = re.sub(r'<.*?>', '', text)
    return text


# In[ ]:





# In[18]:


# Function to collect text from <p> tags


# In[19]:


def collect_text(soup):
    text = f'url: {url}\n\n'
    para_text = soup.find_all('p')
    print(f"paragraphs text = \n {para_text}")
    for para in para_text:
        text += f"{para.text}\n\n"
    return text


# In[ ]:





# In[20]:


# Function to save file in the current directory


# In[24]:


def save_file(text):
    if not os.path.exists('./scraped_articles'):
        os.mkdir('./scraped_articles')
    name = url.split("/")[-1]
    print(name)
    fname = f'scraped_articles/{name}.txt'
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'File saved in directory {fname}')


# In[ ]:





# In[22]:


# Run the full program


# In[23]:


if __name__ == '__main__':
    text = collect_text(get_page())
    save_file(text)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




