import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

### Define column labels, row-lables and missing values for the data
col_labels = ["App-No", "first", "last", "Email","Score"]
row_labels = ["student"+str(i) for i in range(1,21)]
missing_vals = ["NA", "NaN", "nan", "Nan"]

### Read txt file, file should not contain any header rows

df = pd.read_csv('gate-rank.txt', sep="\s+", header=None, names=col_labels, na_values=missing_vals)
df.fillna("principal@gitam.edu")
df.index = row_labels # set row indices

#df.columns = ["App-No", "first", "last", "Email","Rank"]
#df = df.set_index("App-No")

### Sort based on scores and add a rank column
df=df.sort_values("Score", ascending=False) # sorting based on scores
df["Rank"]=[i for i in range(1,21)]

### Read excel file for attendance
attend=pd.read_excel("attendance.xlsx",header=None,skiprows=8,usecols=[i for i in range(5)])
attend.columns=["SNo.", "Roll-No", "Name", "Total-Classes", "Classes-Attended"]
attend.index = ["student"+str(i) for i in range(1,28)]

### Calculate attendance percentage
attend["%-Attendance"]=(attend["Classes-Attended"]/attend["Total-Classes"])*100
attend


### Calculate correlation coefficient between attendance and Score
df["attendance"]=attend["%-Attendance"]
df[["attendance","Score"]].corr()

### Identify student who got rank 1
rank_1 = df[df["Rank"]==1]
#sns.boxplot(data=df["Score"])

#sns.histplot(data=df["Score"],bins=7,kde=True)
#sns.barplot(data=df[["attendance","Score","Rank"]])
sns.scatterplot(x=df["Rank"], y=df["Score"])
plt.show()
### Print rank of student3
print(df.loc["student3"],["Rank"])


### Calculate mean, median and sigma of scores
print(f"mean = {df['Score'].mean()}")
print(f"median = {df['Score'].median()}")
print(f"sigma = {round(df['Score'].std(),1)}")
print(f"correlation data {df.corr()}")

df.to_csv("rank.csv",index=False)
