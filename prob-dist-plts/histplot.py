import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = np.random.randn(500)

sns.histplot(data,kde=True,bins=20)
plt.show()
