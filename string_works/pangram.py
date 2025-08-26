txt=input("enter text").casefold()

alphabet="abcdefghijklmnopqrstvuwxyz"

is_pangram=True

for ch in alphabet:
    if ch not in txt:
        is_pangram=False
print(is_pangram)