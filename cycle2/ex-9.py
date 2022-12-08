def factor(n):
    li=[]
    for i in range(1,n+1):
        if n%i==0:
            li.append(i)
    print("factors : ",li)
n=int(input("enter a number :"))
factor(n)
