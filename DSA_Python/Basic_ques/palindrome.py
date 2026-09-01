n = int(input("enter number"))

temp = n

rev = 0
while n > 0:
    last = n % 10
    rev = rev * 10 + last
    n = n // 10

if temp == rev:
    print("palindrome")
else:
    print("not palindrome")
