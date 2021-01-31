import numpy as np
import matplotlib.pyplot as plt

mu = 0.3
sigma = 0.1

np.random.seed(123)
data = np.random.normal(mu,sigma,100000)
count, bins, ignored = plt.hist(data, bins=25, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *

               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),

         linewidth=2, color='r')
plt.show()
