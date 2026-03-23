"""
DYNAMIC PROGRAMMING - Complete Guide for Interview Preparation
===============================================================

CORE CONCEPTS:
--------------
1. Break problem into overlapping subproblems
2. Store solutions to avoid recomputation (memoization/tabulation)
3. Optimal substructure: optimal solution contains optimal solutions to subproblems
4. Two approaches: Top-down (memoization) vs Bottom-up (tabulation)

WHEN TO USE DP:
- Problem asks for optimization (max, min, count)
- Problem can be broken into overlapping subproblems
- Future decisions depend on earlier decisions

TRICKY PARTS:
-------------
1. Identifying DP problem vs greedy vs other approaches
2. Defining state and transition correctly
3. Base cases are crucial!
4. Space optimization: often can reduce from 2D to 1D
5. Iteration order matters in tabulation

COMMON PATTERNS:
----------------
1. Linear DP (Fibonacci, climbing stairs)
2. Grid/Matrix DP (unique paths, min path sum)
3. Knapsack (0/1, unbounded, fractional)
4. LCS/LIS (longest common/increasing subsequence)
5. Palindrome DP
6. String DP (edit distance, regex)
7. Game Theory DP (min-max)
8. State Machine DP
"""

from typing import List, Dict
from functools import lru_cache


# ============================================================================
# PATTERN 1: LINEAR DP (1D)
# ============================================================================

def fibonacci(n: int) -> int:
    """
    Classic Fibonacci - foundation of DP.

    Time: O(n), Space: O(1)
    """
    if n <= 1:
        return n

    prev2, prev1 = 0, 1

    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr

    return prev1


def climb_stairs(n: int) -> int:
    """
    LeetCode 70 - Climbing stairs (1 or 2 steps at a time).

    Time: O(n), Space: O(1)
    Same as Fibonacci!
    """
    if n <= 2:
        return n

    prev2, prev1 = 1, 2

    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr

    return prev1


def min_cost_climbing_stairs(cost: List[int]) -> int:
    """
    LeetCode 746 - Min cost climbing stairs.

    Time: O(n), Space: O(1)
    """
    n = len(cost)

    if n <= 1:
        return 0

    prev2, prev1 = cost[0], cost[1]

    for i in range(2, n):
        curr = cost[i] + min(prev1, prev2)
        prev2, prev1 = prev1, curr

    return min(prev1, prev2)


def rob_houses(nums: List[int]) -> int:
    """
    LeetCode 198 - House robber (can't rob adjacent houses).

    Time: O(n), Space: O(1)
    DP formula: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2, prev1 = 0, nums[0]

    for i in range(1, len(nums)):
        curr = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, curr

    return prev1


def rob_houses_ii(nums: List[int]) -> int:
    """
    LeetCode 213 - House robber II (houses in circle).

    Time: O(n), Space: O(1)
    Tricky: Either rob first or rob last, not both
    """
    if len(nums) == 1:
        return nums[0]

    def rob_linear(houses):
        prev2, prev1 = 0, 0
        for num in houses:
            curr = max(prev1, prev2 + num)
            prev2, prev1 = prev1, curr
        return prev1

    # Case 1: Rob houses [0, n-2]
    # Case 2: Rob houses [1, n-1]
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


def delete_and_earn(nums: List[int]) -> int:
    """
    LeetCode 740 - Delete and earn (similar to house robber).

    Time: O(n + m) where m is max value, Space: O(m)
    """
    if not nums:
        return 0

    max_val = max(nums)
    points = [0] * (max_val + 1)

    # Sum points for each value
    for num in nums:
        points[num] += num

    # Now it's house robber problem
    prev2, prev1 = 0, 0
    for point in points:
        curr = max(prev1, prev2 + point)
        prev2, prev1 = prev1, curr

    return prev1


# ============================================================================
# PATTERN 2: GRID/MATRIX DP
# ============================================================================

def unique_paths(m: int, n: int) -> int:
    """
    LeetCode 62 - Unique paths in m x n grid.

    Time: O(m*n), Space: O(n)
    """
    dp = [1] * n  # First row all 1s

    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]  # From left + from top

    return dp[n-1]


def unique_paths_with_obstacles(grid: List[List[int]]) -> int:
    """
    LeetCode 63 - Unique paths with obstacles.

    Time: O(m*n), Space: O(n)
    """
    if not grid or grid[0][0] == 1:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = 1

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j-1]

    return dp[n-1]


def min_path_sum(grid: List[List[int]]) -> int:
    """
    LeetCode 64 - Minimum path sum in grid.

    Time: O(m*n), Space: O(n)
    """
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(m):
        for j in range(n):
            if j == 0:
                dp[j] += grid[i][j]
            else:
                dp[j] = grid[i][j] + min(dp[j], dp[j-1])

    return dp[n-1]


def maximal_square(matrix: List[List[str]]) -> int:
    """
    LeetCode 221 - Maximal square in matrix of 0s and 1s.

    Time: O(m*n), Space: O(n)
    DP formula: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    """
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    dp = [0] * (n + 1)
    max_side = 0
    prev = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            temp = dp[j]

            if matrix[i-1][j-1] == '1':
                dp[j] = min(dp[j], dp[j-1], prev) + 1
                max_side = max(max_side, dp[j])
            else:
                dp[j] = 0

            prev = temp

    return max_side * max_side


# ============================================================================
# PATTERN 3: KNAPSACK PROBLEMS
# ============================================================================

def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    """
    0/1 Knapsack - classic DP problem.

    Time: O(n*W), Space: O(W)
    """
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        # Traverse backwards to avoid using same item twice
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]


def can_partition(nums: List[int]) -> bool:
    """
    LeetCode 416 - Partition equal subset sum.

    Time: O(n * sum), Space: O(sum)
    This is 0/1 knapsack variant!
    """
    total = sum(nums)

    if total % 2 != 0:
        return False

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target]


def coin_change(coins: List[int], amount: int) -> int:
    """
    LeetCode 322 - Coin change (minimum coins, unbounded knapsack).

    Time: O(n * amount), Space: O(amount)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_ii(amount: int, coins: List[int]) -> int:
    """
    LeetCode 518 - Coin change II (number of combinations).

    Time: O(n * amount), Space: O(amount)
    """
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]


