def anagram1(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        for character in word1:
            if word1.count(character) != word2.count(character):
                return False
            return True

def anagram2(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        list_word1 = sorted(word1)
        list_word2 = sorted(word2)
        for i, character in enumerate(list_word1):
            if list_word2[i] != character:
                return False
        return True
word1 = str(input('Enter the word: '))
word2 = str(input('Enter the second word: '))
anagram_check = anagram2(word1, word2)
print(f'Is {word1},{word2} anagram? {anagram_check}')