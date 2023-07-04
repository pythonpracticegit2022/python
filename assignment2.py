# 1. Write a program to create a new string made of an input string’s first, middle, and last character.

input_str = "Omkar"

first_char = input_str[0]
n = len(input_str)//2
print(n)
middle_char = input_str[n]
last_char = input_str[-1]

new_str = first_char + middle_char + last_char
print(new_str)

# 2 Write a program to create a new string made of the middle three characters of an input string.

input_str = "Omkar"
length_str = len(input_str)
n = length_str//2
new_str = input_str[n-1:n+2]
print(new_str)

# 3 Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
s1 = "Ganesh"
s2 = "Car"
n = len(s1)//2
s1 = s1[:n]+s2+s1[n:]
print(s1)

# 4  Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle,
# and last characters.
s1 = "sandeep"
s2 = "Akash"
n1 = len(s1)//2
n2 = len(s2)//2
s3 = s1[0]+s1[n1]+s1[-1]+s2[0]+s2[n2]+s2[-1]
print(s3)

# 5 Write a program to find all occurrences of “USA” in a given string ignoring the case.
s1 = "I am going to USA.USA stands for United Sate of America.USA currency is dollar."
s2 = s1.lower()
result = s2.count("usa")
print(result)

# 6 Reverse a given string

s1 = "Ganesh"
rev_str = s1[::-1]
print(rev_str)

# 6 Write a program to find the last position of a substring “Emma” in a given string
s1 = "Emma is clever girl.Emma likes to play cricket also.If Emma sad, she listen music.Emma"
print(len(s1))
n = s1.count("Emma")
print(n)


result = (s1.index("Emma"))<(s1.index("Emma"))<(s1.index("Emma"))
print(result)





