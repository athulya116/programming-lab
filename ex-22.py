import operator
d={1:2,3:4,4:3,2:1,0:0}
print('Dictionary :',d)
sorted_d=dict(sorted(d.items(),key=operator.itemgetter(1)))
print("dictionary in ascending orderby value:",sorted_d)
sorted_d=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
print("dictionary in descending order by value:",sorted_d)
