def odd_evn_count(num):
    while num!=0:
        digit=num%10
        if digit%2!=0:
            odd_count+=1
        else:
            even_count+=1
    print(f"odd count: {odd_count} even count: {even_count}")

print(odd_evn_count(123))
