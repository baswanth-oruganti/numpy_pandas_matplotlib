import matplotlib.pyplot as plt
import seaborn as sns
from seaborn_qqplot import pplot


iris = sns.load_dataset('iris')
pplot(iris, x="petal_length", y="sepal_length",kind='q')
plt.show()
