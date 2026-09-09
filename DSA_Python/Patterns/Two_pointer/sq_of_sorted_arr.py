#square of sorted arr 
 
from typing import List

#bruteforce
#first square and then sort
def sortedSquares_brute(nums: List[int]) -> List[int]:
    return sorted(x ** 2 for x in nums)
#tc s: O(nlogn), sc: O(n)
#what is sorted
# The 'sorted' function takes an iterable and returns a new list containing all items from the iterable in ascending order. In this case, it sorts the squared numbers.
#why not sort()
# The 'sort()' method sorts a list in place and returns None. Since we are using a generator expression, we cannot call 'sort()' directly on it. 'sorted()' works because it takes any iterable and returns a new sorted list.


#we need O(n) solution

# we can understand that all the squares of negative elements in list are in des cending order, and all the squares of non-negative elements are in ascending order. 
# Therefore, we can use a two-pointer approach to merge them into a single sorted list.
# like we can split them in the list into negative and non-negative parts and then merge their squares.
#we can rev the squares of negative elements to make them in ascending order and then merge with the non-negative squares.
# then que becomes merge of two sorted lists using two pointers approach.

def sortedsq(nums:List[int]):

    a=[]
    b=[]

    for i in range (len(nums)):
        if nums[i]>0:
            b.append(nums[i] ** 2)
        else:
            a.append(nums[i] ** 2)

    a.reverse()  # reverse the squares of negative elements to make them ascending

    # merge two sorted lists a and b
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:]) # append any remaining elements from a tell what is i: the current index in a after merging
    result.extend(b[j:]) # append any remaining elements from b
    return result

#tc: O(n), sc: O(n)
#how good is this method
# This method is efficient because it only requires a single pass through the array to separate and merge the squares, resulting in O(n) time complexity. It also uses O(n) extra space for the result array.

