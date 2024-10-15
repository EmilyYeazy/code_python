def consonant(word):
    counter = 0
    for character in word:
        character = character.lower()
        if character.isalpha() and character in {'a','e','i','o','u'}:
            counter+=1
    return counter
text = str(input('Enter the word: '))
consonant_count = consonant(text)
print(f'{text} has {consonant_count} consonants.')