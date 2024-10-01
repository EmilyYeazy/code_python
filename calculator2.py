print("Welcome to our calculator app!")
#Defining a function by our self
def numericInput(prompt):
    #capital True
    while True:
        value = input(prompt)
#Float allows decimal inputs
        try:
            value = float(value)
            return value
        except:
            print(f"{value} cannot be converted into a floating point.")
# end of numericInput()

def menu():
    menu = """
Calculator Menu Options:
    1. Add (+)
    2. Subtract (-)
    3. Multiply (*)
    4. Divide (/)
    5. Exit Program (exit)

"""
    while True:
        print(menu)
        user_choice = input("User's Choice: ").lower()
        # .lower() puts the result of input() to all lowercase
        if user_choice in {'add', '1', '+'}:
            return 1
        elif user_choice in {'subtract', '2', '-'}:
            return 2
        elif user_choice in {'multiply', '3', '*'}:
            return 3
        elif user_choice in {'divide', '4', '/'}:
            return 4
        elif user_choice in {'exit', '5'}:
            return 5
        else:
            print(f"{user_choice} is not a menu option!")
    #end of menu

menu_result = menu()

#Our Main Part of Our Program starts underneath this line

while True:
#Tab to indent multiple line
    #Display Menu First
    menu_result = menu() #Choose one of the operations

    #Get numeric input Second
    num1 = numericInput("Enter the first number: ")
    num2 = numericInput("Enter the second number: ")

    answer = 0

    if menu_result == 1:
        #Addition handling
        answer = num1 + num2
        print(f"{num1} + {num2} = {answer}")
    elif menu_result == 2:
        #Subtraction handling
        answer = num1 - num2
        print(f"{num1} - {num2} = {answer}")
    elif menu_result == 3:
        #Multiplication handling
        answer = num1 * num2
        print(f"{num1} * {num2} = {answer}")
    elif menu_result == 4:
        #Division handling
        try:
            answer = num1 / num2
            print(f"{num1} / {num2} = {answer}")
        except ZeroDivisionError:
            print(f"You cannot divide by zero! Please try different number.")
    elif menu_result == 5:
        print("Thank you for using our calculator.")
        #Exit the infinite Loop
        break