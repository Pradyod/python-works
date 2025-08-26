num=int(input("enter a no"))

is_prime=True

for i in range(2,num):
    if num%i==0:
        is_prime=False
        break

result= "prime no" if is_prime==True else "not prime"

print(result)