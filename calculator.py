# Program Goal: Build a simple python program that can add, subtract, multiply and divide two numbers

#Program Weakness -> Can only do one calculation, then the program finishes

print("Welcome to our calculator app!")

# 1. Create a way to grab 2 numbers
#Weakness -> crashes when the user inputs non integer values, it should also handle decimal numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# 2. Obtain a way to choose add/subtract/multiply/devide
choice = input("Choose either add, subtract, multiply, or devide: ")

# 3. Complete the wanted calculation
#Weakness -> case sensitive, add in support for + sign, create a menu type user interface
if choice == "add":
    print(num1 + num2)
elif choice == "subtract":
    print(num1 - num2)
elif choice == "multiply":
    print(num1 * num2)
elif choice == "devide":
#Weakness -> can't devide by zero
    print(num1 / num2)