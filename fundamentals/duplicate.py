arr=[10,11,12,13,11,10,14]

temp=[]

for i in arr:
    if i in temp:
        break
    else:
        temp.append(i)

print("no duplicate elements:",temp)