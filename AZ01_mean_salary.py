import pandas as pd


df = pd.read_csv('dz.csv')

df.fillna(0, inplace=True)
df['City'] = df['City'].replace(0, 'Город не указан')

group = df.groupby('City')['Salary'].mean().round(2)
print(group)
