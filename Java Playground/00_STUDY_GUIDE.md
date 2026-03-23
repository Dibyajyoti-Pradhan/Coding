# Java Interview Preparation - Complete Study Guide

## 📚 Overview
This comprehensive collection covers all essential topics for **coding interviews** and **LeetCode Medium/Hard** problems in Java. Each file contains:
- **Core concepts** explained clearly with Java-specific nuances
- **Tricky parts** to watch out for (Java gotchas)
- **Common patterns** with templates
- **Production-quality code** examples
- **Practice problems** by difficulty

---

## 🎯 Study Plan Recommendation

### Week 1: Foundations (Files 1-4)
**Goal:** Master fundamental data structures in Java
- **Day 1-2:** Arrays (01_Array.java)
  - Two pointers, sliding window, prefix sum, Kadane's
  - Focus: 3Sum, Container With Most Water, Subarray Sum
- **Day 3-4:** Strings (02_String.java)
  - Character frequency, palindromes, pattern matching
  - Focus: Longest Substring, Min Window, Valid Parentheses
- **Day 5:** Hash Tables (03_HashTable.java)
  - Two sum patterns, frequency counting, LRU cache
  - Focus: Group Anagrams, Longest Consecutive Sequence
- **Day 6-7:** Linked Lists (04_LinkedList.java)
  - Fast & slow pointers, reversal, cycle detection
  - Focus: Reverse List, Merge K Lists, LRU Cache implementation

### Week 2: Algorithm Techniques (Files 5-8)
**Goal:** Learn systematic problem-solving approaches
- **Day 8-9:** Two Pointers & Sliding Window (05, 06)
  - Opposite/same direction, fixed/variable window
  - Focus: 3Sum, Character Replacement, Min Window Substring
- **Day 10-11:** Binary Search (07_BinarySearch.java)
  - Standard BS, rotated arrays, search on answer space
  - Focus: Rotated Array Search, Koko Bananas, Split Array
- **Day 12-14:** Sorting (08_Sorting.java)
  - Quick/merge sort, custom comparators, intervals
  - Focus: Merge Intervals, Largest Number, Quick Select

### Week 3: Trees & Graphs (Files 9, 12)
**Goal:** Master hierarchical and graph structures
- **Day 15-17:** Trees (09_TreeBinaryTree.java)
  - DFS/BFS traversals, BST operations, path problems
  - Focus: LCA, Max Path Sum, Serialize/Deserialize
- **Day 18-21:** Graphs (12_GraphDfsBfs.java)
  - DFS/BFS, topological sort, shortest path
  - Focus: Number of Islands, Course Schedule, Word Ladder

### Week 4: Advanced Topics (Files 10, 11, 13)
**Goal:** Tackle complex algorithmic patterns
- **Day 22-25:** Dynamic Programming (10_DynamicProgramming.java)
  - 1D/2D DP, knapsack, LIS/LCS, string DP
  - Focus: Coin Change, Edit Distance, Partition Equal Subset
- **Day 26-27:** Stack/Queue/Heap (11_StackQueueHeap.java)
  - Monotonic stack, sliding window max, top K problems
  - Focus: Largest Rectangle, Sliding Window Max, Median Finder
- **Day 28-30:** Essential Topics (13_EssentialTopics.java)
  - Greedy, backtracking, bit manipulation, Trie, Union Find
  - Focus: N-Queens, Word Search II, Accounts Merge

---

## 📖 File Directory & Quick Reference

### 01_Array.java
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

### 02_String.java
**Key Patterns:**
- Character Frequency (HashMap/int[26])
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

### 03_HashTable.java
**Key Patterns:**
- Two Sum variants
- Frequency Counting
- Grouping/Categorization
- Prefix Sum + HashMap
- LRU Cache Design (LinkedHashMap)

**Must-Know Problems:**
- Two Sum (1) - Easy
- LRU Cache (146) - Medium
- Longest Consecutive Sequence (128) - Medium
- Group Shifted Strings (249) - Medium

---

### 04_LinkedList.java
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

### 05_TwoPointers.java
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

### 06_SlidingWindow.java
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

### 07_BinarySearch.java
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

