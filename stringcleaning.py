def stringcleaner(text):
    result=''
    for character in text:
        if character.isalpha():
            result+=character.lower()
    return result

value = str(input('Enter a text: '))
cleaned = stringcleaner(value)
print(f'{value} cleaned version is: {cleaned}')