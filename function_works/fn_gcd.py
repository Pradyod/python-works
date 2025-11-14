def gcd(num1,num2):
    limit=min(num1,num2)

    gcd=1

    for i in range(1,limit+1):
        if num1%i==0 and num2%i==0:
            gcd=i
    print(gcd)

print(gcd(5,10))