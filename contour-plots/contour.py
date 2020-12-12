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


data=pd.read_csv("fes_60.dat",header=None,sep="\s+",usecols=[i for i in range(3)])
data.columns = ["s[R]","z[R]", "DG"]


x = data["s[R]"]
y = data["z[R]"]
z = data["DG"]



breaks = np.linspace(0, 12, 13)

matplotlib.rcParams['contour.negative_linestyle'] = 'solid'


fig, ax = plt.subplots()

ax.tricontour(x, y, z, breaks, linewidths=1.0, colors='k')
image = ax.tricontourf(x, y, z, breaks, cmap='winter',vmin=0.0, vmax=12.0)
fig.colorbar(mappable=image,ticks=breaks, orientation='vertical',ax=ax)

#plt.clabel(CS1, inline=1, fontsize=10)

ax.set_xlabel('CV1 (degrees)')
ax.set_ylabel('CV2 (degrees)')


plt.show()






