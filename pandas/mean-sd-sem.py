import pandas as pd

### calculate series mean, std and sem using pandas: can also be calculated on dataframe

data = pd.read_csv("data.txt",header=None)
print(data)
print(data[0].mean())
print(data[0].std()) # uses N-1 to Normalize by default; use ddof=0 to use N intead of N-1
print(data[0].sem()) # uses N-1 to Normalize by default; use ddof=0 to use N intead of N-1
