#prime no


# num = int(input("enter a no"))

# while(num<=1):
#     print("pls enter a positive no or greater than one")
#     num =int(input("enter a no"))
# else:
#     is_prime = True
#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
#     print(is_prime)

#gcd

# num1=int(input("enter a no"))
# num2=int(input("enter a no"))

# limit = min(num1,num2)

# gcd=1

# for i in range(1,limit+1):

#     if num1%i==0 and num2%i==0:

#         gcd=i

# print(gcd)


#factorial

# num = int(input("enter a no"))

# fact=1

# for i in range(1,num+1):

#     fact = fact*i

# print(fact)


#armstrong

# num =153

# temp = num 

# count = len(str(num))

# sum=0

# while num!=0:

#     digit = num%10

#     exponent = digit**count

#     sum= sum+exponent

#     num = num//10

# if sum == temp:

#     print("it is an armstrong")

# else:

#     print("it is not an armstrong")


#leap_yr

# num =int(input("enter a no"))

# if num%4==0 and num%100!=0 or num%400==0:

#     print('it is leap yr')

# else:

#     print('it is not leap yr')


#pallindrome(num)

# num = int(input("enter a no"))

# temp = num

# rev = 0 

# while temp>0:

#     rem=temp%10

#     rev=(rev*10)+rem

#     temp = temp//10

# if num==rev:

#     print("pallindrome")

# else:

#     print("not pallindrome")

#qsn1

# cube = {i:i*3 for i in range(1,6)}


# print(cube)

#anagram

# wrd1 = "dormitory"

# wrd2 = "dirtyroom"

# if set(wrd1)==set(wrd2) and len(wrd1)==len(wrd2):

#     print(True)

# else:
#     print(False)


#longest word in a sentence 


# sen = "my name is Alexander"

# words = sen.split()

# print(max(words,key=len))

#email

# def email_validation(email):

#     if email.count('@')==1:

#         return True
    
#     local,domain = email.split('@')

#     if '.' in domain:

#         return False
    
#     return True

# print(email_validation("pradyod2004gmail.com"))


# email = "pradyod2004@gmail.com"

# is_email=True
# if email.count('@')!=1:
#     is_email=False
# local,domain=email.split("@")

# if '.' in domain:

#     is_email=True

#     print(is_email)

#vowels

vowels=['a','e','i','o','u']

sen = "hello im john wick"

v_count=0
c_count=0

for i in sen:
    if i not in vowels:
        c_count+=1
    else:
        v_count+=1
print(f"vowels:{v_count}")
print(f"consonant:{c_count}")

