def capitalize_first_letter(sentence):
    words = sentence.split()
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    last_word = words[-1]
    if last_word[-1].isalpha():
        last_word = last_word[:-1] + last_word[-1].upper()
        words[-1] = last_word
    return ' '.join(words)

input_sentence = input("Enter a sentence: ")
capitalized_sentence = capitalize_first_letter(input_sentence)
print(capitalized_sentence)
