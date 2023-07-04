# 1.print "Hello, World"
print("Hello, World")

# 2. write a addition program for two numbers
def addition(x,y):
    result = x+y
    return result

print(addition(2,3))

# 3. find square root of the given number
def square_root(num):
    result = num**(1/2)
    return result

print(square_root(16))

# 4. area of triangle

def area_of_triangle(a,b,c):
    # a = float(a)
    # b = float(b)
    # c = float(c)
    s=(a+b+c)/2
    result = (s*(s-a)*(s-b)*(s-c))**0.5
    return result
print(area_of_triangle(7,6,5))

# 5 kilometer to mile
def kilometer_to_mile(distance):
    result = distance*0.6214
    return result

print(kilometer_to_mile(10))
