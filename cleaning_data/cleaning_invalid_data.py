import pandas as pd
import numpy as np
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

df = pd.DataFrame({
    'Sex': ['M', 'F', 'F', 'D', '?'],
    'Age': [29, 30, 24, 290, 25],
})
# print(df['Sex'].unique)
# print(df['Sex'].value_counts())#This tells how many different type of values are their in the dataframe
# print(df['Sex'].replace('D', 'F'))#This replaces the D with an F in Sex column
# print(df['Sex'].replace({'D':'F','?':'M'}))#the replace() function can take dictionary as parameter to replace multiple values
# print(df.replace({
    # 'Sex':{
        # 'D':'F',
        # 'N':'M'
    # },
    # 'Age' : {
        # 290:9
    # }
# }))
# print(df[df['Age']>100])#This find the ages that are more than 100 in age column
df.loc[df['Age']>100,'Age'] = df.loc[df['Age']>100,'Age']/10 #we devide the age more tan 100 by 10
# print(df)
ambassadors = pd.Series([
    'France',
    'United Kingdom',
    'United Kingdom',
    'Italy',
    'Germany',
    'Germany',
    'Germany',
], index=[
    'Gérard Araud',
    'Kim Darroch',
    'Peter Westmacott',
    'Armando Varricchio',
    'Peter Wittig',
    'Peter Ammon',
    'Klaus Scharioth '
], name="List of Ambassadors", dtype='string')
# print(ambassadors)
# print(ambassadors.duplicated())#this will return a boolean series highlighting duplicate values the first instance in not considered duplicate
# print(ambassadors.duplicated(keep='last'))#by using keep='last' we will specify the first instance of a value as duplicate
# print(ambassadors.duplicated(keep=False))#This will mark all double values as duplicate
# print(ambassadors.drop_duplicates())#remove all duplicate which comes after the orignal

