"""
SORTING - Complete Guide for Interview Preparation
===================================================

CORE CONCEPTS:
--------------
1. Python's built-in sort: Timsort (hybrid merge+insertion) - O(n log n)
2. sorted() returns new list, list.sort() modifies in-place
3. Key function for custom sorting
4. Stable sorts preserve relative order of equal elements

COMPARISON-BASED SORTS (Lower bound: O(n log n)):
- Quick Sort: O(n log n) average, O(n²) worst, unstable
- Merge Sort: O(n log n), stable, O(n) space
- Heap Sort: O(n log n), unstable, O(1) space
- Insertion Sort: O(n²), stable, good for small/nearly sorted
- Bubble Sort: O(n²), stable, simple but inefficient

NON-COMPARISON SORTS (Can be O(n)):
- Counting Sort: O(n + k) where k is range
- Radix Sort: O(d * n) where d is digits
- Bucket Sort: O(n) average

TRICKY PARTS:
-------------
1. Stability matters when sorting objects with multiple fields
2. Quick sort pivot selection affects performance
3. Custom comparators: use key function, not cmp
4. Sorting strings vs numbers: different default behavior
5. Sorting in descending order: reverse=True or negative key

COMMON PATTERNS:
----------------
1. Custom sorting with key function
2. Sorting intervals/pairs
3. Sorting with multiple criteria
4. Quick select for kth element
5. Merge k sorted arrays
"""

from typing import List, Tuple
import heapq
from collections import Counter


# ============================================================================
# PYTHON BUILT-IN SORTING
# ============================================================================

def python_sorting_basics():
    """Python sorting fundamentals and tricks."""

    # Basic sorting
    arr = [3, 1, 4, 1, 5, 9, 2, 6]

    # sorted() - returns new sorted list
    sorted_arr = sorted(arr)  # [1, 1, 2, 3, 4, 5, 6, 9]

    # list.sort() - sorts in-place
    arr.sort()  # Modifies arr

    # Reverse order
    sorted(arr, reverse=True)
    arr.sort(reverse=True)

    # Custom key function
    words = ["apple", "pie", "zoo", "a"]
    sorted(words, key=len)  # Sort by length
    sorted(words, key=str.lower)  # Case-insensitive

    # Sort tuples/lists by specific element
    pairs = [(1, 5), (3, 2), (1, 3)]
    sorted(pairs)  # By first element, then second: [(1, 3), (1, 5), (3, 2)]
    sorted(pairs, key=lambda x: x[1])  # By second element: [(3, 2), (1, 3), (1, 5)]

    # Multiple criteria
    sorted(pairs, key=lambda x: (x[1], x[0]))  # By second, then first

    # Reverse specific criteria
    sorted(pairs, key=lambda x: (-x[0], x[1]))  # First desc, second asc

    # Sort objects
    class Student:
        def __init__(self, name, grade, age):
            self.name = name
            self.grade = grade
            self.age = age

    students = [Student("Alice", 90, 20), Student("Bob", 85, 22)]
    sorted(students, key=lambda s: s.grade, reverse=True)

    # Sort dictionary by value
    d = {'a': 3, 'b': 1, 'c': 2}
    sorted(d.items(), key=lambda x: x[1])  # [('b', 1), ('c', 2), ('a', 3)]

    # Stable sort - maintains relative order of equal elements
    # Python's sort is stable!


