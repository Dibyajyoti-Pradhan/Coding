"""
ARRAYS - Complete Guide for Interview Preparation
===================================================

CORE CONCEPTS:
--------------
1. Arrays in Python are implemented as lists (dynamic arrays)
2. Zero-indexed, mutable, can contain mixed types (but usually homogeneous)
3. O(1) access by index, O(n) search, O(n) insertion/deletion (except at end)
4. Continuous memory allocation in CPython (for efficiency)

TRICKY PARTS:
-------------
1. List slicing creates a COPY (shallow), not a view
2. Negative indexing: arr[-1] is last element
3. Modifying list while iterating can cause issues
4. List multiplication creates shallow copies: [[0]*3]*3 shares references!
5. Default parameter gotcha: def func(arr=[]) - mutable default argument

COMMON PATTERNS:
----------------
1. Two Pointers (same/opposite direction)
2. Sliding Window (fixed/variable size)
3. Prefix Sum / Running Sum
4. Kadane's Algorithm (max subarray)
5. Dutch National Flag (3-way partitioning)
6. Fast & Slow Pointers
"""

from typing import List, Optional
import bisect


# ============================================================================
# PATTERN 1: TWO POINTERS - OPPOSITE DIRECTION
# ============================================================================

def two_sum_sorted(arr: List[int], target: int) -> Optional[List[int]]:
    """
    PROBLEM: Two Sum II - Input Array Is Sorted (LeetCode 167)

    Given a 1-indexed array of integers 'numbers' that is already sorted in
    non-decreasing order, find two numbers such that they add up to a specific
    target number. Return the indices of the two numbers (1-indexed).

    You may assume that each input has exactly one solution and you may not
    use the same element twice.

    Example 1:
        Input: numbers = [2,7,11,15], target = 9
        Output: [1,2]
        Explanation: 2 + 7 = 9, so return [1, 2]

    Example 2:
        Input: numbers = [2,3,4], target = 6
        Output: [1,3]

    Time: O(n), Space: O(1)
    Tricky: Remember array must be sorted for two-pointer approach!
    """
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None


def reverse_array_inplace(arr: List[int]) -> None:
    """
    Reverse array in place using two pointers.

    Time: O(n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    PROBLEM: 3Sum (LeetCode 15)

    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.

    Example 1:
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        Explanation:
            nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
            nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
            nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
            The distinct triplets are [-1,0,1] and [-1,-1,2].

    Example 2:
        Input: nums = [0,1,1]
        Output: []
        Explanation: The only possible triplet does not sum up to 0.

    Time: O(n²), Space: O(1) excluding output
    Tricky: Must handle duplicates carefully!
    """
    nums.sort()  # O(n log n)
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicates for first number
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # Two pointer approach for remaining two numbers
        left, right = i + 1, len(nums) - 1
        target = -nums[i]

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for second number
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for third number
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result


# ============================================================================
# PATTERN 2: SLIDING WINDOW
# ============================================================================

def max_sum_subarray_size_k(arr: List[int], k: int) -> int:
    """
    PROBLEM: Maximum Sum Subarray of Size K

    Given an array of integers and a number k, find the maximum sum of a
    contiguous subarray of size k.

    Example 1:
        Input: arr = [2, 1, 5, 1, 3, 2], k = 3
        Output: 9
        Explanation: Subarray [5, 1, 3] has maximum sum = 9

    Example 2:
        Input: arr = [2, 3, 4, 1, 5], k = 2
        Output: 7
        Explanation: Subarray [3, 4] has maximum sum = 7

    Time: O(n), Space: O(1)
    """
    if len(arr) < k:
        return 0

    # Initial window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum


def longest_substring_k_distinct(s: str, k: int) -> int:
    """
    Longest substring with at most k distinct characters (VARIABLE window).

    Time: O(n), Space: O(k)
    Tricky: Shrink window when constraint violated
    """
    char_count = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Expand window
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        # Shrink window if constraint violated
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


# ============================================================================
# PATTERN 3: PREFIX SUM
# ============================================================================

def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    """
    PROBLEM: Subarray Sum Equals K (LeetCode 560)

    Given an array of integers nums and an integer k, return the total number
    of subarrays whose sum equals to k.

    A subarray is a contiguous non-empty sequence of elements within an array.

    Example 1:
        Input: nums = [1,1,1], k = 2
        Output: 2
        Explanation: Subarrays [1,1] appear twice

    Example 2:
        Input: nums = [1,2,3], k = 3
        Output: 2
        Explanation: Subarrays are [1,2] and [3]

    Example 3:
        Input: nums = [1,-1,0], k = 0
        Output: 3
        Explanation: Subarrays are [1,-1], [-1,0], and [1,-1,0]

    Time: O(n), Space: O(n)
    Tricky: Use prefix sum + hashmap. Formula: prefix_sum[j] - prefix_sum[i] = k
    """
    count = 0
    prefix_sum = 0
    # Key: prefix_sum, Value: frequency
    # Important: handle case when prefix_sum itself equals k
    sum_count = {0: 1}

    for num in nums:
        prefix_sum += num

        # Check if (prefix_sum - k) exists
        # This means there's a subarray ending at current index with sum k
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]

        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1

    return count


