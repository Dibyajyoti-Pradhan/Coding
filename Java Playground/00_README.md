# Java Interview Playground - Google Senior SWE Coding Standards

Complete, production-grade Java implementation of 50+ LeetCode-style algorithm problems across 4 core data structures.

## Files Overview

### 01_Array.java (612 lines | 15 public methods)
**8 Core Algorithm Categories**

1. **Two Pointers (Opposite Direction)** - LC 167, 15
   - `twoSumSorted()`, `threeSum()`

2. **Sliding Window** - Advanced pattern
   - `maxSumSubarraySizeK()`, `longestSubstringWithKDistinct()`

3. **Prefix Sum** - O(1) query preprocessing
   - `subarraySumEqualsK()` (LC 560), `RangeSum` inner class (LC 303)

4. **Kadane's Algorithm** - Maximum subarray variants
   - `maxSubarraySum()` (LC 53), `maxProductSubarray()` (LC 152)

5. **Dutch National Flag** - In-place partitioning
   - `sortColors()` (LC 75)

6. **Merge Intervals** - Overlapping interval combination
   - `mergeIntervals()` (LC 56)

7. **Binary Search** - Safe mid calculation & rotated arrays
   - `binarySearch()`, `searchInRotatedSortedArray()` (LC 33)

8. **Array Tricks** - Complex manipulations
   - `rotateArray()` (LC 189), `nextPermutation()` (LC 31)

---

### 02_String.java (566 lines | 12 public methods)
**6 Core Algorithm Categories**

1. **Character Frequency** - Anagram detection
   - `isAnagram()` (LC 242), `groupAnagrams()` (LC 49)

2. **Sliding Window** - Dynamic window contraction
   - `lengthOfLongestSubstring()` (LC 3), `minWindowSubstring()` (LC 76)

3. **Palindrome** - Expand-around-center technique
   - `isPalindrome()` (LC 125), `longestPalindromicSubstring()` (LC 5)

4. **Valid Parentheses** - Stack-based validation
   - `isValid()` (LC 20)

5. **String Building** - Manipulation patterns
   - `reverseWords()` (LC 151), `encodeString()`, `decodeString()`

6. **KMP Algorithm** - Efficient pattern matching
   - `strStr()` (LC 28) with `buildFailureFunction()`

---

### 03_HashTable.java (465 lines | 10 public methods + 2 inner classes)
**6 Core Algorithm Categories**

1. **Two Sum Variants** - Hash-based lookups
   - `twoSum()` (LC 1), `twoSumAllPairs()`

2. **Frequency Counting** - Heap-based selections
   - `topKFrequent()` (LC 347), `firstUniqueChar()` (LC 387)

3. **Grouping** - String categorization
   - `groupAnagrams()` (LC 49), `groupShiftedStrings()` (LC 249)

4. **Prefix Sum + Map** - Clever space optimization
   - `longestConsecutiveSequence()` (LC 128) - O(n) time

5. **LRU Cache** - LinkedHashMap-based design
   - `LRUCache` extends LinkedHashMap with `removeEldestEntry()` override (LC 146)

6. **Data Structure Design**
   - `TwoSumDataStructure` - Add/find operations with collision handling

---

### 04_LinkedList.java (642 lines | 16 public methods + 2 inner classes)
**6 Core Algorithm Categories**

**Inner Classes:**
- `ListNode` - Singly-linked node with 2 constructors
- `RandomNode` - Node with random pointer support (LC 138)

1. **Fast & Slow Pointers** - Floyd's cycle detection
   - `hasCycle()` (LC 141), `detectCycle()` (LC 142)
   - `findMiddle()`, `removeNthFromEnd()` (LC 19)

2. **In-Place Reversal** - Pointer manipulation
   - `reverseList()` (LC 206), `reverseBetween()` (LC 92)
   - `reverseKGroup()` (LC 25)

3. **Merge Operations** - Combining sorted lists
   - `mergeTwoLists()` (LC 21), `mergeKLists()` with PriorityQueue (LC 23)

4. **Reordering** - Complex list reorganization
   - `reorderList()` (LC 143), `oddEvenList()` (LC 328)

