# store freq in dictionary
n = int(input("enter numbers of elements"))
nums = []

for i in range(n):
    nums.append(int(input("enter element")))
freq = {}
for n in nums:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1
print(freq)


print("freq of 1:", freq.get(1))
