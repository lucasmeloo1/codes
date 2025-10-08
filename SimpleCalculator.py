import math

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    num1 = input('Enter a number: ')
    if not is_number(num1):
        print("Let's start again. Please enter a valid number!")
        continue

    num2 = input('Enter another number: ')
    if not is_number(num2):
        print("Let's start again. Please enter a valid number!")
        continue

    num1 = float(num1)
    num2 = float(num2)

    operation = input('Select the operation:\n[ +  -  *  / ]\n')

    if operation == "+":
        print(f'The result is: {add(num1, num2)}')
    elif operation == "-":
        print(f'The result is: {subtract(num1, num2)}')
    elif operation == "*":
        print(f'The result is: {multiply(num1, num2)}')
    elif operation == "/":
        if num2 == 0:
            print("You can't divide by zero!")
        else:
            print(f'The result is: {divide(num1, num2)}')
    else:
        print('Invalid operation!')

    again = input('Do you want to calculate again? (y/n): ').lower()
    if again != "y":
        break
