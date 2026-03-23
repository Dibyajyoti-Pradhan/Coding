"""
ESSENTIAL TOPICS CONSOLIDATED - Interview Preparation
======================================================
Covers: Greedy, Backtracking, Bit Manipulation, Trie, Union Find, Math

This file consolidates the remaining important topics for interview prep.
"""

from typing import List, Optional
from collections import defaultdict


# ============================================================================
# GREEDY ALGORITHMS
# ============================================================================
"""
GREEDY: Make locally optimal choice at each step
Key: Prove greedy choice leads to global optimum
Common: Intervals, scheduling, Huffman coding
"""

def jump_game(nums: List[int]) -> bool:
    """
    LeetCode 55 - Can reach last index.
    Time: O(n), Space: O(1)
    """
    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])

    return True


def jump_game_ii(nums: List[int]) -> int:
    """
    LeetCode 45 - Minimum jumps to reach end.
    Time: O(n), Space: O(1)
    """
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])

        if i == current_end:
            jumps += 1
            current_end = farthest

    return jumps


def max_subarray(nums: List[int]) -> int:
    """
    LeetCode 53 - Kadane's algorithm.
    Time: O(n), Space: O(1)
    """
    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


def partition_labels(s: str) -> List[int]:
    """
    LeetCode 763 - Partition string into max parts with unique chars.
    Time: O(n), Space: O(1)
    """
    last = {c: i for i, c in enumerate(s)}  # Last occurrence of each char

    result = []
    start = end = 0

    for i, char in enumerate(s):
        end = max(end, last[char])

        if i == end:
            result.append(end - start + 1)
            start = i + 1

    return result


def gas_station(gas: List[int], cost: List[int]) -> int:
    """
    LeetCode 134 - Gas station circular tour.
    Time: O(n), Space: O(1)
    """
    if sum(gas) < sum(cost):
        return -1

    tank = 0
    start = 0

    for i in range(len(gas)):
        tank += gas[i] - cost[i]

        if tank < 0:
            start = i + 1
            tank = 0

    return start


# ============================================================================
# BACKTRACKING
# ============================================================================
"""
BACKTRACKING: Try all possibilities, backtrack when constraint violated
Template:
    def backtrack(state):
        if is_solution(state):
            add to result
        for choice in choices:
            make choice
            backtrack(new_state)
            undo choice
"""

def permutations(nums: List[int]) -> List[List[int]]:
    """
    LeetCode 46 - All permutations.
    Time: O(n!), Space: O(n)
    """
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return

        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i+1:])
            path.pop()

    backtrack([], nums)
    return result


def subsets(nums: List[int]) -> List[List[int]]:
    """
    LeetCode 78 - All subsets.
    Time: O(2^n), Space: O(n)
    """
    result = []

    def backtrack(start, path):
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    LeetCode 39 - Combination sum (can reuse elements).
    Time: O(n^(t/m)) where t=target, m=min candidate
    """
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])  # i, not i+1 (can reuse)
            path.pop()

    backtrack(0, [], target)
    return result


def solve_n_queens(n: int) -> List[List[str]]:
    """
    LeetCode 51 - N-Queens.
    Time: O(n!), Space: O(n²)
    """
    result = []
    board = [['.'] * n for _ in range(n)]

    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col

    def backtrack(row):
        if row == n:
            result.append([''.join(row) for row in board])
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            # Place queen
            board[row][col] = 'Q'
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            backtrack(row + 1)

            # Remove queen
            board[row][col] = '.'
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return result


def word_search(board: List[List[str]], word: str) -> bool:
    """
    LeetCode 79 - Word search in grid.
    Time: O(m*n*4^L) where L is word length
    """
    m, n = len(board), len(board[0])

    def backtrack(i, j, idx):
        if idx == len(word):
            return True

        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[idx]:
            return False

        # Mark visited
        temp = board[i][j]
        board[i][j] = '#'

        # Explore 4 directions
        found = (backtrack(i+1, j, idx+1) or
                backtrack(i-1, j, idx+1) or
                backtrack(i, j+1, idx+1) or
                backtrack(i, j-1, idx+1))

        # Restore
        board[i][j] = temp

        return found

    for i in range(m):
        for j in range(n):
            if backtrack(i, j, 0):
                return True

    return False


# ============================================================================
# BIT MANIPULATION
# ============================================================================
"""
BIT OPERATIONS:
- x & 1: check if odd
- x & (x-1): remove rightmost 1 bit
- x & -x: isolate rightmost 1 bit
- x ^ x: 0 (XOR cancels)
- x ^ 0: x
- ~x: flip all bits

