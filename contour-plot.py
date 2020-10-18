#makes a contour plot by reading data from 3 columns from the file argument act.dat

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

data = np.loadtxt(sys.argv[1])


x = data[:, 0]
y = data[:, 1]

z = data[:, 2]

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

plt.axis([0, 180, 0, 180]) # [xstart, xend, ystart, yend]
plt.show()






