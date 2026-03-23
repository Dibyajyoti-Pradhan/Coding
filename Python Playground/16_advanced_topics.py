"""
ADVANCED TOPICS - Complete Guide
=================================
Covers: Monotonic Stack, Prefix Sum Advanced, Matrix DP, Intervals, Design

These are common medium/hard interview patterns that appear frequently.
"""

from typing import List, Optional
from collections import deque
import heapq


# ============================================================================
# TOPIC 1: MONOTONIC STACK
# ============================================================================

"""
MONOTONIC STACK:
- Stack that maintains elements in increasing or decreasing order
- Used to find next greater/smaller element efficiently
- O(n) time for problems that seem O(n²)

Key Insight:
- Each element pushed and popped at most once → O(n) total
"""

def next_greater_elements(nums: List[int]) -> List[int]:
    """
    PROBLEM: Next Greater Element II (LeetCode 503)

    Given a circular integer array nums (the next element of nums[nums.length - 1]
    is nums[0]), return the next greater number for every element in nums.

    The next greater number of a number x is the first greater number to its
    traversing-order next in the array, which means you could search circularly
    to find its next greater number. If it doesn't exist, return -1 for this number.

    Example 1:
        Input: nums = [1,2,1]
        Output: [2,-1,2]
        Explanation:
            - First 1's next greater is 2
            - 2 has no next greater (max element)
            - Second 1's next greater is 2 (circular)

    Example 2:
        Input: nums = [1,2,3,4,3]
        Output: [2,3,4,-1,4]

    Constraints:
        - 1 <= nums.length <= 10^4
        - -10^9 <= nums[i] <= 10^9

    Time: O(n), Space: O(n)
    """
    n = len(nums)
    result = [-1] * n
    stack = []  # Monotonic decreasing stack (stores indices)

    # Process array twice to handle circular nature
    for i in range(2 * n):
        idx = i % n

        # Pop elements smaller than current
        while stack and nums[stack[-1]] < nums[idx]:
            result[stack.pop()] = nums[idx]

        # Only push in first pass
        if i < n:
            stack.append(i)

    return result


def daily_temperatures(temperatures: List[int]) -> List[int]:
    """
    PROBLEM: Daily Temperatures (LeetCode 739)

    Given an array of integers temperatures represents the daily temperatures,
    return an array answer such that answer[i] is the number of days you have
    to wait after the ith day to get a warmer temperature.

    If there is no future day for which this is possible, keep answer[i] == 0 instead.

    Example 1:
        Input: temperatures = [73,74,75,71,69,72,76,73]
        Output: [1,1,4,2,1,1,0,0]
        Explanation:
            Day 0: 73 → next warmer is 74 (day 1) → 1 day
            Day 1: 74 → next warmer is 75 (day 2) → 1 day
            Day 2: 75 → next warmer is 76 (day 6) → 4 days
            ...

    Example 2:
        Input: temperatures = [30,40,50,60]
        Output: [1,1,1,0]

    Example 3:
        Input: temperatures = [30,60,90]
        Output: [1,1,0]

    Constraints:
        - 1 <= temperatures.length <= 10^5
        - 30 <= temperatures[i] <= 100

    Time: O(n), Space: O(n)
    """
    n = len(temperatures)
    result = [0] * n
    stack = []  # Monotonic decreasing stack

    for i, temp in enumerate(temperatures):
        # Pop all days with cooler temperature
        while stack and temperatures[stack[-1]] < temp:
            prev_day = stack.pop()
            result[prev_day] = i - prev_day

        stack.append(i)

    return result


def largest_rectangle_histogram(heights: List[int]) -> int:
    """
    PROBLEM: Largest Rectangle in Histogram (LeetCode 84)

    Given an array of integers heights representing the histogram's bar height
    where the width of each bar is 1, return the area of the largest rectangle
    in the histogram.

    Example 1:
        Input: heights = [2,1,5,6,2,3]
        Output: 10
        Explanation: Rectangle with height=5, width=2 (indices 2-3)

    Example 2:
        Input: heights = [2,4]
        Output: 4

    Constraints:
        - 1 <= heights.length <= 10^5
        - 0 <= heights[i] <= 10^4

    Time: O(n), Space: O(n)
    Trick: Use monotonic increasing stack
    """
    stack = []
    max_area = 0

    for i, h in enumerate(heights):
        # Pop taller bars and calculate area
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)

        stack.append(i)

    # Process remaining bars
    while stack:
        height = heights[stack.pop()]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area


# ============================================================================
# TOPIC 2: ADVANCED PREFIX SUM
# ============================================================================

def product_except_self(nums: List[int]) -> List[int]:
    """
    PROBLEM: Product of Array Except Self (LeetCode 238)

    Given an integer array nums, return an array answer such that answer[i]
    is equal to the product of all the elements of nums except nums[i].

    You must write an algorithm that runs in O(n) time and without using
    the division operation.

    Example 1:
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]
        Explanation:
            answer[0] = 2*3*4 = 24
            answer[1] = 1*3*4 = 12
            answer[2] = 1*2*4 = 8
            answer[3] = 1*2*3 = 6

    Example 2:
        Input: nums = [-1,1,0,-3,3]
        Output: [0,0,9,0,0]

    Constraints:
        - 2 <= nums.length <= 10^5
        - -30 <= nums[i] <= 30
        - The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    Follow up: Can you solve it in O(1) extra space? (Output array doesn't count)

    Time: O(n), Space: O(1) excluding output
    """
    n = len(nums)
    result = [1] * n

    # Left pass: result[i] = product of all elements to left of i
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    # Right pass: multiply by product of all elements to right of i
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result


