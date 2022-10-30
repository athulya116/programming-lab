print("enter the leapyears between two given years")
start_year=int(input("enter the start year"))
end_year=int(input("enter the end year"))
for year in range(start_year,end_year):
    if (year%4==0) and (year%100!=0) or (year%400==0):
       print(year,end=" ")
