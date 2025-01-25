import pandas as pd
import numpy as np
products = ['Car','Basket','Shop','Broom']
print(products)

# .Series() - return a series witha idex number
products_series = pd.Series(products)
print(products_series)

daily_salary = pd.Series([1000,250,589,546])
print(daily_salary)
print(type(daily_salary))

array_a = np.array([10,20,30,40,50])
print(array_a)
print(type(array_a))

series_a = pd.Series(array_a)
print(series_a)
print(type(series_a))

#.dtype - returns data type of series
print(products_series.dtype)
print(daily_salary.dtype)
print(series_a.dtype)

#.size - return size of series
print(products_series.size)
print(daily_salary.size)
print(series_a.size)

#.name - return the name (changed name of any object)
print(products_series.name)
print(daily_salary.name)
print(series_a.name)



