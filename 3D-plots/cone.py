import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

X = np.arange(-1, 1, 0.01)
Y = np.arange(-1, 1, 0.01)
X, Y = np.meshgrid(X, Y)
Z1 = (2*abs(X)-X*X)**(0.95)+(2*abs(Y)-Y*Y)**(0.95)
Z2 = -np.arccos(1-abs(X))-np.arccos(1-abs(Y))

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, 0.7*Z1)
ax.plot_surface(X, Y, -Z1)

#Hide grid lines
ax.grid(False)

# Hide axes ticks
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
plt.axis('off')


plt.show()


