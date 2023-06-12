#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pnd


# In[2]:


# reading csv file
netflix = pnd.read_csv('C:/Users/Nowy_użytkownik/Desktop/netflix.csv')


# In[3]:


# overwiew of the data
netflix.head()
netflix.shape


# In[5]:


# loooking for duplicated values
netflix.duplicated().sum()


# In[6]:


# removing unnecessary column 
netflix = netflix.drop('show_id', axis = 1)


# In[8]:


# checking data types 
netflix.dtypes


# In[9]:


# converting 'date_added' column values to datetime type
netflix['date_added'] = pnd.to_datetime(netflix['date_added'])


# In[10]:


# conversion succeded
netflix.dtypes


# In[11]:


# copying data from 'duration' column to new column 'seasons_count'
netflix['seasons_count'] = netflix['duration']


# In[12]:


# replacing unnecessary data from 'duration' column with '0'
netflix['duration'] = netflix['duration'].str.replace('.+Season.*','0')


# In[13]:


# removing 'min' from 'duration' column
netflix['duration'] = netflix['duration'].str.replace('\smin','')


# In[42]:


netflix


# In[24]:


# replacing unnecessary data from 'seasons_count' column with '0'
netflix['seasons_count'] = netflix['seasons_count'].str.replace('\d+\smin','0')


# In[25]:


# removing 'Season(s)' from 'seasons_count' column
netflix['seasons_count'] = netflix['seasons_count'].str.replace('\sSeason.?','')


# In[ ]:


netflix


# In[27]:


# renaming column 
netflix = netflix.rename(columns = {'duration':'duration_min'})


# In[28]:


netflix.dtypes


# In[29]:


# changing datatype in 'duration_min' column to integer
netflix['duration_min'] = netflix['duration_min'].astype(int)


# In[30]:


# datatype successfully changed
netflix.dtypes


# In[32]:


# changing datatype in 'seasons_count' column to integer
netflix['seasons_count'] = netflix['seasons_count'].astype(int)


# In[33]:


# datatype successfully changed
netflix.dtypes


# In[36]:


# looking for null values
netflix.isna().sum()


# In[40]:


# changing order of columns
netflix = netflix.iloc[:,[1,0,2,3,4,5,6,7,9,8]]


# In[41]:


# dataset after cleaning
netflix


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