class RangeSum:
    """
    Efficient range sum queries using prefix sum.

    Build: O(n), Query: O(1)
    """

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sum_range(self, left: int, right: int) -> int:
        """Sum of elements from index left to right (inclusive)."""
        return self.prefix[right + 1] - self.prefix[left]


# ============================================================================
# PATTERN 4: KADANE'S ALGORITHM
# ============================================================================

def max_subarray_sum(nums: List[int]) -> int:
    """
    PROBLEM: Maximum Subarray (Kadane's Algorithm) - LeetCode 53

    Given an integer array nums, find the subarray with the largest sum,
    and return its sum.

    Example 1:
        Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
        Output: 6
        Explanation: The subarray [4,-1,2,1] has the largest sum 6.

    Example 2:
        Input: nums = [1]
        Output: 1
        Explanation: The subarray [1] has the largest sum 1.

    Example 3:
        Input: nums = [5,4,-1,7,8]
        Output: 23
        Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

    Time: O(n), Space: O(1)
    Tricky: Keep track of current_sum and reset when it goes negative
    """
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


def max_product_subarray(nums: List[int]) -> int:
    """
    LeetCode 152 - Maximum product of contiguous subarray.

    Time: O(n), Space: O(1)
    Tricky: Track both max and min (negative * negative = positive)
    """
    if not nums:
        return 0

    max_prod = min_prod = result = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]

        # When multiplied by negative, max becomes min and vice versa
        if num < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)

        result = max(result, max_prod)

    return result


# ============================================================================
# PATTERN 5: CYCLIC SORT / ARRAY INDEX MANIPULATION
# ============================================================================

def find_missing_number(nums: List[int]) -> int:
    """
    Find missing number in array of 0 to n.

    Time: O(n), Space: O(1)
    Multiple approaches: XOR, sum formula, cyclic sort
    """
    # Approach 1: XOR (0^a^a = 0, 0^a = a)
    xor = 0
    for i in range(len(nums) + 1):
        xor ^= i
    for num in nums:
        xor ^= num
    return xor

    # Approach 2: Sum formula
    # n = len(nums)
    # expected_sum = n * (n + 1) // 2
    # return expected_sum - sum(nums)


def find_duplicates(nums: List[int]) -> List[int]:
    """
    LeetCode 442 - Find all duplicates in array where 1 ≤ nums[i] ≤ n.

    Time: O(n), Space: O(1)
    Tricky: Use array indices as hash, mark visited by negating
    """
    result = []

    for num in nums:
        index = abs(num) - 1

        # If already negative, we've seen this number before
        if nums[index] < 0:
            result.append(abs(num))
        else:
            nums[index] = -nums[index]

    # Restore array (optional)
    for i in range(len(nums)):
        nums[i] = abs(nums[i])

    return result


# ============================================================================
# PATTERN 6: DUTCH NATIONAL FLAG (3-WAY PARTITIONING)
# ============================================================================

def sort_colors(nums: List[int]) -> None:
    """
    LeetCode 75 - Sort array of 0s, 1s, 2s in-place.

    Time: O(n), Space: O(1)
    Tricky: Maintain three pointers - low, mid, high
    """
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            # Don't increment mid! Need to check swapped element


# ============================================================================
# PATTERN 7: MERGE INTERVALS
# ============================================================================

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    PROBLEM: Merge Intervals (LeetCode 56)

    Given an array of intervals where intervals[i] = [start_i, end_i], merge
    all overlapping intervals, and return an array of the non-overlapping
    intervals that cover all the intervals in the input.

    Example 1:
        Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        Explanation: Intervals [1,3] and [2,6] overlap, so merge them into [1,6].

    Example 2:
        Input: intervals = [[1,4],[4,5]]
        Output: [[1,5]]
        Explanation: Intervals [1,4] and [4,5] are considered overlapping.

    Time: O(n log n), Space: O(n)
    Tricky: Sort first, then merge
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


# ============================================================================
# PATTERN 8: BINARY SEARCH ON ARRAY
# ============================================================================

def binary_search(arr: List[int], target: int) -> int:
    """
    Standard binary search on sorted array.

    Time: O(log n), Space: O(1)
    Tricky: Watch for off-by-one errors!
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def search_insert_position(nums: List[int], target: int) -> int:
    """
    LeetCode 35 - Find insert position in sorted array.

    Time: O(log n), Space: O(1)
    Tricky: Return left pointer at end
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left  # Insert position


