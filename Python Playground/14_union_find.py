"""
UNION FIND (Disjoint Set Union) - Complete Guide
=================================================

CORE CONCEPTS:
--------------
1. Also called Disjoint Set Union (DSU)
2. Tracks elements partitioned into disjoint (non-overlapping) sets
3. Two main operations: find() and union()
4. Used for: connected components, cycle detection, Kruskal's MST

OPERATIONS:
-----------
- find(x): Find which set x belongs to (returns representative/root)
- union(x, y): Merge sets containing x and y
- connected(x, y): Check if x and y are in same set

OPTIMIZATIONS:
--------------
1. Path Compression: Make tree flat during find()
2. Union by Rank: Attach smaller tree under larger tree
3. With both: O(α(n)) ≈ O(1) where α is inverse Ackermann function

TRICKY PARTS:
-------------
1. Parent array: parent[i] = parent of node i
2. Initially: parent[i] = i (each element is its own parent)
3. Find root by following parent pointers
4. Union connects two roots
5. Path compression: point all nodes directly to root

WHEN TO USE:
------------
- Finding connected components
- Detecting cycles in undirected graph
- Kruskal's MST algorithm
- Dynamic connectivity problems
- Grouping/clustering problems
"""

from typing import List, Set, Dict
from collections import defaultdict


# ============================================================================
# BASIC UNION FIND IMPLEMENTATION
# ============================================================================

class UnionFind:
    """
    Basic Union Find with Path Compression and Union by Rank.

    PROBLEM: Implement Union Find data structure

    Operations needed:
    1. find(x): Find the root/representative of set containing x
    2. union(x, y): Merge sets containing x and y
    3. connected(x, y): Check if x and y are in same set

    Optimizations:
    - Path Compression: During find(), make all nodes point to root
    - Union by Rank: Attach shorter tree under taller tree

    Time Complexity: O(α(n)) ≈ O(1) per operation
    Space Complexity: O(n)
    """

    def __init__(self, n: int):
        """Initialize n disjoint sets (0 to n-1)."""
        self.parent = list(range(n))  # parent[i] = parent of node i
        self.rank = [0] * n           # rank[i] = approximate height of tree rooted at i
        self.count = n                # number of disjoint sets

    def find(self, x: int) -> int:
        """
        Find root of set containing x (with path compression).

        Path Compression: Make all nodes on path point directly to root.
        This flattens the tree for future operations.

        Time: O(α(n)) ≈ O(1)
        """
        if self.parent[x] != x:
            # Path compression: point x directly to root
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        Union sets containing x and y (union by rank).

        Returns True if union happened (sets were different).
        Returns False if already in same set (cycle detected).

        Union by Rank: Attach tree with lower rank under tree with higher rank.
        This keeps tree height small.

        Time: O(α(n)) ≈ O(1)
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in same set

        # Union by rank: attach smaller tree under larger tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            # Same rank: attach y under x and increase x's rank
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.count -= 1  # Merged two sets
        return True

    def connected(self, x: int, y: int) -> bool:
        """Check if x and y are in same set."""
        return self.find(x) == self.find(y)

    def get_count(self) -> int:
        """Return number of disjoint sets."""
        return self.count


# ============================================================================
# PROBLEM 1: NUMBER OF CONNECTED COMPONENTS
# ============================================================================

def count_components(n: int, edges: List[List[int]]) -> int:
    """
    PROBLEM: Number of Connected Components in Undirected Graph (LeetCode 323)

    You have a graph of n nodes labeled from 0 to n-1. You are given an integer n
    and an array edges where edges[i] = [ai, bi] indicates that there is an
    undirected edge between nodes ai and bi in the graph.

    Return the number of connected components in the graph.

    Example 1:
        Input: n = 5, edges = [[0,1],[1,2],[3,4]]
        Output: 2
        Explanation:
            0 - 1 - 2    3 - 4
            (component 1) (component 2)

    Example 2:
        Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
        Output: 1
        Explanation: All nodes are connected in one component.

    Constraints:
        - 1 <= n <= 2000
        - 1 <= edges.length <= 5000
        - edges[i].length == 2
        - 0 <= ai <= bi < n
        - ai != bi
        - No duplicate edges

    Time: O(E * α(n)), Space: O(n)
    """
    uf = UnionFind(n)

    for u, v in edges:
        uf.union(u, v)

    return uf.count


# ============================================================================
# PROBLEM 2: GRAPH VALID TREE
# ============================================================================

