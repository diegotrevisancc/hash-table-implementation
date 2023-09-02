import pandas as pd
df = pd.read_csv('agenda.csv')
column_index = 0 

column = df.iloc[:, column_index]

heroes = column.tolist()