def search_rotated_sorted_array(nums: List[int], target: int) -> int:
    """
    PROBLEM: Search in Rotated Sorted Array (LeetCode 33)

    There is an integer array nums sorted in ascending order (with distinct values).
    Prior to being passed to your function, nums is possibly rotated at an unknown
    pivot index k (1 <= k < nums.length) such that the resulting array is
    [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

    For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

    Given the array nums after rotation and an integer target, return the index of
    target if it is in nums, or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.

    Example 1:
        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4

    Example 2:
        Input: nums = [4,5,6,7,0,1,2], target = 3
        Output: -1

    Time: O(log n), Space: O(1)
    Tricky: Determine which half is sorted, then decide which side to search
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Determine which half is sorted
        if nums[left] <= nums[mid]:  # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# ============================================================================
# COMMON ARRAY OPERATIONS & TRICKS
# ============================================================================

def rotate_array(nums: List[int], k: int) -> None:
    """
    LeetCode 189 - Rotate array to the right by k steps.

    Time: O(n), Space: O(1)
    Trick: Reverse three times!
    """
    n = len(nums)
    k = k % n  # Handle k > n

    def reverse(left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    # Reverse entire array
    reverse(0, n - 1)
    # Reverse first k elements
    reverse(0, k - 1)
    # Reverse remaining elements
    reverse(k, n - 1)


def next_permutation(nums: List[int]) -> None:
    """
    LeetCode 31 - Find next lexicographic permutation.

    Time: O(n), Space: O(1)
    Tricky: Find pivot, find swap position, reverse suffix
    """
    n = len(nums)

    # Step 1: Find pivot (first decreasing element from right)
    pivot = n - 2
    while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
        pivot -= 1

    if pivot >= 0:
        # Step 2: Find smallest element larger than pivot
        swap = n - 1
        while nums[swap] <= nums[pivot]:
            swap -= 1

        # Step 3: Swap
        nums[pivot], nums[swap] = nums[swap], nums[pivot]

    # Step 4: Reverse suffix
    left, right = pivot + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


# ============================================================================
# PYTHON-SPECIFIC TRICKS
# ============================================================================

def python_array_tricks():
    """Common Python list operations and gotchas."""

    # List comprehension vs generator
    squares_list = [x**2 for x in range(10)]  # Creates list in memory
    squares_gen = (x**2 for x in range(10))   # Generator, lazy evaluation

    # Slicing - creates shallow copy
    arr = [1, 2, 3, 4, 5]
    arr_copy = arr[:]  # Same as arr.copy()
    arr_reversed = arr[::-1]  # [5, 4, 3, 2, 1]
    arr_every_2nd = arr[::2]  # [1, 3, 5]

    # GOTCHA: Shallow copy issue
    matrix = [[0] * 3 for _ in range(3)]  # Correct ✓
    # matrix = [[0] * 3] * 3  # Wrong! All rows are same object ✗

    # GOTCHA: Mutable default argument
    # def append_to(element, arr=[]):  # Wrong! ✗
    #     arr.append(element)
    #     return arr

    def append_to(element, arr=None):  # Correct ✓
        if arr is None:
            arr = []
        arr.append(element)
        return arr

    # Unpacking
    a, *rest, b = [1, 2, 3, 4, 5]  # a=1, rest=[2,3,4], b=5

    # Using bisect module for binary search
    sorted_arr = [1, 3, 5, 7, 9]
    pos = bisect.bisect_left(sorted_arr, 6)  # Insert position
    bisect.insort(sorted_arr, 6)  # Insert and maintain sorted order

    # Enumerate with custom start
    for i, val in enumerate(arr, start=1):
        print(f"Position {i}: {val}")

    # Zip for parallel iteration
    names = ["Alice", "Bob"]
    scores = [95, 87]
    for name, score in zip(names, scores):
        print(f"{name}: {score}")

    # All/Any for boolean checks
    all_positive = all(x > 0 for x in arr)
    has_even = any(x % 2 == 0 for x in arr)


# ============================================================================
# PRACTICE PROBLEMS
# ============================================================================
"""
EASY:
- Two Sum (LeetCode 1)
- Best Time to Buy and Sell Stock (121)
- Contains Duplicate (217)
- Maximum Subarray (53)

MEDIUM:
- 3Sum (15)
- Container With Most Water (11)
- Product of Array Except Self (238)
- Subarray Sum Equals K (560)
- Rotate Image (48)
- Spiral Matrix (54)

HARD:
- Trapping Rain Water (42)
- First Missing Positive (41)
- Median of Two Sorted Arrays (4)
- Sliding Window Maximum (239)
"""

if __name__ == "__main__":
    # Test examples
    print("Two Sum Sorted:", two_sum_sorted([2, 7, 11, 15], 9))
    print("Three Sum:", three_sum([-1, 0, 1, 2, -1, -4]))
    print("Max Subarray Sum:", max_subarray_sum(
        [-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print("Subarray Sum K:", subarray_sum_equals_k([1, 1, 1], 2))
