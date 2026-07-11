my_list = [1, 2, 3, 4, 5]

print(my_list)


print(my_list[-3:])
print(my_list[3:])

# what it does is
print(my_list[len(my_list) - 3 : len(my_list)])
# i want more ex here

print(my_list[len(my_list) - 1 : len(my_list)])


# total length - something and print from that to end

print(my_list[::2])


# print(my_list.append("hero"))


# lists are mutable


# print(my_list.insert(1, "good"))


print("reverseeeeeeeeeeeeeee")
# reverse lists


print(my_list[::-1])

for i in reversed(my_list):
    print(i)


my_list.reverse()
print(my_list)
# permanent

my_list.pop()
print(my_list)
# deletes last element


# list comprehension 
#hey claude add here neat ex tell whats list comprehensoin ok my bro plaese doneat
new_list = [i * i for i in my_list if (i % 2) == 0]
print(new_list)
# new_list = []
# for i in my_list:
#     new_list.append(i * i)
# print(new_list)
