def reversefunction(sentence):
    split = sentence.split()
    new_sentence = split[::-1]
    final_sentence = ''
    for word in new_sentence:
        if new_sentence.index(word) < (len(new_sentence) - 1):
            final_sentence += word + ' '
        else:
            final_sentence += word
    final_sentence = final_sentence.replace(final_sentence[0],final_sentence[0].upper())
    print (final_sentence)

reversefunction("What time is it? Hammer time.")