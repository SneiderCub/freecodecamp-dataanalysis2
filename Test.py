import pandas as pd
df = pd.read_csv('adult.data.csv')

print(df['race'].value_counts())
