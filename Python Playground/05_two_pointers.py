"""
TWO POINTERS - Complete Guide for Interview Preparation
========================================================

CORE CONCEPTS:
--------------
1. Two pointers technique uses two indices to traverse data structure
2. Can move in same direction or opposite directions
3. Reduces time complexity from O(n²) to O(n) for many problems
4. Common in array, string, and linked list problems

TRICKY PARTS:
-------------
1. Pointer initialization depends on problem (both at start, one at start/end, etc.)
2. Loop termination condition: left < right or left <= right
3. When to move which pointer - requires careful analysis
4. Handle duplicates carefully to avoid infinite loops

COMMON PATTERNS:
----------------
1. Opposite Direction (left/right pointers)
2. Same Direction (slow/fast pointers)
3. Sliding Window (special case of two pointers)
4. Partition/Quick Select
"""

from typing import List, Optional


# ============================================================================
# PATTERN 1: OPPOSITE DIRECTION
# ============================================================================

def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    """
    LeetCode 167 - Two sum in sorted array.

    Time: O(n), Space: O(1)
    """
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    LeetCode 15 - Find all unique triplets that sum to zero.

    Time: O(n²), Space: O(1) excluding output
    Tricky: Must handle duplicates
    """
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicates for first number
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i + 1, len(nums) - 1
        target = -nums[i]

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result


def three_sum_closest(nums: List[int], target: int) -> int:
    """
    LeetCode 16 - Find triplet sum closest to target.

    Time: O(n²), Space: O(1)
    """
    nums.sort()
    closest_sum = float('inf')

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return target  # Exact match

    return closest_sum


def four_sum(nums: List[int], target: int) -> List[List[int]]:
    """
    LeetCode 18 - Find all unique quadruplets that sum to target.

    Time: O(n³), Space: O(1) excluding output
    """
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue

            left, right = j + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return result


def container_with_most_water(height: List[int]) -> int:
    """
    LeetCode 11 - Container with most water.

    Time: O(n), Space: O(1)
    Tricky: Move pointer with smaller height
    """
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        current_area = min(height[left], height[right]) * width
        max_area = max(max_area, current_area)

        # Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


def trapping_rain_water(height: List[int]) -> int:
    """
    LeetCode 42 - Trapping rain water.

    Time: O(n), Space: O(1)
    Tricky: Track max heights from both sides
    """
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water


# ============================================================================
# PATTERN 2: SAME DIRECTION (FAST & SLOW)
# ============================================================================

def remove_duplicates_sorted_array(nums: List[int]) -> int:
    """
    LeetCode 26 - Remove duplicates from sorted array in-place.

    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0

    slow = 0  # Position for next unique element

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1


def remove_element(nums: List[int], val: int) -> int:
    """
    LeetCode 27 - Remove all occurrences of val in-place.

    Time: O(n), Space: O(1)
    """
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1

    return slow


def move_zeroes(nums: List[int]) -> None:
    """
    LeetCode 283 - Move all zeros to end while maintaining order.

    Time: O(n), Space: O(1)
    """
    slow = 0  # Position for next non-zero

    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


def remove_duplicates_sorted_array_ii(nums: List[int]) -> int:
    """
    LeetCode 80 - Remove duplicates, allow at most 2 occurrences.

    Time: O(n), Space: O(1)
    Tricky: Compare with element at slow-2
    """
    if len(nums) <= 2:
        return len(nums)

    slow = 2  # Start from index 2

    for fast in range(2, len(nums)):
        # Allow if different from element 2 positions back
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1

    return slow


# ============================================================================
# PATTERN 3: PARTITION
# ============================================================================

