# extract and count digs

n = int(input("enter number"))
count = 0

while n > 0:
    last_dig = n % 10
    print(last_dig)
    n = n // 10
    count += 1

print("count of digits:", count)
