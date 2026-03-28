"""
LeetCode 75-style DSA — File 8/8: Bits, backtracking, trie, misc (~9 problems)
"""
from typing import List, Optional


def hamming_weight(n: int) -> int:
    """191. Number of 1 Bits (treat as 32-bit unsigned for LC parity)."""
    n &= 0xFFFFFFFF
    c = 0
    while n:
        n &= n - 1
        c += 1
    return c


def count_bits(n: int) -> List[int]:
    """338. Counting Bits — DP: i & (i-1)."""
    out = [0] * (n + 1)
    for i in range(1, n + 1):
        out[i] = out[i >> 1] + (i & 1)
    return out


def missing_number(nums: List[int]) -> int:
    """268. Missing Number — XOR."""
    x = len(nums)
    for i, v in enumerate(nums):
        x ^= i ^ v
    return x


def reverse_bits(n: int) -> int:
    """190. Reverse Bits."""
    r = 0
    for _ in range(32):
        r = (r << 1) | (n & 1)
        n >>= 1
    return r


def subsets(nums: List[int]) -> List[List[int]]:
    """78. Subsets — bitmask or DFS."""
    n = len(nums)
    out = []
    for mask in range(1 << n):
        out.append([nums[i] for i in range(n) if mask >> i & 1])
    return out


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """39. Combination Sum — backtrack."""
    res = []
    candidates.sort()

    def dfs(i, total, path):
        if total == target:
            res.append(path.copy())
            return
        if total > target or i == len(candidates):
            return
        dfs(i, total + candidates[i], path + [candidates[i]])
        dfs(i + 1, total, path)

    dfs(0, 0, [])
    return res


def permutations(nums: List[int]) -> List[List[int]]:
    """46. Permutations — swap/backtrack."""
    res = []

    def bt(start):
        if start == len(nums):
            res.append(nums.copy())
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            bt(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    bt(0)
    return res


class TrieNode:
    __slots__ = ("children", "end")

    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    """208. Implement Trie (Prefix Tree)."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        n = self.root
        for ch in word:
            if ch not in n.children:
                n.children[ch] = TrieNode()
            n = n.children[ch]
        n.end = True

    def search(self, word: str) -> bool:
        n = self.root
        for ch in word:
            if ch not in n.children:
                return False
            n = n.children[ch]
        return n.end

    def startsWith(self, prefix: str) -> bool:
        n = self.root
        for ch in prefix:
            if ch not in n.children:
                return False
            n = n.children[ch]
        return True


def word_search(board: List[List[str]], word: str) -> bool:
    """79. Word Search — DFS with backtrack."""
    R, C = len(board), len(board[0])

    def dfs(r, c, k):
        if k == len(word):
            return True
        if not (0 <= r < R and 0 <= c < C) or board[r][c] != word[k]:
            return False
        tmp, board[r][c] = board[r][c], "#"
        ok = (
            dfs(r + 1, c, k + 1)
            or dfs(r - 1, c, k + 1)
            or dfs(r, c + 1, k + 1)
            or dfs(r, c - 1, k + 1)
        )
        board[r][c] = tmp
        return ok

    for r in range(R):
        for c in range(C):
            if dfs(r, c, 0):
                return True
    return False
