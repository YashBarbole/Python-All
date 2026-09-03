from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    res = [0] * len(nums)
    l = 0
    r = len(nums) - 1

    pos = len(nums) - 1

    while l <= r:
        if nums[l] ** 2 > nums[r] ** 2:
            res[pos] = nums[l] ** 2
            l += 1
        else:
            res[pos] = nums[r] ** 2
            r -= 1
        pos -= 1
    return res


print(sortedSquares([-4, -1, 0, 3, 10]))  # whats is none
# The 'None' is passed as the 'self' parameter because the function is defined as a method with 'self', but we are calling it as a standalone function. In practice, you would remove 'self' from the function definition if you intend to call it like this.
# whats self
# 'self' is a reference to the instance of the class in which the method is defined. It is used to access instance variables and other methods within the class. In this standalone function call, 'self' is not needed, which is why 'None' is passed.
# easily explain
# In simple terms, 'self' is used when a function is part of a class to refer to the object itself. Since we are calling the function directly without a class, we pass 'None' for 'self'. In practice, you would remove 'self' from the function definition if you want to call it like a normal function.
# why its standalone func
# It is called a standalone function here because we are not defining it inside a class. If it were inside a class, we would need to create an instance of the class and call the method on that instance, passing 'self' automatically. By defining it outside of a class, we can call it directly without needing 'self'.
#
