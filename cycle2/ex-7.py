def word(b):
    li=[]
    for i in b:
        li.append(len(i))
    return max(li)
a=input("enter a list of words:")
a=a.split(" ")
n=word(a)
print("Length of longest word",n)
