import pandas as pd
import os
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from pandas import Series, DataFrame
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from pylab import plot, show
import numpy as np
import pygal
import lxml
import tinycss
########这个程序用于把一张全车间过车序列表整理出各个点的过车信息，，效率有点低#########################
ax =input('文件名？？')
df = pd.read_excel('E:\DATA_ENGIN'+'\\'+'bodydata'+'\\'+ax+'.xlsx')
df_st= df.groupby(['RW-Station-ID'])['Loaded'].agg(['count']).sort_values('count',ascending=False)
df_st =df_st.sort_values('RW-Station-ID',ascending=False)
df_ar = df.groupby(['Area'])['Loaded'].agg(['count'])
df_VIN= df.groupby(['Body ID'])['Loaded'].agg(['count']).sort_values('count',ascending=False)
print(df_VIN)
# df_PLCT=df_PLCT.sort_values('sum',ascending=False)
# df_PLCT =df_PLCT.head(30)
a = 0
col_name = df.columns.tolist() 
A= list(df_st.index)
B= list(df_VIN.index)
df1 =pd.DataFrame(columns=A,index=B)
df1['Body ID']=df1.index
df1.index =df1['Body ID']
df.date = df.index
df.index = df['Body ID']
df1= df1.drop(columns=['Body ID'])
df1[:] = 0
df= df.drop(columns=['Body ID'])
df2 = pd.merge(df1, df,how='inner',on='Body ID')
#############建立读写站和车子第一张关联表df2
for i in df2['RW-Station-ID']:
    for j in df2.columns:
        if j == i:
            df2.loc[df2['RW-Station-ID'] ==i,j] = df2.loc[df2['RW-Station-ID'] ==i,'Timestamp'] 
            ####### 对第二张无重复车号的关联表df1的元素在DF2里查找
for i in range(len(df2.index)):
    for j in range(len(df2.columns)):
        a= df2.iloc[i].name
        b=df2.iloc[:,j].name
        if df2.iloc[i,j] != 0:
            df1.loc[a,b] = df2.iloc[i,j]
print('打印')
df1.to_excel('E:\DATA_ENGIN'+'\\'+'bodydata'+'\\'+'Shop.xlsx')
df_st.to_excel('E:\DATA_ENGIN'+'\\'+'bodydata'+'\\'+'RW.xlsx')
df_VIN.to_excel('E:\DATA_ENGIN'+'\\'+'bodydata'+'\\'+'VIN.xlsx')
