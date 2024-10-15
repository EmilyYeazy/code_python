#palindrome problem: a word that is same forwards and backwards ex. tacocat
def isPalindrome(word : str) -> bool:
    # def isPalindrome(word):
    # Base case -> Empty string are indeed palindromes
    if not word: # if len(word) == 0:
        return True
    # Base case #2 -> a single character is a palindrome
    elif len(word) == 1:
        return True
    # Base case #3 -> string with 2 or 3 characters
    elif len(word) <= 3:
        return word[0] == word[-1]
    else:
        # Solution 2: reverse the word into a separate variable
        # flipped = word[::-1]
        # return flipped==word
        # Solution 3: traverse forward and backward
        i = 0
        j = len(word)-1
        while i < j:
            if word[i] != word[j]:
                return False
            i+=1
            j-=1
        return True
word=str(input('Enter the word to check palindrome: '))
ans=isPalindrome(word)
print(f'{word} is a palindrome? {ans}')