#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os


# In[5]:


mba=pd.read_csv("C:/Users/USER/Desktop/mba.csv") #importing the dataset


# In[6]:


mba.head() # shows the first five elements from the dataset


# In[7]:


mba.tail() #shows the last five elements from the dataset


# In[8]:


mba.shape #shows the number of rows and columns in the datset


# In[10]:


len(mba) #shows the numbers of elements of length of dataset


# In[11]:


mba.max() #shows all the maximum values from all the elements from each rows columns


# In[12]:


mba.min() #shows all the minimum values from the existing values as below


# In[13]:


del mba['Datasrno'] #Del the unnessary columns "Datasrno"


# In[14]:


mba


# In[15]:


mba['workex'].min() #Finding the minimun and maximum values from the dataset with by each columns


# In[16]:


mba['workex'].max()


# In[17]:


mba['gmat'].max()


# In[18]:


mba['gmat'].min()


# In[19]:


mba.isnull().sum() #Finding the missing values: As from below there are no missing values the mba dataset


# In[20]:


mba.gmat.describe() #describe is a shortcut key used to find the mathematical insites of the data.


# In[21]:


mba.workex.describe()


# In[22]:


mba.describe()


# In[24]:


mba.plot()


# In[32]:


mba.boxplot('gmat') #Finding the outliers using the visualization i.e boxplot


# In[33]:


mba.boxplot('workex')


# In[39]:


plt.hist(mba['gmat'])


# In[40]:


plt.hist(mba['workex'])


# In[45]:


sns.boxplot(mba['gmat']) #boxplot using seaborn 


# In[46]:


from scipy.stats import skew #libraries used for finding the skewness and kutoissi
skew(mba["workex"])


# In[47]:


from scipy.stats import kurtosis
kurtosis(mba["gmat"])

