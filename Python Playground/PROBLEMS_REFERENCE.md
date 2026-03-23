# Complete Problems Reference Guide
## Detailed Problem Statements for All Solutions

This guide contains **detailed problem statements** for every solution in the codebase. Use this to understand what each problem is asking before studying the solution.

---

## 📌 How to Use This Guide
1. **Find the problem** you want to solve
2. **Read the problem statement** carefully
3. **Try solving it yourself** first (30-40 min)
4. **Then check** the corresponding solution file
5. **Understand the pattern** and edge cases

---

# ARRAYS (01_array.py)

## Two Pointers - Opposite Direction

### 1. Two Sum II - Input Array Is Sorted (LeetCode 167)
**Difficulty:** Easy

**Problem:**
Given a **1-indexed** array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Return the indices of the two numbers (1-indexed) as an integer array `answer` of size 2.

You may assume that each input has **exactly one solution** and you may not use the same element twice.

**Examples:**
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: 2 + 7 = 9, so indices are [1, 2]

Input: numbers = [2,3,4], target = 6
Output: [1,3]

Input: numbers = [-1,0], target = -1
Output: [1,2]
```

**Constraints:**
- 2 <= numbers.length <= 3 * 10⁴
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order
- -1000 <= target <= 1000
- The tests are generated such that there is exactly one solution

---

### 2. 3Sum (LeetCode 15)
**Difficulty:** Medium

**Problem:**
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

**Examples:**
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Input: nums = [0,0,0]
Output: [[0,0,0]]
```

**Constraints:**
- 3 <= nums.length <= 3000
- -10⁵ <= nums[i] <= 10⁵

---

### 3. Container With Most Water (LeetCode 11)
**Difficulty:** Medium

**Problem:**
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i-th` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Note:** You may not slant the container.

**Examples:**
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The vertical lines are at indices 1 and 8.
The container can hold water of area = min(8, 7) * (8 - 1) = 7 * 7 = 49.

Input: height = [1,1]
Output: 1
```

**Constraints:**
- n == height.length
- 2 <= n <= 10⁵
- 0 <= height[i] <= 10⁴

---

### 4. Trapping Rain Water (LeetCode 42)
**Difficulty:** Hard

**Problem:**
Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

**Examples:**
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water are being trapped.

Input: height = [4,2,0,3,2,5]
Output: 9
```

**Constraints:**
- n == height.length
- 1 <= n <= 2 * 10⁴
- 0 <= height[i] <= 10⁵

---

## Sliding Window

### 5. Longest Substring Without Repeating Characters (LeetCode 3)
**Difficulty:** Medium

**Problem:**
Given a string `s`, find the length of the **longest substring** without repeating characters.

**Examples:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**Constraints:**
- 0 <= s.length <= 5 * 10⁴
- s consists of English letters, digits, symbols and spaces.

---

### 6. Minimum Window Substring (LeetCode 76)
**Difficulty:** Hard

**Problem:**
Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is unique.

**Examples:**
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Input: s = "a", t = "a"
Output: "a"

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

**Constraints:**
- m == s.length
- n == t.length
- 1 <= m, n <= 10⁵
- s and t consist of uppercase and lowercase English letters.

---

## Prefix Sum

### 7. Subarray Sum Equals K (LeetCode 560)
**Difficulty:** Medium

**Problem:**
Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

**Examples:**
```
Input: nums = [1,1,1], k = 2
Output: 2
Explanation: Subarrays [1,1] at indices [0,1] and [1,2]

Input: nums = [1,2,3], k = 3
Output: 2
Explanation: Subarrays [1,2] and [3]

Input: nums = [1,-1,0], k = 0
Output: 3
Explanation: Subarrays [1,-1], [1,-1,0], and [0]
```

**Constraints:**
- 1 <= nums.length <= 2 * 10⁴
- -1000 <= nums[i] <= 1000
- -10⁷ <= k <= 10⁷

---

## Kadane's Algorithm

### 8. Maximum Subarray (LeetCode 53)
**Difficulty:** Medium

**Problem:**
Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

**Examples:**
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23
```

**Constraints:**
- 1 <= nums.length <= 10⁵
- -10⁴ <= nums[i] <= 10⁴

**Follow up:** If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

---