# ============================================================================
# PATTERN 4: LONGEST INCREASING SUBSEQUENCE (LIS)
# ============================================================================

def length_of_lis(nums: List[int]) -> int:
    """
    LeetCode 300 - Longest increasing subsequence.

    Time: O(n²) DP, O(n log n) with binary search
    """
    # Approach 1: O(n²) DP
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def length_of_lis_optimized(nums: List[int]) -> int:
    """
    LIS using binary search - O(n log n).

    Tricky: Maintain array of smallest tail for each length
    """
    import bisect

    if not nums:
        return 0

    tails = []  # tails[i] = smallest tail for length i+1

    for num in nums:
        pos = bisect.bisect_left(tails, num)

        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num

    return len(tails)


def max_envelopes(envelopes: List[List[int]]) -> int:
    """
    LeetCode 354 - Russian doll envelopes (2D LIS).

    Time: O(n log n), Space: O(n)
    """
    # Sort by width ascending, height descending
    envelopes.sort(key=lambda x: (x[0], -x[1]))

    # Find LIS of heights
    import bisect
    heights = [h for _, h in envelopes]

    tails = []
    for h in heights:
        pos = bisect.bisect_left(tails, h)
        if pos == len(tails):
            tails.append(h)
        else:
            tails[pos] = h

    return len(tails)


# ============================================================================
# PATTERN 5: LONGEST COMMON SUBSEQUENCE (LCS)
# ============================================================================

