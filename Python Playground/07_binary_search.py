"""
BINARY SEARCH - Complete Guide for Interview Preparation
=========================================================

CORE CONCEPTS:
--------------
1. Divide and conquer on sorted data
2. Time: O(log n), Space: O(1) iterative, O(log n) recursive
3. Works on monotonic functions (increasing/decreasing)
4. Can search on answer space, not just arrays

TRICKY PARTS:
-------------
1. Off-by-one errors: left <= right vs left < right
2. Mid calculation: left + (right - left) // 2 to avoid overflow
3. When to return: left, right, or -1
4. Search space: [left, right] vs [left, right)
5. Finding leftmost/rightmost occurrence

COMMON PATTERNS:
----------------
1. Basic Binary Search
2. Find First/Last Occurrence
3. Search in Rotated Array
4. Binary Search on Answer
5. Search in 2D Matrix
6. Peak Finding
"""

from typing import List, Optional
import bisect


# ============================================================================
# PATTERN 1: BASIC BINARY SEARCH
# ============================================================================

def binary_search(nums: List[int], target: int) -> int:
    """
    Standard binary search in sorted array.

    Time: O(log n), Space: O(1)
    Returns: index if found, -1 otherwise
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

    return -1


def binary_search_recursive(nums: List[int], target: int) -> int:
    """
    Recursive binary search.

    Time: O(log n), Space: O(log n) for call stack
    """
    def search(left: int, right: int) -> int:
        if left > right:
            return -1

        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return search(mid + 1, right)
        else:
            return search(left, mid - 1)

    return search(0, len(nums) - 1)


def search_insert(nums: List[int], target: int) -> int:
    """
    LeetCode 35 - Search insert position.

    Time: O(log n), Space: O(1)
    Tricky: Return left (insert position) if not found
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


# ============================================================================
# PATTERN 2: FIND FIRST/LAST OCCURRENCE
# ============================================================================

def find_first_occurrence(nums: List[int], target: int) -> int:
    """
    Find leftmost (first) occurrence of target.

    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def find_last_occurrence(nums: List[int], target: int) -> int:
    """
    Find rightmost (last) occurrence of target.

    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def search_range(nums: List[int], target: int) -> List[int]:
    """
    LeetCode 34 - Find first and last position of target.

    Time: O(log n), Space: O(1)
    """
    return [
        find_first_occurrence(nums, target),
        find_last_occurrence(nums, target)
    ]


def count_occurrences(nums: List[int], target: int) -> int:
    """
    Count occurrences of target in sorted array.

    Time: O(log n), Space: O(1)
    """
    first = find_first_occurrence(nums, target)
    if first == -1:
        return 0

    last = find_last_occurrence(nums, target)
    return last - first + 1


# ============================================================================
# PATTERN 3: ROTATED SORTED ARRAY
# ============================================================================

def search_rotated(nums: List[int], target: int) -> int:
    """
    LeetCode 33 - Search in rotated sorted array (no duplicates).

    Time: O(log n), Space: O(1)
    Tricky: Determine which half is sorted
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


def search_rotated_duplicates(nums: List[int], target: int) -> bool:
    """
    LeetCode 81 - Search in rotated sorted array with duplicates.

    Time: O(log n) average, O(n) worst, Space: O(1)
    Tricky: Handle case when nums[left] == nums[mid]
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return True

        # Skip duplicates
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:  # Left half sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False


def find_minimum_rotated(nums: List[int]) -> int:
    """
    LeetCode 153 - Find minimum in rotated sorted array.

    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            # Minimum is in right half
            left = mid + 1
        else:
            # Minimum is in left half or mid
            right = mid

    return nums[left]


def find_rotation_count(nums: List[int]) -> int:
    """
    Find number of rotations (index of minimum element).

    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return left


# ============================================================================
# PATTERN 4: PEAK FINDING
# ============================================================================

def find_peak_element(nums: List[int]) -> int:
    """
    LeetCode 162 - Find peak element.

    Time: O(log n), Space: O(1)
    Tricky: Move towards higher neighbor
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid + 1]:
            # Peak is on right
            left = mid + 1
        else:
            # Peak is on left or mid
            right = mid

    return left


def peak_index_in_mountain(arr: List[int]) -> int:
    """
    LeetCode 852 - Peak index in mountain array.

    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


# ============================================================================
# PATTERN 5: BINARY SEARCH ON ANSWER SPACE
# ============================================================================

def min_eating_speed(piles: List[int], h: int) -> int:
    """
    LeetCode 875 - Koko eating bananas.

    Time: O(n log m) where m is max pile, Space: O(1)
    Tricky: Binary search on speed (answer space)
    """
    def can_finish(speed: int) -> bool:
        """Check if can finish all piles in h hours at given speed."""
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed  # Ceiling division
        return hours <= h

    left, right = 1, max(piles)

    while left < right:
        mid = left + (right - left) // 2

        if can_finish(mid):
            right = mid  # Try smaller speed
        else:
            left = mid + 1

    return left


def split_array_largest_sum(nums: List[int], k: int) -> int:
    """
    LeetCode 410 - Split array largest sum.

    Time: O(n log(sum - max)), Space: O(1)
    Tricky: Binary search on the answer (max sum)
    """
    def can_split(max_sum: int) -> bool:
        """Check if can split into k subarrays with max sum <= max_sum."""
        splits = 1
        current_sum = 0

        for num in nums:
            if current_sum + num > max_sum:
                splits += 1
                current_sum = num
                if splits > k:
                    return False
            else:
                current_sum += num

        return True

    left, right = max(nums), sum(nums)

    while left < right:
        mid = left + (right - left) // 2

        if can_split(mid):
            right = mid
        else:
            left = mid + 1

    return left