### 08_Sorting.java
**Key Patterns:**
- Merge Sort, Quick Sort
- Custom Comparators (Comparator interface)
- Interval Sorting
- Counting Sort, Bucket Sort
- Quick Select (Kth element)

**Must-Know Problems:**
- Merge Intervals (56) - Medium
- Largest Number (179) - Medium
- Kth Largest Element (215) - Medium
- Meeting Rooms II (253) - Medium

---

### 09_TreeBinaryTree.java
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

### 10_DynamicProgramming.java
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

### 11_StackQueueHeap.java
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

### 12_GraphDfsBfs.java
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

### 13_EssentialTopics.java
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
- Empty input (`null`, `[]`, `""`)
- Single element
- Duplicates
- Negative numbers
- Integer overflow (use `long` when needed)
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

## ☕ Java-Specific Tips

### Key Imports
```java
import java.util.*;          // ArrayList, HashMap, LinkedList, PriorityQueue, etc.
import java.util.stream.*;   // Stream API
import java.util.Arrays;     // Arrays.sort(), Arrays.fill()
import java.util.Collections; // Collections.sort(), Collections.reverse()
```

### Common Data Structures
```java
// Dynamic Array
List<Integer> list = new ArrayList<>();

// HashMap
Map<Integer, Integer> map = new HashMap<>();
map.getOrDefault(key, 0);  // Safe get

// HashSet
Set<Integer> set = new HashSet<>();

// Queue (BFS)
Queue<Integer> queue = new LinkedList<>();
queue.offer(val);  queue.poll();  queue.peek();

// Stack
Deque<Integer> stack = new ArrayDeque<>();
stack.push(val);  stack.pop();  stack.peek();

// Min Heap (PriorityQueue)
PriorityQueue<Integer> minHeap = new PriorityQueue<>();

// Max Heap
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
```

### Integer Overflow
```java
// Use long for large sums
long sum = 0L;
int mid = left + (right - left) / 2;  // Avoid overflow in binary search
Integer.MAX_VALUE  // 2^31 - 1 = 2,147,483,647
Integer.MIN_VALUE  // -2^31 = -2,147,483,648
```

### Sorting with Custom Comparator
```java
// Sort array of arrays by first element
Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

// Sort strings by length then alphabetically
list.sort((a, b) -> a.length() != b.length() ? a.length() - b.length() : a.compareTo(b));

// Sort in reverse
Arrays.sort(arr, Collections.reverseOrder());  // Only for Integer[]
```

### String Operations
```java
char[] chars = s.toCharArray();
String str = new String(chars);              // char[] -> String
StringBuilder sb = new StringBuilder();
sb.append('a');  sb.toString();              // Build string efficiently
s.charAt(i);                                 // Access character
s.substring(left, right);                   // [left, right) exclusive
String.valueOf(num);                         // int -> String
Integer.parseInt(str);                       // String -> int
```

### Arrays
```java
int[] arr = new int[n];                      // Default: 0
int[][] matrix = new int[m][n];             // Default: 0
Arrays.fill(arr, -1);                        // Fill with value
Arrays.sort(arr);                            // Sort ascending
int[] copy = Arrays.copyOf(arr, arr.length);// Copy array
Arrays.copyOfRange(arr, from, to);          // Copy range [from, to)
```

---

## 🎯 Final Checklist Before Interview
- [ ] Solved 50+ Medium problems in Java
- [ ] Solved 10+ Hard problems
- [ ] Can explain time/space complexity
- [ ] Comfortable with all 13 file topics
- [ ] Practiced coding without IDE help
- [ ] Can write bug-free Java code in 30-40 min
- [ ] Comfortable with Java collections API
- [ ] Can handle integer overflow edge cases

---

## 📌 Remember
- **Quality > Quantity:** Deeply understand 100 problems > superficially know 300
- **Patterns > Problems:** Master patterns, not specific problems
- **Practice Talking:** Explain your approach out loud
- **Time Management:** 5 min clarify, 10 min approach, 20 min code, 5 min test
- **Java Specifics:** Always consider null checks, integer overflow, and use appropriate collections

**Good luck with your interview! 🚀**

---

*Last Updated: 2026-03-18*
*Total Lines of Code: ~8000+*
*Total Problems Covered: 200+*
