import csv
with open('detail.csv',newline='')as f:
    s=csv.reader(f,delimiter=' ',quotechar='!')
    for i in s:
        print(','.join(i))