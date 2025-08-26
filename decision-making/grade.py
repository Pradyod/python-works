sub_1=int(input("enter the mark"))
sub_2=int(input("enter the mark"))
sub_3=int(input("enter the mark"))
sub_4=int(input("enter the mark"))
sub_5=int(input("enter the mark"))

result=sub_1+sub_2+sub_3+sub_4+sub_5/5

print(result)

if result>=90 and result>100:
    print("A Grade")
elif result>=70 and result==80:
    print("B Grade")
elif result>=50 and result==60:
    print("C Grade")
elif result>=30 and result==40:
    print("D Grade")
elif result>=10 and result==20:
    print("E grade")
else:
    print("fail")