def valid_tree(n: int, edges: List[List[int]]) -> bool:
    """
    PROBLEM: Graph Valid Tree (LeetCode 261)

    Given n nodes labeled from 0 to n-1 and a list of undirected edges,
    check if these edges make up a valid tree.

    A valid tree must satisfy:
    1. All nodes are connected (n-1 edges for n nodes)
    2. No cycles exist

    Example 1:
        Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
        Output: true
        Explanation:
            0
           /|\\
          1 2 3
         /
        4

    Example 2:
        Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
        Output: false
        Explanation: Contains a cycle: 1-2-3-1

    Constraints:
        - 1 <= n <= 2000
        - 0 <= edges.length <= 5000

    Time: O(E * α(n)), Space: O(n)
    """
    # Tree must have exactly n-1 edges
    if len(edges) != n - 1:
        return False

    uf = UnionFind(n)

    for u, v in edges:
        # If union returns False, there's a cycle
        if not uf.union(u, v):
            return False

    # After all unions, should be exactly 1 component
    return uf.count == 1


# ============================================================================
# PROBLEM 3: REDUNDANT CONNECTION
# ============================================================================

def find_redundant_connection(edges: List[List[int]]) -> List[int]:
    """
    PROBLEM: Redundant Connection (LeetCode 684)

    In this problem, a tree is an undirected graph that is connected and has no cycles.

    You are given a graph that started as a tree with n nodes labeled from 1 to n,
    with one additional edge added. The added edge has two different vertices chosen
    from 1 to n, and was not an edge that already existed.

    Return an edge that can be removed so that the resulting graph is a tree of n nodes.
    If there are multiple answers, return the answer that occurs last in the input.

    Example 1:
        Input: edges = [[1,2],[1,3],[2,3]]
        Output: [2,3]
        Explanation:
            1 - 2
            |   |
            +---3
            Edge [2,3] creates cycle, so remove it.

    Example 2:
        Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
        Output: [1,4]
        Explanation: Cycle is 1-2-3-4-1, edge [1,4] is last in cycle.

    Constraints:
        - n == edges.length
        - 3 <= n <= 1000
        - edges[i].length == 2
        - 1 <= ai < bi <= n

    Time: O(n * α(n)), Space: O(n)
    """
    uf = UnionFind(len(edges) + 1)  # +1 because nodes are 1-indexed

    for u, v in edges:
        # If union fails, this edge creates a cycle
        if not uf.union(u, v):
            return [u, v]

    return []


# ============================================================================
# PROBLEM 4: ACCOUNTS MERGE
# ============================================================================

def accounts_merge(accounts: List[List[str]]) -> List[List[str]]:
    """
    PROBLEM: Accounts Merge (LeetCode 721)

    Given a list of accounts where each element accounts[i] is a list of strings,
    where the first element accounts[i][0] is a name, and the rest of the elements
    are emails representing emails of the account.

    Two accounts definitely belong to the same person if there is some common email
    to both accounts. Note that even if two accounts have the same name, they may
    belong to different people as people could have the same name.

    Merge the accounts and return them in the following format: the first element
    of each account is the name, and the rest are emails in sorted order.

    Example 1:
        Input: accounts = [
            ["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]
        ]
        Output: [
            ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]
        ]
        Explanation:
            First two Johns have common email "johnsmith@mail.com", so merge them.
            Third John has no common emails with first two, so separate.

    Example 2:
        Input: accounts = [
            ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
            ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
            ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
            ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
            ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]
        ]
        Output: [
            ["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
            ["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
            ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
            ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
            ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]
        ]

    Constraints:
        - 1 <= accounts.length <= 1000
        - 2 <= accounts[i].length <= 10
        - 1 <= accounts[i][j].length <= 30
        - accounts[i][0] consists of English letters.
        - accounts[i][j] (for j > 0) is a valid email.

    Time: O(n * k * α(n)) where k is max emails per account
    Space: O(n * k)
    """
    email_to_name = {}
    email_to_id = {}
    uf = UnionFind(len(accounts))

    # Map each email to account ID
    for i, account in enumerate(accounts):
        name = account[0]
        for email in account[1:]:
            email_to_name[email] = name

            if email in email_to_id:
                # This email seen before - union with previous account
                uf.union(i, email_to_id[email])
            else:
                email_to_id[email] = i

    # Group emails by root account
    root_to_emails = defaultdict(set)
    for email, acc_id in email_to_id.items():
        root = uf.find(acc_id)
        root_to_emails[root].add(email)

    # Build result
    result = []
    for root, emails in root_to_emails.items():
        name = email_to_name[list(emails)[0]]
        result.append([name] + sorted(emails))

    return result


