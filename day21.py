def character_dictionary(sentence):
    dictionary = {}
    for letter in sentence.replace(' ', ''):
        dictionary[letter.casefold()] = dictionary.get(letter.casefold(), 0) + 1
    return dictionary

def word_dictionary(sentence):
    word_list = sentence.split()
    dictionary = {}
    for word in word_list:
        dictionary[word.casefold()] = dictionary.get(word.casefold(), 0) + 1
    return dictionary

def word_character_dictionary(statement):
    print(f'The dictionary containing all the characters is: {character_dictionary(statement)}')
    print(f'The dictionary containing all the words is: {word_dictionary(statement)}')

word_character_dictionary(str(input('Please enter your sentence:\n')))