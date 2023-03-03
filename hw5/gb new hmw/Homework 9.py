import pandas as pd
df = pd.read_csv('california_housing_train.csv')
# Задача 40
print(df[(df['population'] <= 500)]['median_house_value'].mean())
# Задача 42
print(df[df['population']==df['population'].min()]['households'].max())

