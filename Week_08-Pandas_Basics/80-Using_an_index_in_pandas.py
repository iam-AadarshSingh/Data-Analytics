import pandas as pd
import numpy as np

prices = {
    'Car':250000,
    'Cycle':4000,
    'Bike':90000,
}
print(prices)
print(type(prices))

prices_series = pd.Series(prices)
print(prices_series)
print(type(prices_series))

print(prices_series.index)
print(type(prices_series.index))