def str(s):
    if s[-3:]=="ing":
        s=s.replace(s[-3:],"ly")
    else:
        s=s+"ing"
    print(s)
s=input("enter a string")
str(s)
