from random import randint

target= randint(1,10)

count=0

while True:
    num=int(input("guess the no"))
    
    if num==target:
        print("you guessed right!")
        break

    if num!=target:
        print("you guessed wrong!")
    count+=1

print(f"total attempt:{count}")