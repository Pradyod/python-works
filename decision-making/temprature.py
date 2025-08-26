temp=int(input("enter the temprature in celsius"))

if temp<10:
    print("cold")
elif temp<=20:
    print("cool")
elif temp<=25:
    print("pleasant")
elif temp<=30:
    print("warm")
elif temp<=35:
    print("hot")
else:
    print("very hot")