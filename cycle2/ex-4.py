def pyramid(n):
    for i in range(1,n+1):
        n1=i
        for j in range(0,i):
            print(n1,end=" ")
            n1=n1+i
        print("\r")
a=int(input("enter a number"))
pyramid(a)
