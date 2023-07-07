"""
1. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    
    Output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}



2. Merge two Python dictionaries into one
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    
    Output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}



3. Print the value of key ‘history’ from the below dict
    sample_dict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }



4. Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

    Given dictionary:
    
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"}
    
    # Keys to extract
    keys = ["name", "salary"]
    
    Output: {'name': 'Kelly', 'salary': 8000}


5. Delete a list of keys from a dictionary
    Given:
    
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    
    # Keys to remove
    keys = ["name", "salary"]
    Expected output:
    
    {'city': 'New york', 'age': 25}


6. Write a Python program to check if value 200 exists in the following dictionary.
    
    Given:
    
    sample_dict = {'a': 100, 'b': 200, 'c': 300}
    Expected output:
    
    200 present in a dict


7. Change value of a key in a nested dictionary
    Write a Python program to change Brad’s salary to 8500 in the following dictionary.
    
    Given:
    
    sample_dict = {
        'emp1': {'name': 'Jhon', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 500}
    }
    
"""

# Q.1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

output = dict(zip(keys, values))

print(output)                    # {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
print('-'*130)

# Q.2

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

output = {**dict1, **dict2}

print(output)               # {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
print('-'*130)

# Q.3 

sample_dict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }

output = sample_dict['class']['student']['marks']['history']
print(output)                   # 80
print('-'*130)

# Q.4

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
# Keys to extract
keys = ["name", "salary"]
output = {}
for key, value in sample_dict.items():
    if key == 'name':
        output[key] = value
    elif key == 'salary':
        output[key] = value
print(output)               # {'name': 'Kelly', 'salary': 8000}
print('-'*130)


# Q.5

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]
for key in keys:
    if key == 'name' or key == 'salary':
        sample_dict.pop(key)
print(sample_dict)                       # {'age': 25, 'city': 'New york'}
print('-'*130)

# Q.6

sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print("200 is present in dict")     # 200 is present in dict
print('-'*130)


# Q.7


sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3']['salary']=8500

print(sample_dict)                   #{'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000}, 'emp3': {'name': 'Brad', 'salary': 8500}}
print('-'*130)