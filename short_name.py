import pandas as pd

df = pd.read_excel('product.xlsx', sheet_name='Sheet1')
list_product = list(df['продукты'])
print(list_product)
