# num=int(input("enter a no"))

# is_prime=True

# for i in range(2,num):
#     if num%i==0:
#         is_prime=False
#         break

# result= "prime no" if is_prime==True else "not prime"

# print(result)

#-----------------new prime no pgm------------------

num = int(input("enter a no"))

while(num<1):

    print("pls enter a positive no")

    num = int(input("enter a no"))

else:

    is_prime=True

    for i in range(2,num):

        if num%i==0:

            is_prime=False

    print(is_prime)