def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    LeetCode 1143 - Longest common subsequence.

    Time: O(m*n), Space: O(n)
    """
    m, n = len(text1), len(text2)

    prev = [0] * (n + 1)

    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                curr[j] = prev[j-1] + 1
            else:
                curr[j] = max(curr[j-1], prev[j])
        prev = curr

    return prev[n]


def edit_distance(word1: str, word2: str) -> int:
    """
    LeetCode 72 - Edit distance (Levenshtein distance).

    Time: O(m*n), Space: O(n)
    Operations: insert, delete, replace
    """
    m, n = len(word1), len(word2)

    prev = list(range(n + 1))

    for i in range(1, m + 1):
        curr = [i] + [0] * n

        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                curr[j] = prev[j-1]
            else:
                curr[j] = 1 + min(
                    prev[j],      # Delete
                    curr[j-1],    # Insert
                    prev[j-1]     # Replace
                )

        prev = curr

    return prev[n]


# ============================================================================
# PATTERN 6: PALINDROME DP
# ============================================================================

def longest_palindrome_substring(s: str) -> str:
    """
    LeetCode 5 - Longest palindromic substring.

    Time: O(n²), Space: O(1) with expand, O(n²) with DP
    """
    def expand_around_center(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    if not s:
        return ""

    start = end = 0

    for i in range(len(s)):
        len1 = expand_around_center(i, i)      # Odd length
        len2 = expand_around_center(i, i + 1)  # Even length
        max_len = max(len1, len2)

        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]


def count_palindromic_substrings(s: str) -> int:
    """
    LeetCode 647 - Count palindromic substrings.

    Time: O(n²), Space: O(1)
    """
    def expand_around_center(left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

    total = 0
    for i in range(len(s)):
        total += expand_around_center(i, i)
        total += expand_around_center(i, i + 1)

    return total


def longest_palindrome_subsequence(s: str) -> int:
    """
    LeetCode 516 - Longest palindromic subsequence.

    Time: O(n²), Space: O(n)
    Equals LCS(s, reverse(s))!
    """
    n = len(s)
    prev = [0] * n

    for i in range(n - 1, -1, -1):
        curr = [0] * n
        curr[i] = 1

        for j in range(i + 1, n):
            if s[i] == s[j]:
                curr[j] = prev[j-1] + 2
            else:
                curr[j] = max(curr[j-1], prev[j])

        prev = curr

    return prev[n-1]


# ============================================================================
# PATTERN 7: STRING DP
# ============================================================================

def word_break(s: str, wordDict: List[str]) -> bool:
    """
    LeetCode 139 - Word break.

    Time: O(n²), Space: O(n)
    """
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[len(s)]


def num_decodings(s: str) -> int:
    """
    LeetCode 91 - Decode ways ('A' = 1, 'Z' = 26).

    Time: O(n), Space: O(1)
    """
    if not s or s[0] == '0':
        return 0

    prev2, prev1 = 1, 1

    for i in range(1, len(s)):
        curr = 0

        # Single digit
        if s[i] != '0':
            curr += prev1

        # Two digits
        two_digit = int(s[i-1:i+1])
        if 10 <= two_digit <= 26:
            curr += prev2

        prev2, prev1 = prev1, curr

    return prev1


# ============================================================================
# PATTERN 8: MEMOIZATION (TOP-DOWN)
# ============================================================================

@lru_cache(maxsize=None)
def fib_memo(n: int) -> int:
    """Fibonacci with memoization using decorator."""
    if n <= 1:
        return n
    return fib_memo(n-1) + fib_memo(n-2)


def max_profit_k_transactions(prices: List[int], k: int) -> int:
    """
    LeetCode 188 - Best time to buy/sell stock with at most k transactions.

    Time: O(n*k), Space: O(k)
    """
    if not prices or k == 0:
        return 0

    # If k >= n/2, unlimited transactions
    if k >= len(prices) // 2:
        return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices) - 1))

    # dp[i][j] = max profit with at most i transactions by day j
    buy = [-prices[0]] * (k + 1)
    sell = [0] * (k + 1)

    for price in prices:
        for j in range(k, 0, -1):
            sell[j] = max(sell[j], buy[j] + price)
            buy[j] = max(buy[j], sell[j-1] - price)

    return sell[k]


# ============================================================================
# PRACTICE PROBLEMS
# ============================================================================
"""
EASY:
- Climbing Stairs (70)
- Min Cost Climbing Stairs (746)
- House Robber (198)
- Max Subarray (53) - Kadane's

MEDIUM:
- Coin Change (322)
- Longest Increasing Subsequence (300)
- Longest Common Subsequence (1143)
- Unique Paths (62)
- Word Break (139)
- Partition Equal Subset Sum (416)
- Decode Ways (91)

HARD:
- Edit Distance (72)
- Regular Expression Matching (10)
- Wildcard Matching (44)
- Best Time to Buy Sell Stock IV (188)
- Burst Balloons (312)
- Russian Doll Envelopes (354)
"""

if __name__ == "__main__":
    # Test examples
    print("Fibonacci(10):", fibonacci(10))
    print("Climb Stairs(5):", climb_stairs(5))
    print("Rob Houses([2,7,9,3,1]):", rob_houses([2, 7, 9, 3, 1]))
    print("Unique Paths(3,7):", unique_paths(3, 7))
    print("LIS([10,9,2,5,3,7,101,18]):", length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))
    print("LCS('abcde', 'ace'):", longest_common_subsequence("abcde", "ace"))
    print("Coin Change([1,2,5], 11):", coin_change([1, 2, 5], 11))
