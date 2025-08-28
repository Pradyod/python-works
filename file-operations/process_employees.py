fp="D:\\Develpment journey\\python_works\\file-operations\\employess.csv"

fr=open(fp,'r')

all_employees=[]

for line in fr:

    line=line.rstrip("\n")

    data=line.split(',')

    dictionary={

                'id':data[0],'name':data[1],
                'Department':data[2],'Salary':data[3],
                'Location':data[4]

                }
    
    all_employees.append(dictionary)
    
print(all_employees)