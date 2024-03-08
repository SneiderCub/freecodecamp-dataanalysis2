import pandas as pd
df = pd.read_csv('adult.data.csv')
num_min_workers = df[df['hours-per-week']==df['hours-per-week'].min()]
rich_percentage = num_min_workers[num_min_workers['salary']=='>50K']

