"""
GRAPH, DFS & BFS - Complete Guide for Interview Preparation
============================================================

CORE CONCEPTS:
--------------
GRAPH REPRESENTATION:
1. Adjacency Matrix: 2D array, O(V²) space, O(1) edge check
2. Adjacency List: dict/list of lists, O(V+E) space, O(deg(v)) edge check
3. Edge List: list of (u, v) pairs

GRAPH TYPES:
- Directed vs Undirected
- Weighted vs Unweighted
- Cyclic vs Acyclic (DAG)
- Connected vs Disconnected

DFS (Depth-First Search):
- Uses stack (recursion or explicit)
- Time: O(V+E), Space: O(V)
- Use: cycle detection, topological sort, connected components

BFS (Breadth-First Search):
- Uses queue
- Time: O(V+E), Space: O(V)
- Use: shortest path (unweighted), level-order traversal

TRICKY PARTS:
-------------
1. Graph can be implicit (generate neighbors on the fly)
2. Visited tracking crucial to avoid infinite loops
3. Directed vs undirected affects algorithm
4. DFS can hit stack limit - use iterative if deep
5. Disconnected graphs need to iterate all nodes

COMMON PATTERNS:
----------------
1. DFS: Connected components, cycle detection, path finding
2. BFS: Shortest path, level-order
3. Union Find: Connected components, cycle detection
4. Topological Sort: DAG ordering
5. Shortest Path: Dijkstra, Bellman-Ford
"""

from typing import List, Set, Dict, Optional
from collections import deque, defaultdict
import heapq


# ============================================================================
# PATTERN 1: DFS - RECURSIVE
# ============================================================================

def dfs_recursive(graph: Dict[int, List[int]], start: int, visited: Set[int]):
    """
    Basic DFS traversal - recursive.

    Time: O(V+E), Space: O(V) for recursion stack
    """
    visited.add(start)
    print(start, end=' ')

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def dfs_iterative(graph: Dict[int, List[int]], start: int) -> List[int]:
    """
    DFS traversal - iterative using stack.

    Time: O(V+E), Space: O(V)
    """
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            result.append(node)

            # Add neighbors in reverse to maintain order
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result


# ============================================================================
# PATTERN 2: BFS
# ============================================================================

def bfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    """
    BFS traversal using queue.

    Time: O(V+E), Space: O(V)
    """
    visited = {start}
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def bfs_level_order(graph: Dict[int, List[int]], start: int) -> List[List[int]]:
    """
    BFS with level tracking.

    Time: O(V+E), Space: O(V)
    """
    visited = {start}
    queue = deque([start])
    result = []

    while queue:
        level = []
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        result.append(level)

    return result


# ============================================================================
# PATTERN 3: NUMBER OF ISLANDS / CONNECTED COMPONENTS
# ============================================================================

def num_islands(grid: List[List[str]]) -> int:
    """
    LeetCode 200 - Number of islands (connected components).

    Time: O(m*n), Space: O(m*n) for recursion
    """
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    count = 0

    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
            return

        grid[i][j] = '0'  # Mark as visited

        # Explore 4 directions
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1

    return count


def max_area_island(grid: List[List[int]]) -> int:
    """
    LeetCode 695 - Max area of island.

    Time: O(m*n), Space: O(m*n)
    """
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])

    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
            return 0

        grid[i][j] = 0  # Mark visited

        return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)

    max_area = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                max_area = max(max_area, dfs(i, j))

    return max_area


def count_connected_components(n: int, edges: List[List[int]]) -> int:
    """
    LeetCode 323 - Number of connected components in undirected graph.

    Time: O(V+E), Space: O(V+E)
    """
    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    count = 0

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for node in range(n):
        if node not in visited:
            dfs(node)
            count += 1

    return count


# ============================================================================
# PATTERN 4: CYCLE DETECTION
# ============================================================================

def has_cycle_undirected(n: int, edges: List[List[int]]) -> bool:
    """
    Detect cycle in undirected graph using DFS.

    Time: O(V+E), Space: O(V)
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                # Visited and not parent = cycle
                return True

        return False

    for node in range(n):
        if node not in visited:
            if dfs(node, -1):
                return True

    return False


def has_cycle_directed(n: int, edges: List[List[int]]) -> bool:
    """
    LeetCode 207 variation - Detect cycle in directed graph.

    Time: O(V+E), Space: O(V)
    Tricky: Need to track nodes in current path
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    UNVISITED, VISITING, VISITED = 0, 1, 2
    state = [UNVISITED] * n

    def dfs(node):
        if state[node] == VISITING:
            return True  # Cycle detected
        if state[node] == VISITED:
            return False

        state[node] = VISITING

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True

        state[node] = VISITED
        return False

    for node in range(n):
        if dfs(node):
            return True

    return False


# ============================================================================
# PATTERN 5: SHORTEST PATH (BFS - Unweighted)
# ============================================================================

def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
    """
    LeetCode 1091 - Shortest path in binary matrix.

    Time: O(n²), Space: O(n²)
    """
    n = len(grid)

    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1

    # 8 directions
    directions = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

    queue = deque([(0, 0, 1)])  # (row, col, distance)
    grid[0][0] = 1  # Mark visited

    while queue:
        row, col, dist = queue.popleft()

        if row == n-1 and col == n-1:
            return dist

        for dr, dc in directions:
            r, c = row + dr, col + dc

            if 0 <= r < n and 0 <= c < n and grid[r][c] == 0:
                grid[r][c] = 1  # Mark visited
                queue.append((r, c, dist + 1))

    return -1


