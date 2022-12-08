def pattern(n):
    for i in range(n):
        for j in range(0,i+1):
            print("*",end=" ")
        print("\n")
    for i in range(n,0,-1):
        for j in range(0,i-1):
            print("*",end=" ")
        print("\n")
n=int(input("enter the limit"))
pattern(n)
