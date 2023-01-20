import csv
with open('detail.csv',newline='')as f:
    s=csv.DictReader(f)
    for i in s:
        print(i['rollno'],i['name'],i['mark'])