# ============================================================================
# PROBLEM 5: NUMBER OF ISLANDS II
# ============================================================================

def num_islands_ii(m: int, n: int, positions: List[List[int]]) -> List[int]:
    """
    PROBLEM: Number of Islands II (LeetCode 305)

    You are given an empty 2D binary grid of size m x n. The grid represents
    a map where 0's represent water and 1's represent land. Initially, all
    the cells of grid are water cells.

    We may perform an add land operation which turns the water at position
    into a land. You are given an array positions where positions[i] = [ri, ci]
    is the position (ri, ci) at which we should operate the ith operation.

    Return an array of integers answer where answer[i] is the number of islands
    after turning the cell (ri, ci) into a land.

    An island is surrounded by water and is formed by connecting adjacent lands
    horizontally or vertically. You may assume all four edges of the grid are
    all surrounded by water.

    Example 1:
        Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
        Output: [1,1,2,3]
        Explanation:
            Initially: all water
            After [0,0]: 1 island
                1 0 0
                0 0 0
                0 0 0
            After [0,1]: 1 island (merged with [0,0])
                1 1 0
                0 0 0
                0 0 0
            After [1,2]: 2 islands
                1 1 0
                0 0 1
                0 0 0
            After [2,1]: 3 islands
                1 1 0
                0 0 1
                0 1 0

    Example 2:
        Input: m = 1, n = 1, positions = [[0,0]]
        Output: [1]

    Constraints:
        - 1 <= m, n, positions.length <= 10^4
        - 1 <= m * n <= 10^4
        - positions[i].length == 2
        - 0 <= ri < m
        - 0 <= ci < n

    Time: O(k * α(m*n)) where k is positions length
    Space: O(m * n)
    """
    uf = UnionFind(m * n)
    result = []
    island_count = 0
    grid = [[0] * n for _ in range(m)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def get_id(r: int, c: int) -> int:
        return r * n + c

    for r, c in positions:
        # If already land, don't add again
        if grid[r][c] == 1:
            result.append(island_count)
            continue

        grid[r][c] = 1
        island_count += 1  # New island added

        # Check 4 neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                # Neighbor is land, try to union
                if uf.union(get_id(r, c), get_id(nr, nc)):
                    island_count -= 1  # Merged two islands

        result.append(island_count)

    return result


# ============================================================================
# PROBLEM 6: MOST STONES REMOVED
# ============================================================================

def remove_stones(stones: List[List[int]]) -> int:
    """
    PROBLEM: Most Stones Removed with Same Row or Column (LeetCode 947)

    On a 2D plane, we place n stones at some integer coordinate points. Each
    coordinate point may have at most one stone.

    A stone can be removed if it shares either the same row or the same column
    as another stone that has not been removed.

    Given an array stones of length n where stones[i] = [xi, yi] represents the
    location of the ith stone, return the largest possible number of stones that
    can be removed.

    Example 1:
        Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
        Output: 5
        Explanation: One way to remove 5 stones:
            Remove [2,2], then [2,1], then [1,2], then [1,0], then [0,1]
            Stone [0,0] remains.

    Example 2:
        Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
        Output: 3
        Explanation: One possible way is:
            Remove [2,2], then [0,2], then [2,0]

    Example 3:
        Input: stones = [[0,0]]
        Output: 0

    Constraints:
        - 1 <= stones.length <= 1000
        - 0 <= xi, yi <= 10^4

    Trick: Stones in same row/column form connected component.
           Max removable = total_stones - num_components

    Time: O(n * α(n)), Space: O(n)
    """
    uf = UnionFind(len(stones))

    # Map to track which stone is at each row/column
    row_map = {}  # row -> stone index
    col_map = {}  # col -> stone index

    for i, (x, y) in enumerate(stones):
        # Union with stone in same row
        if x in row_map:
            uf.union(i, row_map[x])
        else:
            row_map[x] = i

        # Union with stone in same column
        if y in col_map:
            uf.union(i, col_map[y])
        else:
            col_map[y] = i

    # Max stones removable = total - number of components
    return len(stones) - uf.count


# ============================================================================
# PROBLEM 7: SATISFIABILITY OF EQUALITY EQUATIONS
# ============================================================================

def equations_possible(equations: List[str]) -> bool:
    """
    PROBLEM: Satisfiability of Equality Equations (LeetCode 990)

    You are given an array of strings equations that represent relationships
    between variables where each string equations[i] is of length 4 and takes
    one of two different forms: "xi==yi" or "xi!=yi".

    Here, xi and yi are lowercase letters (not necessarily different) that
    represent one-letter variable names.

    Return true if it is possible to assign integers to variable names so as
    to satisfy all the given equations, or false otherwise.

    Example 1:
        Input: equations = ["a==b","b!=a"]
        Output: false
        Explanation: If we assign a = 1 and b = 1, then a == b and b != a are
        both true, which is impossible.

    Example 2:
        Input: equations = ["b==a","a==b"]
        Output: true
        Explanation: We can assign a = 1 and b = 1 to satisfy both equations.

    Example 3:
        Input: equations = ["a==b","b==c","a==c"]
        Output: true

    Example 4:
        Input: equations = ["a==b","b!=c","c==a"]
        Output: false

    Constraints:
        - 1 <= equations.length <= 500
        - equations[i].length == 4
        - equations[i][0] is a lowercase letter
        - equations[i][1] is either '=' or '!'
        - equations[i][2] is '='
        - equations[i][3] is a lowercase letter

    Time: O(n), Space: O(1) - only 26 letters
    """
    uf = UnionFind(26)  # 26 letters

    # First pass: process all equality equations
    for eq in equations:
        if eq[1] == '=':  # "a==b"
            x = ord(eq[0]) - ord('a')
            y = ord(eq[3]) - ord('a')
            uf.union(x, y)

    # Second pass: check inequality equations
    for eq in equations:
        if eq[1] == '!':  # "a!=b"
            x = ord(eq[0]) - ord('a')
            y = ord(eq[3]) - ord('a')
            # If they're in same set, inequality is impossible
            if uf.connected(x, y):
                return False

    return True


# ============================================================================
# ADVANCED: UNION FIND WITH SIZE TRACKING
# ============================================================================

class UnionFindWithSize:
    """
    Union Find that tracks size of each component.

    Useful when you need to know component sizes.
    """

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n  # size[i] = size of component rooted at i
        self.count = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        # Union by size: attach smaller to larger
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]

        self.count -= 1
        return True

    def get_size(self, x: int) -> int:
        """Get size of component containing x."""
        return self.size[self.find(x)]

    def get_max_component_size(self) -> int:
        """Get size of largest component."""
        return max(self.size[i] for i in range(len(self.parent))
                   if self.parent[i] == i)


