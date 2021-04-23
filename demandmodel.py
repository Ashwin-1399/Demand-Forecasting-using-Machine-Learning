#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import io
import datetime


# In[2]:


# df=pd.read_csv('dataset/combine.csv',parse_dates=True)
# df.head()
df = pd.read_csv('dataset/combine.csv')
df.head()


# In[3]:


# seaborn check for missing value
sns.heatmap(df.isnull())


# In[4]:


#remove the missing value
df.drop(['Discount','P.O. Date', 'Packing & Forwarding','Freight','Rounded Off'], axis = 1, inplace=True) 
df.head()


# In[5]:


#convert data to dataframe
data = pd.DataFrame(df) 
data.head()


# In[6]:


# data.to_csv('demandnew.csv') 


# In[7]:


#drop the coulmns 
data.drop(['Sub Total'], axis=1,inplace=True)
data.head()


# In[8]:


#rename the filed value
data.rename(columns = {'Date':'Month', 'Total':'Sales'}, inplace = True) 


# In[9]:


data.head()


# In[ ]:





# In[10]:


#show the sales
data1=data[['Month', 'Sales']] 
data1


# In[11]:


data1.drop(563,axis=0,inplace=True)


# In[12]:


data1.tail()


# In[13]:


#check the information
data1.info()


# In[14]:


type(data1['Month'])


# In[15]:


# Convert Month into Datetime
data1['Month']=pd.to_datetime(data1['Month'], errors='coerce')


# In[16]:


data1.head()


# In[17]:


#reset index column name of month
data1.set_index('Month',inplace=True)


# In[18]:


data1.head()


# In[19]:


data1.describe()


# In[20]:


type(data1)


# In[21]:


df = data1.apply(pd.to_numeric, errors='coerce')


# In[22]:


#visualize year wise data
df.plot()


# In[23]:


from statsmodels.tsa.stattools import adfuller
import statsmodels.api as sm 


# In[24]:


df.info()


# In[25]:


df[np.isnan(df)] = 0


# In[26]:


test_result=adfuller(df['Sales'])


# In[27]:


#define the threshold of sales
def adfuller_test(sales):
    result=adfuller(sales)
    labels = ['ADF Test Statistic','p-value','#Lags Used','Number of Observations Used']
    for value,label in zip(result,labels):
        print(label+' : '+str(value) )
    if result[1] <= 0.05:
        print("strong evidence against the null hypothesis(Ho), reject the null hypothesis. Data has no unit root and is stationary")
    else:
        print("weak evidence against null hypothesis, time series has a unit root, indicating it is non-stationary ")
    


# In[28]:


#find the lag of sales difference
adfuller_test(df['Sales'])


# In[29]:


#difference bewteen sales
df['Sales First Difference'] = df['Sales'] - df['Sales'].shift(1)


# In[30]:


df['Sales'].shift(1)


# In[31]:


df['Seasonal First Difference']=df['Sales']-df['Sales'].shift(12)


# In[32]:


df.head(14)


# In[33]:


adfuller_test(df['Seasonal First Difference'].dropna())


# In[34]:


#monthly sales difference
df['Seasonal First Difference'].plot()


# In[35]:


#monthly sales difference
from pandas.plotting import autocorrelation_plot
autocorrelation_plot(df['Sales'])
plt.show()


# In[36]:


from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
import statsmodels.api as sm


# In[37]:


fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(df['Seasonal First Difference'].iloc[13:],lags=40,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(df['Seasonal First Difference'].iloc[13:],lags=40,ax=ax2)


# In[38]:


#apply the arima model
from statsmodels.tsa.arima_model import ARIMA


# In[39]:


#train the model
model=ARIMA(df['Sales'],order=(1,1,1))
model=model.fit()


# In[40]:


model.summary()


# In[41]:


df.values.dtype


# In[42]:


#sales difference
df


# In[43]:


type(model)


# In[44]:


#month sales 
df = df.sort_values('Month')

df.isnull().sum()


# In[45]:


#group by month and sales
df = df.groupby('Month')['Sales'].sum().reset_index()


# In[46]:


df = df.set_index('Month')
df.index


# In[47]:


df = df['Sales'].resample('MS').mean()


# In[ ]:





# In[48]:


#2017 sales
df['2017':]


# In[49]:


#month sales 
df.plot(figsize=(15, 6))
plt.show()


# In[50]:


from pylab import rcParams
rcParams['figure.figsize'] = 18, 8

decomposition = sm.tsa.seasonal_decompose(df, model='additive')
fig = decomposition.plot()
plt.show()


# In[51]:


import itertools


# In[52]:


p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))


# In[53]:


for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(y,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            results = mod.fit()
            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue


# In[54]:


#model fit
mod = sm.tsa.statespace.SARIMAX(df,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 0, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)

results = mod.fit()

print(results.summary().tables[1])


# In[55]:


import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm
import matplotlib

matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'


# In[56]:


results.plot_diagnostics(figsize=(12, 8))
plt.show()


# In[57]:


#future sales observed
pred = results.get_prediction(start=pd.to_datetime('2020-01-01'), dynamic=False)
pred_ci = pred.conf_int()

ax = df['2017':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))

ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)

ax.set_xlabel('Month')
ax.set_ylabel('Sales')
plt.legend()

plt.show()


# In[58]:


#future sale observed
pred_uc = results.get_forecast(steps=100)
pred_ci = pred_uc.conf_int()

ax = df.plot(label='observed', figsize=(14, 7))
pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.25)
ax.set_xlabel('Date')
ax.set_ylabel('Furniture Sales')

plt.legend()
plt.show()


# In[ ]:




