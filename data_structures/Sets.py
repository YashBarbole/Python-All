# ==========================================
# PYTHON SETS - BEGINNER NOTES
# ==========================================

# A Set is an unordered collection of unique elements.
# Duplicate values are automatically removed.
# Sets are mainly used for:
# 1. Removing duplicates
# 2. Fast searching
# 3. Mathematical set operations (Union, Intersection, Difference)

my_set = {1, 2, 3, 4, 4, 4, 4}
set1 = {3, 4, 5, 6}

print("Original Set:")
print(my_set)          # {1, 2, 3, 4}

# ==========================================
# ADD & REMOVE
# ==========================================

print("\n----- ADD -----")

my_set.add(10)
print(my_set)

print("\n----- REMOVE -----")

my_set.remove(10)      # Error if element doesn't exist
print(my_set)

# discard() doesn't give an error if element isn't found
my_set.discard(100)

# ==========================================
# MATHEMATICAL OPERATIONS
# ==========================================

print("\n----- UNION -----")

# Combines both sets (no duplicates)
print(my_set.union(set1))
# Output: {1, 2, 3, 4, 5, 6}

print("\n----- INTERSECTION -----")

# Common elements
print(my_set.intersection(set1))
# Output: {3, 4}

print("\n----- DIFFERENCE -----")

# Elements present only in my_set
print(my_set.difference(set1))
# Output: {1, 2}

print("\n----- SYMMETRIC DIFFERENCE -----")

# Elements present in either set but not both
print(my_set.symmetric_difference(set1))
# Output: {1, 2, 5, 6}

# ==========================================
# CHECKING ELEMENTS
# ==========================================

print("\n----- MEMBERSHIP -----")

print(3 in my_set)     # True
print(10 in my_set)    # False

# ==========================================
# IMPORTANT POINTS
# ==========================================

# 1. Sets are unordered.
# 2. Duplicate values are not allowed.
# 3. Indexing is NOT possible.
# 4. Sets are mutable (can add/remove elements).
# 5. Very useful for mathematical operations.
# 6. Membership checking (in) is very fast.

print("\nProgram Finished.")