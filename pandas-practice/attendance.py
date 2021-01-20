import pandas as pd

### Ignore first 8 rows of xlsx file and read only first 5 columns
attend=pd.read_excel("attendance.xlsx",header=None,skiprows=8,usecols=[i for i in range(5)])

### Creating column names and row indices
attend.columns=["SNo.", "Roll-No", "Name", "Total-Classes", "Classes-Attended"]
attend.index = ["student"+str(i) for i in range(1,28)]

### Calculate Attendance Percentage
attend["%-Attendance"]=(attend["Classes-Attended"]/attend["Total-Classes"])*100
print(attend)

### Write results to a csv file
attend.to_excel("attendance-modified.xlsx",index=False)
