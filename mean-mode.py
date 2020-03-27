# Find the mean, median, mode, min and max for all numeric attributes.

import pandas as pd
df = pd.read_csv('KCLT.csv')
print("Mean of the values \n ",df.mean())
print("Median of values\n ",df.median())
print("Mode of values\n ",df.mode())
