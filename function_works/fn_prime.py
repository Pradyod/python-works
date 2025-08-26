def prime_py(prime):

    if prime%1==0 and prime%prime==0:
        return f"{prime} is a prime no"
    else:
        return f"{prime} is not prime no"

print(prime_py(9))