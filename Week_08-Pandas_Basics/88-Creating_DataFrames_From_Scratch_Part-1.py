import pandas as pd
#1 Dataframe froma dictionary of lists
data = {
    'ProductName':['Product A','Product B','Product C'],
    'ProductPrice':[22250,16600,12500]
    }
df = pd.DataFrame(data)
print(df)

#2 Construct a Datafram from a dictionary of list + specify an index
data = {
    'ProductName':['Product A','Product B','Product C'],
    'ProductPrice':[22250,16600,12500]
    }
df_index = pd.DataFrame(data, index=['A','B','C'])
print(df_index)

data = {
    'ProductName':['Product A','Product B','Product C'],
    'ProductPrice':[22250,16600,12500]
    }
Product_IDs = ['A','B','C']
df_Product_IDs = pd.DataFrame(data, index=Product_IDs)
print(df_Product_IDs)