def smallest_divisor(nums: List[int], threshold: int) -> int:
    """
    LeetCode 1283 - Find smallest divisor given threshold.

    Time: O(n log m), Space: O(1)
    """
    def compute_sum(divisor: int) -> int:
        return sum((num + divisor - 1) // divisor for num in nums)

    left, right = 1, max(nums)

    while left < right:
        mid = left + (right - left) // 2

        if compute_sum(mid) <= threshold:
            right = mid
        else:
            left = mid + 1

    return left


def capacity_to_ship(weights: List[int], days: int) -> int:
    """
    LeetCode 1011 - Capacity to ship packages within D days.

    Time: O(n log(sum - max)), Space: O(1)
    """
    def can_ship(capacity: int) -> bool:
        days_needed = 1
        current_weight = 0

        for weight in weights:
            if current_weight + weight > capacity:
                days_needed += 1
                current_weight = weight
            else:
                current_weight += weight

        return days_needed <= days

    left, right = max(weights), sum(weights)

    while left < right:
        mid = left + (right - left) // 2

        if can_ship(mid):
            right = mid
        else:
            left = mid + 1

    return left


# ============================================================================
# PATTERN 6: 2D MATRIX SEARCH
# ============================================================================

def search_matrix(matrix: List[List[int]], target: int) -> bool:
    """
    LeetCode 74 - Search 2D matrix (each row sorted, first of next > last of prev).

    Time: O(log(m*n)), Space: O(1)
    Tricky: Treat as 1D sorted array
    """
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = left + (right - left) // 2
        row, col = mid // n, mid % n
        mid_val = matrix[row][col]

        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


def search_matrix_ii(matrix: List[List[int]], target: int) -> bool:
    """
    LeetCode 240 - Search 2D matrix II (each row/column sorted independently).

    Time: O(m + n), Space: O(1)
    Tricky: Start from top-right or bottom-left
    """
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    row, col = 0, n - 1  # Start from top-right

    while row < m and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down

    return False


# ============================================================================
# PATTERN 7: SQUARE ROOT / PERFECT SQUARE
# ============================================================================

def my_sqrt(x: int) -> int:
    """
    LeetCode 69 - Integer square root.

    Time: O(log n), Space: O(1)
    """
    if x < 2:
        return x

    left, right = 1, x // 2

    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid

        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1

    return right  # Return floor


def is_perfect_square(num: int) -> bool:
    """
    LeetCode 367 - Valid perfect square.

    Time: O(log n), Space: O(1)
    """
    if num < 2:
        return True

    left, right = 1, num // 2

    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid

        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1

    return False


# ============================================================================
# PYTHON bisect MODULE
# ============================================================================

def python_bisect_examples():
    """
    Python's bisect module for binary search operations.
    """
    import bisect

    arr = [1, 3, 4, 4, 4, 6, 7]

    # bisect_left: leftmost insertion point
    pos = bisect.bisect_left(arr, 4)  # 2 (first 4)

    # bisect_right (bisect): rightmost insertion point
    pos = bisect.bisect_right(arr, 4)  # 5 (after last 4)
    pos = bisect.bisect(arr, 4)  # Same as bisect_right

    # insort: insert and maintain sorted order
    bisect.insort_left(arr, 5)  # Insert 5 at leftmost position

    # Find if element exists
    def contains(arr, x):
        i = bisect.bisect_left(arr, x)
        return i < len(arr) and arr[i] == x

    # Find first occurrence
    def find_first(arr, x):
        i = bisect.bisect_left(arr, x)
        return i if i < len(arr) and arr[i] == x else -1

    # Find last occurrence
    def find_last(arr, x):
        i = bisect.bisect_right(arr, x)
        return i - 1 if i > 0 and arr[i-1] == x else -1

    # Count occurrences
    def count(arr, x):
        left = bisect.bisect_left(arr, x)
        right = bisect.bisect_right(arr, x)
        return right - left


# ============================================================================
# PRACTICE PROBLEMS
# ============================================================================
"""
EASY:
- Binary Search (704)
- Search Insert Position (35)
- Sqrt(x) (69)
- Valid Perfect Square (367)
- First Bad Version (278)

MEDIUM:
- Find First and Last Position (34)
- Search in Rotated Sorted Array (33)
- Find Minimum in Rotated Sorted Array (153)
- Find Peak Element (162)
- Koko Eating Bananas (875)
- Capacity To Ship Packages (1011)
- Search 2D Matrix (74)

HARD:
- Median of Two Sorted Arrays (4)
- Split Array Largest Sum (410)
- Aggressive Cows (not on LeetCode)
"""

if __name__ == "__main__":
    # Test examples
    print("Binary Search:", binary_search([1, 2, 3, 4, 5, 6], 4))
    print("Search Insert:", search_insert([1, 3, 5, 6], 2))
    print("Search Range:", search_range([5, 7, 7, 8, 8, 10], 8))
    print("Search Rotated:", search_rotated([4, 5, 6, 7, 0, 1, 2], 0))
    print("Find Min Rotated:", find_minimum_rotated([3, 4, 5, 1, 2]))
    print("Min Eating Speed:", min_eating_speed([3, 6, 7, 11], 8))
