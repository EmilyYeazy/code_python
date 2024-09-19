# Goal: To create a password generator
# Requires password length
# Requires password criteria
# Does it contain uppercase characters?
# Does it include numbers?
# Does it include special characters?
# Generate a password the given constraints
# Output the generated password

import random

#Program introduction
print("Welcome to password generating app!")

# Set password length
pwd_length = int(input("Enter the password length: "))

#Password criteria
lowercase = list(range(1,10))
uppercase = list(range(65,91)) #Range never include the last value
digits = list(range(48,58))
special = list(range(33,48)) + list(range(58,65)) + list(range(91,97)) + list(range(123,127))

pwd_symbols = lowercase.copy() #List of possible character for our password

has_upper = input("Include uppercase characters?(y/n): ")
if has_upper == 'y' or has_upper == 'Y':
    pwd_symbols.extend(uppercase)
    #pwd_symbols = pwd_symbols + uppercase

has_special = input("Include special characters?(y/n): ")
if has_special == 'y' or has_special == 'Y':
    pwd_symbols.extend(special)
    #pwd_symbols = pwd_symbols + special

has_digits = input("Include digits?(y/n): ")
if has_digits == 'y' or has_digits == 'Y':
    pwd_symbols.extend(digits)
    #pwd_symbols = pwd_symbols + digits

new_password = "" #Empty string to hold new password

while len(new_password)!=pwd_length:
    random_symbol = chr(random.choice(pwd_symbols))
    new_password = new_password + random_symbol
#end of while loop

print(f"{new_password} has been generated.")