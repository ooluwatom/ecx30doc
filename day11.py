def gcd(number1,number2):
    if number1 > number2:
        a = number1
        b = number2
    else:
        a = number2
        b = number1
    while (b > 0):
        c = a % b
        a = b
        b = c
    return('The Greatest Common Divisor of {} and {} is: {}'.format(number1,number2,a))

print(gcd(462,1071))