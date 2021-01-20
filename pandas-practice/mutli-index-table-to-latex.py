import numpy as np
import pandas as pd
array1 = ['B3LYP', 'B3LYP', 'M062X', 'M062X', 'PBE0', 'PBE0', 'HF', 'HF']
array2 = ['SVP', 'TZVP', 'SVP', 'TZVP', 'SVP', 'TZVP', 'SVP', 'TZVP']
tuples = list(zip(array1,array2))
ind = pd.MultiIndex.from_tuples(tuples,names=['Method','Basis set'])
df = pd.DataFrame(np.random.randn(8, 4),index=ind,columns=["rand1","rand2","rand3","rand4"])
print(ind)
print(df.loc["B3LYP","SVP"])
print(df.to_latex(caption="Random Numbers at Different Levels of Theory"))

