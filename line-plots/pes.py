import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

sns.set(rc={"xtick.bottom" : True, "ytick.left" : True})
sns.set_style("white")
sns.set_style("ticks")

plt.rcParams['font.family']="sans-serif"
plt.rcParams['font.sans-serif'] = "Arial"
plt.rcParams['font.size'] = 10

data_np = pd.read_csv('nP-G-plot.txt',header=None,sep="\s+")
data_np_sem = pd.read_csv('nP-G-sem.txt',header=None,sep="\s+")
data_p = pd.read_csv('P-G-plot.txt',header=None,sep="\s+")
data_p_sem = pd.read_csv('P-G-sem.txt',header=None,sep="\s+")

x1 = np.arange(1,len(data_np[0])+1)
y1 = data_np[0]
y11 = data_np_sem[0]


x2 = np.arange(1,len(data_p[0])+1)
y2 = data_p[0]
y22 = data_p_sem[0]

fig, ax = plt.subplots(figsize=(3.3,3.3))
ax.set_xlim(0,11)
ax.set_ylim(-2.0,29.0)
ax.set_xlabel('Configuration #')
ax.set_ylabel(r'$\Delta$$G$(kcal/mol)')
ax.set_xticks([i for i in range(1,11)])
ax.set_yticks(np.linspace(0.0,25.0,6))
formatter = ticker.FormatStrFormatter('%1.1f')
ax.yaxis.set_major_formatter(formatter)
ax.yaxis.set_minor_locator(ticker.MultipleLocator(2.5))

ax.plot(x1,y1,ls="--",lw=1,marker="_",ms=5,label="Non-phosphorylated")
ax.plot(x2,y2,ls="--",lw=1,marker="_",ms=5,label="Phosphorylated")

plt.legend(loc=2,frameon=False)
plt.tight_layout()
plt.savefig("fig1.eps",dpi=600)
plt.show()
