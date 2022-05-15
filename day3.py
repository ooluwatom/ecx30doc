def palindrome(number):
    palindrome_list = []
    for x in range(number):
        reverse = 0
        num = x
        while (num>0):
            digit = num%10
            reverse = reverse * 10 + digit
            num = num//10
        if x == reverse:
            palindrome_list.append(x)
    return ('The palindromes less than {} are: {} and the total number is {}'.format(number,palindrome_list,len(palindrome_list)))
        
print(palindrome(3467))