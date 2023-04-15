# Задача 40:  Работать с файлом california_housing_train.csv,
# который находится в папке sample_data. Определить среднюю стоимость
# дома, где кол-во людей от 0 до 500 (population)

# Задача 42: Узнать какая максимальная households в зоне минимального значения population

import pandas as pd
df=pd.read_csv('california_housing_train.csv')

df.info()

df.describe()

df[(df['population']>=0)&(df['population']<=500)]

df[(df['population']>=0)&(df['population']<=500)]['median_house_value'].median()

df[df['population']==df['population'].min()]['households'].max()