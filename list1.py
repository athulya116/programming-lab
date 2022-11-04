a=input("enter the elements in first list")
a=a.split(" ")
a=list(map(int,a))
b=input ("enter the elements of second list")
b=b.split(" ")
b=list(map(int,b))
n=len(a)
m=len(b)
if n==m:
   print("the length are same")
else :
   print("length are different")
sum1=0
sum2=0
for i in range(n):
    sum1=sum1+a[i]
for i in range(m):
    sum2=sum2+b[i]
print("sum of first list = ", sum1)
print("the sum of second list = ",sum2)
if (sum1==sum2):
    print("the sum is same")
else:
    print("the sum is different")
c=[]
for i in range(n):
    if a[i] in b:
        c.append(a[i])
        print("the elements in both are ",c)