Common patterns: XOR for finding unique, bit masks for subsets
"""

def single_number(nums: List[int]) -> int:
    """
    LeetCode 136 - Find element appearing once (others twice).
    Time: O(n), Space: O(1)
    Trick: XOR cancels pairs
    """
    result = 0
    for num in nums:
        result ^= num
    return result


def count_bits(n: int) -> List[int]:
    """
    LeetCode 338 - Count 1s in binary for 0 to n.
    Time: O(n), Space: O(1)
    DP: bits[i] = bits[i >> 1] + (i & 1)
    """
    result = [0] * (n + 1)

    for i in range(1, n + 1):
        result[i] = result[i >> 1] + (i & 1)

    return result


def reverse_bits(n: int) -> int:
    """
    LeetCode 190 - Reverse bits of 32-bit integer.
    Time: O(1), Space: O(1)
    """
    result = 0

    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1

    return result


def hamming_distance(x: int, y: int) -> int:
    """
    LeetCode 461 - Count differing bits.
    Time: O(1), Space: O(1)
    """
    xor = x ^ y
    count = 0

    while xor:
        count += xor & 1
        xor >>= 1

    return count


def subsets_bitmasking(nums: List[int]) -> List[List[int]]:
    """
    LeetCode 78 - Subsets using bitmasks.
    Time: O(n * 2^n), Space: O(1)
    """
    n = len(nums)
    result = []

    for mask in range(1 << n):  # 2^n possibilities
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        result.append(subset)

    return result


# ============================================================================
# TRIE (Prefix Tree)
# ============================================================================
"""
TRIE: Tree for storing strings, efficient prefix operations
- Insert: O(L), Search: O(L), StartsWith: O(L) where L is word length
- Use: autocomplete, spell checker, IP routing
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    """
    LeetCode 208 - Implement Trie.
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True


def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    """
    LeetCode 212 - Word Search II (using Trie).
    Time: O(m*n*4^L), Space: O(N) where N is total chars in words
    """
    # Build Trie
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    m, n = len(board), len(board[0])
    result = set()

    def backtrack(i, j, node, path):
        if node.is_end:
            result.add(path)

        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] not in node.children:
            return

        char = board[i][j]
        board[i][j] = '#'  # Mark visited

        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            backtrack(i+di, j+dj, node.children[char], path + char)

        board[i][j] = char  # Restore

    for i in range(m):
        for j in range(n):
            if board[i][j] in root.children:
                backtrack(i, j, root, '')

    return list(result)


# ============================================================================
# UNION FIND (Disjoint Set Union)
# ============================================================================
"""
UNION FIND: Track connected components, detect cycles
- find: O(α(n)) ≈ O(1) with path compression
- union: O(α(n)) ≈ O(1) with union by rank
- Use: connected components, Kruskal's MST, cycle detection
"""

class UnionFind:
    """
    Optimized Union Find with path compression and union by rank.
    """
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # Number of components

    def find(self, x: int) -> int:
        """Find with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """Union by rank. Returns True if union happened (no cycle)."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already connected (cycle detected)

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.count -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        """Check if x and y are in same component."""
        return self.find(x) == self.find(y)


def num_islands_uf(grid: List[List[str]]) -> int:
    """
    LeetCode 200 - Number of islands using Union Find.
    Time: O(m*n), Space: O(m*n)
    """
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])

    # Count initial 1s
    count = sum(row.count('1') for row in grid)
    uf = UnionFind(m * n)

    def get_id(i, j):
        return i * n + j

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                # Union with adjacent 1s
                for di, dj in [(0,1), (1,0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
                        if uf.union(get_id(i,j), get_id(ni,nj)):
                            count -= 1

    # Adjust for 0 cells
    return count - sum(row.count('0') for row in grid)


def accounts_merge(accounts: List[List[str]]) -> List[List[str]]:
    """
    LeetCode 721 - Merge accounts with same emails.
    Time: O(n*k*α(n)), Space: O(n*k)
    """
    email_to_name = {}
    email_to_id = {}
    uf = UnionFind(len(accounts))

    # Map emails to account IDs
    for i, account in enumerate(accounts):
        name = account[0]
        for email in account[1:]:
            email_to_name[email] = name

            if email in email_to_id:
                uf.union(i, email_to_id[email])
            else:
                email_to_id[email] = i

    # Group emails by root
    root_to_emails = defaultdict(set)
    for email, acc_id in email_to_id.items():
        root = uf.find(acc_id)
        root_to_emails[root].add(email)

    # Build result
    return [[email_to_name[emails.pop()]] + sorted(emails)
            for emails in root_to_emails.values()]


# ============================================================================
# MATH & NUMBER THEORY
# ============================================================================
"""
Common: GCD, prime numbers, modular arithmetic, combinations
"""

def gcd(a: int, b: int) -> int:
    """Greatest Common Divisor - Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a


