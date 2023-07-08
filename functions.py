"""

1. Write a function to print multiplication table of a number given by user.
    Output:

        Enter the number of which the user wants to print the multiplication table:  13
        The Multiplication Table of:  13
        13 x 1 = 13
        13 x 2 = 26
        13 x 3 = 39
        13 x 4 = 52
        13 x 5 = 65
        13 x 6 = 78
        13 x 7 = 91
        13 x 8 = 104
        13 x 9 = 117
        13 x 10 = 130

2. Write a program to convert given list into a single string, list may contain integers.


3. Write a calculator in Python. with following requirements
    - Take two number input from user
    - Ask the operation the user want to perform with above two numbers
    - Allowed operations are - addition, subtraction, multiplication, division, square
    - Show the result of a operation to the user


4. Write a function that accepts a number and return cube of it.

"""

# Q.1

def multiplication():
    num = int(input("Enter the number of which the user wants to print the multiplication table: "))
    print(f"The Multiplication Table of: {num}")
    for i in range(1,11):
        result = num * i
        print(f"{num} * {i} = {result}")

multiplication()


# Q.2 
list1 = ['ganesh', 'dhotre', 10, 50.33]

def list_to_string(list1):
    list1 = [str(x) for x in list1]
    result = ''.join(list1)
    print(result)
    
list_to_string(list1)                # ganeshdhotre1050.33


# Q.3

def calculator():
    num1 = int(input("Enter number1: "))
    num2 = int(input("Enter number2: "))
    print("List of operations:")
    print("For add enter:1")
    print("For sub enter:2")
    print("For mul enter:3")
    print("For div enter:4")
    value = int(input("Enter operation value: "))

    def add (num1, num2):
        result = num1+num2
        print(f"Addition of {num1} and {num2} is: {result}")
    
    def sub(num1, num2):
        result = num1-num2
        print(f"Subtraction of {num1} and {num2} is: {result}")
    
    def mul(num1, num2):
        result = num1*num2
        print(f"Multiplication of {num1} and {num2} is: {result}")

    def div(num1, num2):
        if num2 == 0:
            print(f"You can not divide by zero number.")
        else:
            result = num1/num2
            print(f"Division of {num1} and {num2} is: {result}")
    
    if value == 1:
        add(num1, num2)
    elif value == 2:
        sub(num1, num2)
    elif value == 3:
        mul(num1, num2)
    elif value == 4:
        div(num1, num2)
    else:
        print("Entered value is not present in operation list")

calculator()

# Q.4

def cube(num):
    result = num**3
    print(f"Cube of {num} is:{result}")

cube(5)