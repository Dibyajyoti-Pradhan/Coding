# Method Inventory - Files 5-8

## FILE 5: 05_TwoPointers.java

### Public Methods (11)
| Method | Signature | LeetCode | Difficulty | Time | Space |
|--------|-----------|----------|------------|------|-------|
| twoSumSorted | `int[]` | 167 | Medium | O(n) | O(1) |
| threeSum | `List<List<Integer>>` | 15 | Medium | O(n²) | O(1) |
| fourSum | `List<List<Integer>>` | 18 | Medium | O(n³) | O(1) |
| containerWithMostWater | `int` | 11 | Medium | O(n) | O(1) |
| removeDuplicates | `int` | 26 | Easy | O(n) | O(1) |
| removeElement | `int` | 27 | Easy | O(n) | O(1) |
| moveZeroes | `void` | 283 | Easy | O(n) | O(1) |
| sortColors | `void` | 75 | Medium | O(n) | O(1) |
| validPalindrome | `boolean` | 680 | Medium | O(n) | O(1) |
| trap | `int` | 42 | Hard | O(n) | O(1) |
| main | `void` | - | - | - | - |

### Private Methods (2)
- `isPalindrome(String, int, int)` → boolean
- `swap(int[], int, int)` → void

---

## FILE 6: 06_SlidingWindow.java

### Public Methods (11)
| Method | Signature | LeetCode | Difficulty | Time | Space |
|--------|-----------|----------|------------|------|-------|
| maxSumSubarraySizeK | `int` | Custom | - | O(n) | O(1) |
| findAnagrams | `List<Integer>` | 438 | Medium | O(n) | O(1)* |
| containsNearbyDuplicate | `boolean` | 219 | Easy | O(n) | O(k) |
| lengthOfLongestSubstring | `int` | 3 | Medium | O(n) | O(1)* |
| longestSubstringWithKDistinct | `int` | 340 | Medium | O(n) | O(k) |
| characterReplacement | `int` | 424 | Medium | O(n) | O(26) |
| minWindowSubstring | `String` | 76 | Hard | O(n) | O(1)* |
| minSizeSubarraySum | `int` | 209 | Medium | O(n) | O(1) |
| subarraysWithKDistinct | `int` | 992 | Hard | O(n) | O(k) |
| maxSlidingWindow | `int[]` | 239 | Hard | O(n) | O(k) |
| main | `void` | - | - | - | - |

### Private Methods (1)
- `atMostKDistinct(int[], int)` → int

*For ASCII/bounded character set

---

## FILE 7: 07_BinarySearch.java

### Public Methods (14)
| Method | Signature | LeetCode | Difficulty | Time | Space |
|--------|-----------|----------|------------|------|-------|
| search | `int` | 704 | Easy | O(log n) | O(1) |
| searchInsertPosition | `int` | 35 | Easy | O(log n) | O(1) |
| findFirstOccurrence | `int` | Custom | - | O(log n) | O(1) |
| findLastOccurrence | `int` | Custom | - | O(log n) | O(1) |
| searchRange | `int[]` | 34 | Medium | O(log n) | O(1) |
| searchInRotatedArray | `int` | 33 | Medium | O(log n) | O(1) |
| findMinInRotatedArray | `int` | 153 | Medium | O(log n) | O(1) |
| kokoEatingBananas | `int` | 875 | Medium | O(n log m) | O(1) |
| splitArrayLargestSum | `int` | 410 | Hard | O(n log S) | O(1) |
| shipPackagesWithinDays | `int` | 1011 | Medium | O(n log S) | O(1) |
| searchMatrix | `boolean` | 74 | Medium | O(log(mn)) | O(1) |
| searchMatrixII | `boolean` | 240 | Medium | O(m+n) | O(1) |
| findPeakElement | `int` | 162 | Medium | O(log n) | O(1) |
| main | `void` | - | - | - | - |

### Private Methods (3)
- `canFinish(int[], int, int)` → boolean
- `canSplit(int[], int, int)` → boolean
- `canShip(int[], int, int)` → boolean

*m,n = matrix dimensions; S = sum of array

---

## FILE 8: 08_Sorting.java

### Public Methods (12)
| Method | Signature | LeetCode | Difficulty | Time | Space |
|--------|-----------|----------|------------|------|-------|
| mergeSort | `void` | - | - | O(n log n) | O(n) |
| quickSort | `void` | - | - | O(n log n)* | O(log n) |
| findKthLargest | `int` | 215 | Medium | O(n) avg* | O(log n) |
| largestNumber | `String` | 179 | Medium | O(n log n) | O(n) |
| sortByFrequencyThenValue | `int[]` | 1636 | Medium | O(n log n) | O(n) |
| mergeIntervals | `int[][]` | 56 | Medium | O(n log n) | O(1)** |
| insertInterval | `int[][]` | 57 | Medium | O(n) | O(n) |
| meetingRoomsII | `int` | 253 | Medium | O(n log n) | O(n) |
| topKFrequentBucket | `int[]` | 347 | Medium | O(n) | O(n) |
| findMissingNumber | `int` | 268 | Easy | O(n) | O(1) |
| findDuplicateNumber | `int` | 287 | Medium | O(n) | O(1) |
| main | `void` | - | - | - | - |