def sort_colors(nums: List[int]) -> None:
    """
    LeetCode 75 - Sort array of 0s, 1s, 2s (Dutch National Flag).

    Time: O(n), Space: O(1)
    Tricky: Three pointers - low, mid, high
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
            # Don't increment mid - need to check swapped element


def partition_array(nums: List[int], k: int) -> int:
    """
    Partition array: elements < k on left, >= k on right.

    Time: O(n), Space: O(1)
    Returns: index where partition occurs
    """
    left = 0

    for right in range(len(nums)):
        if nums[right] < k:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

    return left


# ============================================================================
# PATTERN 4: PALINDROME / REVERSE
# ============================================================================

def is_palindrome(s: str) -> bool:
    """
    LeetCode 125 - Valid palindrome (alphanumeric only).

    Time: O(n), Space: O(1)
    """
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


def valid_palindrome_ii(s: str) -> bool:
    """
    LeetCode 680 - Valid palindrome after deleting at most one character.

    Time: O(n), Space: O(1)
    """
    def is_palindrome_range(left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Try deleting left or right character
            return is_palindrome_range(left + 1, right) or \
                   is_palindrome_range(left, right - 1)
        left += 1
        right -= 1

    return True


def reverse_string(s: List[str]) -> None:
    """
    LeetCode 344 - Reverse string in-place.

    Time: O(n), Space: O(1)
    """
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverse_vowels(s: str) -> str:
    """
    LeetCode 345 - Reverse only vowels in string.

    Time: O(n), Space: O(n)
    """
    vowels = set('aeiouAEIOU')
    s = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and s[left] not in vowels:
            left += 1
        while left < right and s[right] not in vowels:
            right -= 1

        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return ''.join(s)


# ============================================================================
# PATTERN 5: MERGE SORTED ARRAYS
# ============================================================================

def merge_sorted_arrays(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    LeetCode 88 - Merge sorted arrays (nums1 has space for nums2).

    Time: O(m + n), Space: O(1)
    Tricky: Fill from end to avoid overwriting
    """
    p1, p2 = m - 1, n - 1
    p = m + n - 1

    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1


def squares_of_sorted_array(nums: List[int]) -> List[int]:
    """
    LeetCode 977 - Squares of sorted array (may have negatives).

    Time: O(n), Space: O(n)
    Tricky: Largest square is at either end
    """
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1

        pos -= 1

    return result


# ============================================================================
# PATTERN 6: SUBSEQUENCE
# ============================================================================

def is_subsequence(s: str, t: str) -> bool:
    """
    LeetCode 392 - Check if s is subsequence of t.

    Time: O(n), Space: O(1)
    """
    i = 0

    for char in t:
        if i < len(s) and s[i] == char:
            i += 1

    return i == len(s)


def longest_common_prefix(strs: List[str]) -> str:
    """
    LeetCode 14 - Find longest common prefix.

    Time: O(n * m) where m is min string length, Space: O(1)
    """
    if not strs:
        return ""

    # Use first string as reference
    for i in range(len(strs[0])):
        char = strs[0][i]

        # Check if all strings have this character at position i
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]

    return strs[0]


# ============================================================================
# ADVANCED PROBLEMS
# ============================================================================

def min_size_subarray_sum(target: int, nums: List[int]) -> int:
    """
    LeetCode 209 - Minimum size subarray sum >= target.

    Time: O(n), Space: O(1)
    Note: This is also a sliding window problem
    """
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0


def backspace_string_compare(s: str, t: str) -> bool:
    """
    LeetCode 844 - Compare strings with backspace (#).

    Time: O(n + m), Space: O(1)
    Tricky: Process from right to left
    """
    def next_valid_char(string: str, index: int) -> int:
        """Find next valid character (skipping backspaces)."""
        backspace_count = 0

        while index >= 0:
            if string[index] == '#':
                backspace_count += 1
            elif backspace_count > 0:
                backspace_count -= 1
            else:
                break
            index -= 1

        return index

    i, j = len(s) - 1, len(t) - 1

    while i >= 0 or j >= 0:
        i = next_valid_char(s, i)
        j = next_valid_char(t, j)

        # Compare characters
        if i >= 0 and j >= 0:
            if s[i] != t[j]:
                return False
        elif i >= 0 or j >= 0:
            # One string finished, other has characters
            return False

        i -= 1
        j -= 1

    return True


# ============================================================================
# PRACTICE PROBLEMS
# ============================================================================
"""
EASY:
- Two Sum II (167)
- Remove Duplicates from Sorted Array (26)
- Valid Palindrome (125)
- Merge Sorted Array (88)
- Squares of Sorted Array (977)

MEDIUM:
- 3Sum (15)
- Container With Most Water (11)
- Sort Colors (75)
- Remove Duplicates II (80)
- 3Sum Closest (16)

HARD:
- Trapping Rain Water (42)
- 4Sum (18)
- Substring with Concatenation of All Words (30)
"""

if __name__ == "__main__":
    # Test examples
    print("Two Sum:", two_sum_sorted([2, 7, 11, 15], 9))
    print("Three Sum:", three_sum([-1, 0, 1, 2, -1, -4]))
    print("Container Water:", container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print("Trap Water:", trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    print("Move Zeroes:", nums)
