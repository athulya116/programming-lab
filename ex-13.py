str1=str(input("enter the word:"))
z=list(str1)
print("string is :",str1)
print("string after exchanging the first and last characters")
temp=z[0]
z[0]=z[-1]
z[-1]=temp
str2=''.join([str(x)for x in z])
print(str2)
