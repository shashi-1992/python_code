"""
LeetCode 75-style DSA — File 2/8: Two pointers & sliding window (~10 problems)
"""
from collections import Counter, defaultdict
from typing import List, Optional


def max_area(height: List[int]) -> int:
    """11. Container With Most Water."""
    lo, hi, best = 0, len(height) - 1, 0
    while lo < hi:
        best = max(best, min(height[lo], height[hi]) * (hi - lo))
        if height[lo] < height[hi]:
            lo += 1
        else:
            hi -= 1
    return best


def trap_rain_water(height: List[int]) -> int:
    """42. Trapping Rain Water."""
    if not height:
        return 0
    lo, hi = 0, len(height) - 1
    lm = rm = water = 0
    while lo <= hi:
        if height[lo] < height[hi]:
            if height[lo] >= lm:
                lm = height[lo]
            else:
                water += lm - height[lo]
            lo += 1
        else:
            if height[hi] >= rm:
                rm = height[hi]
            else:
                water += rm - height[hi]
            hi -= 1
    return water


def longest_substring_k_distinct(s: str, k: int) -> int:
    """340. Longest Substring with At Most K Distinct Characters (variant)."""
    if k == 0:
        return 0
    cnt = defaultdict(int)
    lo = best = 0
    for hi, ch in enumerate(s):
        cnt[ch] += 1
        while len(cnt) > k:
            cnt[s[lo]] -= 1
            if cnt[s[lo]] == 0:
                del cnt[s[lo]]
            lo += 1
        best = max(best, hi - lo + 1)
    return best


def length_longest_substring(s: str) -> int:
    """3. Longest Substring Without Repeating Characters."""
    last = {}
    lo = best = 0
    for hi, ch in enumerate(s):
        if ch in last and last[ch] >= lo:
            lo = last[ch] + 1
        last[ch] = hi
        best = max(best, hi - lo + 1)
    return best


def min_window_substring(s: str, t: str) -> str:
    """76. Minimum Window Substring."""
    need = Counter(t)
    missing = len(t)
    lo = 0
    start, length = 0, float("inf")
    for hi, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:
            if hi - lo + 1 < length:
                start, length = lo, hi - lo + 1
            need[s[lo]] += 1
            if need[s[lo]] > 0:
                missing += 1
            lo += 1
    return "" if length == float("inf") else s[start : start + length]


def is_palindrome(s: str) -> bool:
    """125. Valid Palindrome (alnum only)."""
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


class _ListNode:
    __slots__ = ("val", "next")

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: Optional[_ListNode], n: int) -> Optional[_ListNode]:
    """19. Remove Nth Node From End of List — dummy + fast/slow."""
    dummy = _ListNode(0, head)
    fast = slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast, slow = fast.next, slow.next
    slow.next = slow.next.next
    return dummy.next


def sort_colors(nums: List[int]) -> None:
    """75. Sort Colors — Dutch national flag."""
    lo = mid = 0
    hi = len(nums) - 1
    while mid <= hi:
        if nums[mid] == 0:
            nums[lo], nums[mid] = nums[mid], nums[lo]
            lo += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[hi] = nums[hi], nums[mid]
            hi -= 1


def merge_sorted(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """88. Merge Sorted Array — fill from end."""
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1


def move_zeroes(nums: List[int]) -> None:
    """283. Move Zeroes."""
    w = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[w], nums[r] = nums[r], nums[w]
            w += 1
