import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt

# temp_table = pd.DataFrame({
#     'Population': [35.467, 63.951, 80.94 , 60.665, 127.061, 64.511, 318.523],
#     'GDP': [
#         1785387,
#         2833687,
#         3874437,
#         2167744,
#         4602367,
#         2950039,
#         17348075
#     ],
#     'Surface Area': [
#         9984670,
#         640679,
#         357114,
#         301336,
#         377930,
#         242495,
#         9525067
#     ],
#     'HDI': [
#         0.913,
#         0.888,
#         0.916,
#         0.873,
#         0.891,
#         0.907,
#         0.915
#     ],
#     'Continent': [
#         'America',
#         'Europe',
#         'Europe',
#         'Europe',
#         'Asia',
#         'Europe',
#         'America'
#     ]
# }, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])
# temp_table.index = [
#     'Canada',
#     'France',
#     'Germany',
#     'Italy',
#     'Japan',
#     'United Kingdom',
#     'United States',
# ]
# print(temp_table)
# print(temp_table.info())
# print(temp_table.size)
# print(temp_table.describe())
# print(temp_table.value_counts())
# print(temp_table['Population'].to_frame())
# print(temp_table[0:10])
# print(temp_table.loc['France':'Italy'])
# print(temp_table.drop('Canada')) #This drops canada row for the table
# print(temp_table.drop(['Canada', 'Japan'])) #This removes the selected column
# print(temp_table.drop(['Population', 'HDI'], axis=1))   #This remove the selected row
# temp_table.drop(columns='Population', inplace=True)
# print(temp_table)
marvel_data = [
    ['Spider-Man', 'male', 1962],
    ['Captain America', 'male', 1941],
    ['Wolverine', 'male', 1974],
    ['Iron Man', 'male', 1963],
    ['Thor', 'male', 1963],
    ['Thing', 'male', 1961],
    ['Mister Fantastic', 'male', 1961],
    ['Hulk', 'male', 1962],
    ['Beast', 'male', 1963],
    ['Invisible Woman', 'female', 1961],
    ['Storm', 'female', 1975],
    ['Namor', 'male', 1939],
    ['Hawkeye', 'male', 1964],
    ['Daredevil', 'male', 1964],
    ['Doctor Strange', 'male', 1963],
    ['Hank Pym', 'male', 1962],
    ['Scarlet Witch', 'female', 1964],
    ['Wasp', 'female', 1963],
    ['Black Widow', 'female', 1964],
    ['Vision', 'male', 1968]
]
temp = pd.DataFrame(data=[None],
                    index=[None],
                    columns=[None])
marvel_df = pd.DataFrame(data=marvel_data)
# print(marvel_df)
col_names = ['name', 'sex', 'first_appearance']
marvel_df.columns = col_names
# print(marvel_df)
marvel_df.index = marvel_df['name']
# print(marvel_df)
marvel_df = marvel_df.drop(['name'], axis = 1)
# print(marvel_df)
marvel_df = marvel_df.drop(['Namor', 'Hank Pym'], axis = 0)
# print(marvel_df.iloc[:5])
# print(marvel_df.iloc[-5:])  #Negative indexing means ulta chalna
# print(marvel_df.iloc[0:5].sex.to_frame())
# print(marvel_df.iloc[1:-1].first_appearance.to_frame())
marvel_df['year_since'] = 2018 - marvel_df['first_appearance']
# print(marvel_df)
mask = marvel_df['sex'] == 'female'
# print(mask)
temp_answer = marvel_df['first_appearance'] > 1970
# print(temp_answer)
female_answer = marvel_df[(marvel_df['first_appearance'] > 1970) & (marvel_df['sex'] == 'female')]
# print(female_answer)
# plt.plot(marvel_df.first_appearance)
# plt.show()
num_py_array = (np.array([0, 1, 2, 3, 4]),np.dtype(np.int8).itemsize)
normal_array = [0, 1, 2, 3, 4]
# print(num_py_array + 2)
# print(num_py_array[num_py_array > num_py_array.mean()])
random_array = np.random.randint(100, size=(3, 3))
# print(random_array)
# print(random_array[random_array > 50])
# print(sys.getsizeof(num_py_array))
# print(sys.getsizeof(normal_array))\
# a = np.arange(5)
# b = [0, 1, 2, 3, 4]
# print(np.eye(8, 4))
print(np.identity(3))