arr=[-2,-3,-4,-1,1,2,3,4,5,1]

closest_num=arr[0]

for num in arr:
    if abs(num)<abs(closest_num):
        closest_num==num

if closest_num<=0 and closest_num in arr:
    closest_num=abs(closest_num)

print(closest_num)








