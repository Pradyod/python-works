num=153

temp=num

count=len(str(num))

sum=0

while num!=0:
    digit= num%10

    exponent=digit**count

    sum=sum+exponent

    num=num//10

if sum==temp:
    print("Armstrong")
else:
    print("Not Armstrong")

#store the num in another variable
#take the count of the number in str
#set a variable as 0
#while num not =0
#digit=num%10
#exponent=digit**count
#expenent+sum
#num//10
#sum==temp is armstrong