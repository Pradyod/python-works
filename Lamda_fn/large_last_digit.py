large_last_digit=lambda n1,n2: n1 if n1%10>n2%10 else n2

print(large_last_digit(124,178))