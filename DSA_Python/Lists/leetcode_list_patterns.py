"""
LeetCode — Arrays / Lists Problems Grouped by Pattern
=====================================================

Each section covers one pattern. Problems are ordered Easy -> Medium -> Hard.
Every entry has: LeetCode number, title, difficulty, one-line idea, and a
reference Python solution. Use this as a study index + template bank.

Patterns covered:
    1. Sliding Window
    2. Two Pointers
    3. Kadane's Algorithm (Max Subarray / DP on arrays)
    4. Prefix Sum
    5. Binary Search on Arrays
    6. Hashing / Frequency Map
    7. Sorting + Greedy
    8. In-place / Cyclic Sort & Index tricks
"""

from collections import defaultdict, Counter
from typing import List
import heapq

# ============================================================================
# 1. SLIDING WINDOW
#    Use when: contiguous subarray/substring, "max/min/longest" with a window.
# ----------------------------------------------------------------------------
# LC 643  Maximum Average Subarray I ................. Easy
# LC 209  Minimum Size Subarray Sum .................. Medium
# LC 3    Longest Substring Without Repeating Chars .. Medium
# LC 424  Longest Repeating Char Replacement ......... Medium
# LC 567  Permutation in String ..................... Medium
# LC 76   Minimum Window Substring ................... Hard
# LC 239  Sliding Window Maximum .................... Hard
# ============================================================================


def max_average_subarray(nums: List[int], k: int) -> float:
    """LC 643 (Easy). Max average of any length-k window."""
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best / k


def min_subarray_len(target: int, nums: List[int]) -> int:
    """LC 209 (Medium). Shortest subarray with sum >= target."""
    left = 0
    total = 0
    best = float("inf")
    for right, val in enumerate(nums):
        total += val
        while total >= target:
            best = min(best, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if best == float("inf") else best


def length_of_longest_substring(s: str) -> int:
    """LC 3 (Medium). Longest substring without repeating characters."""
    seen = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)
    return best


def sliding_window_maximum(nums: List[int], k: int) -> List[int]:
    """LC 239 (Hard). Max of each window using a monotonic deque of indices."""
    from collections import deque

    dq = deque()
    out = []
    for i, val in enumerate(nums):
        while dq and nums[dq[-1]] <= val:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out


# ============================================================================
# 2. TWO POINTERS
#    Use when: sorted array, pair/triplet sums, in-place partition, palindrome.
# ----------------------------------------------------------------------------
# LC 283  Move Zeroes .............................. Easy
# LC 167  Two Sum II (sorted input) ................ Medium
# LC 15   3Sum ..................................... Medium
# LC 11   Container With Most Water ................ Medium
# LC 42   Trapping Rain Water ...................... Hard
# ============================================================================


def move_zeroes(nums: List[int]) -> None:
    """LC 283 (Easy). Move all zeroes to the end, in-place, keep order."""
    last = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last], nums[i] = nums[i], nums[last]
            last += 1


def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    """LC 167 (Medium). 1-indexed pair that sums to target in a sorted array."""
    lo, hi = 0, len(numbers) - 1
    while lo < hi:
        s = numbers[lo] + numbers[hi]
        if s == target:
            return [lo + 1, hi + 1]
        if s < target:
            lo += 1
        else:
            hi -= 1
    return []


def three_sum(nums: List[int]) -> List[List[int]]:
    """LC 15 (Medium). All unique triplets that sum to zero."""
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        lo, hi = i + 1, n - 1
        while lo < hi:
            s = nums[i] + nums[lo] + nums[hi]
            if s < 0:
                lo += 1
            elif s > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi + 1]:
                    hi -= 1
    return res


def max_area(height: List[int]) -> int:
    """LC 11 (Medium). Max water container between two lines."""
    lo, hi = 0, len(height) - 1
    best = 0
    while lo < hi:
        best = max(best, (hi - lo) * min(height[lo], height[hi]))
        if height[lo] < height[hi]:
            lo += 1
        else:
            hi -= 1
    return best


