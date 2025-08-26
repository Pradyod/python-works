def max_odd_no(number):
    while(number!=0):
        digit=number%10
        if digit%2!=0:
            print(number)
            break
        number=number//10

print(max_odd_no(4371))