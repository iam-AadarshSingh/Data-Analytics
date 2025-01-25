import pandas as pd
#4 Construct a Datafram from a dictionary of pandas Series
ser_products = pd.Series(['Car', 'Cycle', 'Airplane'])
ser_prices = pd.Series([950000, 4500, 95000000])
data = {'Product_Name':ser_products,
        'Product_Price':ser_prices}
df = pd.DataFrame(data)
print(df)


ser_products = pd.Series(['Product A', 'Product B', 'Product c'], index=['A','B','C'])
ser_prices = pd.Series([950000, 4500, 95000000], index=['A','B','C'])
data = {'Product_Name':ser_products,
        'Product_Price':ser_prices}
df = pd.DataFrame(data)
print(df)


ser_products = pd.Series(['Product A', 'Product B', 'Product c'], index=['A','B','C'])
ser_prices = pd.Series([950000, 4500, 95000000], index=['B','A','C'])
data = {'Product_Name':ser_products,
        'Product_Price':ser_prices}
df = pd.DataFrame(data)
print(df)

#5 Construct a Datafram from list of list
data = [['Product A', 22250], ['Product A', 22250], ['Product A', 22250]]
df = pd.DataFrame(data)
print(df)

data = [['Product A', 22250], ['Product A', 22250], ['Product A', 22250]]
df = pd.DataFrame(data)
print(df)

data = [['Product A', 22250], ['Product A', 22250], ['Product A', 22250]]
df = pd.DataFrame(data)
print(df)

df.columns = ['ProductName', 'ProductPrice']
print(df)

df.index = ['A', 'B', 'C']
print(df)

#6 - Construct a Datafram in a Professional way
df = pd.DataFrame(data=[['Product A', 222],['Product B', 166],['Product C', 125]],
                  columns=['ProductName','ProductPrice'],
                  index=['A','B','C'])
print(df)
print(df.shape)