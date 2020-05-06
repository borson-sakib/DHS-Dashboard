
import pandas as pd



df=pd.read_csv('/Users/pcworld/Desktop/dashproject/2014.csv')


#print(df.head(10))

#print(df.info())

df1=df.dropna(how='all',axis=1)


#print(df1.info())

#print(df1.head(10))

df3=df1.head(50)



#df2=df1[['v139','v152']]

#print(df2.head())

#print(df2.groupby('v139')[['v152']].max())




df3.to_csv('/Users/pcworld/Desktop/dashproject/data_sample.csv')