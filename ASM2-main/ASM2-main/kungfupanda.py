import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

df = pd.read_excel("ASM2_PBI_Exel.xlsx",sheet_name="Sheet1")
pd.set_option('display.max_rows', 100)
df = df.dropna()
duplicates = df.duplicated()
df = df.drop(df[duplicates].index)
print (df)