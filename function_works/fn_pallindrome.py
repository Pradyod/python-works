def pallindrome(num):
    temp=num
    rev=0
    while temp>0:
        rem=temp%10
        rev=(rev*10)+rem
        temp=temp//10
    if num==rev:
        print("pallindrome")
    else:
        print("not pallindrome")

print(pallindrome(1221))