# ============================================================================
# PATTERN 1: SORTING INTERVALS
# ============================================================================

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    LeetCode 56 - Merge overlapping intervals.

    Time: O(n log n), Space: O(n)
    """
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        if current[0] <= last[1]:  # Overlapping
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged


def insert_interval(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """
    LeetCode 57 - Insert interval and merge if necessary.

    Time: O(n), Space: O(n)
    """
    result = []
    i = 0
    n = len(intervals)

    # Add all intervals before newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    result.append(newInterval)

    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


def non_overlapping_intervals(intervals: List[List[int]]) -> int:
    """
    LeetCode 435 - Minimum intervals to remove for non-overlapping.

    Time: O(n log n), Space: O(1)
    Tricky: Sort by end time, greedy approach
    """
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])  # Sort by end time
    count = 0
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] < end:  # Overlapping
            count += 1
        else:
            end = intervals[i][1]

    return count


def meeting_rooms(intervals: List[List[int]]) -> bool:
    """
    LeetCode 252 - Can attend all meetings (no overlap).

    Time: O(n log n), Space: O(1)
    """
    if not intervals:
        return True

    intervals.sort()

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True


def meeting_rooms_ii(intervals: List[List[int]]) -> int:
    """
    LeetCode 253 - Minimum meeting rooms needed.

    Time: O(n log n), Space: O(n)
    Tricky: Use separate start/end arrays or heap
    """
    if not intervals:
        return 0

    # Approach 1: Using two sorted arrays
    starts = sorted(interval[0] for interval in intervals)
    ends = sorted(interval[1] for interval in intervals)

    rooms = 0
    end_ptr = 0

    for start in starts:
        if start < ends[end_ptr]:
            rooms += 1
        else:
            end_ptr += 1

    return rooms


# ============================================================================
# PATTERN 2: CUSTOM SORTING / COMPARATORS
# ============================================================================

def largest_number(nums: List[int]) -> str:
    """
    LeetCode 179 - Arrange numbers to form largest number.

    Time: O(n log n), Space: O(n)
    Tricky: Custom comparator - compare concatenations
    """
    from functools import cmp_to_key

    def compare(x: str, y: str) -> int:
        # Compare x+y vs y+x
        if x + y > y + x:
            return -1  # x should come before y
        elif x + y < y + x:
            return 1
        else:
            return 0

    nums_str = [str(num) for num in nums]
    nums_str.sort(key=cmp_to_key(compare))

    result = ''.join(nums_str)

    # Handle edge case: all zeros
    return '0' if result[0] == '0' else result


def reorder_log_files(logs: List[str]) -> List[str]:
    """
    LeetCode 937 - Reorder log files.

    Time: O(n log n), Space: O(1)
    """
    def get_key(log: str):
        identifier, rest = log.split(' ', 1)

        if rest[0].isdigit():
            # Digit log: keep original order (return large value)
            return (1,)  # Will be placed after letter logs
        else:
            # Letter log: sort by content, then identifier
            return (0, rest, identifier)

    return sorted(logs, key=get_key)


# ============================================================================
# PATTERN 3: SORTING WITH FREQUENCY
# ============================================================================

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    LeetCode 347 - Top k frequent elements.

    Time: O(n log n), Space: O(n)
    Multiple approaches: heap, bucket sort, quickselect
    """
    # Approach 1: Sort by frequency
    count = Counter(nums)
    return sorted(count.keys(), key=lambda x: count[x], reverse=True)[:k]

    # Approach 2: Using heap (better for large n, small k)
    # return heapq.nlargest(k, count.keys(), key=count.get)


def frequency_sort_string(s: str) -> str:
    """
    LeetCode 451 - Sort characters by frequency.

    Time: O(n log n), Space: O(n)
    """
    count = Counter(s)
    sorted_chars = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return ''.join(char * freq for char, freq in sorted_chars)


def sort_by_frequency(nums: List[int]) -> List[int]:
    """
    Sort array by frequency, then by value.

    Time: O(n log n), Space: O(n)
    """
    count = Counter(nums)
    # Sort by frequency (desc), then by value (asc)
    return sorted(nums, key=lambda x: (-count[x], x))


# ============================================================================
# PATTERN 4: QUICK SELECT (kth Element)
# ============================================================================

def find_kth_largest(nums: List[int], k: int) -> int:
    """
    LeetCode 215 - Kth largest element using QuickSelect.

    Time: O(n) average, O(n²) worst, Space: O(1)
    """
    def partition(left: int, right: int, pivot_idx: int) -> int:
        pivot = nums[pivot_idx]
        # Move pivot to end
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

        store_idx = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[store_idx] = nums[store_idx], nums[i]
                store_idx += 1

        # Move pivot to final position
        nums[store_idx], nums[right] = nums[right], nums[store_idx]
        return store_idx

    def quickselect(left: int, right: int, k_smallest: int) -> int:
        if left == right:
            return nums[left]

        # Choose random pivot
        import random
        pivot_idx = random.randint(left, right)

        pivot_idx = partition(left, right, pivot_idx)

        if k_smallest == pivot_idx:
            return nums[k_smallest]
        elif k_smallest < pivot_idx:
            return quickselect(left, pivot_idx - 1, k_smallest)
        else:
            return quickselect(pivot_idx + 1, right, k_smallest)

    # kth largest = (n - k)th smallest
    return quickselect(0, len(nums) - 1, len(nums) - k)


