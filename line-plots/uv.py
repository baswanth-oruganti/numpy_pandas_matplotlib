import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

file_list = ['6.txt','8a.txt', '8b.txt', '8c.txt', '8d.txt', '8e.txt']
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
        ax[i][j].plot(x,y)
        item_no += 1
        ax[i][j].set_xlabel("Wavelength (nm)")
        ax[i][j].set_ylabel("Absrobance")
        ax[i][j].set_xlim(200,500)
        ax[i][j].set_ylim(0.0,0.42)
        ax[i][j].xaxis.set_minor_locator(ticker.MultipleLocator(50))
        ax[i][j].yaxis.set_minor_locator(ticker.MultipleLocator(0.05))

plt.tight_layout()
fig.savefig('6a.eps',dpi=600)
plt.show()
