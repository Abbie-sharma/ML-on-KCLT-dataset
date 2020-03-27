import numpy 
import datetime
import pandas as pd

df2 = pd.read_csv("KCLT.csv",parse_dates=['date'])#To deal with dates

cols = [col for col in df2.columns if col in ['date','actual_mean_temp']] #for keeping only particluar columns
df3 = df2[cols]

df4=df3[(df3['date']>pd.Timestamp(2014,7,31)) & (df3['date']<pd.Timestamp(2014,9,1))] #for keeping relevant dates

#plt.hist(x, bins=None, range=None, density=None)# x should be an array
df4.hist(bins=15)
plt.xlabel('Mean Temperature')
plt.ylabel('Probability')
plt.title('Actual Mean Temperature for Aug,2014')
plt.grid(True)

#For March 2015
df4=df3[(df3['date']>pd.Timestamp(2015,2,28)) & (df3['date']<pd.Timestamp(2015,4,1))] #for keeping relevant dates
print(df4)
#plt.hist(x, bins=None, range=None, density=None)# x should be an array
df4.hist(bins=15)
plt.xlabel('Mean Temperature')
plt.ylabel('Probability')
plt.title('Actual Mean Temperature for March,2015')
plt.grid(True)
