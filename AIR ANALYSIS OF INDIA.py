#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as st

df=pd.read_csv("air-quality-india.csv")
data=pd.DataFrame(df)
print(data)


# In[3]:


data.describe()


# In[11]:


df.info()


# In[4]:


data.head(10)


# In[22]:


df['Date']=df['Timestamp'].apply(lambda x:x[0:11])
dataA=df.loc[:,['Date','PM2.5']]
print(dataA)


# In[23]:


df['Date']=df['Timestamp'].apply(lambda x:x[0:11])
dataA=df.loc[:,['Date','PM2.5']]
dataA=dataA.groupby('Date',as_index=False).max()
print(dataA)


# In[26]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as st

df=pd.read_csv("air-quality-india.csv")
data=pd.DataFrame(df)
plt.subplots(figsize=(10,10))
plt.bar(data["Year"],data["PM2.5"],fc="grey")
plt.xlabel("YEAR",size=40)
plt.ylabel("PM2.5",size=40)
plt.title("AIR ANALYSIS OF INDIA",size=45)
plt.grid()
plt.show()


# In[8]:


dataB=data.loc[:,['Month','PM2.5']]
dataB=dataB.groupby('Month',as_index=False).mean()
display(dataB)


# In[27]:


plt.subplots(figsize=(10,10))
plt.barh(data["Month"],data["PM2.5"],fc="orange")
plt.xlabel("PM2.5",size=40)
plt.ylabel("Month",size=40)
plt.title("AIR ANALYSIS OF INDIA",size=45)
plt.grid()
plt.show()


# In[25]:


dataC=data.loc[:,['Timestamp','PM2.5']]
dataC['Time']=dataC['Timestamp'].apply(lambda x:x[11:13])
dataC=dataC.groupby('Time',as_index=False).mean()
display(dataC)


# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as st
df=pd.read_csv("air-quality-india.csv")
data=pd.DataFrame(df)
dataC=data.loc[:,['Timestamp','PM2.5']]
dataC['Time']=dataC['Timestamp'].apply(lambda x:x[11:13])
dataC=dataC.groupby('Time',as_index=False).mean()
plt.subplots(figsize=(15,7))
plt.plot(dataC["Time"],dataC["PM2.5"],marker='d',linewidth=7,linestyle='--',markerfacecolor='k',markeredgecolor='g',
markeredgewidth=6, markersize=6)
plt.xlabel("Timestamp",size=40)
plt.ylabel("PM2.5",size=40)
plt.title("AIR ANALYSIS OF INDIA",size=45)
plt.axis([0, 23, 0, 70])
plt.grid()
plt.show()


# In[ ]:




