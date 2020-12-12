import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

X = np.arange(-2.6, 2.6, 0.1)
Y = np.arange(-2.6, 2.6, 0.1)
X, Y = np.meshgrid(X, Y)
Z = np.cos(1.4*X)+0.5*X

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z)

#Hide grid lines
ax.grid(False)

# Hide axes ticks
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
plt.axis('off')

plt.show()