def trap(height: List[int]) -> int:
    """LC 42 (Hard). Trapped rainwater via two pointers."""
    lo, hi = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while lo < hi:
        if height[lo] < height[hi]:
            left_max = max(left_max, height[lo])
            water += left_max - height[lo]
            lo += 1
        else:
            right_max = max(right_max, height[hi])
            water += right_max - height[hi]
            hi -= 1
    return water


# ============================================================================
# 3. KADANE'S ALGORITHM  (Max Subarray / DP on arrays)
#    Use when: best contiguous sum/product, running-best decisions.
# ----------------------------------------------------------------------------
# LC 53   Maximum Subarray ......................... Medium
# LC 152  Maximum Product Subarray ................. Medium
# LC 918  Maximum Sum Circular Subarray ............ Medium
# ============================================================================


def max_sub_array(nums: List[int]) -> int:
    """LC 53 (Medium). Largest contiguous sum."""
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


def max_product(nums: List[int]) -> int:
    """LC 152 (Medium). Largest contiguous product (track min & max)."""
    best = cur_max = cur_min = nums[0]
    for x in nums[1:]:
        if x < 0:
            cur_max, cur_min = cur_min, cur_max
        cur_max = max(x, cur_max * x)
        cur_min = min(x, cur_min * x)
        best = max(best, cur_max)
    return best


def max_subarray_sum_circular(nums: List[int]) -> int:
    """LC 918 (Medium). Kadane for both normal max and 'wrap' via total - min."""
    total = 0
    cur_max = best_max = nums[0]
    cur_min = best_min = nums[0]
    for i, x in enumerate(nums):
        total += x
        if i == 0:
            continue
        cur_max = max(x, cur_max + x)
        best_max = max(best_max, cur_max)
        cur_min = min(x, cur_min + x)
        best_min = min(best_min, cur_min)
    if best_max < 0:  # all negative
        return best_max
    return max(best_max, total - best_min)


# ============================================================================
# 4. PREFIX SUM
#    Use when: many range-sum queries, subarray sum equals K, running totals.
# ----------------------------------------------------------------------------
# LC 303  Range Sum Query - Immutable .............. Easy
# LC 560  Subarray Sum Equals K .................... Medium
# LC 238  Product of Array Except Self ............. Medium
# LC 724  Find Pivot Index ......................... Easy
# ============================================================================


class NumArray:
    """LC 303 (Easy). O(1) range-sum queries with a prefix array."""

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for x in nums:
            self.prefix.append(self.prefix[-1] + x)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    """LC 560 (Medium). Count subarrays summing to k using prefix-sum counts."""
    counts = defaultdict(int)
    counts[0] = 1
    running = 0
    result = 0
    for x in nums:
        running += x
        result += counts[running - k]
        counts[running] += 1
    return result


def product_except_self(nums: List[int]) -> List[int]:
    """LC 238 (Medium). Product of all elements except self, no division."""
    n = len(nums)
    out = [1] * n
    prefix = 1
    for i in range(n):
        out[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        out[i] *= suffix
        suffix *= nums[i]
    return out


def pivot_index(nums: List[int]) -> int:
    """LC 724 (Easy). Index where left sum == right sum."""
    total = sum(nums)
    left = 0
    for i, x in enumerate(nums):
        if left == total - left - x:
            return i
        left += x
    return -1


# ============================================================================
# 5. BINARY SEARCH ON ARRAYS
#    Use when: sorted array, "find boundary", or search on the answer space.
# ----------------------------------------------------------------------------
# LC 704  Binary Search ............................ Easy
# LC 35   Search Insert Position ................... Easy
# LC 33   Search in Rotated Sorted Array ........... Medium
# LC 153  Find Minimum in Rotated Sorted Array ..... Medium
# LC 4    Median of Two Sorted Arrays .............. Hard
# ============================================================================


def binary_search(nums: List[int], target: int) -> int:
    """LC 704 (Easy). Classic binary search, returns index or -1."""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def search_rotated(nums: List[int], target: int) -> int:
    """LC 33 (Medium). Search in a rotated sorted array."""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:  # left half sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:  # right half sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


def find_min_rotated(nums: List[int]) -> int:
    """LC 153 (Medium). Minimum in a rotated sorted array."""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]


