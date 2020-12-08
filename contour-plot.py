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
#data = np.loadtxt(sys.argv[1])


x = data["s[R]"]
y = data["z[R]"]
z = data["DG"]

print(x)

#x = data[:, 0]
#y = data[:, 1]
#z = data[:, 2]

breaks = np.linspace(0, 12, 13)

matplotlib.rcParams['contour.negative_linestyle'] = 'solid'


CS1=plt.tricontour(x, y, z, breaks, linewidths=1.0, colors='k')
CS2=plt.tricontourf(x, y, z, breaks, cmap='seismic',vmin=0.0, vmax=12.0)
plt.colorbar(ticks=breaks, orientation='vertical')

#plt.clabel(CS1, inline=1, fontsize=10)

plt.xlabel('CV1 (degrees)')
plt.ylabel('CV2 (degrees)')

#plt.xticks(x)
#plt.yticks(y)
#plt.legend()
#plt.grid()

plt.axis([-3.1, 3.1, -3.1, 3.1]) # [xstart, xend, ystart, yend]
plt.show()






