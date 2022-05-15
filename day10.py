ussd = input('Enter your USSD code:\n')
password = '3986'
balance = 469384
if ussd != '*957#':
    print ('Invalid Ussd code.')
else:
    first_response = input('Welcome to BrightStar Bank. Please perform one of the following operations:\n1. Check Balance\n2. Send money\n3. Transfer Airtime\n')
    if first_response == '1':
        second_response = input('Please provide your transaction password:\n')
        if second_response == password:
            print('Your current balance is:\n$',balance)
        else:
            print('WRONG PASSWORD. Goodbye!')
    elif first_response == '2':
        second_response = input('Select bank:\n1. Zenith Bank\n2. GTB\n3. First Bank\n4. UBA\n5. Sterling Bank\n6. Access Bank\n')
        second_responses = ['1','2','3','4','5','6']
        if second_response not in second_responses:
            print('Invalid Response')
        else:
            third_response = input('Enter Account Number:\n')
            if len(third_response) != 10:
                print ('Invalid Response')
            else:
                fourth_response = input('Enter Amount to send:\n')
                if int(fourth_response) <= balance:
                    fifth_response = input('To send {} to {}\nPlease provide your transaction password:\n'.format(fourth_response, third_response))
                    if fifth_response == password:
                        print('Money sent!')
                        balance -= int(fifth_response)
                        sixth_response = input('Will you like to see your balance? Y/N:\n')
                        if sixth_response == 'Y':
                            seventh_response = input('Please provide your transaction password:\n')
                            if seventh_response == password:
                                print('Your current balance is:\n$',balance)
                            else:
                                print('WRONG PASSWORD. Goodbye!')
                        elif sixth_response == 'N':
                            print('Goodbye')
                    else:
                        print('Wrong Password. Goodbye')
                else:
                    print('Balance Insufficient. Goodbye')
    elif first_response == '3':
        second_response = input('Select network:\n1. 9mobile\n2. Airtel\n3. Glo\n4. MTN\n')
        second_responses = ['1','2','3','4']
        if second_response not in second_responses:
            print('Invalid Response')
        else:
            third_response = input('Enter Phone Number in format 0*0********:\n')
            if len(third_response) != 11:
                print ('Invalid Response')
            else:
                fourth_response = input('Enter Airtime Amount:\n')
                if int(fourth_response) <= balance:
                    fifth_response = input('To send {} to {}\nPlease provide your transaction password:\n'.format(fourth_response, third_response))
                    if fifth_response == password:
                        print('Airtime sent!')
                        balance -= int(fifth_response)
                        sixth_response = input('Will you like to see your balance? Y/N:\n')
                        if sixth_response == 'Y':
                            seventh_response = input('Please provide your transaction password:\n')
                            if seventh_response == password:
                                print('Your current balance is:\n$',balance)
                            else:
                                print('WRONG PASSWORD. Goodbye!')
                        elif sixth_response == 'N':
                            print('Goodbye')
                    else:
                        print('Wrong Password. Goodbye')
                else:
                    print('Balance Insufficient. Goodbye')
    else:
        print('Invalid Input')