### 9. Maximum Product Subarray (LeetCode 152)
**Difficulty:** Medium

**Problem:**
Given an integer array `nums`, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

**Examples:**
```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

**Constraints:**
- 1 <= nums.length <= 2 * 10⁴
- -10 <= nums[i] <= 10
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

---

## Merge Intervals

### 10. Merge Intervals (LeetCode 56)
**Difficulty:** Medium

**Problem:**
Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

**Examples:**
```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

**Constraints:**
- 1 <= intervals.length <= 10⁴
- intervals[i].length == 2
- 0 <= starti <= endi <= 10⁴

---

## Binary Search on Array

### 11. Search in Rotated Sorted Array (LeetCode 33)
**Difficulty:** Medium

**Problem:**
There is an integer array `nums` sorted in ascending order (with distinct values).

Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` (1 <= k < nums.length) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index 3 and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with **O(log n)** runtime complexity.

**Examples:**
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1
```

**Constraints:**
- 1 <= nums.length <= 5000
- -10⁴ <= nums[i] <= 10⁴
- All values of nums are unique.
- nums is an ascending array that is possibly rotated.
- -10⁴ <= target <= 10⁴

---

# DYNAMIC PROGRAMMING (10_dynamic_programming.py)

### 12. Climbing Stairs (LeetCode 70)
**Difficulty:** Easy

**Problem:**
You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Examples:**
```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

**Constraints:**
- 1 <= n <= 45

---

### 13. House Robber (LeetCode 198)
**Difficulty:** Medium

**Problem:**
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight **without alerting the police**.

**Examples:**
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
```

**Constraints:**
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400

---

### 14. Coin Change (LeetCode 322)
**Difficulty:** Medium

**Problem:**
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the **fewest number of coins** that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an **infinite number** of each kind of coin.

**Examples:**
```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

Input: coins = [1], amount = 0
Output: 0
```

**Constraints:**
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2³¹ - 1
- 0 <= amount <= 10⁴

---

### 15. Longest Increasing Subsequence (LeetCode 300)
**Difficulty:** Medium

**Problem:**
Given an integer array `nums`, return the length of the longest **strictly increasing subsequence**.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

**Examples:**
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Input: nums = [0,1,0,3,2,3]
Output: 4

Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

**Constraints:**
- 1 <= nums.length <= 2500
- -10⁴ <= nums[i] <= 10⁴

**Follow up:** Can you come up with an algorithm that runs in O(n log(n)) time complexity?

---

### 16. Longest Common Subsequence (LeetCode 1143)
**Difficulty:** Medium

**Problem:**
Given two strings `text1` and `text2`, return the length of their longest **common subsequence**. If there is no common subsequence, return `0`.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

**Examples:**
```
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
```

**Constraints:**
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.

---

### 17. Edit Distance (LeetCode 72)
**Difficulty:** Hard

**Problem:**
Given two strings `word1` and `word2`, return the minimum number of **operations** required to convert `word1` to `word2`.

You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character

**Examples:**
```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

**Constraints:**
- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters.

---

### 18. Partition Equal Subset Sum (LeetCode 416)
**Difficulty:** Medium

**Problem:**
Given an integer array `nums`, return `true` if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or `false` otherwise.

**Examples:**
```
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
```

**Constraints:**
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100

---

# TREES (09_tree_binary_tree.py)

### 19. Maximum Depth of Binary Tree (LeetCode 104)
**Difficulty:** Easy

**Problem:**
Given the `root` of a binary tree, return its maximum depth.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Examples:**
```
Input: root = [3,9,20,null,null,15,7]
       3
      / \
     9  20
       /  \
      15   7
Output: 3

Input: root = [1,null,2]
Output: 2
```

**Constraints:**
- The number of nodes in the tree is in the range [0, 10⁴].
- -100 <= Node.val <= 100

---

### 20. Binary Tree Level Order Traversal (LeetCode 102)
**Difficulty:** Medium

**Problem:**
Given the `root` of a binary tree, return the **level order traversal** of its nodes' values. (i.e., from left to right, level by level).

**Examples:**
```
Input: root = [3,9,20,null,null,15,7]
       3
      / \
     9  20
       /  \
      15   7
