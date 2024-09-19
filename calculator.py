# Program Goal: Build a simple python program that can add, subtract, multiply and divide two numbers

# Functional Decompotion:
# 1. Obtain a way to grab two numbers
# 2. Obtain a way to choose either add, subtract, multiply and divide
# 3. Do the wanted calculation with the given two numbers
# 4. Output the calculation/result

print("Welcome to our calculator app!")

# 1. Create a way to grab 2 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# 2. Obtain a way to choose add/subtract/multiply/devide
choice = input("Choose either add, subtract, multiply, or devide: ")

# 3. Complete the wanted calculation
if choice == "add":
    print(num1 + num2)
elif choice == "subtract":
    print(num1 - num2)
elif choice == "multiply":
    print(num1 * num2)
elif choice == "devide":
    print(num1 / num2)