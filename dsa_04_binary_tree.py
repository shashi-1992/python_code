"""
LeetCode 75-style DSA — File 4/8: Binary trees (~10 problems)
"""
from collections import deque
from typing import List, Optional


class TreeNode:
    __slots__ = ("val", "left", "right")

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """226. Invert Binary Tree."""
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root


def max_depth(root: Optional[TreeNode]) -> int:
    """104. Maximum Depth of Binary Tree."""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    """543. Diameter of Binary Tree."""
    best = 0

    def depth(n):
        nonlocal best
        if not n:
            return 0
        L, R = depth(n.left), depth(n.right)
        best = max(best, L + R)
        return 1 + max(L, R)

    depth(root)
    return best


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """100. Same Tree."""
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


def is_subtree(root: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
    """572. Subtree of Another Tree."""

    def same(a, b):
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return same(a.left, b.left) and same(a.right, b.right)

    if not root:
        return False
    return same(root, sub) or is_subtree(root.left, sub) or is_subtree(
        root.right, sub
    )


def lowest_common_ancestor(
    root: TreeNode, p: TreeNode, q: TreeNode
) -> TreeNode:
    """235. LCA of BST."""
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """102. Binary Tree Level Order Traversal."""
    if not root:
        return []
    q, out = deque([root]), []
    while q:
        row = []
        for _ in range(len(q)):
            n = q.popleft()
            row.append(n.val)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        out.append(row)
    return out


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """98. Validate BST — bounds."""

    def dfs(n, lo, hi):
        if not n:
            return True
        if not (lo < n.val < hi):
            return False
        return dfs(n.left, lo, n.val) and dfs(n.right, n.val, hi)

    return dfs(root, float("-inf"), float("inf"))


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    """230. Kth Smallest Element in a BST — inorder."""
    st, n = [], root
    while st or n:
        while n:
            st.append(n)
            n = n.left
        n = st.pop()
        k -= 1
        if k == 0:
            return n.val
        n = n.right
    return -1


def build_tree_pre_in(pre: List[int], ino: List[int]) -> Optional[TreeNode]:
    """105. Construct Binary Tree from Preorder and Inorder."""
    idx = {v: i for i, v in enumerate(ino)}
    pi = 0

    def build(lo, hi):
        nonlocal pi
        if lo > hi:
            return None
        v = pre[pi]
        pi += 1
        i = idx[v]
        node = TreeNode(v)
        node.left = build(lo, i - 1)
        node.right = build(i + 1, hi)
        return node

    return build(0, len(ino) - 1)
