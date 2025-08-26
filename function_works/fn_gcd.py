def gcd(num1,num2):
    limit=min(num1,num2)

    gcd=1

    for i in range(1,limit+1):
        if num1%2==0 and num2%2==0:
            gcd=i
    print(gcd)

print(gcd(12,24))