age=int(input("enter your age"))
gender=input("enter your gender")
qualification=input("enter your qualification")

if age>=18 and age<=40:
    print("you are eligible")
else:
    print("sorry, you are not eligible")

    if qualification=="Degree Graduate":
        print("you are eligible for HR position")
    elif qualification=="+2":
        print("you are eligible for the clerk position")
    else:
        print("not eligible")