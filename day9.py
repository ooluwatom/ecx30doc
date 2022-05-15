def prime_numbers(n):
    if n == 0 or n == 1:
        return '{} is not a prime number'.format(n)
    elif n == 2:
        return '{} is a prime number'.format(n)
    elif n > 2:
        if n % 2 == 0:
            return '{} is not a prime number'.format(n)
        else:
            for a in range(3,(n//2) + 1):
                if n % a == 0:
                    return '{} is not a prime number'.format(n)
            return '{} is a prime number'.format(n)
        
print(prime_numbers(197))