def subarray_sum_divisible_k(nums: List[int], k: int) -> int:
    """
    PROBLEM: Subarray Sums Divisible by K (LeetCode 974)

    Given an integer array nums and an integer k, return the number of
    non-empty subarrays that have a sum divisible by k.

    A subarray is a contiguous part of an array.

    Example 1:
        Input: nums = [4,5,0,-2,-3,1], k = 5
        Output: 7
        Explanation: Subarrays with sum divisible by 5:
            [4,5,0,-2,-3,1], [5], [5,0], [5,0,-2,-3], [0], [0,-2,-3], [-2,-3]

    Example 2:
        Input: nums = [5], k = 9
        Output: 0

    Constraints:
        - 1 <= nums.length <= 3 * 10^4
        - -10^4 <= nums[i] <= 10^4
        - 2 <= k <= 10^4

    Time: O(n), Space: O(k)
    Trick: Use prefix sum remainders
    """
    prefix_sum = 0
    remainder_count = {0: 1}  # remainder -> count
    result = 0

    for num in nums:
        prefix_sum += num
        remainder = prefix_sum % k

        # Handle negative remainders
        if remainder < 0:
            remainder += k

        # If we've seen this remainder before, those subarrays are divisible by k
        result += remainder_count.get(remainder, 0)
        remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

    return result


# ============================================================================
# TOPIC 3: MATRIX / 2D DP
# ============================================================================

def maximal_square(matrix: List[List[str]]) -> int:
    """
    PROBLEM: Maximal Square (LeetCode 221)

    Given an m x n binary matrix filled with 0's and 1's, find the largest
    square containing only 1's and return its area.

    Example 1:
        Input: matrix = [
            ["1","0","1","0","0"],
            ["1","0","1","1","1"],
            ["1","1","1","1","1"],
            ["1","0","0","1","0"]
        ]
        Output: 4
        Explanation: Largest square has side length 2

    Example 2:
        Input: matrix = [["0","1"],["1","0"]]
        Output: 1

    Example 3:
        Input: matrix = [["0"]]
        Output: 0

    Constraints:
        - m == matrix.length
        - n == matrix[i].length
        - 1 <= m, n <= 300
        - matrix[i][j] is '0' or '1'.

    Time: O(m*n), Space: O(n) with optimization
    DP Formula: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    """
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    dp = [0] * (n + 1)
    max_side = 0
    prev = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            temp = dp[j]

            if matrix[i-1][j-1] == '1':
                dp[j] = min(dp[j], dp[j-1], prev) + 1
                max_side = max(max_side, dp[j])
            else:
                dp[j] = 0

            prev = temp

    return max_side * max_side


def max_sum_rectangle(matrix: List[List[int]]) -> int:
    """
    PROBLEM: Max Sum Rectangle in 2D Matrix

    Given a 2D matrix, find the maximum sum rectangle.

    Example:
        Input: matrix = [
            [1, 2, -1, -4, -20],
            [-8, -3, 4, 2, 1],
            [3, 8, 10, 1, 3],
            [-4, -1, 1, 7, -6]
        ]
        Output: 29
        Explanation: Rectangle from (1,2) to (3,3) has sum 29

    Time: O(n² * m), Space: O(m)
    Trick: Fix left and right columns, use Kadane's on rows
    """
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    max_sum = float('-inf')

    # Fix left column
    for left in range(n):
        temp = [0] * m

        # Extend to right column
        for right in range(left, n):
            # Add current column to temp
            for i in range(m):
                temp[i] += matrix[i][right]

            # Apply Kadane's algorithm on temp
            current_sum = 0
            for val in temp:
                current_sum = max(val, current_sum + val)
                max_sum = max(max_sum, current_sum)

    return max_sum


# ============================================================================
# TOPIC 4: INTERVALS ADVANCED
# ============================================================================

