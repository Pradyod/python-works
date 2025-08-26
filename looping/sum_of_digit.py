#set a no
#set a sum
#loop
#extract last digit
#add last digit with sum(remove last digit from no)
#flow division of no
#print sum outside the loop


num=471
sum=0

while num!=0:
    last_digit=num%10
    sum+=last_digit
    num=num//10
print(sum)