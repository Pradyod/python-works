arr1=[10,11,20,17,18]

arr2=[20,10,12,17]

cmmn=[]

for i in arr1:
    if i in arr2:
        cmmn.append(i)

print(cmmn)