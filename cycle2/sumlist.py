list=[45,6,7,4,32,78]
def sum(list,size):
    if(size==0):
        return 0
    else:
        return list[size-1]+sum(list,size-1)
total=sum(list,len(list))
print("sum of all elements in given list:",total)
