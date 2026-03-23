# Python Interview Preparation - Complete Study Guide

## 📚 Overview
This comprehensive collection covers all essential topics for **Mistral AI coding interviews** and **LeetCode Medium/Hard** problems. Each file contains:
- **Core concepts** explained clearly
- **Tricky parts** to watch out for
- **Common patterns** with templates
- **Production-quality code** examples
- **Practice problems** by difficulty

---

## 🎯 Study Plan Recommendation

### Week 1: Foundations (Files 1-4)
**Goal:** Master fundamental data structures
- **Day 1-2:** Arrays (01_array.py)
  - Two pointers, sliding window, prefix sum, Kadane's
  - Focus: 3Sum, Container With Most Water, Subarray Sum
- **Day 3-4:** Strings (02_string.py)
  - Character frequency, palindromes, pattern matching
  - Focus: Longest Substring, Min Window, Valid Parentheses
- **Day 5:** Hash Tables (03_hash_table.py)
  - Two sum patterns, frequency counting, LRU cache
  - Focus: Group Anagrams, Longest Consecutive Sequence
- **Day 6-7:** Linked Lists (04_linked_list.py)
  - Fast & slow pointers, reversal, cycle detection
  - Focus: Reverse List, Merge K Lists, LRU Cache implementation

### Week 2: Algorithm Techniques (Files 5-8)
**Goal:** Learn systematic problem-solving approaches
- **Day 8-9:** Two Pointers & Sliding Window (05, 06)
  - Opposite/same direction, fixed/variable window
  - Focus: 3Sum, Character Replacement, Min Window Substring
- **Day 10-11:** Binary Search (07_binary_search.py)
  - Standard BS, rotated arrays, search on answer space
  - Focus: Rotated Array Search, Koko Bananas, Split Array
- **Day 12-14:** Sorting (08_sorting.py)
  - Quick/merge sort, custom comparators, intervals
  - Focus: Merge Intervals, Largest Number, Quick Select

### Week 3: Trees & Graphs (Files 9, 12)
**Goal:** Master hierarchical and graph structures
- **Day 15-17:** Trees (09_tree_binary_tree.py)
  - DFS/BFS traversals, BST operations, path problems
  - Focus: LCA, Max Path Sum, Serialize/Deserialize
- **Day 18-21:** Graphs (12_graph_dfs_bfs.py)
  - DFS/BFS, topological sort, shortest path
  - Focus: Number of Islands, Course Schedule, Word Ladder

### Week 4: Advanced Topics (Files 10, 11, 13)
**Goal:** Tackle complex algorithmic patterns
- **Day 22-25:** Dynamic Programming (10_dynamic_programming.py)
  - 1D/2D DP, knapsack, LIS/LCS, string DP
  - Focus: Coin Change, Edit Distance, Partition Equal Subset
- **Day 26-27:** Stack/Queue/Heap (11_stack_queue_heap.py)
  - Monotonic stack, sliding window max, top K problems
  - Focus: Largest Rectangle, Sliding Window Max, Median Finder
- **Day 28-30:** Essential Topics (13_essential_topics_consolidated.py)
  - Greedy, backtracking, bit manipulation, Trie, Union Find
  - Focus: N-Queens, Word Search II, Accounts Merge

---

## 📖 File Directory & Quick Reference

### 01_array.py (Lines: ~600)
**Key Patterns:**
- Two Pointers (opposite direction)
- Sliding Window (fixed & variable)
- Prefix Sum
- Kadane's Algorithm
- Dutch National Flag
- Binary Search on Array

**Must-Know Problems:**
- 3Sum (15) - Medium
- Container With Most Water (11) - Medium
- Subarray Sum Equals K (560) - Medium
- Trapping Rain Water (42) - Hard

---

### 02_string.py (Lines: ~650)
**Key Patterns:**
- Character Frequency (HashMap/Array)
- Two Pointers (palindrome check)
- Sliding Window (substrings)
- KMP Pattern Matching
- Parentheses Matching

**Must-Know Problems:**
- Longest Substring Without Repeating (3) - Medium
- Minimum Window Substring (76) - Hard
- Group Anagrams (49) - Medium
- Valid Parentheses (20) - Easy

---

### 03_hash_table.py (Lines: ~600)
**Key Patterns:**
- Two Sum variants
- Frequency Counting (Counter)
- Grouping/Categorization
- Prefix Sum + HashMap
- LRU Cache Design

**Must-Know Problems:**
- Two Sum (1) - Easy
- LRU Cache (146) - Medium
- Longest Consecutive Sequence (128) - Medium
- Group Shifted Strings (249) - Medium

---

### 04_linked_list.py (Lines: ~550)
**Key Patterns:**
- Fast & Slow Pointers (cycle, middle, nth from end)
- In-place Reversal
- Merge Sorted Lists
- Reorder/Partition

