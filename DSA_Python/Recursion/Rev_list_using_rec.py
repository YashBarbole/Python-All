# rev list by recurison
def rev(nums, left, right):
    if left >= right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    rev(nums, left + 1, right - 1)


nums = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    nums.append(int(input(f"Enter element : ")))

print("Original list:", nums)
rev(nums, 0, n - 1)
print("Reversed list:", nums)

# tc O(n)
# sc O(n)

# best ways to rev list?
# 1. Using recursion (as implemented above)
# 2. Using list slicing: nums[::-1]
# 3. Using the reverse() method: nums.reverse()
# 4. Using a for loop to swap elements manually.
# 5. Using the reversed() function: list(reversed(nums))
# Note: The recursion method is not the most efficient in terms
# of space complexity due to the call stack.
# Example usage:
# nums = [1, 2, 3, 4, 5]
# rev(nums, 0, len(nums) - 1)
# print(nums)  # Output: [5, 4, 3, 2, 1]