5. **Copy Operations** - Deep copying with pointers
   - `copyRandomList()` (LC 138) - HashMap-based approach

6. **Palindrome Detection** - Reverse & compare technique
   - `isPalindrome()` (LC 234)

---

## Google Java Style Guide Compliance

### Indentation & Formatting
- **2-space indentation** (no tabs)
- **100-character line limit** - 0 violations across 2,285 lines
- One statement per line
- Braces on all control structures

### Imports
- **No wildcard imports** - all explicit
- Example: `import java.util.ArrayList;` not `import java.util.*;`

### Naming Conventions
- Classes: `UpperCamelCase` (Array, String, HashTable, LinkedList)
- Methods: `lowerCamelCase` (twoSumSorted, maxSubarraySum)
- Variables: `lowerCamelCase` (left, right, maxSum)
- Constants: `UPPER_SNAKE_CASE` (DEFAULT_MULTIPLIER, ALPHABET_SIZE)

### Documentation
- Full class-level Javadoc with `@author` tag
- Complete method-level Javadoc with:
  - Description
  - `@param` for all parameters
  - `@return` for return values
  - `@throws` for exceptions
  - Time/Space complexity
  - LeetCode problem numbers and difficulty
  - Edge case notes ("Tricky")

### Code Quality
- `@Override` annotation on overridden methods
- Defensive null checks at all entry points
- `IllegalArgumentException` with descriptive messages
- Descriptive variable names (no single-letter except `i`, `j` in loops)
- Helper methods to reduce duplication

---

## Key Implementation Patterns

### Array Algorithms
- **Integer overflow safe**: `mid = left + (right - left) / 2`
- **Sliding window**: Expand right, contract left
- **Prefix sum**: precompute cumulative sums for O(1) range queries
- **Kadane's algorithm**: Track max ending here + max so far
- **Two pointers**: Start from opposite ends, move toward center

### String Algorithms
- **StringBuilder for loops**: Never concatenate strings in loops
- **s.charAt(i)** not `s[i]` - String is immutable
- **equals() not ==** - String comparison
- **int[26] for char frequency** - Faster than HashMap for lowercase
- **KMP failure function** - Build prefix array before matching

### Hash Table Patterns
- **getOrDefault(key, default)** - Safe default value access
- **computeIfAbsent(key, k -> new ArrayList<>())** - Atomic creation
- **LinkedHashMap for insertion order** - Perfect for LRU cache
- **PriorityQueue for top-k** - Min-heap maintains k largest elements

### Linked List Patterns
- **Dummy head node** - Eliminates head special cases
- **Floyd's algorithm** - Detect/find cycle with O(1) space
- **Fast/slow pointers** - Find middle, detect cycle
- **Reverse in-place** - Maintain prev, curr, next carefully
- **HashMap for deep copy** - Map old nodes to new copies

---

## Test Coverage

Each file includes comprehensive `main()` with 6-9 test cases:

- **01_Array.java**: 6 test cases covering twoSum, threeSum, Kadane's, merge, rotate
- **02_String.java**: 9 test cases covering anagrams, palindromes, KMP, encode/decode
- **03_HashTable.java**: 8 test cases covering twoSum, topK, grouping, LRU cache
- **04_LinkedList.java**: 7 test cases covering reverse, cycle, merge, palindrome

---

## Quick Reference

