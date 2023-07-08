"""
1. Take two number input from user and multiply them without using * operator

2. Write a program to sum up only ones (1 digit) from following list without using "if"
    Given: [1, 0, 0, 1, 1, 1, 0, 1, 0, 1]

3. Python program to remove spaces from string without any inbuilt function
    Given: "Learning Python is a fun"
    Output: LearningPythonisafun

"""

# Q.1
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
result = 0
for i in range(num2):
    result = result + num1

print(f"Multiplication of {num1} and {num2}: {result}")


# Q.2
list1 = [1, 0, 0, 1, 1, 1, 0, 1, 0, 1]
sum = 0
for num in list1:
    sum = sum + num
print(sum)


# Q.3
str1 = "Learning Python is a fun"
result = " "
for item in str1:
    if item == " ":
        continue
    result = result +item
print(result)



