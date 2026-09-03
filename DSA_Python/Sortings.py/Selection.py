# selection sort notes
# Selection sort is an in-place comparison sorting algorithm.
# It divides the input list into two parts: the sublist of items already sorted, which is built up from left to right at the front (left) of the list, and the sublist of items remaining to be sorted that occupy the rest of the list.
# Initially, the sorted sublist is empty, and the unsorted sublist is the entire input list.
# The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element from the unsorted sublist, swapping it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.

# Time complexity: O(n^2) for all cases (best, average, worst)
# Space complexity: O(1) (in-place sorting)

# sorts on elemetn in one pass through the unsorted sublist

# The process is repeated for each position in the list until the entire list is sorted.


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


# descending order
def selection_sort_descending(arr):
    n = len(arr)

    for i in range(n):
        max = i
        for j in range(i + 1, n):
            if arr[j] > arr[max]:
                max = j
        arr[i], arr[max] = arr[max], arr[i]
    return arr


nums = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    nums.append(int(input(f"Enter element {i+1}: ")))

selection_sort(nums)
print("Sorted list:", nums)
selection_sort_descending(nums)
print("Sorted list in descending order:", nums)
