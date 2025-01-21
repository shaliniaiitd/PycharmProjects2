from logging import raiseExceptions

v1 = 10
v3 = v1
v1 = 20
v3 = 30
print(v3)
print(v1)

# some_string = "Python"
# a, b, c, d = some_string   # ValueError: too many values to unpack (expected 4)

names_ages = [['John', 35], ['Jill', 38], ['Tim', 27]]
# covert to dictionary

print(dict(names_ages))

if None:
          print('Hi')

# Mutable objects are passed by reference,and so any update done to them inside the function
# reflects outside the function also;  unless the object is reassigned a value in function
# (because then the object points to a different memory than the calling reference)

list1 = [1,2,3,4]
def func1(list1):
    list1[2]=5
    print(list1)

func1(list1)
print(list1)

#Use recursion to define a function to arrange a list in descending order

#fibnacci

def fib(n):
    result = [0]
    if n==0:
        return result
    result.append(1)
    if n==1:
        return result
    for i in range(3,n+1):
        num = fib(i-1)[-1] + fib(i-2)[-1]
        result.append(num)
    return result


print(fib(10))

#Define a decorator that does error checking for area, perimeter and diameter function
from math import pi

def print_dec(func):
    def inner_func(*args):
        print("Here is the result:")
        return func(*args)
    return inner_func

def error_checker(func):

    def inner_func(*args):
        for arg in args:
            if arg < 0:
                raise ValueError("dimension should be positive")
        return func(*args)
    return inner_func


@print_dec
@error_checker
def area(r):
    return print(f"area = {pi*(r^2)}")
@print_dec
@error_checker
def perimeter(r):
    return print(f"perimeter = {2*pi*r}")
@print_dec
@error_checker
def area_rect(l,b):
    return print(f"area of rectangle= {l*b}")

area(1)
# perimeter(1)
# area_rect(2,3)

#Chaining decorators
# decorator closer to func def. is executed first and then outside one
# @print_dec
# @error_checker
# def area(r):
#     return print(f"area = {pi*(r^2)}")
# is equivalent to print_dec(error_checker(area(r))), which has the following code:
'''def area_with_decorators(*args):
    # Inner function of print_dec
    print("Here is the result:")
    # Call the inner function of error_checker
    for arg in args:
        if arg < 0:
            raise ValueError("dimension should be positive")
    return area_original(*args)  # This is the original area function
    '''
# So correct order in this case would be
#@error_checker
#@print_dec
#def area(r)
x="World"
a,b,c,d,_ = x       #valid
print(a,b,c)





