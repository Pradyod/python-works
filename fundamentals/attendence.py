attendance = ["H","P","P","P","P","L","H","H","P","P","P","P","L","H"]

present=0

absent=0
for i in range(0,len(attendance )):
    if attendance[i]=="P":
        present+=1
    else:
        absent+=1

print(present)
print(absent)