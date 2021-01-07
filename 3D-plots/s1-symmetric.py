import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

sns.set_style()

X = np.arange(-2.6, 2.6, 0.05)
Y = np.arange(-2.6, 2.6, 0.05)
X, Y = np.meshgrid(X, Y)
Z = np.cos(1.4*X)+4

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, color='green')

#Hide grid lines
ax.grid(False)

# Hide axes ticks
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
plt.axis('off')

plt.show()


