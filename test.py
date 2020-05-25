import pandas as pd
import plotly.express as px


df=pd.read_csv('/Users/pcworld/Desktop/dashproject/2014.csv')

df_division=df[['v016','v024','v013']]

df_five=df_division.groupby('v013').count()
print(df_five)

fig=px.pie(df_five,values='v013',names='')



fig.show()