# ============================================================================
# PATTERN 5: SORTING ALGORITHMS IMPLEMENTATION
# ============================================================================

def quick_sort(arr: List[int]) -> List[int]:
    """
    Quick Sort implementation.

    Time: O(n log n) average, O(n²) worst
    Space: O(log n) recursion
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge Sort implementation.

    Time: O(n log n), Space: O(n)
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted arrays."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def insertion_sort(arr: List[int]) -> None:
    """
    Insertion Sort (in-place).

    Time: O(n²), Space: O(1)
    Good for small or nearly sorted arrays
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# ============================================================================
# PATTERN 6: COUNTING SORT / BUCKET SORT
# ============================================================================

def counting_sort(arr: List[int]) -> List[int]:
    """
    Counting Sort for non-negative integers.

    Time: O(n + k), Space: O(k) where k is range
    """
    if not arr:
        return []

    max_val = max(arr)
    count = [0] * (max_val + 1)

    # Count occurrences
    for num in arr:
        count[num] += 1

    # Build result
    result = []
    for num, freq in enumerate(count):
        result.extend([num] * freq)

    return result


def bucket_sort(arr: List[float]) -> List[float]:
    """
    Bucket Sort for floats in range [0, 1).

    Time: O(n) average, Space: O(n)
    """
    if not arr:
        return []

    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Distribute into buckets
    for num in arr:
        idx = int(num * n)
        if idx == n:
            idx = n - 1
        buckets[idx].append(num)

    # Sort each bucket and concatenate
    result = []
    for bucket in buckets:
        result.extend(sorted(bucket))

    return result


# ============================================================================
# PATTERN 7: SPECIAL SORTING PROBLEMS
# ============================================================================

def sort_colors(nums: List[int]) -> None:
    """
    LeetCode 75 - Sort colors (0, 1, 2) - Dutch National Flag.

    Time: O(n), Space: O(1)
    """
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


def wiggle_sort(nums: List[int]) -> None:
    """
    LeetCode 280 - Wiggle sort (nums[0] <= nums[1] >= nums[2] <= nums[3]...).

    Time: O(n), Space: O(1)
    Tricky: Swap when condition violated
    """
    for i in range(len(nums) - 1):
        if i % 2 == 0:  # Even index: should be <=
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        else:  # Odd index: should be >=
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]


def pancake_sort(arr: List[int]) -> List[int]:
    """
    LeetCode 969 - Pancake sorting (find k-flips to sort).

    Time: O(n²), Space: O(1)
    """
    def flip(k: int) -> None:
        """Reverse arr[0:k+1]."""
        left, right = 0, k
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    result = []
    n = len(arr)

    for size in range(n, 1, -1):
        # Find index of max element in arr[0:size]
        max_idx = arr[:size].index(max(arr[:size]))

        if max_idx != size - 1:
            # Flip to bring max to front
            if max_idx != 0:
                flip(max_idx)
                result.append(max_idx + 1)

            # Flip to bring max to correct position
            flip(size - 1)
            result.append(size)

    return result


# ============================================================================
# PRACTICE PROBLEMS
# ============================================================================
"""
EASY:
- Merge Sorted Array (88)
- Sort Colors (75)
- Meeting Rooms (252)
- Squares of Sorted Array (977)

MEDIUM:
- Merge Intervals (56)
- Sort List (148)
- Kth Largest Element (215)
- Top K Frequent Elements (347)
- Meeting Rooms II (253)
- Largest Number (179)
- Wiggle Sort (280)

HARD:
- Merge k Sorted Lists (23)
- Count of Smaller Numbers After Self (315)
- Reverse Pairs (493)
"""

if __name__ == "__main__":
    # Test examples
    print("Merge Intervals:", merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print("Largest Number:", largest_number([3, 30, 34, 5, 9]))

    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Quick Sort:", quick_sort(arr))
    print("Merge Sort:", merge_sort(arr))
    print("Kth Largest:", find_kth_largest([3, 2, 1, 5, 6, 4], 2))
