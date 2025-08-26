text=input("enter text")
vowel="aeiouAEIOU"
v_count=0

for ch in text:
    if ch in vowel:
        v_count+=1
print("no of vowels in the sentence:",v_count)
