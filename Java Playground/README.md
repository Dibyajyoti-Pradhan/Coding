# Java Interview Playground - Senior SWE Standards

This directory contains **5 comprehensive Java files** (3,752 lines of production-grade code) implementing essential coding interview patterns at **Google Senior SWE standards**.

## Files Overview

### **09_TreeBinaryTree.java** (769 lines, 21 methods)
- **DFS Traversals:** Inorder, Preorder, Postorder (recursive + iterative)
- **BFS:** Level-order, Zigzag level-order
- **Tree Properties:** Max depth, balanced check, diameter
- **Path Problems:** Has path sum, max path sum
- **BST Operations:** Validation, LCA, kth smallest
- **Tree Construction:** Build from preorder+inorder, serialize/deserialize

**LeetCode Problems:** 94, 102, 103, 104, 110, 112, 124, 143, 144, 145, 230, 236, 297

---

### **10_DynamicProgramming.java** (658 lines, 17 methods)
- **Linear DP:** Climbing stairs, house robber (I & II)
- **Grid DP:** Unique paths, min path sum
- **Knapsack:** Unbounded coin change, 0/1 subset partition
- **LIS/LCS:** O(n log n) LIS, longest common subsequence
- **Palindrome:** Longest palindromic subsequence, min cuts
- **String DP:** Edit distance, word break
- **Stock Trading:** One transaction, unlimited, with cooldown

**LeetCode Problems:** 70, 72, 98, 121, 122, 132, 139, 143, 198, 213, 300, 309, 322, 338, 416, 516

---

### **11_StackQueueHeap.java** (611 lines, 13 methods + 2 inner classes)
- **Basic Stack:** Valid parentheses, decode string
- **Monotonic Stack:** Daily temperatures, next greater, histogram, rain water
- **MinStack:** O(1) getMin with two stacks
- **Sliding Window:** Monotonic deque for max in window
- **Heap (Top-K):** Top k frequent, kth largest, k closest points
- **Median Finder:** Two heaps for dynamic median

**LeetCode Problems:** 20, 42, 84, 155, 239, 295, 347, 394, 496, 739

---

### **12_GraphDfsBfs.java** (858 lines, 16 methods + 2 inner classes)
- **DFS on Grids:** Number of islands, max area, Pacific Atlantic
- **BFS Shortest Path:** Binary matrix, word ladder, rotting oranges
- **Graph Cloning:** With cycle handling via HashMap
- **Connected Provinces:** Adjacency matrix traversal
- **Cycle Detection:** 3-color DFS approach
- **Topological Sort:** Kahn's BFS algorithm
- **Bipartite Check:** 2-coloring validation
- **Union Find:** Path compression + union by rank

**LeetCode Problems:** 133, 200, 207, 210, 212, 323, 417, 547, 695, 721, 785, 1091, 127, 994

---

### **13_EssentialTopics.java** (856 lines, 20 methods + 2 inner classes)
- **Greedy:** Jump game, gas station, partition labels
- **Backtracking:** Permutations, subsets, combinations, N-Queens, word search
- **Bit Manipulation:** Single number (XOR), count bits, reverse bits, missing number
- **Trie:** Insert, search, startsWith; word search II
- **Math:** GCD, prime checking, Sieve of Eratosthenes, fast exponentiation

**LeetCode Problems:** 39, 45, 46, 50, 51, 55, 78, 79, 134, 136, 138, 190, 212, 215, 268, 338, 763, 785

---

## Google Java Style Guide Compliance

### ✓ Code Quality Standards
- **2-space indentation** throughout
- **100-character line limit** enforced
- **No wildcard imports** — each class imported explicitly
- **Private utility class constructors** to prevent instantiation
- **Defensive null checks** at method entry points (IllegalArgumentException)
- **Final classes** for utility classes

### ✓ Documentation Standards
- **Class-level Javadoc** with comprehensive descriptions
- **Method-level Javadoc** with:
  - Description of purpose
  - `@param` tags for all parameters
  - `@return` tags with type and behavior
  - `@throws` tags for checked exceptions
  - LeetCode problem number & difficulty
  - Time/space complexity analysis
  - Tricky insights & edge case notes

### ✓ Naming Conventions
- **Classes:** `UpperCamelCase` (e.g., `TreeBinaryTree`, `MinStack`)
- **Methods/Variables:** `lowerCamelCase` (e.g., `inorderTraversal`, `maxDepth`)
- **Constants:** `UPPER_SNAKE_CASE`, declared `private static final`

### ✓ Code Idioms
- **`@Override`** annotation on overridden methods
- **Braces** for all control structures (if, for, while)
- **Enhanced for loops** for iterating collections
- **Proper exception handling** with meaningful messages
- **Immutable helper objects** where appropriate

---

## Statistics

| Metric | Count |
|--------|-------|
| Total Lines | 3,752 |
| Public Methods | 87 |
| Inner Classes | 4 (TreeNode, MinStack, Trie, UnionFind) |
| LeetCode Problems Covered | 60+ |
| Time Complexity Analysis | Every method |
| Complete Test Cases (main) | 5 |

---

## Usage Examples

### Compile
```bash
javac *.java
```

### Run Individual File
```bash
java TreeBinaryTree
java DynamicProgramming
java StackQueueHeap
java GraphDfsBfs
java EssentialTopics
```

### Test Output
Each file includes a comprehensive `main()` method demonstrating:
- Real LeetCode examples
- Expected outputs
- Edge case handling

---

## Design Patterns & Insights

### Tree Algorithms
- Recursion vs. iteration tradeoffs
- DFS traversal order semantics
- Binary search tree invariants
- Balanced tree properties

### Dynamic Programming
- Top-down (memoization) vs. bottom-up (tabulation)
- Space optimization techniques (1D from 2D)
- State machine design for stock problems
- LIS binary search optimization

### Graph Algorithms
- Adjacency list vs. matrix tradeoffs
- DFS cycle detection with colors
- Topological sort with Kahn's algorithm
- Union Find path compression benefits

### Advanced Data Structures
- Monotonic stack/deque invariants
- Heap property maintenance
- Trie prefix compression
- Hash-based time/space tradeoffs

---

## References

- **Google Java Style Guide:** https://google.github.io/styleguide/javaguide.html
- **LeetCode:** https://leetcode.com
- **Effective Java (3rd Edition):** Item-based design patterns

---

**Created:** 2026-03-18  
**Standards:** Google Senior SWE Coding Standards  
**Total Development:** 3,752 lines of production-grade Java
