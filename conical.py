import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

X = np.arange(-1, 1, 0.05)
Y = np.arange(-1, 1, 0.05)
X, Y = np.meshgrid(X, Y)
Z1 = -(-X**2-Y**2+2*abs(X)+2*abs(Y))**0.65
Z2 = (-X**2-Y**2+2*abs(X)+2*abs(Y))**0.65

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X, Y, 1.0*Z1, color='green')
ax.plot_wireframe(X, Y, 0.7*Z2, color='red')

#Hide grid lines
ax.grid(False)

# Hide axes ticks
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
plt.axis('off')


plt.show()


