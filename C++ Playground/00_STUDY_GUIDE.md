# C++ Interview Preparation — Complete Study Guide

## Overview
This collection mirrors the Python and Java playgrounds in structure and depth,
covering all essential topics for **coding interviews** and **LeetCode Medium/Hard**
problems in modern C++ (C++17). Each file contains:
- Core concepts with C++-specific nuances
- Tricky parts (pitfalls unique to C++)
- Common patterns with STL-idiomatic templates
- Production-quality code at **Google C++ Style Guide** standards
- Practice problems by difficulty

---

## Google C++ Style Quick Reference

```cpp
// Naming
ClassName, FunctionName()          // UpperCamelCase for types & functions
local_variable, parameter_name    // snake_case for variables & params
member_variable_                   // trailing underscore for class members
kConstantName                      // kCamelCase for constants
MACRO_NAME                         // ALL_CAPS for macros only

// Headers — include in this order, each group alpha-sorted:
#include <system_header>           // 1. Standard library
#include <third_party>             // 2. Third-party
#include "local_header.h"          // 3. Project headers

// Prefer these over raw alternatives
nullptr        over NULL
int64_t        over long (platform-independent)
const&         for read-only params larger than a word
std::move()    for transferring ownership
```

---

## C++ vs Java/Python — Key Differences

### Memory & Ownership
```cpp
// Raw pointer (avoid unless necessary)
ListNode* node = new ListNode(1);
delete node;  // manual cleanup!

// Prefer smart pointers
auto node = std::make_unique<ListNode>(1);  // auto-deleted when out of scope
std::shared_ptr<TreeNode> root;             // reference-counted

// Stack allocation (cheapest, always prefer for small objects)
std::vector<int> vec = {1, 2, 3};  // manages its own memory
```

### STL Container Quick Reference
```cpp
#include <vector>          std::vector<int>                 // dynamic array
#include <string>          std::string                      // mutable string
#include <unordered_map>   std::unordered_map<K,V>          // O(1) avg HashMap
#include <unordered_set>   std::unordered_set<K>            // O(1) avg HashSet
#include <map>             std::map<K,V>                    // O(log n) sorted map
#include <set>             std::set<K>                      // O(log n) sorted set
#include <queue>           std::queue<T>                    // BFS queue
                           std::priority_queue<T>           // max-heap
                           std::priority_queue<T,           // min-heap
                             std::vector<T>, std::greater<T>>
#include <stack>           std::stack<T>                    // LIFO
#include <deque>           std::deque<T>                    // double-ended queue
#include <list>            std::list<T>                     // doubly linked list
#include <algorithm>       std::sort, std::binary_search,   // algorithms
                           std::max, std::min, std::reverse
#include <numeric>         std::accumulate, std::iota       // numeric ops
#include <climits>         INT_MAX, INT_MIN, LLONG_MAX      // limits
```

### Passing Parameters
```cpp
void ReadOnly(const std::vector<int>& nums);   // read-only — pass by const ref
void Modify(std::vector<int>& nums);            // in-place modify — pass by ref
void Take(std::vector<int> nums);               // takes ownership copy — rare
std::vector<int> Return();                      // return by value (RVO optimises)
```

### Sorting with Custom Comparator
```cpp
// Sort ascending (default)
std::sort(v.begin(), v.end());

// Sort descending
std::sort(v.begin(), v.end(), std::greater<int>());

// Custom comparator (lambda)
std::sort(intervals.begin(), intervals.end(),
          [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[0] < b[0];  // sort by first element
          });

// Sort by frequency then value
std::sort(v.begin(), v.end(), [&freq](int a, int b) {
  return freq[a] != freq[b] ? freq[a] > freq[b] : a < b;
});
```

### String Operations
```cpp
std::string s = "hello";
s.size()                    // length (prefer over s.length())
s[i]                        // char access (no bounds check)
s.at(i)                     // char access (bounds checked)
s.substr(pos, len)          // substring
s.find("ll")                // first occurrence, npos if not found
s += "world"                // append (prefer over s = s + "world")
std::to_string(42)          // int → string
std::stoi("42")             // string → int
s.begin(), s.end()          // iterators for std::sort etc.
std::reverse(s.begin(), s.end());
```

