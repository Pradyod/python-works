num1=int(input("enter num1"))
num2=int(input("enter num2"))

try:
    div_res=num1/num2
    print(div_res)
except Exception as e:

    num2=int(input("enter the num2"))

    div_res=num1/num2

    print(div_res)

finally:
    print("send text msg to uswer phn num")
    print("send email condirmation")