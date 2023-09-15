"""
1. Make a decorator which calls a given function twice. You can assume the functions don't return anything important, but they may take arguments.

2.  Imagine you have a list called books, which several functions in your application interact with. Write a decorator which causes your functions to run only if books is not empty.

3. Write a decorator called printer which causes any decorated function to print their return values. If the return value of a given function is None, printer should do nothing.

4. Write a generator function that yields the cube of every other number in a given range starting from 1.
"""

# Q.1

def deco_fun(func):
    def inner(s1):
        func(s1)
        func(s1)
    return inner

@deco_fun
def greeting(str1):
    print(str1)

greeting("Good Morning!")


# Q.2

def process_book(func):
    def inner(list1):
        if list1 != []:
            func(list1)
        else:
            print("Book list is empty")
    return inner

@process_book
def display_book_list(books):
    print("Having following books")
    for book in books:
        print(book)

book1 = ["Physics","Chemistry","Math","English"]
display_book_list(book1)

book2 = []
display_book_list(book2)


# Q.4

def cube_function():
    i = 1
    while True:
        result = i**3
        yield result
        i = i + 1

cube_series = cube_function()
print(next(cube_series))
print(next(cube_series))
print(next(cube_series))
print(next(cube_series))
print(next(cube_series))