input=open("data.txt","r")
output=open("odd.txt","w")
l=input.readlines()
for x in range(0,len(l),2):   
    output.write(l[x])
    print(l[x])
input.close()
output.close()