# ============================================================================
# PRACTICE PROBLEMS
# ============================================================================

"""
EASY:
- Redundant Connection (684)
- Find if Path Exists in Graph (1971)

MEDIUM:
- Number of Connected Components (323)
- Graph Valid Tree (261)
- Accounts Merge (721)
- Satisfiability of Equality Equations (990)
- Most Stones Removed (947)
- Smallest String With Swaps (1202)

HARD:
- Number of Islands II (305)
- Minimize Malware Spread (924)
- Minimize Malware Spread II (928)
- Bricks Falling When Hit (803)
"""


if __name__ == "__main__":
    print("="*70)
    print("UNION FIND - Test Examples")
    print("="*70)

    # Test 1: Connected Components
    print("\n1. Number of Connected Components:")
    print(f"   n=5, edges=[[0,1],[1,2],[3,4]]")
    print(f"   Result: {count_components(5, [[0,1],[1,2],[3,4]])} components")

    # Test 2: Valid Tree
    print("\n2. Graph Valid Tree:")
    print(f"   n=5, edges=[[0,1],[0,2],[0,3],[1,4]]")
    print(f"   Result: {valid_tree(5, [[0,1],[0,2],[0,3],[1,4]])}")

    # Test 3: Redundant Connection
    print("\n3. Redundant Connection:")
    print(f"   edges=[[1,2],[1,3],[2,3]]")
    print(f"   Result: {find_redundant_connection([[1,2],[1,3],[2,3]])}")

    # Test 4: Equality Equations
    print("\n4. Satisfiability of Equality Equations:")
    print(f"   equations=['a==b','b!=a']")
    print(f"   Result: {equations_possible(['a==b','b!=a'])}")

    print("\n" + "="*70)
    print("Union Find is powerful for grouping and connectivity problems!")
    print("="*70)
