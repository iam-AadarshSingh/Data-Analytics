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