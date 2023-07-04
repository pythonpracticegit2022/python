"""
1. Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

  Output: 
          Printing current and previous number sum in a range(10)
          Current Number 0 Previous Number  0  Sum:  0
          Current Number 1 Previous Number  0  Sum:  1
          Current Number 2 Previous Number  1  Sum:  3
          Current Number 3 Previous Number  2  Sum:  5
          Current Number 4 Previous Number  3  Sum:  7
          Current Number 5 Previous Number  4  Sum:  9
          Current Number 6 Previous Number  5  Sum:  11
          Current Number 7 Previous Number  6  Sum:  13
          Current Number 8 Previous Number  7  Sum:  15
          Current Number 9 Previous Number  8  Sum:  17


2. Write a program to accept a string from the user and display characters that are present at an even index number.

        Given: I am Learning Python

        Output: 'I'
                'a'
                ' '
                'e'
                'r'
                'i'
                'g'
                'P'
                't'
                'o'


3. Check if the first and last number of a list is the same
      Given: 
      numbers_x = [10, 20, 30, 40, 10]
      numbers_y = [75, 65, 35, 75, 30]


      Output:

      Given list: [10, 20, 30, 40, 10]
      result is True
      
      numbers_y = [75, 65, 35, 75, 30]
      result is False

4. Write a program to check if the given number is a palindrome number.
   Note: A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

   Output:

    original number 121
    Yes. given number is palindrome number
    
    original number 125
    No. given number is not palindrome number
"""

# Answers
# Q. 1

list_num= list(range(10))
pre_num = 0
for num in list_num:
    current_num = num
    sum = current_num + pre_num
    print(f"Current Number {current_num} Previous Number {pre_num} Sum: {sum} ")
    pre_num = current_num

print('----------------------------------------------------------------------------')

# Q. 2

input_str = input("Enter string: ")
# list1 = list(input_str)
n = len(input_str)
for i in range(n):
    if i%2 == 0:
        print(input_str[i])
print('------------------------------------------------------------------------------')

# Q. 3

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def fun3(raw_list):
    if raw_list[0] == raw_list[-1]:
        print("result is True")
    else:
        print("result is False")

fun3(numbers_x)
fun3(numbers_y)

print('------------------------------------------------------------------------------')

# Q. 4

def check_palindrome_num(num):
    digit = 0
    rev_num = 0
    temp = num
    while temp>0:
        digit = temp % 10
        rev_num = rev_num*10 + digit
        temp = temp // 10
    if num == rev_num:
        print("It is a palindrome number")
    else:
        print("It is not a palindrome number")

check_palindrome_num(121)
check_palindrome_num(123)
