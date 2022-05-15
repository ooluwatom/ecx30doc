from random import randint


number = randint(0,50)
attempts = 0
while attempts < 5:
    attempts += 1
    attempt = int(input('Please input your guess attempt: '))
    if attempt < number:
        print('Wrong! The number is greater than', attempt)
    elif attempt > number:
        print('Wrong! The answer is less than', attempt)
    elif attempt == number:
        print(f'Congratulations! You have gotten the number ,{number} in {attempts} attempts.')
        break
else:
    print ('Sorry! You have exhausted  your attempts and have failed the challenge. The correct number is', number)