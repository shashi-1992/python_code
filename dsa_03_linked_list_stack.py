"""
LeetCode 75-style DSA — File 3/8: Linked lists & stacks (~10 problems)
"""
from typing import List, Optional


class ListNode:
    __slots__ = ("val", "next")

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """206. Reverse Linked List."""
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    return prev


def merge_two_lists(
    a: Optional[ListNode], b: Optional[ListNode]
) -> Optional[ListNode]:
    """21. Merge Two Sorted Lists."""
    dummy = ListNode()
    t = dummy
    while a and b:
        if a.val <= b.val:
            t.next, a = a, a.next
        else:
            t.next, b = b, b.next
        t = t.next
    t.next = a or b
    return dummy.next


def has_cycle(head: Optional[ListNode]) -> bool:
    """141. Linked List Cycle — Floyd."""
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False


def reorder_list(head: Optional[ListNode]) -> None:
    """143. Reorder List — split, reverse second half, merge."""
    if not head or not head.next:
        return
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    second = slow.next
    slow.next = None
    prev, cur = None, second
    while cur:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    first, second = head, prev
    while second:
        a, b = first.next, second.next
        first.next, second.next = second, a
        first, second = a, b


def is_valid_parentheses(s: str) -> bool:
    """20. Valid Parentheses."""
    st = []
    pair = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in pair:
            if not st or st.pop() != pair[ch]:
                return False
        else:
            st.append(ch)
    return not st


def min_stack_class():
    """155. Min Stack — auxiliary stack of mins."""

    class MinStack:
        def __init__(self):
            self.st = []
            self.mins = []

        def push(self, x: int) -> None:
            self.st.append(x)
            self.mins.append(x if not self.mins else min(x, self.mins[-1]))

        def pop(self) -> None:
            self.st.pop()
            self.mins.pop()

        def top(self) -> int:
            return self.st[-1]

        def getMin(self) -> int:
            return self.mins[-1]

    return MinStack


def lru_cache_class():
    """146. LRU Cache — OrderedDict O(1) get/put."""
    from collections import OrderedDict

    class LRUCache:
        def __init__(self, capacity: int):
            self.cap = capacity
            self.od = OrderedDict()

        def get(self, key: int) -> int:
            if key not in self.od:
                return -1
            self.od.move_to_end(key)
            return self.od[key]

        def put(self, key: int, value: int) -> None:
            if key in self.od:
                self.od.move_to_end(key)
            self.od[key] = value
            if len(self.od) > self.cap:
                self.od.popitem(last=False)

    return LRUCache


def daily_temperatures(t: List[int]) -> List[int]:
    """739. Daily Temperatures — monotonic stack."""
    n = len(t)
    ans = [0] * n
    st = []
    for i in range(n - 1, -1, -1):
        while st and t[st[-1]] <= t[i]:
            st.pop()
        ans[i] = 0 if not st else st[-1] - i
        st.append(i)
    return ans


def largest_rectangle_histogram(heights: List[int]) -> int:
    """84. Largest Rectangle in Histogram."""
    st = []
    best = 0
    for i, h in enumerate(heights + [0]):
        while st and heights[st[-1]] > h:
            j = st.pop()
            w = i if not st else i - st[-1] - 1
            best = max(best, heights[j] * w)
        st.append(i)
    return best


def car_fleet(target: int, position: List[int], speed: List[int]) -> int:
    """853. Car Fleet — sort by position, stack monotonic times."""
    cars = sorted(zip(position, speed), key=lambda x: -x[0])
    fleets = 0
    cur = 0.0
    for p, s in cars:
        t = (target - p) / s
        if t > cur:
            fleets += 1
            cur = t
    return fleets
