arr=[1,10,11,12,34,35]

odd_arr=[]
evn_arr=[]

for i in arr:
    if i%2==0:
        evn_arr.append(i)
    else:
        odd_arr.append(i)

print(evn_arr)
print(odd_arr)