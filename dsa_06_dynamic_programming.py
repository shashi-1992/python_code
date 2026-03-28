"""
LeetCode 75-style DSA — File 6/8: Dynamic programming (~9 problems)
"""
from typing import List


def climb_stairs(n: int) -> int:
    """70. Climbing Stairs."""
    a = b = 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def coin_change(coins: List[int], amount: int) -> int:
    """322. Coin Change — unbounded knapsack."""
    dp = [0] + [amount + 1] * amount
    for x in range(1, amount + 1):
        for c in coins:
            if c <= x:
                dp[x] = min(dp[x], dp[x - c] + 1)
    return dp[amount] if dp[amount] <= amount else -1


def longest_increasing_subsequence(nums: List[int]) -> int:
    """300. Longest Increasing Subsequence — patience / binary search."""
    tails = []
    for x in nums:
        lo, hi = 0, len(tails)
        while lo < hi:
            mid = (lo + hi) // 2
            if tails[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        if lo == len(tails):
            tails.append(x)
        else:
            tails[lo] = x
    return len(tails)


def longest_common_subsequence(a: str, b: str) -> int:
    """1143. Longest Common Subsequence."""
    m, n = len(a), len(b)
    dp = [0] * (n + 1)
    for i in range(1, m + 1):
        prev = 0
        for j in range(1, n + 1):
            tmp = dp[j]
            if a[i - 1] == b[j - 1]:
                dp[j] = prev + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            prev = tmp
    return dp[n]


def word_break(s: str, wordDict: List[str]) -> bool:
    """139. Word Break."""
    words = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]


def combination_sum_iv(nums: List[int], target: int) -> int:
    """377. Combination Sum IV — order matters (count compositions)."""
    dp = [0] * (target + 1)
    dp[0] = 1
    for x in range(1, target + 1):
        for c in nums:
            if c <= x:
                dp[x] += dp[x - c]
    return dp[target]


def house_robber(nums: List[int]) -> int:
    """198. House Robber."""
    prev2 = prev1 = 0
    for x in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + x)
    return prev1


def house_robber_ii(nums: List[int]) -> int:
    """213. House Robber II — circular: max(rob 0..n-2, rob 1..n-1)."""

    def linear(arr):
        a = b = 0
        for x in arr:
            a, b = b, max(b, a + x)
        return b

    if len(nums) == 1:
        return nums[0]
    return max(linear(nums[:-1]), linear(nums[1:]))


def unique_paths(m: int, n: int) -> int:
    """62. Unique Paths — combinatorics C(m+n-2, m-1)."""
    from math import comb

    return comb(m + n - 2, m - 1)
