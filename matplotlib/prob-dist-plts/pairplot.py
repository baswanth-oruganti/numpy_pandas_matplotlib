import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame()

df[1] = np.random.randn(100)
df[2] = df[1] ** 2
df[3] = np.exp(df[1])
df[4] = np.sin(df[1])
df[5] = np.cos(df[1])

mu = df[1].mean()
sigma = df[2].std()
gauss = (1/(np.sqrt(2*np.pi)*sigma))*(np.exp(-(df[1]-mu)**2)/2*sigma**2)
df[6] = gauss

df.columns = ["x","square(x)","exp(x)","sin(x)","cos(x)","N(x)"]

print(df)
sns.pairplot(df)
plt.tight_layout()
plt.savefig("pairplot.eps")
plt.show()
