"""
LeetCode 75-style DSA — File 7/8: Heaps, intervals, greedy (~9 problems)
"""
import heapq
from typing import List, Optional


class ListNode:
    __slots__ = ("val", "next")

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def find_median_stream():
    """295. Find Median from Data Stream — two heaps."""
    small = []
    large = []

    def addNum(x: int) -> None:
        if len(small) == len(large):
            heapq.heappush(large, -heapq.heappushpop(small, -x))
        else:
            heapq.heappush(small, -heapq.heappushpop(large, x))

    def findMedian() -> float:
        if len(small) == len(large):
            return (large[0] - small[0]) / 2
        return float(large[0])

    return addNum, findMedian


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """347. Top K Frequent Elements — bucket or heap."""
    from collections import Counter

    cnt = Counter(nums)
    return [x for x, _ in heapq.nlargest(k, cnt.items(), key=lambda p: p[1])]


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """23. Merge k Sorted Lists — min-heap by (val, list_index)."""
    dummy = cur = ListNode()
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    while heap:
        _, i, node = heapq.heappop(heap)
        cur.next = node
        cur = cur.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next


def insert_interval(
    intervals: List[List[int]], new: List[int]
) -> List[List[int]]:
    """57. Insert Interval."""
    out = []
    i, n = 0, len(intervals)
    ns, ne = new
    while i < n and intervals[i][1] < ns:
        out.append(intervals[i])
        i += 1
    while i < n and intervals[i][0] <= ne:
        ns = min(ns, intervals[i][0])
        ne = max(ne, intervals[i][1])
        i += 1
    out.append([ns, ne])
    out.extend(intervals[i:])
    return out


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """56. Merge Intervals."""
    intervals.sort(key=lambda x: x[0])
    out = []
    for s, e in intervals:
        if not out or s > out[-1][1]:
            out.append([s, e])
        else:
            out[-1][1] = max(out[-1][1], e)
    return out


def non_overlapping_intervals(intervals: List[List[int]]) -> int:
    """435. Non-overlapping Intervals — greedy by end time."""
    intervals.sort(key=lambda x: x[1])
    end, cnt = float("-inf"), 0
    for s, e in intervals:
        if s >= end:
            end = e
        else:
            cnt += 1
    return cnt


def meeting_rooms_ii(intervals: List[List[int]]) -> int:
    """253. Meeting Rooms II — sweep line."""
    ev = []
    for s, e in intervals:
        ev.append((s, 1))
        ev.append((e, -1))
    ev.sort()
    cur = best = 0
    for _, d in ev:
        cur += d
        best = max(best, cur)
    return best


def jump_game(nums: List[int]) -> bool:
    """55. Jump Game — greedy reach."""
    reach = 0
    for i, x in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + x)
    return True


def jump_game_ii(nums: List[int]) -> int:
    """45. Jump Game II — BFS layers / greedy."""
    if len(nums) <= 1:
        return 0
    jumps = end = farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == end:
            jumps += 1
            end = farthest
    return jumps
