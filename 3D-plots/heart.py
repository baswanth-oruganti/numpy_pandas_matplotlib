import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

X = np.arange(-4.2, 4.2, 0.1)
Z1 = ((2*abs(X)-X*X)**0.5).real
Z2 = (-np.arccos(1-abs(X))).real-np.pi

fig = plt.figure()
plt.plot(X, Z1)
plt.plot(X, Z2)

#Hide grid lines
#plt.grid(False)

# Hide axes ticks
#plt.set_xticks([])
#plt.set_yticks([])
plt.axis('off')


plt.show()


