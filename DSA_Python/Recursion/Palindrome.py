# using recursion to check if a string is a palindrome
def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


s = str(input("Enter a string: "))
print("Is palindrome:", is_palindrome(s, 0, len(s) - 1))

# explain
# The function is_palindrome checks if a string is a palindrome using a two-pointer approach.
# It starts with the left and right pointers at the beginning and end of the string, respectively.
# It compares the characters at these pointers. If they are not equal, it returns False.
# If they are equal, it moves the pointers towards the center (left increases, right decreases).
# The loop continues until the pointers meet or cross each other.
# If all characters match, the function returns True, indicating the string is a palindrome.