Output: [[3],[9,20],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []
```

**Constraints:**
- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000

---

### 21. Lowest Common Ancestor of a Binary Tree (LeetCode 236)
**Difficulty:** Medium

**Problem:**
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in T that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**)."

**Examples:**
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
       3
      / \
     5   1
    / \ / \
   6  2 0  8
     / \
    7   4
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself.
```

**Constraints:**
- The number of nodes in the tree is in the range [2, 10⁵].
- -10⁹ <= Node.val <= 10⁹
- All Node.val are unique.
- p != q
- p and q will exist in the tree.

---

### 22. Binary Tree Maximum Path Sum (LeetCode 124)
**Difficulty:** Hard

**Problem:**
A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence **at most once**. Note that the path does not need to pass through the root.

The **path sum** of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return the maximum **path sum** of any **non-empty** path.

**Examples:**
```
Input: root = [1,2,3]
     1
    / \
   2   3
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Input: root = [-10,9,20,null,null,15,7]
      -10
      / \
     9  20
       /  \
      15   7
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
```

**Constraints:**
- The number of nodes in the tree is in the range [1, 3 * 10⁴].
- -1000 <= Node.val <= 1000

---

# GRAPHS (12_graph_dfs_bfs.py)

### 23. Number of Islands (LeetCode 200)
**Difficulty:** Medium

**Problem:**
Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Examples:**
```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

**Constraints:**
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'.

---

### 24. Course Schedule (LeetCode 207)
**Difficulty:** Medium

**Problem:**
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.

For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

**Examples:**
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```

**Constraints:**
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs prerequisites[i] are unique.

---

### 25. Clone Graph (LeetCode 133)
**Difficulty:** Medium

**Problem:**
Given a reference of a node in a **connected** undirected graph.

Return a **deep copy** (clone) of the graph.

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

**Examples:**
```
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
```

**Constraints:**
- The number of nodes in the graph is in the range [0, 100].
- 1 <= Node.val <= 100
- Node.val is unique for each node.
- There are no repeated edges and no self-loops in the graph.

---

### 26. Word Ladder (LeetCode 127)
**Difficulty:** Hard

**Problem:**
A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:
- Every adjacent pair of words differs by a single letter.
- Every `si` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
- `sk == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the **number of words** in the **shortest transformation sequence** from `beginWord` to `endWord`, or `0` if no such sequence exists.

**Examples:**
```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", which is 5 words long.

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
```

**Constraints:**
- 1 <= beginWord.length <= 10
- endWord.length == beginWord.length
- 1 <= wordList.length <= 5000
- wordList[i].length == beginWord.length
- beginWord, endWord, and wordList[i] consist of lowercase English letters.
- beginWord != endWord
- All the words in wordList are unique.

---

# STACK, QUEUE & HEAP (11_stack_queue_heap.py)

### 27. Valid Parentheses (LeetCode 20)
**Difficulty:** Easy

**Problem:**
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Examples:**
```
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([])"
Output: true
```

**Constraints:**
- 1 <= s.length <= 10⁴
- s consists of parentheses only '()[]{}'.

---

### 28. Daily Temperatures (LeetCode 739)
**Difficulty:** Medium

**Problem:**
Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `ith` day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

**Examples:**
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Explanation:
On day 0: wait 1 day (74 > 73)
On day 1: wait 1 day (75 > 74)
On day 2: wait 4 days (76 > 75)
On day 3: wait 2 days (72 > 71)
...

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Input: temperatures = [30,60,90]
Output: [1,1,0]
```

**Constraints:**
- 1 <= temperatures.length <= 10⁵
- 30 <= temperatures[i] <= 100

---

### 29. Kth Largest Element in an Array (LeetCode 215)
**Difficulty:** Medium

**Problem:**
Given an integer array `nums` and an integer `k`, return the `kth` largest element in the array.

Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

Can you solve it without sorting?

**Examples:**
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

**Constraints:**
- 1 <= k <= nums.length <= 10⁵
- -10⁴ <= nums[i] <= 10⁴

---

### 30. Find Median from Data Stream (LeetCode 295)
**Difficulty:** Hard

**Problem:**
The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

Implement the MedianFinder class:
- `MedianFinder()` initializes the `MedianFinder` object.
- `void addNum(int num)` adds the integer `num` from the data stream to the data structure.
- `double findMedian()` returns the median of all elements so far.

**Examples:**
```
Input:
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]

Output:
[null, null, null, 1.5, null, 2.0]

Explanation:
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

**Constraints:**
- -10⁵ <= num <= 10⁵
- There will be at least one element in the data structure before calling findMedian.
- At most 5 * 10⁴ calls will be made to addNum and findMedian.

**Follow up:**
- If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
- If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

---

# BACKTRACKING (13_essential_topics_consolidated.py)

### 31. Permutations (LeetCode 46)
**Difficulty:** Medium

**Problem:**
Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in **any order**.

**Examples:**
```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Input: nums = [1]
Output: [[1]]
```

**Constraints:**
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique.

---

### 32. Subsets (LeetCode 78)
**Difficulty:** Medium

**Problem:**
Given an integer array `nums` of **unique** elements, return all possible subsets (the power set).

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

**Examples:**
```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input: nums = [0]
Output: [[],[0]]
```

**Constraints:**
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.

---

### 33. N-Queens (LeetCode 51)
**Difficulty:** Hard

**Problem:**
The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return all distinct solutions to the **n-queens puzzle**. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

**Examples:**
```
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle

Input: n = 1
Output: [["Q"]]
```

**Constraints:**
- 1 <= n <= 9

---

### 34. Word Search (LeetCode 79)
**Difficulty:** Medium

**Problem:**
Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Examples:**
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

**Constraints:**
- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters.

**Follow up:** Could you use search pruning to make your solution faster with a larger board?

---

# LINKED LIST (04_linked_list.py)

### 35. Reverse Linked List (LeetCode 206)
**Difficulty:** Easy

**Problem:**
Given the `head` of a singly linked list, reverse the list, and return the reversed list.

**Examples:**
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []
```

**Constraints:**
- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

---

### 36. Linked List Cycle (LeetCode 141)
**Difficulty:** Easy

**Problem:**
Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

**Examples:**
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Input: head = [1,2], pos = 0
Output: true

Input: head = [1], pos = -1
Output: false
```

**Constraints:**
- The number of the nodes in the list is in the range [0, 10⁴].
- -10⁵ <= Node.val <= 10⁵
- pos is -1 or a valid index in the linked-list.

**Follow up:** Can you solve it using O(1) (i.e. constant) memory?

---

### 37. Merge Two Sorted Lists (LeetCode 21)
**Difficulty:** Easy

**Problem:**
You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

**Examples:**
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]
```

**Constraints:**
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.

---

### 38. Merge k Sorted Lists (LeetCode 23)
**Difficulty:** Hard

**Problem:**
You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

**Examples:**
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Input: lists = []
Output: []

Input: lists = [[]]
Output: []
```

**Constraints:**
- k == lists.length
- 0 <= k <= 10⁴
- 0 <= lists[i].length <= 500
- -10⁴ <= lists[i][j] <= 10⁴
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 10⁴.

---

# BIT MANIPULATION (13_essential_topics_consolidated.py)

### 39. Single Number (LeetCode 136)
**Difficulty:** Easy

**Problem:**
Given a **non-empty** array of integers `nums`, every element appears **twice** except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

**Examples:**
```
Input: nums = [2,2,1]
Output: 1

Input: nums = [4,1,2,1,2]
Output: 4

Input: nums = [1]
Output: 1
```

**Constraints:**
- 1 <= nums.length <= 3 * 10⁴
- -3 * 10⁴ <= nums[i] <= 3 * 10⁴
- Each element in the array appears twice except for one element which appears only once.

---

### 40. Counting Bits (LeetCode 338)
**Difficulty:** Easy

**Problem:**
Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (0 <= i <= n), `ans[i]` is the **number of 1's** in the binary representation of `i`.

**Examples:**
```
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
```

**Constraints:**
- 0 <= n <= 10⁵

**Follow up:**
- It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
- Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

---

**Total Problems Documented:** 40 core problems covering all major patterns

---

## 📝 How to Practice

1. **Read the problem** statement above
2. **Think about** the approach (5-10 min)
3. **Code the solution** yourself (20-30 min)
4. **Test with examples** provided
5. **Check the solution** in the corresponding file
6. **Understand the pattern** and edge cases
7. **Redo** the problem after 1 day, then 1 week

Good luck! 🚀
