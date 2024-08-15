import pandas as pd
df1 = pd.read_excel("saledatabase.xlxx"), sheet_name="productData")
df2 = pd.read_excel("saledatabase.xlxx"), sheet_name="productTrending")

pd.set_option('display.max_rows', 120)
merged = pd.merge(df1, df2, on=['ProductID, ProductName'])

print(merged)