arr=[10,11,12,13,11,10,14]

temp=[]

for i in arr(0,len(arr)):
    if i in temp:
        break
    else:
        arr[i]+=temp