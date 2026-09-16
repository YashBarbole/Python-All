# triplet sum zero
# here we have to use 2sum many times ?
# when sum == target we store the triplet


def triplet_sum_zero(arr: list[int]):
    arr.sort()
    res = []

    # for each i we want  to run 2sum wiht sum= - arr[i]
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        left = i + 1  # why import left?
        right = len(arr) - 1
        sum = -1 * arr[i]

        while left < right:
            s = arr[left] + arr[right]
            if s == sum:
                res.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            elif s < sum:
                left += 1
            else:
                right -= 1
    return res
