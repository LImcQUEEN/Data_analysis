import numpy as np
import pandas as pd
g7_pop = pd.Series([35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523])
g7_pop.name = 'Population in millions'
# print(g7_pop.values)
type(g7_pop.values) #In reality the pandas series are backed by numpy array so have all the functionality of numpy
# print(g7_pop[0])
# print(g7_pop.index) #This will tell the starting index and ending index and steps meaning difference between index in conventional case it would be 1
g7_pop.index = [ #By doing this we give custom index to our series so we could access them directly using these indexes
    'Canada',   #Be cautious that assigning less numb of indexes as  compared to data would result in error if we have 7 elements we have to assign 7 indexes
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]
myDictionary = {    #A series might look like dictionary, but they are very different and as dictionary are unordered
    'Canada': 35.467,
    'France': 63.951,
    'Germany': 80.94,
    'Italy': 60.665,
    'Japan': 127.061,
    'United Kingdom': 64.511,
    'United States': 318.523
}
# print(myDictionary)
arrayDictionary = pd.Series(myDictionary, name='G7 Population in millions')
# print(arrayDictionary)
# print(arrayDictionary['Canada'])    #You can use your assign index to access series elements
# print(arrayDictionary.iloc[0])  #Or you can use conventional method of accessing elements using their indexes by .iloc()
# print(g7_pop[['Italy', 'France']])  #Selecting multiple elements return a new series
# print(g7_pop['Canada':'Italy']) #We can also slice a series like string but unlike string UPPER LIMIT IS ALSO INCLUDED
# print(g7_pop[g7_pop>70])    #Can also include condition to filter data
# print(g7_pop[g7_pop>g7_pop.mean()])
# print(g7_pop*1000000)
# print(np.log(g7_pop))
#   ~ --> This is for NOT
#   | --> This is for OR
#   & --> This is for AND
# print(g7_pop[(g7_pop > g7_pop.mean())|(g7_pop > 200)])
x = ['A', 'B', 'C', 'D', 'E']
# print(x, type(x))
y = pd.Series(x, index=['first', 'second', 'third', 'fourth', 'fifth'])
# print(y, type(y))
# print(y[1:-1])
# print(y[::-1])  # this shows the element in reverse position
# print(y[0:2])
# print(y['first': 'third'])  #using custom index slicing also includes the upper-limit
temp = pd.Series([4,2,5,1,3], index=['forth','second','fifth','first','third'])
# print(temp.sort_values())
# print(temp.sum())
# print(temp.all())
print(temp.any())
