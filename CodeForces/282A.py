# Bit++
# give soln for this problem
n = int(input())
x = 0
for y in range(n):
    s = input()  # read the next operation as a string why not used str() explicitly?
    # input() already returns a string, so there's no need to explicitly convert it using str()
    if "++" in s:
        x += 1
    else:
        x -= 1
print(x)


# what is _
# In the for loop, _ is used as a variable name when the actual value is not needed. It is a convention to indicate that the loop variable is intentionally being ignored.
# is it correct ?