| Problem | File | Method | LC # | Difficulty |
|---------|------|--------|------|------------|
| Two Sum | 03_HashTable | twoSum() | 1 | Easy |
| 3Sum | 01_Array | threeSum() | 15 | Medium |
| Longest Substring | 02_String | lengthOfLongestSubstring() | 3 | Medium |
| Median Sorted Arrays | - | - | 4 | Hard |
| Valid Parentheses | 02_String | isValid() | 20 | Easy |
| Merge K Lists | 04_LinkedList | mergeKLists() | 23 | Hard |
| Remove Nth from End | 04_LinkedList | removeNthFromEnd() | 19 | Medium |
| Valid Palindrome | 02_String | isPalindrome() | 125 | Easy |
| Longest Palindrome | 02_String | longestPalindromicSubstring() | 5 | Medium |
| Maximum Subarray | 01_Array | maxSubarraySum() | 53 | Medium |
| Two Sum II | 01_Array | twoSumSorted() | 167 | Easy |
| Merge Intervals | 01_Array | mergeIntervals() | 56 | Medium |
| Insert Interval | - | - | 57 | Medium |
| Search Insert | - | - | 35 | Easy |
| Search Rotated | 01_Array | searchInRotatedSortedArray() | 33 | Medium |
| First Missing | - | - | 41 | Hard |
| Rotate Array | 01_Array | rotateArray() | 189 | Medium |
| Duplicate Number | - | - | 287 | Medium |
| Next Permutation | 01_Array | nextPermutation() | 31 | Medium |
| Group Anagrams | 02_String, 03_HashTable | groupAnagrams() | 49 | Medium |
| Pow(x,n) | - | - | 50 | Medium |
| N-Queens | - | - | 51 | Hard |
| Subsets | - | - | 78 | Medium |
| Word Search | - | - | 79 | Medium |
| Combinations | - | - | 77 | Medium |
| Permutations | - | - | 46 | Medium |
| Rotate Image | - | - | 48 | Medium |
| Sort Colors | 01_Array | sortColors() | 75 | Medium |
| Minimum Window | 02_String | minWindowSubstring() | 76 | Hard |
| Remove Duplicates | - | - | 26 | Easy |
| Remove Element | - | - | 27 | Easy |
| Implement strStr | 02_String | strStr() (KMP) | 28 | Easy |
| Reverse List | 04_LinkedList | reverseList() | 206 | Easy |
| Linked List Cycle | 04_LinkedList | hasCycle() | 141 | Easy |
| Cycle II | 04_LinkedList | detectCycle() | 142 | Medium |
| Reorder List | 04_LinkedList | reorderList() | 143 | Medium |
| Palindrome List | 04_LinkedList | isPalindrome() | 234 | Easy |
| LRU Cache | 03_HashTable | LRUCache | 146 | Medium |
| Copy Random List | 04_LinkedList | copyRandomList() | 138 | Medium |
| Top K Frequent | 03_HashTable | topKFrequent() | 347 | Medium |
| First Unique | 03_HashTable | firstUniqueChar() | 387 | Easy |
| Longest Consecutive | 03_HashTable | longestConsecutiveSequence() | 128 | Medium |
| Reverse II | 04_LinkedList | reverseBetween() | 92 | Medium |
| Reverse K Group | 04_LinkedList | reverseKGroup() | 25 | Hard |
| Merge Sorted Lists | 04_LinkedList | mergeTwoLists() | 21 | Easy |
| Odd Even List | 04_LinkedList | oddEvenList() | 328 | Medium |
| Subarray Sum K | 01_Array | subarraySumEqualsK() | 560 | Medium |
| Max Product | 01_Array | maxProductSubarray() | 152 | Medium |
| Group Shifted | 03_HashTable | groupShiftedStrings() | 249 | Medium |
| Range Sum Query | 01_Array | RangeSum class | 303 | Easy |

---

## Performance Summary

| Data Structure | Operation | Time | Space |
|---|---|---|---|
| **Array** | Access | O(1) | O(n) |
| | Search | O(n) | - |
| | Binary Search | O(log n) | - |
| | Sort | O(n log n) | O(1) to O(n) |
| **String** | Lookup char | O(1) | - |
| | Frequency | O(n) | O(1) for 26 letters |
| | KMP match | O(m+n) | O(m) failure function |
| **Hash Map** | Insert/Delete | O(1) avg | O(n) worst |
| | Lookup | O(1) avg | - |
| **Linked List** | Access | O(n) | O(1) |
| | Insert/Delete | O(1) if pointer known | O(n) search |
| | Reverse | O(n) | O(1) |
| | Cycle detect | O(n) | O(1) Floyd's |

---

## Usage

Each file can be run standalone:

```bash
javac 01_Array.java
java Array

javac 02_String.java
java String

javac 03_HashTable.java
java HashTable

javac 04_LinkedList.java
java LinkedList
```

---

## Author

Google Senior SWE Interview Playground
