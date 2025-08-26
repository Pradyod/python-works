text=input("enter the text").casefold()
vowels="aeiou"

v_count=0
c_count=0

for ch in text:
    if ch in vowels:
        v_count+=1
    elif ch.isalpha():
        c_count+=1

print("no of vowels:",v_count)
print("no of consonants:",c_count)

