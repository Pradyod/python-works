fp="D:\\Develpment journey\\python_works\\file-operations\\years.txt"

fr=open(fp,'r')

years=[]

for yr in fr:
    years.append(str(yr.rstrip("\n")))

print(years)

for yr in years:
    if int(yr)%4==0 and int(yr)%100!=0 or int(yr)%400==0:
        print(yr) 