### Private Methods (6)
- `mergeSortHelper(int[], int, int)` → void
- `merge(int[], int, int, int)` → void
- `quickSortHelper(int[], int, int)` → void
- `partition(int[], int, int)` → int
- `quickSelect(int[], int, int, int)` → int
- `swap(int[], int, int)` → void

*Average case; O(n²) worst case
**Excluding output array

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total Public Methods | 48 |
| Total Private Helpers | 15 |
| Total Methods | 63 |
| LeetCode Problems Covered | 30+ |
| Easy Problems | 8 |
| Medium Problems | 16 |
| Hard Problems | 6 |

---

## Complexity Categories

### O(n) Time Complexity (7 methods)
- maxSumSubarraySizeK
- findAnagrams
- lengthOfLongestSubstring
- minWindowSubstring (2-pass)
- kokoEatingBananas (with binary search: O(n log m))
- shipPackagesWithinDays (with binary search: O(n log S))
- insertInterval
- topKFrequentBucket
- findMissingNumber

### O(n log n) Time Complexity (10 methods)
- twoSumSorted (after sort)
- threeSum (after sort)
- fourSum (after sort)
- mergeSort
- quickSort (average)
- largestNumber
- sortByFrequencyThenValue
- mergeIntervals
- meetingRoomsII
- splitArrayLargestSum (with binary search: O(n log S))

### O(log n) Time Complexity (8 methods)
- search
- searchInsertPosition
- findFirstOccurrence
- findLastOccurrence
- searchRange
- searchInRotatedArray
- findMinInRotatedArray
- findPeakElement

### O(n²) Time Complexity (3 methods)
- threeSum (worst case)
- fourSum (worst case)
- quickSort (worst case)

### O(n log k) Time Complexity (1 method)
- maxSlidingWindow (k = window size)

### O(m*n) Time Complexity (1 method)
- searchMatrix (m x n matrix)

### Special Complexity (3 methods)
- findKthLargest: O(n) avg, O(n²) worst (quickSelect)
- findDuplicateNumber: O(n) with O(1) space (Floyd's cycle)
- minSizeSubarraySum: O(n) two-pointer

---

## Method by Problem Type

### Array Problems (25 methods)
- Two-pointer: 11 methods
- Sliding window: 8 methods
- Binary search: 6 methods

### String Problems (3 methods)
- lengthOfLongestSubstring
- longestSubstringWithKDistinct
- characterReplacement

### Sorting Problems (6 methods)
- mergeSort
- quickSort
- findKthLargest
- largestNumber
- sortByFrequencyThenValue
- topKFrequentBucket

### Interval Problems (3 methods)
- mergeIntervals
- insertInterval
- meetingRoomsII

### Matrix Problems (2 methods)
- searchMatrix
- searchMatrixII

### Special Techniques (6 methods)
- findMissingNumber (XOR)
- findDuplicateNumber (Floyd's cycle)
- subarraysWithKDistinct (at-most-k trick)
- maxSlidingWindow (deque optimization)
- kokoEatingBananas (binary search on answer)
- splitArrayLargestSum (binary search on answer)

---

## Interview Preparation by Difficulty

### Must-Know (Easy - 8 problems)
1. Binary Search (LC 704)
2. Remove Duplicates (LC 26)
3. Remove Element (LC 27)
4. Move Zeroes (LC 283)
5. Contains Nearby Duplicate (LC 219)
6. Search Insert Position (LC 35)
7. Find Missing Number (LC 268)
8. Find Anagrams (LC 438)

### Important (Medium - 16 problems)
1. Container With Most Water (LC 11)
2. Longest Substring Without Repeating (LC 3)
3. Three Sum (LC 15)
4. Four Sum (LC 18)
5. Search Range (LC 34)
6. Merge Intervals (LC 56)
7. Insert Interval (LC 57)
8. Sort Colors (LC 75)
9. Min in Rotated Array (LC 153)
10. Find Peak (LC 162)
11. Two Sum Sorted (LC 167)
12. Largest Number (LC 179)
13. Min Size Subarray (LC 209)
14. Meeting Rooms II (LC 253)
15. Longest Substring K Distinct (LC 340)
16. Character Replacement (LC 424)

### Advanced (Hard - 6 problems)
1. Trap Rainwater (LC 42)
2. Min Window Substring (LC 76)
3. Max Sliding Window (LC 239)
4. Find Duplicate (LC 287)
5. Split Array Largest Sum (LC 410)
6. Subarrays With K Distinct (LC 992)

### Expert (8+ problems)
1. Koko Eating Bananas (LC 875)
2. Ship Packages (LC 1011)
3. Search Matrix (LC 74)
4. Search Matrix II (LC 240)
5. Top K Frequent (LC 347)
6. Sort by Frequency (LC 1636)
7. Valid Palindrome II (LC 680)
8. Custom problems
