import pandas as pd
series_a = pd.Series([10,20,30,40,50,60])
price = pd.Series({'Car':25000,
                   'Bike':160000,
                   'Cycle':4000})
print(series_a[0])
print(price)
print(price['Car'])
print(price[0]) #will rum with a warning
series_b = pd.Series([10,20,30,40,50,60], index=[1,2,3,4,5,6])
print(series_b)
print(series_b[0])
print(series_b[1])