sentence = input('Type in the statement:\n')
words = sentence.split()
acronym_list = []
for word in words:
    if len(word) > 1:
        acronym = ''
        for letter in word:
            if letter.isupper():
                acronym += letter
        if len(acronym) > 1:
            acronym_list.append(acronym)
print(acronym_list)