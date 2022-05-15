small_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def encode(password, shift_value):
    i = 0
    encoded_password = ''
    for i in range(len(password)):
        if password[i] in small_letters:
            a = small_letters.index(password[i])
            b = (a + shift_value) % 26
            encoded_password += small_letters[b]
            i += 1
        elif password[i] in capital_letters:
            a = capital_letters.index(password[i])
            b = (a + shift_value) % 26
            encoded_password += capital_letters[b]
            i += 1
    print ('The encoding, when the shift value is {} is: {}'.format(shift_value,encoded_password))

def decode(password, shift_value):
    i = 0
    decoded_password = ''
    for i in range(len(password)):
        if password[i] in small_letters:
            a = small_letters.index(password[i])
            b = (a - shift_value) % 26
            decoded_password += small_letters[b]
            i += 1
        elif password[i] in capital_letters:
            a = capital_letters.index(password[i])
            b = (a - shift_value) % 26
            decoded_password += capital_letters[b]
            i += 1
    print ('The decoding, when the shift value is {} is: {}'.format(shift_value,decoded_password))

def ceaser(password, shift_value, value):
    if value == True:
        encode(password, shift_value)
    elif value == False:
        decode(password,shift_value)

ceaser('Python',5,False)