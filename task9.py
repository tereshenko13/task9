

import pandas as pd
import csv

df = pd.read_csv('./data.csv', delimiter=',')
df['23'] = pd.to_datetime(df['23'], unit='s') 
df.sort_values(by='23', ascending=True)

error_counts_1 = df[df['2'] == 'Error'].groupby([
               pd.Grouper(key='23', freq='1Min')]).size()

error_counts_2 = df[df['2'] == 'Error'].groupby([
                 pd.Grouper('15'),
               pd.Grouper(key='23', freq='1H')]).size()

with open('./output1.txt', 'w') as file:
    for timestamp, count in error_counts_1.items():
        if count > 10:
            file.write(f'Замечено {count} ошибок меньше, чем за 1 час\n')

with open('./output2.txt', 'w') as file:
    for (value, timestamp), count in zip(error_counts_2.index, error_counts_2.values):
        if count > 10:
            file.write(f'Замечено {count} ошибок меньше, чем за 1 час по следующему bundle_id : {value}\n')