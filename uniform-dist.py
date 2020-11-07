import numpy as np
import matplotlib.pyplot as plt


rolls = np.random.randint(1,7,10000)
val, counts = np.unique(rolls, return_counts=True)
plt.stem(val, counts/len(counts))
plt.show()
