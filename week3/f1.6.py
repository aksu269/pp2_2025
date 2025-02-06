def reverse(sentence):
    new_sentence = ''
    i = len(sentence) - 1
    while i >= 0:
        word = ''
        if sentence[i] == ' ':
            i -= 1
            continue
        while sentence[i] != ' ' and i >= 0:
            word += sentence[i]
            i -= 1
        i -= 1
        new_sentence += word[::-1]
        new_sentence += ' '
    return new_sentence
print(reverse("My  name is Aksu"))