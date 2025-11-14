def prime_py(prime):

    prime = int(input('enter a no'))

    is_prime = True

    for i in range(2,prime):

        if prime%1==0:

            is_prime=False
            break

    result = "prime no" if is_prime ==True else "not prime"

    prime_py()

