"""
PYTHON BASICS — PERSONAL REVISION NOTES
========================================
Python is:
  - cross-platform (runs on Windows, macOS, Linux)
  - high-level (close to human language, abstracts away memory management)
  - interpreted (runs via the Python interpreter, no separate compile step)

Run this file with:  python python_basics_notes.py
"""

# ------------------------------------------------------------------
# 1. VARIABLES
# ------------------------------------------------------------------
# A variable is just a label pointing to a value stored in memory.
# You don't declare a type — Python figures it out at runtime.

students = 1000
print(students)

unit_price = 3
x = 1


# ------------------------------------------------------------------
# 2. PRIMITIVE DATA TYPES: booleans, numbers, strings
# ------------------------------------------------------------------

is_published = True          # boolean
price = 9.99                 # float
count = 10                    # int

# Triple-quoted string -> can span multiple lines
msg = """i am yashi
i am cool
okkkk"""

print(len(msg))    # total number of characters (including newlines)
print(msg[0])      # first character -> 'i'
print(msg[-1])     # last character (negative index counts from the end)

# STRING SLICING -> string[start:stop]  (stop is NOT included)
print(msg[0:3])    # first 3 characters
print(msg[0:])     # from index 0 to the end
print(msg[:10])    # from the start up to (not including) index 10
print(msg[:])      # the whole string (a copy)


# ------------------------------------------------------------------
# 3. STRING CONCATENATION vs FORMATTED STRINGS (f-strings)
# ------------------------------------------------------------------

first = "yash"
last = "barbole"

full = first + " " + last          # manual concatenation (need the space!)
full2 = f"{first} {last}"          # f-string — cleaner and preferred

print(full)
print(full2)


# ------------------------------------------------------------------
# 4. STRING METHODS
# ------------------------------------------------------------------

course = "    python programming"

print(course.upper())      # PYTHON PROGRAMMING
print(course.title())      # Python Programming (title case)
print(course.strip())      # removes leading/trailing whitespace
print(course.lower())      # all lowercase
print(course.replace("python", "java"))   # replace substring
print(course.find("pro"))                 # index of first match, -1 if not found
# there are many more: .split(), .join(), .startswith(), .endswith(), .count(), etc.


# ------------------------------------------------------------------
# 5. WORKING WITH NUMBERS & TYPE CONVERSION
# ------------------------------------------------------------------
# input() always returns a string, so convert it before doing math.

x_input = input("x: ")
y = int(x_input) + 1
print(f"x:{x_input}, y:{y}")

# Other conversions:
# float("3.14"), str(42), bool(0), int("101", base=2)


# ------------------------------------------------------------------
# 6. COMPARISON OPERATORS
# ------------------------------------------------------------------
# ==  equal to            !=  not equal to
# >   greater than        <   less than
# >=  greater or equal    <=  less or equal
print(5 == 5, 5 != 3, 5 > 3, 5 < 3, 5 >= 5, 5 <= 4)


# ------------------------------------------------------------------
# 7. LOGICAL OPERATORS
# ------------------------------------------------------------------
# and  -> True only if BOTH sides are True
# or   -> True if AT LEAST ONE side is True
# not  -> flips True/False
has_high_income = True
has_good_credit = False
print(has_high_income and has_good_credit)   # False
print(has_high_income or has_good_credit)    # True
print(not has_high_income)                   # False


# ------------------------------------------------------------------
# 8. CONDITIONAL STATEMENTS (if / elif / else)
# ------------------------------------------------------------------

age = 22
if age >= 18:
    print("eligible")
else:
    print("not eligible")
print("done")

# elif example
temperature = 35
if temperature > 30:
    print("hot")
elif temperature > 20:
    print("warm")
else:
    print("cold")


# ------------------------------------------------------------------
# 9. TERNARY OPERATOR (one-line if/else)
# ------------------------------------------------------------------

age = 90
msg = "eligible" if age >= 18 else "not eligible"
print(msg)


# ------------------------------------------------------------------
# 10. LOOPS
# ------------------------------------------------------------------

# for loop -> repeats a fixed/known number of times, or over a sequence
for number in range(3):        # 0, 1, 2
    print("attempt", number)

for char in "abc":              # looping over a string
    print("char:", char)

# while loop -> repeats while a condition stays True
count = 0
while count < 3:
    print("while count:", count)
    count += 1                   # don't forget to update, or it loops forever!

# loop control keywords
for number in range(5):
    if number == 2:
        continue                # skip this iteration
    if number == 4:
        break                    # exit the loop entirely
    print("controlled loop:", number)


# ------------------------------------------------------------------
# 11. FUNCTIONS
# ------------------------------------------------------------------
# Two broad types:
#   a) functions that just PERFORM A TASK (no return value -> returns None)
#   b) functions that RETURN A VALUE (use it in further calculations)

def greet():
    """Performs a task (prints something), returns nothing useful."""
    print("hello boii")


def greet_person(name):
    """Same idea, but takes a parameter."""
    print(f"hello {name}")


def square(number):
    """Returns a value the caller can use."""
    return number ** 2


greet()
greet_person("Yash")

result = square(5)
print("square:", result)

# Function with a default parameter value
def power(base, exponent=2):
    return base ** exponent

print(power(3))        # uses default exponent=2 -> 9
print(power(3, 3))      # overrides default -> 27


# ------------------------------------------------------------------
# NEXT TOPICS TO ADD LATER (for future revision passes):
# - Lists, tuples, dictionaries, sets
# - *args and **kwargs
# - List comprehensions
# - Exception handling (try/except)
# - Classes & OOP basics
# - Modules & imports
# ------------------------------------------------------------------