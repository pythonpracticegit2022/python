"""
1. Reverse a given list in Python
    list1 = [100, 200, 300, 400, 500]
    output - [500, 400, 300, 200, 100]
    
2. Turn every item of a list into its square. Given a list of numbers. write a program to turn every item of a list into its square.
    numbers = [1, 2, 3, 4, 5, 6, 7]
    Output - [1, 4, 9, 16, 25, 36, 49]
    
3. Remove empty strings from the list of strings
    list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    
    
4. Add a new item to the list after a specified item. Write a program to add item 7000 after 6000 in the following Python List
    Input
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    Expected output: [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
    
    
5. Extend the nested list by adding the sublist. You have given a nested list. Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.
    Input:
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

    # Input
    sub_list = ["h", "i", "j"]
    
    Expected Output:
    ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
    
    
6. Replace list’s item with new value if found. You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.

    Input:
    list1 = [5, 10, 15, 20, 25, 50, 20]
    
    Expected output:
    [5, 10, 15, 200, 25, 50, 20]
    
    
7. Remove all occurrences of a specific item from a list. Given a Python list, write a program to remove all occurrences of item 20.

    Given:
    list1 = [5, 20, 15, 20, 25, 50, 20]
    
    Expected output:
    [5, 15, 25, 50]

8. Calculate the length of a given list
    Input: [x for x in range(50)]
    Output: 50
    
9. Create a list of all even numbers between 1 and 100 using list comprehension.

10. Concatenate two lists index-wise. Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

    Input:
    list1 = ["M", "na", "i", "Ke"]
    list2 = ["y", "me", "s", "lly"]
    
    Output:
    ['My', 'name', 'is', 'Kelly']

11. Write a program to sum all the elements of a list.
   
    Input: [2,3,2,4,7,8]
    
    Output:
    Sum of list items 26

12. Write a program to get the maximum number from a list.
    Input = [2,3,2,4,7,8]
    
    Output:
    Max number in list items is 8

13. Write a program to append data of the second list to the first list.
    Input: 
    list1 = [23, 24, 25, 26] 
    list2 = [27, 28, 29, 30]
    
    Output:
    [23, 24, 25, 26, 27, 28, 29, 30]

14. Write a program in Python to filter odd and even number from a list.
    Input: [2, 23, 24, 51, 46, 67]
    
    Output:
    Even [2, 24, 46] 
    Odd [23, 51, 67]
"""

# Q.1
list1 = [100, 200, 300, 400, 500]
output = list1[::-1]
print(output)                   # [500, 400, 300, 200, 100]

# Q.2
numbers = [1, 2, 3, 4, 5, 6, 7]
output = [num*num for num in numbers]
print(output)                   #[1, 4, 9, 16, 25, 36, 49]

# Q.3
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
for item in list1:
    if item == "":
        list1.remove(item)
print(list1)

# Q.4
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)                   #[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

# Q.5
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list1[2][1][2].extend(["h","i","j"])
print(list1)                   #['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

# Q.6
list1 = [5, 10, 15, 20, 25, 50, 20]
n = len(list1)
for i in range(n):
    if list1[i] == 20:
        list1[i] = 200
        break
print(list1)                   #[5, 10, 15, 200, 25, 50, 20]

# Q.7
list1 = [5, 20, 15, 20, 25, 50, 20]
for num in list1:
    if num == 20:
        list1.remove(num)
print(list1)                   #[5, 15, 25, 50]

# Q.8
list1 = [x for x in range(50)]
length = len(list1)
print(length)

# Q.9
list1 = [x for x in range(1,100) if x%2==0]
print(list1)

# Q.10
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = []
n = len(list1)
for i in range(n):
    list3.append(list1[i]+list2[i])
print(list3)                      #['My', 'name', 'is', 'Kelly']

# Q.11
list1 = [2,3,2,4,7,8]
sum = 0
for num in list1:
    sum = sum + num
print(f"Sum of list items {sum}")

# Q.12
list1 = [2,3,2,4,7,8]
max = list1[0]
for num in list1:
    if num>max:
        max = num
print(f"Max number in list items is {max}")

# Q.13
list1 = [23, 24, 25, 26] 
list2 = [27, 28, 29, 30]
list1.extend(list2)
print(list1)                     #[23, 24, 25, 26, 27, 28, 29, 30]

# Q.14
list1 = [2, 23, 24, 51, 46, 67]
even = []
odd = []
for item in list1:
    if item % 2 ==0:
        even.append(item)
    else:
        odd.append(item)
print(f"Even list: {even}")      #Even list: [2, 24, 46]
print(f"Odd list: {odd}")        #Odd list: [23, 51, 67]