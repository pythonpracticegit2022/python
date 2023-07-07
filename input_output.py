"""
1. Write a program to accept two numbers from the user and calculate multiplication

2. Display three string “Name”, “Is”, “James” as “Name**Is**James” using print()

3. Accept a list of 5 float numbers as an input from the user
  Output: [78.6, 78.6, 85.3, 1.2, 3.5]

4. Write a program to take three names as input from a user in the single input() function call.

5. Write a program to use string.format() method to format the following three variables as per the expected output
    Given:

    total_money = 1000
    quantity = 3
    price = 450

    Output: I have 1000 dollars so I can buy 3 football for 450.00 dollars.
"""

# Q.1

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1*num2
print(f"Multiplication of {num1} and {num2} is {result}")

# Q.2 

s1 = "Name"
s2 = "Is"
s3 = "James"

result = s1 + "**" + s2 + "**" + s3
print(result)

# Q.3

output = [ ]
for i in range(5):
    num = float(input(f"Enter {i+1} vaule: "))
    output.append(num)
print(output)

# Q.4

str1, str2, str3 = input("Enter three names separate by comma: ").split(",")        # eg = ganesh,dinesh,mahesh

print(f"Frist name is {str1}")
print(f"Second name is {str2}")
print(f"Third name is {str3}")


# Q.5

total_money = 1000
quantity = 3
price = 450

output = "I have {total_money} dollars so I can buy {quantity} football for {price} dollars.".format(total_money=1000,quantity=3,price=float(450))
print(output)                 # I have 1000 dollars so I can buy 3 football for 450.0 dollars.