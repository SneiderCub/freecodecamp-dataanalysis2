import pandas as pd
df = pd.read_csv('adult.data.csv')
print(df[df.salary == ">50K"]['occupation'].value_counts().idxmax())