def insert_interval(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """
    PROBLEM: Insert Interval (LeetCode 57)

    You are given an array of non-overlapping intervals intervals where
    intervals[i] = [starti, endi] represent the start and the end of the ith
    interval and intervals is sorted in ascending order by starti.

    You are also given an interval newInterval = [start, end] that represents
    the start and end of another interval.

    Insert newInterval into intervals such that intervals is still sorted in
    ascending order by starti and intervals still does not have any overlapping
    intervals (merge overlapping intervals if necessary).

    Return intervals after the insertion.

    Example 1:
        Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
        Output: [[1,5],[6,9]]

    Example 2:
        Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
        Output: [[1,2],[3,10],[12,16]]
        Explanation: [4,8] overlaps with [3,5],[6,7],[8,10].

    Constraints:
        - 0 <= intervals.length <= 10^4
        - intervals[i].length == 2
        - 0 <= starti <= endi <= 10^5
        - intervals is sorted by starti in ascending order.
        - newInterval.length == 2
        - 0 <= start <= end <= 10^5

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


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """
    PROBLEM: Meeting Rooms II (LeetCode 253)

    Given an array of meeting time intervals where intervals[i] = [starti, endi],
    return the minimum number of conference rooms required.

    Example 1:
        Input: intervals = [[0,30],[5,10],[15,20]]
        Output: 2
        Explanation:
            Room 1: [0,30]
            Room 2: [5,10], [15,20]

    Example 2:
        Input: intervals = [[7,10],[2,4]]
        Output: 1

    Constraints:
        - 1 <= intervals.length <= 10^4
        - 0 <= starti < endi <= 10^6

    Time: O(n log n), Space: O(n)
    """
    if not intervals:
        return 0

    # Separate start and end times
    starts = sorted(interval[0] for interval in intervals)
    ends = sorted(interval[1] for interval in intervals)

    rooms = 0
    end_ptr = 0

    for start in starts:
        if start < ends[end_ptr]:
            # Need new room
            rooms += 1
        else:
            # Can reuse room
            end_ptr += 1

    return rooms


# ============================================================================
# TOPIC 5: DESIGN PROBLEMS
# ============================================================================

class LRUCache:
    """
    PROBLEM: LRU Cache (LeetCode 146)

    Design a data structure that follows the constraints of a Least Recently
    Used (LRU) cache.

    Implement the LRUCache class:
    - LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    - int get(int key) Return the value of the key if the key exists, otherwise return -1.
    - void put(int key, int value) Update the value of the key if the key exists.
      Otherwise, add the key-value pair to the cache. If the number of keys exceeds
      the capacity from this operation, evict the least recently used key.

    The functions get and put must each run in O(1) average time complexity.

    Example:
        Input:
            ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
        Output:
            [null, null, null, 1, null, -1, null, -1, 3, 4]
        Explanation:
            LRUCache lRUCache = new LRUCache(2);
            lRUCache.put(1, 1); // cache is {1=1}
            lRUCache.put(2, 2); // cache is {1=1, 2=2}
            lRUCache.get(1);    // return 1
            lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
            lRUCache.get(2);    // returns -1 (not found)
            lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
            lRUCache.get(1);    // return -1 (not found)
            lRUCache.get(3);    // return 3
            lRUCache.get(4);    // return 4

    Constraints:
        - 1 <= capacity <= 3000
        - 0 <= key <= 10^4
        - 0 <= value <= 10^5
        - At most 2 * 10^5 calls will be made to get and put.

    Time: O(1) for both operations
    Space: O(capacity)
    """

    class Node:
        def __init__(self, key: int, value: int):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy head and tail
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove node from linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node):
        """Add node right after head (most recently used)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        # Move to head (mark as recently used)
        self._remove(node)
        self._add_to_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else:
            # Add new key
            if len(self.cache) >= self.capacity:
                # Remove LRU (node before tail)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]

            # Add new node
            new_node = self.Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)


# ============================================================================
# PRACTICE PROBLEMS
# ============================================================================

"""
MONOTONIC STACK:
- Next Greater Element I (496)
- Next Greater Element II (503)
- Daily Temperatures (739)
- Largest Rectangle in Histogram (84)
- Trapping Rain Water (42)
- Online Stock Span (901)

PREFIX SUM ADVANCED:
- Product of Array Except Self (238)
- Subarray Sums Divisible by K (974)
- Continuous Subarray Sum (523)
- Range Sum Query 2D (304)

MATRIX DP:
- Maximal Square (221)
- Maximal Rectangle (85)
- Dungeon Game (174)

INTERVALS:
- Insert Interval (57)
- Meeting Rooms II (253)
- Non-overlapping Intervals (435)
- Minimum Number of Arrows (452)

DESIGN:
- LRU Cache (146)
- LFU Cache (460)
- Design Twitter (355)
- Implement Queue using Stacks (232)
"""


if __name__ == "__main__":
    print("="*70)
    print("ADVANCED TOPICS - Test Examples")
    print("="*70)

    # Test 1: Monotonic Stack
    print("\n1. Daily Temperatures:")
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    print(f"   Input: {temps}")
    print(f"   Output: {daily_temperatures(temps)}")

    # Test 2: Product Except Self
    print("\n2. Product of Array Except Self:")
    nums = [1, 2, 3, 4]
    print(f"   Input: {nums}")
    print(f"   Output: {product_except_self(nums)}")

    # Test 3: LRU Cache
    print("\n3. LRU Cache:")
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(f"   get(1): {cache.get(1)}")
    cache.put(3, 3)
    print(f"   get(2): {cache.get(2)}")  # -1 (evicted)
    cache.put(4, 4)
    print(f"   get(1): {cache.get(1)}")  # -1 (evicted)
    print(f"   get(3): {cache.get(3)}")
    print(f"   get(4): {cache.get(4)}")

    print("\n" + "="*70)
    print("Master these patterns for hard interview problems!")
    print("="*70)
