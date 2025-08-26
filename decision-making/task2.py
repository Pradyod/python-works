#:read three numbers num1,num2,num3 display largest amount three number

num1=int(input("enter the first no"))

num2=int(input("enter the second no"))

num3=int(input("enter the third no"))


if num1>num2:
    print(num1,"is the largest")
    
elif num2>num3:
    print(num2,"is the largest")
    
else:
    print(num3,"is the largest")