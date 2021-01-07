import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data1 = np.random.randn(500)
data2 = data1**2

sns.jointplot(x=data1,y=data2)
plt.savefig("jointplot.eps")
plt.show()
