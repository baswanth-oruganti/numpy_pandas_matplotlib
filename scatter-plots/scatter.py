import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


df1 = pd.read_csv("data-S1.dat",sep="\s+",header=None,names=['S0','S1'])
df2 = pd.read_csv("data-T1.dat",sep="\s+",header=None,names=['S0','T1'])

x1 = np.linspace(3.72,2.10,17)
x2 = np.linspace(3.72,2.20,16)
y1 = df1["S0"]
y2 = df1["S1"]
y3 = df2["S0"]
y4 = df2["T1"]

fig, ax = plt.subplots(1,2,figsize=(7,4))
formatter = ticker.FormatStrFormatter('%1.1f')
plt.rcParams['font.family'] = "sans-serif"
plt.rcParams['font.sans-serif'] = "Arial"
plt.rcParams['font.size'] = 10


print(x2)
for axis in ax:
	axis.set_xlim([3.8,2.0])
	axis.set_ylim([-0.1,3.7])
	axis.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))
	axis.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))
	axis.set_xlabel('Bond length (Å)')
	axis.set_ylabel(r'$\Delta E$ (eV)')


ax[0].scatter(x1,y2,label=r'S$_1$',color='r')
ax[0].scatter(x1,y1,label=r'S$_0$',color='b')
ax[1].scatter(x2,y4,label=r'T$_1$',color='r')
ax[1].scatter(x2,y3,label=r'S$_0$',color='b')
ax[0].legend(loc=(0.3,0.85),frameon=False)
ax[1].legend(loc=(0.3,0.85),frameon=False)

plt.tight_layout()
fig.savefig('Fig1-BPh.eps',dpi=600)
plt.show()
