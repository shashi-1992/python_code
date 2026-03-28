"""
LeetCode 75-style DSA — File 5/8: Graphs (~9 problems)
"""
from collections import defaultdict, deque
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    """200. Number of Islands — DFS."""
    if not grid:
        return 0
    R, C = len(grid), len(grid[0])
    seen = set()

    def dfs(r, c):
        if not (0 <= r < R and 0 <= c < C) or grid[r][c] != "1" or (r, c) in seen:
            return
        seen.add((r, c))
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc)

    cnt = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "1" and (r, c) not in seen:
                dfs(r, c)
                cnt += 1
    return cnt


def clone_graph(node):
    """133. Clone Graph — BFS/DFS with map."""
    if not node:
        return None
    old2new = {}

    def dfs(n):
        if n in old2new:
            return old2new[n]
        copy = type(n)(n.val)
        old2new[n] = copy
        copy.neighbors = [dfs(nb) for nb in n.neighbors]
        return copy

    return dfs(node)


def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    """417. Pacific Atlantic Water Flow — multi-source BFS."""
    if not heights:
        return []
    R, C = len(heights), len(heights[0])
    pac, atl = set(), set()

    def bfs(starts, ocean):
        q = deque(starts)
        for r, c in starts:
            ocean.add((r, c))
        while q:
            r, c = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < R
                    and 0 <= nc < C
                    and (nr, nc) not in ocean
                    and heights[nr][nc] >= heights[r][c]
                ):
                    ocean.add((nr, nc))
                    q.append((nr, nc))

    bfs([(r, 0) for r in range(R)] + [(0, c) for c in range(C)], pac)
    bfs([(r, C - 1) for r in range(R)] + [(R - 1, c) for c in range(C)], atl)
    return [list(p) for p in pac & atl]


def can_finish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """207. Course Schedule — topological sort (Kahn)."""
    g = defaultdict(list)
    indeg = [0] * numCourses
    for a, b in prerequisites:
        g[b].append(a)
        indeg[a] += 1
    q = deque(i for i in range(numCourses) if indeg[i] == 0)
    taken = 0
    while q:
        u = q.popleft()
        taken += 1
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return taken == numCourses


def find_order(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """210. Course Schedule II."""
    g = defaultdict(list)
    indeg = [0] * numCourses
    for a, b in prerequisites:
        g[b].append(a)
        indeg[a] += 1
    q = deque(i for i in range(numCourses) if indeg[i] == 0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == numCourses else []


def redundant_connection(edges: List[List[int]]) -> List[int]:
    """684. Redundant Connection — Union-Find."""
    parent = list(range(len(edges) + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[ra] = rb
        return True

    for a, b in edges:
        if not union(a, b):
            return [a, b]
    return []


def count_components(n: int, edges: List[List[int]]) -> int:
    """323. Number of Connected Components — Union-Find."""
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
            return True
        return False

    comps = n
    for a, b in edges:
        if union(a, b):
            comps -= 1
    return comps


def word_ladder_length(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """127. Word Ladder — BFS on implicit graph."""
    words = set(wordList)
    if endWord not in words:
        return 0
    q = deque([(beginWord, 1)])
    seen = {beginWord}
    L = len(beginWord)
    while q:
        w, d = q.popleft()
        if w == endWord:
            return d
        arr = list(w)
        for i in range(L):
            old = arr[i]
            for c in "abcdefghijklmnopqrstuvwxyz":
                arr[i] = c
                nw = "".join(arr)
                if nw in words and nw not in seen:
                    seen.add(nw)
                    q.append((nw, d + 1))
            arr[i] = old
    return 0


def oranges_rotting(grid: List[List[int]]) -> int:
    """994. Rotting Oranges — multi-source BFS."""
    R, C = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 2:
                q.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1
    t = 0
    while q:
        r, c, t = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                q.append((nr, nc, t + 1))
    return t if fresh == 0 else -1
