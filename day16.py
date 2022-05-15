def romanNumeral(number):
    Romannumeral = ''
    while number > 0:
        if number >= 1000:
            N = number // 1000
            Romannumeral += N * 'M'
            number = number % 1000
        elif number >= 900:
            Romannumeral += 'CM'
            number = number % 100
        elif number >= 500:
            N = (number - 500) // 100
            Romannumeral += 'D' + N * 'C'
            number = number % 100
        elif number >= 400:
            Romannumeral += 'CD'
            number = number % 100
        elif number >= 100:
            N = number //100
            Romannumeral += N * 'C'
            number = number % 100
        elif number >= 90:
            Romannumeral += 'XC'
            number = number % 10
        elif number >= 50:
            N = (number - 50) // 10
            Romannumeral += 'L' + N * 'X'
            number = number % 10
        elif number >= 40:
            Romannumeral += 'XL'
            number = number % 10
        elif number >= 10:
            N = number //10
            Romannumeral += N * 'X'
            number = number % 10
        elif number == 9:
            Romannumeral += 'IX'
            number = number % 1
        elif number > 5:
            N = number - 5
            Romannumeral += 'V' + N * 'I'
            number = number % 1
        elif number == 4:
            Romannumeral += 'IV'
            number = number % 1
        elif number >= 1:
            N = number / 1
            Romannumeral += N * 'I'
    print (f'{integer} in Roman Numerals is {Romannumeral}')
integer = int(input('Input the integer: '))
romanNumeral(integer)