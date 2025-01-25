import pandas as pd
start_date_deposite = pd.Series({
    '7/01/2025' : 0,
    '8/01/2025' : 1000,
    '9/01/2025' : 5550,
    '10/01/2025' : 9000,
    '11/01/2025' : 10000,
    '12/01/2025' : 18000,
    '13/01/2025' : 12000
})
print(start_date_deposite)
print(start_date_deposite.sum)
print(start_date_deposite.sum())
print(start_date_deposite.min())
print(start_date_deposite.max())
print(start_date_deposite.idxmax())
print(start_date_deposite.idxmin)


print(start_date_deposite.head())
print(start_date_deposite.tail())