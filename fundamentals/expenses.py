expenses=[10000,12000,13000,14000]

expenses[1]=12500

print(expenses)

result=expenses[0]+expenses[1]+expenses[2]+expenses[3]

print(max(expenses))

avg=expenses[0]+expenses[1]+expenses[2]+expenses[3]/4

print(avg)

total=0
for i in range(0,len(expenses)):
    total+=expenses[i]

print(total)