**Must-Know Problems:**
- Reverse Linked List (206) - Easy
- Linked List Cycle II (142) - Medium
- Merge K Sorted Lists (23) - Hard
- Copy List with Random Pointer (138) - Medium

---

### 05_two_pointers.py (Lines: ~450)
**Key Patterns:**
- Opposite Direction (two sum, 3sum)
- Same Direction (remove duplicates)
- Partition (Dutch flag)
- Palindrome Checking

**Must-Know Problems:**
- 3Sum (15) - Medium
- Container With Most Water (11) - Medium
- Trapping Rain Water (42) - Hard
- Sort Colors (75) - Medium

---

### 06_sliding_window.py (Lines: ~500)
**Key Patterns:**
- Fixed Size Window
- Variable Size - Maximum Window
- Variable Size - Minimum Window
- At Most K Pattern

**Must-Know Problems:**
- Longest Substring Without Repeating (3) - Medium
- Minimum Window Substring (76) - Hard
- Sliding Window Maximum (239) - Hard
- Longest Repeating Character Replacement (424) - Medium

---

### 07_binary_search.py (Lines: ~600)
**Key Patterns:**
- Standard Binary Search
- Find First/Last Occurrence
- Rotated Sorted Array
- Binary Search on Answer Space
- 2D Matrix Search

**Must-Know Problems:**
- Search in Rotated Sorted Array (33) - Medium
- Find Minimum in Rotated Sorted Array (153) - Medium
- Koko Eating Bananas (875) - Medium
- Split Array Largest Sum (410) - Hard

---

### 08_sorting.py (Lines: ~550)
**Key Patterns:**
- Merge Sort, Quick Sort
- Custom Comparators
- Interval Sorting
- Counting Sort, Bucket Sort
- Quick Select (Kth element)

**Must-Know Problems:**
- Merge Intervals (56) - Medium
- Largest Number (179) - Medium
- Kth Largest Element (215) - Medium
- Meeting Rooms II (253) - Medium

---

### 09_tree_binary_tree.py (Lines: ~700)
**Key Patterns:**
- DFS Traversals (inorder, preorder, postorder)
- BFS Level Order
- Tree Properties (height, diameter, balanced)
- Path Problems (sum, max path)
- Tree Construction
- Lowest Common Ancestor

**Must-Know Problems:**
- Binary Tree Level Order (102) - Medium
- Lowest Common Ancestor (236) - Medium
- Binary Tree Maximum Path Sum (124) - Hard
- Serialize and Deserialize Binary Tree (297) - Hard

---

### 10_dynamic_programming.py (Lines: ~650)
**Key Patterns:**
- Linear DP (Fibonacci, House Robber)
- Grid DP (Unique Paths, Min Path Sum)
- Knapsack (0/1, Unbounded)
- LIS/LCS (Longest Increasing/Common Subsequence)
- Palindrome DP
- String DP (Edit Distance, Word Break)

**Must-Know Problems:**
- Coin Change (322) - Medium
- Longest Increasing Subsequence (300) - Medium
- Edit Distance (72) - Hard
- Longest Common Subsequence (1143) - Medium
- Partition Equal Subset Sum (416) - Medium

---

### 11_stack_queue_heap.py (Lines: ~600)
**Key Patterns:**
- Stack: Expression Evaluation, Next Greater Element
- Monotonic Stack/Queue
- Design Problems (MinStack)
- Heap: Top K, Merge K Sorted, Median Tracking

**Must-Know Problems:**
- Valid Parentheses (20) - Easy
- Daily Temperatures (739) - Medium
- Largest Rectangle in Histogram (84) - Hard
- Sliding Window Maximum (239) - Hard
- Find Median from Data Stream (295) - Hard

---

### 12_graph_dfs_bfs.py (Lines: ~650)
**Key Patterns:**
- DFS (Recursive & Iterative)
- BFS (Shortest Path)
- Connected Components
- Cycle Detection
- Topological Sort
- Bipartite Check

**Must-Know Problems:**
- Number of Islands (200) - Medium
- Course Schedule (207) - Medium
- Clone Graph (133) - Medium
- Word Ladder (127) - Hard
- Pacific Atlantic Water Flow (417) - Medium

---

### 13_essential_topics_consolidated.py (Lines: ~700)
**Covers:**
- **Greedy:** Jump Game, Gas Station, Partition Labels
- **Backtracking:** Permutations, Subsets, N-Queens, Word Search
- **Bit Manipulation:** Single Number, Counting Bits, Reverse Bits
- **Trie:** Implement Trie, Word Search II
- **Union Find:** Connected Components, Accounts Merge
- **Math:** GCD, Primes, Modular Arithmetic

**Must-Know Problems:**
- Permutations (46) - Medium
- N-Queens (51) - Hard
- Word Search II (212) - Hard
- Accounts Merge (721) - Medium

---

## 🎓 Interview Preparation Tips

