import numpy as np
import pandas as pd
falsy_values = (0, False, None, '', [], ())# All the values are considered falsy in python
# print(3+np.nan)# where ever np.nan comes that whole value become nan
# a = np.array([1, 2, 3, np.nan, np.nan, 4])
a  = np.array([1, 2, 3, np.nan, None], dtype='float')
# print(a.mean())#due to presence of np.nan the operation returns nan as answer
# print(a.sum())#this also returns nan
b = np.array([1, 2, 3, np.inf], dtype='float')#we also have np.inf which also works similar to no.nan
# print(b.sum())
# print(b.mean())
# print(np.isfinite(a))#returns boolean array as output indicating which values are nan of infinite
# print(np.isfinite(b))
# print(a[~np.isnan(a)])#returns all values that are not nan
# print(a[np.isfinite(a)].sum())
# print(a[pd.notnull(a)])#notnull() and isfinite() function in the same way
#while isnull() work similar to isnan()
# print(pd.Series([1, 2, np.nan]).count())#panda simply ignores any nan value
s = pd.Series([1, 2, 3, np.nan, np.nan, 4], dtype="float")
# print(s[s.notnull()])
# print(s.dropna())
df = pd.DataFrame({
    'Column A': [1, np.nan, 30, np.nan],
    'Column B': [2, 8, 31, np.nan],
    'Column C': [np.nan, 9, 32, 100],
    'Column D': [5, 8, 34, 110],
})
# print(df.isnull())
# print(df.isnull().sum())
# print(df.dropna())#this will drop all the row with having even on nan value
# print(df.dropna(axis=1))#this will drop column having even one nan value
# print(df.dropna(how='any', axis = 1))#how ='any' mean that even one nan row or columns will be removed
# print(df.dropna(thresh=3, axis='columns'))#columns having atleast 3 non-null values will not be removed
# print(s.fillna(0))#fillna() fill the choosen(0) value by nan in array
# print(df.fillna(df.mean()))#this fill nan values with mean of the dataframe
# print(s.fillna(s.bfill()))#this takes the last extreme values and start adding it to the nan values but this method leaves extreme nan values
print(df.fillna({'Column A': 0, 'Column B': 99, 'Column C':df['Column C'].mean()}))#in dataframe we can specify which values in place of nan in different rows
