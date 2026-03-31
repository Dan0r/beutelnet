#!/usr/bin/env python
# coding: utf-8

# # Data cleaning pipeline

# In[ ]:


import pandas as pd


# In[ ]:


df = pd.read_csv("data.csv")


# ### Remove leading and trailing whitespace

# In[ ]:


df["vacuum"] = df["vacuum"].str.strip()


# ### Filter strings starting only with: "r "; special characters

# In[ ]:


df["vacuum"] = df["vacuum"].apply(
   lambda x: x[1:] if not x[0].isalnum() or x[0] == "r" else x
)
df["vacuum"] = df["vacuum"].str.replace("?", "")


# ### Remove text anomalies specific to EDEKA products

# In[ ]:


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

# In[ ]:


df = df[
    ~df["vacuum"].isin(text_anomalies)
    & (df["vacuum"].str.len() > 3)
    & (df["vacuum"].str.strip() != 0)
]


# In[ ]:


print(df.to_string())


# # Filter product names

# In[ ]:


product_names = df[df["vacuum"].str.isupper() & df["vacuum"].str.isalpha()]["vacuum"]
product_names = product_names[product_names != "ALLFLOOR"]
product_names = product_names.replace("ELEGTROLUX", "ELECTROLUX").replace("HANSEATIG", "HANSEATIC")
print(product_names)


# ### Forward fill to assign a brand to all data

# In[ ]:


df["brand"] = product_names
df["brand"] = df["brand"].ffill()
print(df.to_string())

