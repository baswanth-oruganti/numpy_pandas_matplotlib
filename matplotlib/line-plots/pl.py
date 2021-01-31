import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()

file_list = ['6-pl.txt','8a-pl.txt', '8b-pl.txt', '8c-pl.txt', '8d-pl.txt', '8e-pl.txt']
sns.set_style()
fig, ax = plt.subplots(nrows=3,ncols=2,figsize=(7,7))

plt.rcParams['font.family'] = "sans-serif"
plt.rcParams['font.sans-serif'] = "Arial"
plt.rcParams['font.size'] = 10


item_no = 0
for  i in list(range(0,3)):
    for j in list(range(0,2)):
        df = pd.read_csv(file_list[item_no],sep="\s+",header=None)
        x = df[0]
        y = df[1]
        y = np.array(y).reshape(-1,1)
        y = min_max_scaler.fit_transform(y)
        ax[i][j].plot(x,y)
        item_no += 1
        ax[i][j].set_xlabel("Wavelength (nm)")
        ax[i][j].set_ylabel("Normalized Intensity (a.u.)")
        ax[i][j].set_xlim(300,600)
        ax[i][j].set_ylim(0.0,1.05)
        ax[i][j].xaxis.set_minor_locator(ticker.MultipleLocator(25))
        ax[i][j].yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

plt.tight_layout()
fig.savefig('6a.eps',dpi=600)
plt.show()