### 1. **Pattern Recognition**
Most problems fall into these categories:
- **Array/String:** Two pointers, sliding window, prefix sum
- **Tree/Graph:** DFS, BFS, topological sort
- **Optimization:** DP, greedy, binary search on answer
- **Design:** Stack, queue, heap, LRU cache

### 2. **Time Complexity Goals**
- **O(n):** Optimal for single pass (hash map, two pointers)
- **O(n log n):** Sorting, heap operations, binary search
- **O(n²):** Acceptable for n ≤ 1000 (2D DP)
- **O(2ⁿ):** Backtracking, subsets (n ≤ 20)

### 3. **Space Complexity Optimization**
- Can you reduce 2D DP to 1D?
- Use two pointers instead of extra arrays?
- In-place modification allowed?

### 4. **Communication Template**
1. **Clarify:** Ask about edge cases, constraints
2. **Example:** Walk through 2-3 examples
3. **Approach:** Explain algorithm, time/space complexity
4. **Code:** Write clean, production-quality code
5. **Test:** Verify with edge cases

### 5. **Common Edge Cases**
- Empty input (`[]`, `""`, `None`)
- Single element
- Duplicates
- Negative numbers
- Integer overflow
- Large inputs (n = 10⁵)

---

## 🔥 Top 50 Problems to Master

### Easy (10)
1. Two Sum (1)
2. Valid Parentheses (20)
3. Merge Two Sorted Lists (21)
4. Best Time to Buy/Sell Stock (121)
5. Valid Palindrome (125)
6. Invert Binary Tree (226)
7. Climbing Stairs (70)
8. Maximum Subarray (53)
9. Contains Duplicate (217)
10. Reverse Linked List (206)

### Medium (30)
11. 3Sum (15)
12. Longest Substring Without Repeating (3)
13. Container With Most Water (11)
14. Group Anagrams (49)
15. Longest Palindromic Substring (5)
16. Product of Array Except Self (238)
17. Subarray Sum Equals K (560)
18. Merge Intervals (56)
19. Binary Tree Level Order (102)
20. Validate BST (98)
21. Kth Largest Element (215)
22. Course Schedule (207)
23. Number of Islands (200)
24. LRU Cache (146)
25. Coin Change (322)
26. Longest Increasing Subsequence (300)
27. Word Break (139)
28. House Robber (198)
29. Implement Trie (208)
30. Top K Frequent Elements (347)
31. Rotate Image (48)
32. Search in Rotated Sorted Array (33)
33. Permutations (46)
34. Combination Sum (39)
35. Unique Paths (62)
36. Decode Ways (91)
37. Clone Graph (133)
38. Accounts Merge (721)
39. Daily Temperatures (739)
40. Longest Repeating Character Replacement (424)

### Hard (10)
41. Trapping Rain Water (42)
42. Merge K Sorted Lists (23)
43. Minimum Window Substring (76)
44. Binary Tree Maximum Path Sum (124)
45. Word Ladder (127)
46. Word Search II (212)
47. Largest Rectangle in Histogram (84)
48. Sliding Window Maximum (239)
49. Edit Distance (72)
50. Find Median from Data Stream (295)

---

## 🚀 Quick Start
1. **Start with:** `01_array.py` - Most common interview topic
2. **Practice:** Solve 2-3 problems from each pattern
3. **Review:** Tricky parts section in each file
4. **Code:** Write solutions from scratch, don't just read
5. **Optimize:** Always analyze time/space complexity

---

## 📝 Python-Specific Tips

### Collections
```python
from collections import Counter, defaultdict, deque, OrderedDict
```

### Heap (Min Heap only)
```python
import heapq
# Max heap: negate values
heapq.heappush(heap, -val)
```

### Binary Search
```python
import bisect
bisect.bisect_left(arr, x)  # Leftmost position
bisect.bisect_right(arr, x)  # Rightmost position
```

### Sorting
```python
sorted(arr, key=lambda x: (x[0], -x[1]))  # Multiple criteria
arr.sort(reverse=True)  # In-place descending
```

### String Operations
```python
''.join(chars)  # O(n) - use instead of += in loop
s.split()  # Split by whitespace
```

---

## 🎯 Final Checklist Before Interview
- [ ] Solved 50+ Medium problems
- [ ] Solved 10+ Hard problems
- [ ] Can explain time/space complexity
- [ ] Comfortable with all 13 file topics
- [ ] Practiced coding without IDE help
- [ ] Can write bug-free code in 30-40 min
- [ ] Comfortable with edge cases
- [ ] Can optimize brute force solutions

---

## 📌 Remember
- **Quality > Quantity:** Deeply understand 100 problems > superficially know 300
- **Patterns > Problems:** Master patterns, not specific problems
- **Practice Talking:** Explain your approach out loud
- **Time Management:** 5 min clarify, 10 min approach, 20 min code, 5 min test

**Good luck with your Mistral AI interview! 🚀**

---

*Last Updated: 2026-01-04*
*Total Lines of Code: ~8000+*
*Total Problems Covered: 200+*