# ============================================================================
# 6. HASHING / FREQUENCY MAP
#    Use when: lookups, counting, grouping, "seen before?" checks.
# ----------------------------------------------------------------------------
# LC 1    Two Sum .................................. Easy
# LC 217  Contains Duplicate ....................... Easy
# LC 242  Valid Anagram ............................ Easy
# LC 49   Group Anagrams ........................... Medium
# LC 347  Top K Frequent Elements .................. Medium
# LC 128  Longest Consecutive Sequence ............. Medium
# ============================================================================


def two_sum(nums: List[int], target: int) -> List[int]:
    """LC 1 (Easy). Indices of two numbers adding to target."""
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []


def contains_duplicate(nums: List[int]) -> bool:
    """LC 217 (Easy). True if any value repeats."""
    return len(set(nums)) != len(nums)


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """LC 347 (Medium). K most frequent elements via a heap."""
    freq = Counter(nums)
    return [val for val, _ in heapq.nlargest(k, freq.items(), key=lambda p: p[1])]


def longest_consecutive(nums: List[int]) -> int:
    """LC 128 (Medium). Longest run of consecutive integers, O(n)."""
    num_set = set(nums)
    best = 0
    for x in num_set:
        if x - 1 not in num_set:  # only start counting at a run start
            length = 1
            while x + length in num_set:
                length += 1
            best = max(best, length)
    return best


# ============================================================================
# 7. SORTING + GREEDY
#    Use when: intervals, scheduling, "arrange to optimize" problems.
# ----------------------------------------------------------------------------
# LC 268  Missing Number ........................... Easy  (also XOR/prefix)
# LC 56   Merge Intervals .......................... Medium
# LC 57   Insert Interval .......................... Medium
# LC 435  Non-overlapping Intervals ................ Medium
# ============================================================================


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """LC 56 (Medium). Merge all overlapping intervals."""
    intervals.sort(key=lambda iv: iv[0])
    merged = []
    for start, end in intervals:
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    """LC 435 (Medium). Min removals so none overlap (greedy by end time)."""
    intervals.sort(key=lambda iv: iv[1])
    prev_end = float("-inf")
    removals = 0
    for start, end in intervals:
        if start >= prev_end:
            prev_end = end
        else:
            removals += 1
    return removals


# ============================================================================
# 8. IN-PLACE / CYCLIC SORT & INDEX TRICKS
#    Use when: values in range [1..n], find missing/duplicate in O(1) space.
# ----------------------------------------------------------------------------
# LC 448  Find All Numbers Disappeared in an Array .. Easy
# LC 41   First Missing Positive ................... Hard
# ============================================================================


def find_disappeared_numbers(nums: List[int]) -> List[int]:
    """LC 448 (Easy). Missing values in [1..n] via sign marking."""
    for x in nums:
        idx = abs(x) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]
    return [i + 1 for i, x in enumerate(nums) if x > 0]


def first_missing_positive(nums: List[int]) -> int:
    """LC 41 (Hard). Smallest missing positive using cyclic placement."""
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            target = nums[i] - 1
            nums[i], nums[target] = nums[target], nums[i]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1


# ============================================================================
# Quick self-check (run this file directly to sanity-test a few solutions).
# ============================================================================
if __name__ == "__main__":
    assert min_subarray_len(7, [2, 3, 1, 2, 4, 3]) == 2
    assert length_of_longest_substring("abcabcbb") == 3
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert subarray_sum_equals_k([1, 1, 1], 2) == 2
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6],
        [8, 10],
        [15, 18],
    ]
    assert first_missing_positive([3, 4, -1, 1]) == 2
    print("All sample checks passed.")