def walls_and_gates(rooms: List[List[int]]) -> None:
    """
    LeetCode 286 - Walls and gates (multi-source BFS).

    Time: O(m*n), Space: O(m*n)
    Tricky: Start BFS from all gates simultaneously
    """
    if not rooms:
        return

    m, n = len(rooms), len(rooms[0])
    queue = deque()
    INF = 2147483647

    # Add all gates to queue
    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:
                queue.append((i, j))

    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    while queue:
        row, col = queue.popleft()

        for dr, dc in directions:
            r, c = row + dr, col + dc

            if 0 <= r < m and 0 <= c < n and rooms[r][c] == INF:
                rooms[r][c] = rooms[row][col] + 1
                queue.append((r, c))


# ============================================================================
# PATTERN 6: TOPOLOGICAL SORT
# ============================================================================

def topological_sort_dfs(n: int, edges: List[List[int]]) -> List[int]:
    """
    Topological sort using DFS.

    Time: O(V+E), Space: O(V)
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

        stack.append(node)

    for node in range(n):
        if node not in visited:
            dfs(node)

    return stack[::-1]  # Reverse to get topological order


def can_finish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    LeetCode 207 - Course schedule (detect cycle in directed graph).

    Time: O(V+E), Space: O(V)
    """
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    UNVISITED, VISITING, VISITED = 0, 1, 2
    state = [UNVISITED] * numCourses

    def has_cycle(node):
        if state[node] == VISITING:
            return True
        if state[node] == VISITED:
            return False

        state[node] = VISITING

        for neighbor in graph[node]:
            if has_cycle(neighbor):
                return True

        state[node] = VISITED
        return False

    for course in range(numCourses):
        if has_cycle(course):
            return False

    return True


def find_order(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    LeetCode 210 - Course schedule II (topological sort).

    Time: O(V+E), Space: O(V)
    Using Kahn's algorithm (BFS-based)
    """
    graph = defaultdict(list)
    indegree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    # Start with nodes having 0 indegree
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == numCourses else []


# ============================================================================
# PATTERN 7: CLONE GRAPH
# ============================================================================

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    """
    LeetCode 133 - Clone graph.

    Time: O(V+E), Space: O(V)
    """
    if not node:
        return None

    old_to_new = {}

    def dfs(node):
        if node in old_to_new:
            return old_to_new[node]

        copy = Node(node.val)
        old_to_new[node] = copy

        for neighbor in node.neighbors:
            copy.neighbors.append(dfs(neighbor))

        return copy

    return dfs(node)


# ============================================================================
# PATTERN 8: WORD LADDER / TRANSFORMATION
# ============================================================================

def ladder_length(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    LeetCode 127 - Word ladder (shortest transformation sequence).

    Time: O(M² * N) where M is word length, N is word count
    Space: O(M * N)
    """
    word_set = set(wordList)

    if endWord not in word_set:
        return 0

    queue = deque([(beginWord, 1)])
    visited = {beginWord}

    while queue:
        word, level = queue.popleft()

        if word == endWord:
            return level

        # Try changing each character
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]

                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, level + 1))

    return 0


# ============================================================================
# PATTERN 9: BIPARTITE GRAPH
# ============================================================================

def is_bipartite(graph: List[List[int]]) -> bool:
    """
    LeetCode 785 - Check if graph is bipartite (2-colorable).

    Time: O(V+E), Space: O(V)
    Tricky: Color nodes with two colors, check for conflicts
    """
    n = len(graph)
    color = [-1] * n

    def dfs(node, c):
        color[node] = c

        for neighbor in graph[node]:
            if color[neighbor] == c:
                return False
            if color[neighbor] == -1 and not dfs(neighbor, 1 - c):
                return False

        return True

    for node in range(n):
        if color[node] == -1:
            if not dfs(node, 0):
                return False

    return True


# ============================================================================
# PRACTICE PROBLEMS
# ============================================================================
"""
EASY:
- Find Center of Star Graph (1791)
- Find if Path Exists in Graph (1971)

MEDIUM (DFS/BFS):
- Number of Islands (200)
- Clone Graph (133)
- Course Schedule (207)
- Course Schedule II (210)
- Pacific Atlantic Water Flow (417)
- Number of Connected Components (323)
- Graph Valid Tree (261)
- Walls and Gates (286)

MEDIUM (Shortest Path):
- Shortest Path in Binary Matrix (1091)
- Word Ladder (127)
- Open the Lock (752)
- Minimum Knight Moves (1197)

HARD:
- Word Ladder II (126)
- Alien Dictionary (269)
- Minimum Cost to Make Valid Path (1368)
- Swim in Rising Water (778)
"""

if __name__ == "__main__":
    # Test DFS/BFS
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [3]}

    print("DFS:", dfs_iterative(graph, 0))
    print("BFS:", bfs(graph, 0))

    # Test Number of Islands
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    # Note: This will modify grid
    print("Number of Islands:", num_islands(grid))

    # Test Course Schedule
    print("Can Finish:", can_finish(2, [[1, 0]]))
    print("Course Order:", find_order(2, [[1, 0]]))
