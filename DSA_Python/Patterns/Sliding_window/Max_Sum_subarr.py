# maximum sum of subarray
# given an arr, max sum of any subarr of size k.


# here its fixed size sliding window problem



def maxsubarr(arr, k):
    n = len(arr)
    if n < k:
        return "Wrong input"
    max_sum = sum(arr[:k])  # sum of the first 'k' elements, initial window sum
    window_sum = max_sum

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    return max_sum


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # example array
# example subarray size
print(maxsubarr(arr, 30))



# tc sc
# Time Complexity: O(n) where n is the number of elements in the array
# Space Complexity: O(1) as we are using a fixed amount of extra space


#now solve this using 2 pointers
def maxsubarr_two_ptr(arr,k):
    l=0
    h=k-1
    n=len(arr)
    if n < k:
        return "Wrong input"
    sum=0
    res=sum
   
    for i in range(l,h+1):
        sum=sum+arr[i]

    while(h<n-1):  #why n-1 tell us that the last valid window ends at index n-1
        res=max(res,sum)
        h+=1
        l+=1
        sum=sum-arr[l-1]+arr[h]

    return res




#which is better and why
# Both approaches have the same time complexity O(n) and space complexity O(1).
# The first approach using a fixed-size sliding window is more concise and easier to understand.
# The two-pointer approach is slightly more verbose but achieves the same result.