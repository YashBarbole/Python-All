n = int(input("enter number"))

temp = n
sum = 0
while n > 0:
    digit = n % 10
    sum += digit**3
    n = n // 10

if temp == sum:
    print("armstrong")
else:
    print("not armstrong")
