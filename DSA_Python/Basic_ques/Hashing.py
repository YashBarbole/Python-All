# hashing in python
# In Python, hashing is typically implemented using dictionaries and sets.
# A hash function maps data to a fixed-size value, which is used to quickly compare dictionary keys or set elements.
# Dictionaries use hash values to store and retrieve key-value pairs efficiently.
# Sets use hash values to store unique elements efficiently.

# we will check 2 lists n and m and see how many times elements of m are present in n using hashing
n = [1, 2, 3, 4, 5, 1, 2, 1]
m = [1, 2, 1, 6]

hash_list = [0] * 11
for num in n:
    hash_list[num] += 1
for num in m:
    if num < 1 or num > 10:
        print("out of range")
    else:
        print(num, "->", hash_list[num])


# tc -> time complexity
# The time complexity of this approach is O(n + m), where n is the length of list n and m is the length of list m.
# The space complexity is O(k), where k is the range of numbers (in this case, 11).


# using dictionary
hash_dict = {}
for num in n:
    if num in hash_dict:
        hash_dict[num] += 1
    else:
        hash_dict[num] = 1
for num in m:
    if num in hash_dict:
        print(num, "->", hash_dict[num])
    else:
        print(num, "->", 0)
