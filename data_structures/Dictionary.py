# ==========================================
# PYTHON DICTIONARIES - BEGINNER NOTES
# ==========================================

# A Dictionary stores data as key : value pairs.
# It is used when you want to give names (keys) to values.

student = {
    "name": "Yash",
    "age": 22,
    "city": "Pune"
}

print("Original Dictionary:")
print(student)

# ==========================================
# ACCESS VALUES
# ==========================================

print("\n----- ACCESS VALUES -----")

print(student["name"])      # Yash
print(student["age"])       # 22

# Using get() (returns None if key doesn't exist)
print(student.get("city"))

# ==========================================
# ADD & UPDATE
# ==========================================

print("\n----- ADD & UPDATE -----")

# Add a new key-value pair
student["college"] = "AISSMS"
print(student)

# Update an existing value
student["age"] = 23
print(student)

# ==========================================
# REMOVE ITEMS
# ==========================================

print("\n----- REMOVE -----")

student.pop("city")      # Removes the key "city"
print(student)

# ==========================================
# DICTIONARY METHODS
# ==========================================

print("\n----- KEYS -----")
print(student.keys())

print("\n----- VALUES -----")
print(student.values())

print("\n----- ITEMS -----")
print(student.items())
# Returns (key, value) pairs

# ==========================================
# LOOPING THROUGH A DICTIONARY
# ==========================================

print("\n----- LOOP -----")

for key, value in student.items():
    print(key, ":", value)

# ==========================================
# CHECK IF KEY EXISTS
# ==========================================

print("\n----- MEMBERSHIP -----")

print("name" in student)     # True
print("salary" in student)   # False

# ==========================================
# IMPORTANT POINTS
# ==========================================

# 1. Dictionaries store data as key : value pairs.
# 2. Keys are unique.
# 3. Values can be duplicated.
# 4. Dictionaries are mutable (can be changed).
# 5. Access values using keys.

print("\nProgram Finished.")