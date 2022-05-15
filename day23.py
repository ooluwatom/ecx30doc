def Erasothenes(n):
    prime_numbers = list(range(2,n))
    for p in prime_numbers:
        m_list = list(range(2,(n//2) + 1))
        new_list = [(p * m) for m in m_list]
        for number in new_list:
            if number in prime_numbers:
                prime_numbers.remove(number)
            else:
                continue       
    return f'The prime numbers before {n} are: {prime_numbers}'

print(Erasothenes(100000))