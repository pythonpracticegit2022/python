# Assignment 1

"""
1. Calculate the length of the string.
    Input: "ABCDFGH"
    Output: 7
    
2. Create a string made of the first, middle and last character. Write a program to create a new string made of an input string’s first, middle, and last character.
    Input: "James"
    Output: "Jms"
    
    
3. Create a string made of the middle three characters. Write a program to create a new string made of the middle three characters of an input string.
    Input: "JhonDipPeta"
    Output: "Dip"


4. Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
    Input:
    s1 = "Ault"
    s2 = "Kelly"
    
    Output: "AuKellylt"


5. Create a new string made of the first, middle, and last characters of each input string. Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
    Input:
    s1 = "America"
    s2 = "Japan"
    
    Expected Output:
    AJrpan

6. Arrange string characters such that lowercase letters should come first. Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
    Input: IamLearningPython
    Output: amearningpthonILP

7. Count all letters, digits, and special symbols from a given string
    Input: "I@#am26at^&i5ve"

    Output:
    Total counts of chars, digits, and symbols 

    Chars = 8 
    Digits = 3 
    Symbol = 4

8. Find all occurrences of a substring in a given string by ignoring the case. Write a program to find all occurrences of “USA” in a given string ignoring the case.
    Input:  "Welcome to USA. usa awesome, isn't it?"
    Output: The USA count is: 2

9. Reverse a given string
    Input: "IamLearningPython"
    Output: "nohtyPgninraeLmaI"
    
10. Find the last position of a given substring. Write a program to find the last position of a substring “Emma” in a given string.
    Input: "Emma is a data scientist who knows Python. Emma works at google."
    Output: Last occurrence of Emma starts at index 43
"""


# Q.1
str1 = "ABCDFGH"
length = len(str1)
print(length)            #7


# Q.2
str1 = "James"
new_str = str1[0]+str1[len(str1)//2]+str1[-1]
print(new_str)           #Jms


# Q.3
str1 = "JhonDipPeta"
middle_index = len(str1)//2
new_str = str1[middle_index-1]+str1[middle_index]+str1[middle_index+1]
print(new_str)           #Dip


# Q.4
s1 = "Ault"
s2 = "Kelly"
n = len(s1)//2
print(n)
s3 = s1[0:n]+s2+s1[n:]
print(s3)                #AuKellylt


# Q.5
s1 = "America"
s2 = "Japan"
n1 = len(s1)//2
n2 = len(s2)//2
new_str = s1[0]+s2[0]+s1[n1]+s2[n2]+s1[-1]+s2[-1]
print(new_str)            #AJrpan


# Q.6
str1 = "IamLearningPython"
low_str = ""
upper_str = ""
for item in str1:
    if item.isupper():
        upper_str = upper_str + item
    else:
        low_str = low_str + item
new_str = low_str+upper_str
print(new_str)            #amearningythonILP


# Q.7
str1 = "I@#am26at^&i5ve"
chars = ""
digit = ""
symbol = ""
for item in str1:
    if item.isalpha():
        chars = chars + item
    elif item.isnumeric():
        digit = digit + item
    else:
        symbol = symbol + item
print(f"Chars = {len(chars)}")
print(f"Digit = {len(digit)}")
print(f"Symbol = {len(symbol)}")


# Q.8
str1 = "Welcome to USA. usa awesome, isn't it?"
result = (str1.lower()).count('usa')
print(result)


# Q.9
str1 = "IamLearningPython"
result = str1[::-1]
print(result)              # "nohtyPgninraeLmaI"


# Q.10
str1 = "Emma is a data scientist who knows Python. Emma works at google."
result = str1.rindex('Emma')
print(f"Last occurrence of Emma starts at index {result}")          #Last occurrence of Emma starts at index 43

