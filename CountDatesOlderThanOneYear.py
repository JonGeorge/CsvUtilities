import csv
from datetime import datetime as dt

f = open('Case.csv',encoding="utf8")

# Each row is returned as list of strings
file = csv.reader(f)

# Column heaader you are looking for
header = "LastModifiedDate"

# Get column number for specific column header
colNumber = 0
for (row) in file:
    if row.index(header):
        colNumber = row.index(header)
        break
    else:
        print("Column header not found")
        break

# Count number of dates in specified column older than a year
count = 0
for (row) in file:
    oneYearAgo = dt.strptime('2018-02-06', '%Y-%m-%d')
    date = dt.strptime(row[colNumber], '%Y-%m-%d %H:%M:%S')

    if (oneYearAgo > date):
        count = count + 1

print(count)
f.close()
