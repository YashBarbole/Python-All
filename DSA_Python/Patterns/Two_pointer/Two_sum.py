#soln for two sum:
def two_sum(arr: list[int], target: int):
    arr.sort()  # Sort the array to use the two-pointer technique
    left, right = 0, len(arr) - 1  # Initialize two pointers

    while left < right:
        current_sum = arr[left] + arr[right]  # Calculate the sum of the two pointers
        if current_sum == target:  # Check if the sum matches the target
            return [arr[left], arr[right]]  # Return the pair that sums to the target
        elif current_sum < target:  # If the sum is less than the target, move the left pointer to the right
            left += 1
        else:  # If the sum is greater than the target, move the right pointer to the left
            right -= 1

    return []  # Return an empty list if no pair is found


# two sum with duplicates in arr bu tin soln we dont want duplicate pair 
#what does this code do 

# It finds all unique pairs in the array that sum up to the target, including duplicates.
#  but we dont want duplicates make another soln that has no duplicate pairs in the result.
# now explain what does below code do           
 
def two_sum_with_duplicates(arr: list[int], target: int):
    arr.sort()  # Sort the array to use the two-pointer technique
    left, right = 0, len(arr) - 1  # Initialize two pointers
    result = []

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            result.append([arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return result