def is_prime(n: int) -> bool:
    """Check if n is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check odd divisors up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


def sieve_of_eratosthenes(n: int) -> List[int]:
    """Find all primes up to n."""
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(n + 1) if is_prime[i]]


def power_mod(base: int, exp: int, mod: int) -> int:
    """Fast modular exponentiation."""
    result = 1

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2

    return result


def factorial_mod(n: int, mod: int) -> int:
    """Factorial modulo mod."""
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % mod
    return result


# ============================================================================
# PRACTICE PROBLEMS
# ============================================================================
"""
GREEDY:
- Jump Game (55), Jump Game II (45)
- Best Time to Buy/Sell Stock (121, 122)
- Gas Station (134)
- Partition Labels (763)

BACKTRACKING:
- Permutations (46), Subsets (78), Combinations (77)
- Combination Sum (39, 40)
- N-Queens (51)
- Word Search (79)
- Palindrome Partitioning (131)

BIT MANIPULATION:
- Single Number (136, 137, 260)
- Power of Two (231)
- Counting Bits (338)
- Bitwise AND of Range (201)

TRIE:
- Implement Trie (208)
- Word Search II (212)
- Design Add and Search Words (211)

UNION FIND:
- Number of Connected Components (323)
- Graph Valid Tree (261)
- Accounts Merge (721)
- Redundant Connection (684)

MATH:
- Pow(x, n) (50)
- Sqrt(x) (69)
- Happy Number (202)
- Excel Sheet Column (168, 171)
"""

if __name__ == "__main__":
    # Test Greedy
    print("Jump Game:", jump_game([2,3,1,1,4]))
    print("Max Subarray:", max_subarray([-2,1,-3,4,-1,2,1,-5,4]))

    # Test Backtracking
    print("Permutations:", permutations([1,2,3]))
    print("Subsets:", subsets([1,2,3]))

    # Test Bit Manipulation
    print("Single Number:", single_number([4,1,2,1,2]))
    print("Count Bits:", count_bits(5))

    # Test Trie
    trie = Trie()
    trie.insert("apple")
    print("Trie search 'apple':", trie.search("apple"))
    print("Trie starts with 'app':", trie.startsWith("app"))

    # Test Union Find
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    print("UF connected(0, 2):", uf.connected(0, 2))
    print("UF connected(0, 3):", uf.connected(0, 3))

    # Test Math
    print("GCD(48, 18):", gcd(48, 18))
    print("Is 17 prime:", is_prime(17))
    print("Primes up to 20:", sieve_of_eratosthenes(20))
