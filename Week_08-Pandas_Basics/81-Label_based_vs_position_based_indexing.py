import pandas as pd
series_a = pd.Series([10,20,30,40,50,60])
print(series_a)
print(series_a.index)
print(type(series_a.index))
print(list(series_a.index))

price = pd.Series({'Car':25000,
                   'Bike':160000,
                   'Cycle':4000})
print(price.index)
print(type(price.index))