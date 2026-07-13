# ==========================================
# PYTHON LISTS - QUICK NOTES
# ==========================================

# List = Ordered, Mutable (can change), Allows duplicates

my_list = [1, 2, 3, 4, 5]

print("Original:", my_list)

# ------------------------------------------
# SLICING
# list[start:end:step]
# start -> included
# end   -> excluded
# ------------------------------------------

print(my_list[:])      # Entire list
print(my_list[:3])     # First 3 elements
print(my_list[2:])     # From index 2 to end
print(my_list[-3:])    # Last 3 elements
print(my_list[::2])    # Every 2nd element
print(my_list[::-1])   # Reverse list

# Same as [-3:]
print(my_list[len(my_list)-3 : len(my_list)])

# ------------------------------------------
# LIST METHODS
# ------------------------------------------

my_list.append(6)      # Add at end
print(my_list)

my_list.insert(1, 100) # Insert at index
print(my_list)

my_list.remove(100)    # Remove by value
print(my_list)

my_list.pop()          # Remove last element
print(my_list)

my_list.reverse()      # Permanent reverse
print(my_list)

# ------------------------------------------
# LIST COMPREHENSION
# Short way to create a new list
# Syntax:
# [expression for item in iterable if condition]
# ------------------------------------------

numbers = [1, 2, 3, 4, 5]

# Squares of even numbers
new_list = [i*i for i in numbers if i % 2 == 0]
print(new_list)

# Same using for loop
result = []
for i in numbers:
    if i % 2 == 0:
        result.append(i*i)

print(result)

# More examples
print([i*2 for i in numbers])          # Double numbers
print([i for i in numbers if i > 2])   # Numbers > 2
print([str(i) for i in numbers])       # Convert to strings

# ------------------------------------------
# Important Points
# ------------------------------------------

# ✔ Ordered
# ✔ Mutable
# ✔ Allows duplicates
# ✔ Supports indexing & slicing
# ✔ append() -> Add
# ✔ insert() -> Insert
# ✔ remove() -> Remove by value
# ✔ pop() -> Remove by index (default last)
# ✔ reverse() -> Reverse permanently