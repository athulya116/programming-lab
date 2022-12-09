def list_sum(b):
    s=0
    for i in b:
        s=s+i
    print("SUM OF ELEMENTS OF LIST: ",s)
a=input("enter the list")
a=a.split(" ")
a=list(map(int,a))
list_sum(a)

