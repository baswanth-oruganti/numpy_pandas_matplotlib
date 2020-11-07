import numpy as np
import matplotlib.pyplot as plt


np.random.seed(123)
data = np.random.normal(0.3,0.01,100000)
plt.hist(data, bins=25, range=(0.25,0.35))
plt.show()
