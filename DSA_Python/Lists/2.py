# when we create list it creates dynamic array in the background
# revision of lists


brands = ["Nike", "Adidas", "Puma", "Reebok"]

print(brands[2])

print(len(brands))

brands.append("Under Armour")
print(brands)
# append at last

brands.remove("Puma")
print(brands)
# it iterates through the list to find the element to remove
# tc O(n)


brands.insert(1, "New Balance")
print(brands)
# insert at given pos
# it shifts the elements to the right from the given position


brands.pop()
print(brands)
# remove last element

brands.clear()
print(brands)

# etc etc these are list methods
# all of these are O(1) on average, except for remove() and insert() which are O(n) in the worst case.


# for iterating
# use  for loop
for brand in brands:
    print(brand)
# use  while loop
i = 0
while i < len(brands):
    print(brands[i])
    i += 1

# list comprehension

# create a list of first n numbers

l = []
for i in range(10):
    l.append(i)

# list comp

li = [p for p in range(10)]
li2 = [5] * 10


li = [(i, j) for i in range(5) for j in range(5) if i < j]
print(li)

li3 = [[i for i in range(5)] for j in range(5)]
print(li3)
