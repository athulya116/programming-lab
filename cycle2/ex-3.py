def digit(c,d):
    l=[]
    for i in range(c,d):
        k=[int(x) for x in str(i)]
        if k[0]%2==0 and k[1]%2==0 and k[2]%2==0 and k[3]%2==0:
            l.append(i)
    li=[]
    for i in l:
        for j in range(1,i//2+1):
            if i/j==j:
                li.append(i)
    print(li)
a=int(input("enter the starting range"))
b=int(input("enter the ending range"))
digit(a,b)