### Integer Overflow
```cpp
// Prefer int64_t for sums that can overflow 32-bit
int64_t total = static_cast<int64_t>(a) * b;

// Safe midpoint in binary search — NEVER (left + right) / 2
int mid = left + (right - left) / 2;

// Limits
INT_MAX   // 2,147,483,647  (2^31 − 1)
INT_MIN   // −2,147,483,648 (−2^31)
LLONG_MAX // 9,223,372,036,854,775,807
```

### Useful Patterns
```cpp
// Auto type deduction
auto it = my_map.find(key);
if (it != my_map.end()) { /* found */ }

// Range-based for
for (const auto& val : vec) { /* read-only */ }
for (auto& val : vec)       { /* modifiable */ }

// Structured bindings (C++17)
for (const auto& [key, val] : my_map) { }
auto [first, second] = std::make_pair(1, 2);

// Initialise with default
std::unordered_map<int, int> freq;
freq[key]++;           // default-constructs to 0, then increments

// emplace vs push_back (avoids extra copy)
vec.emplace_back(args...);
pq.emplace(args...);
```

---

## Study Plan (4 Weeks)

### Week 1 — Foundations (Files 01–04)
| Day | File | Focus Problems |
|-----|------|----------------|
| 1–2 | 01_Array.cpp | 3Sum (15), Container With Most Water (11), Subarray Sum K (560) |
| 3–4 | 02_String.cpp | Longest Substring (3), Min Window Substring (76), Group Anagrams (49) |
| 5   | 03_HashTable.cpp | LRU Cache (146), Longest Consecutive (128) |
| 6–7 | 04_LinkedList.cpp | Merge K Lists (23), Reverse K-Group (25) |

### Week 2 — Algorithm Techniques (Files 05–08)
| Day | File | Focus Problems |
|-----|------|----------------|
| 8–9  | 05_TwoPointers.cpp + 06_SlidingWindow.cpp | Trapping Rain Water (42), Min Window (76) |
| 10–11 | 07_BinarySearch.cpp | Koko Bananas (875), Split Array (410) |
| 12–14 | 08_Sorting.cpp | Kth Largest (215), Merge Intervals (56), Largest Number (179) |

### Week 3 — Trees & Graphs (Files 09, 12)
| Day | File | Focus Problems |
|-----|------|----------------|
| 15–17 | 09_TreeBinaryTree.cpp | Max Path Sum (124), Serialize/Deserialize (297), LCA (236) |
| 18–21 | 12_GraphDfsBfs.cpp | Course Schedule (207), Word Ladder (127), Accounts Merge (721) |

### Week 4 — Advanced (Files 10, 11, 13–17)
| Day | File | Focus Problems |
|-----|------|----------------|
| 22–25 | 10_DynamicProgramming.cpp | Edit Distance (72), Partition Subset (416), Burst Balloons (312) |
| 26–27 | 11_StackQueueHeap.cpp | Largest Rectangle (84), Sliding Window Max (239), Median Finder (295) |
| 28–30 | 13–17 | N-Queens (51), Word Search II (212), Accounts Merge (721) |

---

## File Directory

| File | Topic | Key Patterns |
|------|-------|-------------|
| 01_Array.cpp | Arrays | Two pointers, sliding window, prefix sum, Kadane's, Dutch flag |
| 02_String.cpp | Strings | Frequency array, KMP, palindrome, window matching |
| 03_HashTable.cpp | Hash Maps/Sets | Two sum variants, LRU cache, grouping, consecutive |
| 04_LinkedList.cpp | Linked Lists | Fast/slow pointers, reversal, merge, cycle detection |
| 05_TwoPointers.cpp | Two Pointers | Opposite direction, same direction, partition |
| 06_SlidingWindow.cpp | Sliding Window | Fixed, variable max/min, at-most-K, deque |
| 07_BinarySearch.cpp | Binary Search | Standard, rotated, answer-space, 2D matrix |
| 08_Sorting.cpp | Sorting | Merge/quick sort, comparators, intervals, quick-select |
| 09_TreeBinaryTree.cpp | Trees | DFS/BFS, BST, path, LCA, serialize |
| 10_DynamicProgramming.cpp | DP | Knapsack, LIS/LCS, string DP, interval DP |
| 11_StackQueueHeap.cpp | Stack/Queue/Heap | Monotonic stack, design, median finder, top-K |
| 12_GraphDfsBfs.cpp | Graphs | DFS/BFS, topo sort, Dijkstra, union-find |
| 13_EssentialTopics.cpp | Essentials | Greedy, backtracking, bit manipulation |
| 14_UnionFind.cpp | Union-Find (DSU) | Path compression, rank, dynamic connectivity |
| 15_Trie.cpp | Trie | Prefix tree, wildcard search, word search II |
| 16_AdvancedTopics.cpp | Advanced | Monotonic stack, prefix sum, interval scheduling, LFU |
| 17_Matrix.cpp | Matrix | Spiral, BFS/DFS, DP, Game of Life, rotate |

