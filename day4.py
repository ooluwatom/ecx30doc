def dec_to_hex (number):
    x = number
    hex_value = ''
    while (x > 0):
        digit = x % 16
        if digit == 10:
            digit = 'a'
        elif digit == 11:
            digit = 'b'
        elif digit == 12:
            digit = 'c'
        elif digit == 13:
            digit = 'd'
        elif digit == 14:
            digit = 'e'
        elif digit == 15:
            digit = 'f'
        hex_value = str(digit) + hex_value
        x = x // 16
    return ''.join(hex_value)

print(dec_to_hex(547834))