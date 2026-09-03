# find largest element in list


nums = list(
    map(int, input("Enter the elements of the list separated by spaces: ").split())
)  # explain that this line takes input from the user, splits it by spaces, converts each element to an integer, and stores them in a list called nums.

largest = nums[0]
for num in nums:
    if num > largest:
        largest = num
print("The largest element in the list is:", largest)