---

## Top 50 Problems to Master

### Easy (10)
1. Two Sum (1) · Valid Parentheses (20) · Merge Two Sorted Lists (21)
4. Best Time to Buy Stock (121) · Valid Palindrome (125)
6. Invert Binary Tree (226) · Climbing Stairs (70)
8. Maximum Subarray (53) · Contains Duplicate (217) · Reverse Linked List (206)

### Medium (30)
11. 3Sum (15) · Longest Substring Without Repeating (3)
13. Container With Most Water (11) · Group Anagrams (49)
15. Longest Palindromic Substring (5) · Product Except Self (238)
17. Subarray Sum Equals K (560) · Merge Intervals (56)
19. Binary Tree Level Order (102) · Validate BST (98)
21. Kth Largest Element (215) · Course Schedule (207)
23. Number of Islands (200) · LRU Cache (146)
25. Coin Change (322) · Longest Increasing Subsequence (300)
27. Word Break (139) · House Robber (198)
29. Implement Trie (208) · Top K Frequent Elements (347)
31. Rotate Image (48) · Search Rotated Array (33)
33. Permutations (46) · Combination Sum (39)
35. Unique Paths (62) · Decode Ways (91)
37. Clone Graph (133) · Accounts Merge (721)
39. Daily Temperatures (739) · Character Replacement (424)

### Hard (10)
41. Trapping Rain Water (42) · Merge K Sorted Lists (23)
43. Minimum Window Substring (76) · Binary Tree Max Path Sum (124)
45. Word Ladder (127) · Word Search II (212)
47. Largest Rectangle in Histogram (84) · Sliding Window Maximum (239)
49. Edit Distance (72) · Find Median from Data Stream (295)

---

## C++ Interview Tips

### Before You Code
1. **Clarify** constraints (n size → choose O(n) or O(n log n))
2. **Pick the right container** — `unordered_map` for O(1), `map` for ordered
3. **Check for overflow** — use `int64_t` when multiplying or summing large values

### Common Mistakes to Avoid
```cpp
// ❌ Integer overflow in binary search
int mid = (left + right) / 2;      // overflows when left+right > INT_MAX
// ✅ Safe version
int mid = left + (right - left) / 2;

// ❌ Comparing signed and unsigned
for (int i = 0; i < vec.size(); i++)  // vec.size() is size_t (unsigned)
// ✅ Cast or use range-based for
for (int i = 0; i < static_cast<int>(vec.size()); i++)

// ❌ Iterator invalidation
for (auto it = vec.begin(); it != vec.end(); ++it)
    if (condition) vec.erase(it);   // invalidates iterator!
// ✅ Use erase-remove idiom
vec.erase(std::remove_if(vec.begin(), vec.end(), condition), vec.end());

// ❌ Modifying unordered_map while iterating
for (auto& [k, v] : my_map) my_map.erase(k);  // undefined behaviour
// ✅ Collect keys first, then erase

// ❌ Using [] on const map (inserts default if missing)
const std::unordered_map<int,int> m;
auto val = m[key];  // compile error on const map
// ✅ Use .at() or .find()
auto it = m.find(key);
```

### Compile & Run Template
```cpp
#include <bits/stdc++.h>    // convenience include (acceptable in competitive/interview)
using namespace std;

int main() {
    // test cases here
    return 0;
}
// g++ -std=c++17 -O2 -Wall -o solution 01_Array.cpp && ./solution
```

---

*Last Updated: 2026-03-23 | C++17 | Google C++ Style Guide*
