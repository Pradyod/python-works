fp="D:\\Develpment journey\\python_works\\file-operations\\employess.csv"

fr=open(fp,'r')

all_employees=[]

for line in fr:

    line=line.rstrip("\n")

    data=line.split(',')

    dictionary={

                'id':data[0],'name':data[1],
                'department':data[2],'salary':data[3],
                'email':data[4],'location':data[5]

                }
    
    all_employees.append(dictionary)

# print(all_employees)


all_employees_name=[e.get("name") for e in all_employees]
# print(all_employees_name)

ekm_employees=[e.get("name") for e in all_employees if e.get("location").lower()=='ekm']
# print(ekm_employees)

max_salary=max(all_employees,key=lambda e:e.get("salary"))
# print(max_salary)

min_salary=min(all_employees,key=lambda e:e.get("salary"))
print(min_salary)

least_salary_emp=[e for e in all_employees if e.get("salary")==min_salary]
print(least_salary_emp)