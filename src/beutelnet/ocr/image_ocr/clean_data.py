#!/usr/bin/env python
# coding: utf-8

# # Data cleaning pipeline

# In[224]:


import pandas as pd


# In[225]:


df = pd.read_csv("data.csv")


# ### Remove leading and trailing whitespace

# In[232]:


df["vacuum"] = df["vacuum"].str.strip()


# ### Filter strings starting only with: "r "; special characters

# In[233]:


df["vacuum"] = df["vacuum"].apply(
   lambda x: x[1:] if not x[0].isalnum() or x[0] == "r" else x
)
df["vacuum"] = df["vacuum"].str.replace("?", "")


# ### Remove text anomalies specific to EDEKA products

# In[234]:


text_anomalies = [ 
    "WEITERE",
    "JMALLFLRLR",
    "GEEIGNET",
    "(0)",
    "_ M&",
    "FOLGENDE",
    "MAX 4L",
    "MAX4L",
    "S-BA",
    "STANDARD-BAG",
    "S-BA",
    "GREEN",
    "STANDARD",
    "POWER",
    "ANDEREN"
]


# ### Delete rows containing text anomalies
# ### Remove strings with less than three symbols
# ### Remove leading and trailng whitespace

# In[235]:


df = df[
    ~df["vacuum"].isin(text_anomalies)
    & (df["vacuum"].str.len() > 3)
    & (df["vacuum"].str.strip() != 0)
]


# In[236]:


print(df.to_string())


# # Filter product names

# In[ ]:
