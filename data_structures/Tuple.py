# ==========================================
# PYTHON TUPLES - BEGINNER NOTES
# ==========================================

# A Tuple is an ordered collection of items.
# Unlike lists, tuples are immutable (cannot be changed).

my_tuple = (1, 2, 3, 4, 5)

print("Original Tuple:")
print(my_tuple)

# ==========================================
# ACCESSING ELEMENTS
# ==========================================

print("\n----- ACCESS ELEMENTS -----")

print(my_tuple[0])     # First element
print(my_tuple[-1])    # Last element
print(my_tuple[1:4])   # Slicing

# ==========================================
# TUPLES ARE IMMUTABLE
# ==========================================

# This will give an error:
# my_tuple[0] = 100

# Tuples cannot be modified directly.

# ==========================================
# CONVERT TUPLE -> LIST
# ==========================================

print("\n----- TUPLE TO LIST -----")

my_list = list(my_tuple)
print(my_list)

# Now we can modify it
my_list.append(6)
my_list[0] = 100

print(my_list)

# ==========================================
# CONVERT LIST -> TUPLE
# ==========================================

print("\n----- LIST TO TUPLE -----")

new_tuple = tuple(my_list)
print(new_tuple)

# ==========================================
# USEFUL METHODS
# ==========================================

print("\n----- METHODS -----")

numbers = (1, 2, 2, 3, 4, 2)

print(numbers.count(2))   # How many times 2 appears
print(numbers.index(3))   # Index of value 3

# ==========================================
# IMPORTANT POINTS
# ==========================================

# 1. Tuples are ordered.
# 2. Tuples are immutable (cannot be changed).
# 3. Duplicate values are allowed.
# 4. Faster than lists.
# 5. Used when data should not change.

print("\nProgram Finished.")