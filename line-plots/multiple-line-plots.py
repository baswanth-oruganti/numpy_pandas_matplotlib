import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


files1 = ['rmsd-ca-tar.xvg','rmsd-nH-tar.xvg','aloop-nH-tar.xvg','dfg-nH-tar.xvg','ahelix-nH-tar.xvg','ploop-nH-tar.xvg']
labels = [r'C$\alpha$','non-H','A-loop','DFG',r'$\alpha$C-helix','P-loop']
colors = ['blue','orange','black','red','green','brown']


fig,ax = plt.subplots(5,2,sharex=True,figsize=(7,7),squeeze=True)
formatter = ticker.FormatStrFormatter('%1.1f')
plt.rcParams['font.family'] = "sans-serif"
plt.rcParams['font.sans-serif'] = "Arial"
plt.rcParams['font.size'] = 10

print(ax)
for item in ax:
    for axis in item:
        axis.spines['top'].set_color('none') 
        axis.spines['right'].set_color('none')
        axis.set_xlim([0,500]) 
        axis.set_ylim([0.0,7.0]) 
        axis.set_xticks([0,100,200,300,400,500])
        axis.xaxis.set_minor_locator(ticker.MultipleLocator(50))
        axis.set_yticks(np.linspace(0,6,7))
        axis.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
        axis.yaxis.set_major_formatter(formatter)
        axis.set_ylabel('RMSD (Å)')


ax[4][0].set_xlabel('Time (ps)')
ax[4][1].set_xlabel('Time (ps)')

directory = 1


for ind in range(2):
    for number in range(5):
        label_col = 0
        for item in files1:
            path = str(directory) + "/" + str(item)
            data=pd.read_csv(path,sep='\s+',header=None,skiprows=18,names=["time","rmsd"])
            data["time"]=round(data["time"],1)
            data["rmsd"]=round(10*data["rmsd"],2)
            x=data["time"]
            y=data["rmsd"]
            ax[number][ind].plot(x,y,label=labels[label_col],lw=1,color=colors[label_col])
            label_col += 1
        directory += 1

ax[0][0].legend(loc=[0.5,0.3],fontsize=7,frameon=False)
ax[0][1].legend(loc=[0.5,0.3],fontsize=7,frameon=False)
plt.style.use('seaborn')
plt.tight_layout()
fig.savefig('rmsd.tiff',dpi=600)
plt.show()
