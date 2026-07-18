# ==========================================
# PYTHON FUNCTIONS - COMPLETE BEGINNER NOTES
# ==========================================

# Function:
# A function is a reusable block of code that performs a specific task.

# Advantages:
# 1. Reusability
# 2. Cleaner code
# 3. Easy debugging
# 4. Better readability

# ------------------------------------------
# ABSTRACTION
# ------------------------------------------
# Abstraction means hiding the implementation.
# Example: We use print() but don't know how it is internally written.

print("Hello")

# ------------------------------------------
# DECOMPOSITION
# ------------------------------------------
# Breaking a large problem into smaller functions.

# Example:
# login()
# validate_user()
# send_email()
# Each function does one small task.

# ==========================================
# SIMPLE FUNCTION
# ==========================================

def is_even(i):
    """
    Returns True if number is even.
    Returns False if odd.
    Returns 'bad value' if input is not integer.
    """

    if type(i) == int:
        return i % 2 == 0
    else:
        return "bad value"


print(is_even(10))
print(is_even(7))
print(is_even("hello"))

# ------------------------------------------
# PARAMETERS vs ARGUMENTS
# ------------------------------------------

# Parameter -> Variable in function definition
# Argument  -> Actual value passed while calling

def greet(name):          # name -> Parameter
    print("Hello", name)

greet("Yash")             # "Yash" -> Argument

# ==========================================
# DEFAULT ARGUMENTS
# ==========================================

def power(a=1, b=1):
    return a ** b

print(power())        # 1^1
print(power(2))       # 2^1
print(power(2, 3))    # 2^3

# ==========================================
# KEYWORD ARGUMENTS
# ==========================================

# Order doesn't matter.

print(power(b=2, a=5))

# ==========================================
# *args
# ==========================================

# *args allows us to pass any number of values.
# Python stores them inside a tuple.

def multiply(*args):

    print(args)        # tuple

    product = 1

    for i in args:
        product *= i

    return product


print(multiply(1,2,3))
print(multiply(1,2,3,4,5))

# ==========================================
# **kwargs
# ==========================================

# **kwargs allows us to pass any number
# of keyword arguments.
#
# Python stores them inside a dictionary.

def display(**kwargs):

    print(kwargs)      # dictionary

    for key, value in kwargs.items():
        print(key, "->", value)


display(country="India",
        capital="Delhi",
        currency="Rupee")

# ==========================================
# DOCSTRING
# ==========================================

# Docstring explains what a function does.

print(is_even.__doc__)

# ==========================================
# FUNCTION MEMORY EXECUTION
# ==========================================

# Every time a function is called,
# Python creates a new memory space (Stack Frame).

def square(x):

    result = x * x

    return result


print(square(5))

# Internally:
#
# square(5)
#
# x = 5
# result = 25
# return 25
#
# After returning,
# x and result are removed from memory.

# ==========================================
# VARIABLE SCOPE
# ==========================================

# Global Variable
x = 100

def demo():

    # Local Variable
    y = 50

    print("Inside Function")
    print(x)      # Can access global
    print(y)

demo()

print(x)

# print(y)
# Error
# Local variables exist only inside the function.

# ==========================================
# FIRST CLASS CITIZENS
# ==========================================

# In Python, functions behave like variables.

def greet():
    print("Hello")

# Store function in another variable
a = greet

a()

# Pass function as argument

def execute(func):
    func()

execute(greet)

# ==========================================
# LAMBDA FUNCTION
# ==========================================

# Small anonymous function.

square = lambda x: x*x

print(square(5))

add = lambda a,b: a+b

print(add(10,20))

# ==========================================
# MAP
# ==========================================

# Applies a function to every element.

numbers = [1,2,3,4]

result = list(map(lambda x: x*x, numbers))

print(result)

# Output:
# [1,4,9,16]

# ==========================================
# FILTER
# ==========================================

# Keeps only elements satisfying condition.

numbers = [1,2,3,4,5,6]

even = list(filter(lambda x: x%2==0, numbers))

print(even)

# Output:
# [2,4,6]

# ==========================================
# REDUCE
# ==========================================

from functools import reduce

# Combines all elements into one value.

numbers = [1,2,3,4]

total = reduce(lambda a,b: a+b, numbers)

print(total)

# Output:
# 10

# ==========================================
# IMPORTANT INTERVIEW POINTS
# ==========================================

# Function -> Reusable block of code.
# Parameter -> Variable in function definition.
# Argument -> Actual value passed.
# Default arguments -> Have default value.
# Keyword arguments -> Passed using name=value.
# *args -> Tuple of positional arguments.
# **kwargs -> Dictionary of keyword arguments.
# Docstring -> Explains function.
# Local variable -> Exists inside function.
# Global variable -> Exists outside function.
# Lambda -> Anonymous one-line function.
# map() -> Transform every element.
# filter() -> Keep elements matching condition.
# reduce() -> Reduce all values to one.

print("\nProgram Finished.")