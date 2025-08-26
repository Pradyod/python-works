text="a b c d e f"

words=text.split(" ")


count={}

for i in words:
    if i in count:
         print(i,"frst chr")
         break
    else:
        count[i]=1

