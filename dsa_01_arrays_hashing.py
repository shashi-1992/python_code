"""
LeetCode 75-style DSA — File 1/8: Arrays & Hashing (~9 problems)
"""
from collections import Counter, defaultdict
from typing import List, Optional


def two_sum(nums: List[int], target: int) -> List[int]:
    """1. Two Sum — O(n) hash map."""
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []


def contains_duplicate(nums: List[int]) -> bool:
    """217. Contains Duplicate."""
    return len(set(nums)) != len(nums)


def max_profit(prices: List[int]) -> int:
    """121. Best Time to Buy and Sell Stock."""
    lo, best = float("inf"), 0
    for p in prices:
        lo = min(lo, p)
        best = max(best, p - lo)
    return best


def max_subarray(nums: List[int]) -> int:
    """53. Maximum Subarray (Kadane)."""
    cur = best = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


def product_except_self(nums: List[int]) -> List[int]:
    """238. Product of Array Except Self."""
    n = len(nums)
    out = [1] * n
    for i in range(1, n):
        out[i] = out[i - 1] * nums[i - 1]
    r = 1
    for i in range(n - 1, -1, -1):
        out[i] *= r
        r *= nums[i]
    return out


def max_product(nums: List[int]) -> int:
    """152. Maximum Product Subarray."""
    a = b = best = nums[0]
    for x in nums[1:]:
        if x < 0:
            a, b = b, a
        a = max(x, a * x)
        b = min(x, b * x)
        best = max(best, a)
    return best


def find_min_rotated(nums: List[int]) -> int:
    """153. Find Minimum in Rotated Sorted Array."""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]


def search_rotated(nums: List[int], target: int) -> int:
    """33. Search in Rotated Sorted Array."""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


def three_sum(nums: List[int]) -> List[List[int]]:
    """15. 3Sum — sorted two pointers."""
    nums.sort()
    res, n = [], len(nums)
    for i in range(n):
        if i and nums[i] == nums[i - 1]:
            continue
        t = -nums[i]
        lo, hi = i + 1, n - 1
        while lo < hi:
            s = nums[lo] + nums[hi]
            if s < t:
                lo += 1
            elif s > t:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
    return res
