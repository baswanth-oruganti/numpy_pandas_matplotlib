import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import scipy.ndimage
from scipy import interpolate
import matplotlib.mlab as ml
import matplotlib.tri as tri
import matplotlib
import pandas as pd
from sklearn import preprocessing


data=pd.read_csv("fes.dat",header=None,sep="\s+",skiprows=9,usecols=[i for i in range(3)])
data.columns = ["s(R)","z(R)", f"$\Delta$G"]

data=data[(data["s(R)"]>1.2) & (data["s(R)"]<83.0) & (data["z(R)"]>0.0)]
#x_norm = (data["s[R]"]-data["s[R]"].min())/(data["s[R]"].max()-data["s[R]"].min())

min_max_scaler = preprocessing.MinMaxScaler()
s = np.array(data["s(R)"]).reshape(-1,1)
data["Normalized s(R)"] = min_max_scaler.fit_transform(s)
data["z(R)"]=data["z(R)"]*100
data[f"$\Delta$G"]=data[f"$\Delta$G"]/4.2

x = data["Normalized s(R)"]
y = data["z(R)"]
z = data[f"$\Delta$G"]
x1 = data["Normalized s(R)"]



breaks = np.linspace(0, 30, 11)

matplotlib.rcParams['contour.negative_linestyle'] = 'solid'


fig, ax = plt.subplots()

ax.set_ylim([0.5,6.5])
CS = ax.tricontour(x, y, z, breaks, linewidths=1.0, colors='k')
#manual_locations = [(0.17, 3.98), (0.275,4.0),(0.45, 4.16),(0.54,4.20),(0.66,4.2),(0.89,4.05)]
#ax.clabel(CS, fontsize=15, inline=True,manual=manual_locations,inline_spacing=2,colors='w', fmt='%1.1f',rightside_up=True)
image = ax.tricontourf(x, y, z, breaks, cmap='seismic',vmin=0.0, vmax=30.0)
fig.colorbar(mappable=image,ticks=breaks, orientation='vertical',ax=ax)

#plt.clabel(CS1, inline=1, fontsize=10)

ax.set_xlabel('Normalized s(R)')
ax.set_ylabel('z(R)')


data["Normalized s(R)"] = (data["s(R)"]-data["s(R)"].min())/(data["s(R)"].max()-data["s(R)"].min())
bins=pd.cut(data["Normalized s(R)"],bins=25)
g=data["$\Delta$G"].groupby(bins).min()
z=[data[data["$\Delta$G"]==i]['z(R)'] for i in g]
s=data["Normalized s(R)"].groupby(bins).mean()

df=pd.DataFrame()
df["s(R)"]=s.unique()
df["G"]=g.unique()
print(df)
df.to_csv("fes1D.dat",sep="\t",index=None)


plt.scatter(s,z,color='w',marker=".")
plt.savefig("test.eps")
plt.show()






