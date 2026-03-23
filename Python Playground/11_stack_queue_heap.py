"""
STACK, QUEUE & HEAP - Complete Guide for Interview Preparation
===============================================================

CORE CONCEPTS:
--------------
STACK (LIFO - Last In First Out):
- Operations: push O(1), pop O(1), peek O(1)
- Use cases: function calls, expression evaluation, backtracking, DFS
- Python: list.append(), list.pop()

QUEUE (FIFO - First In First Out):
- Operations: enqueue O(1), dequeue O(1)
- Use cases: BFS, scheduling, buffering
- Python: collections.deque (not list!)

HEAP (Priority Queue):
- Min heap: parent ≤ children, Max heap: parent ≥ children
- Operations: insert O(log n), extract-min/max O(log n), peek O(1)
- Use cases: top K elements, median tracking, Dijkstra's
- Python: heapq module (min heap only)

TRICKY PARTS:
-------------
1. Python list is NOT efficient queue (pop(0) is O(n))
2. heapq is min heap - negate values for max heap
3. Stack for DFS, Queue for BFS
4. Monotonic stack/queue for next greater/smaller element
5. Parentheses matching requires stack

COMMON PATTERNS:
----------------
1. Stack: expression evaluation, next greater element
2. Queue: BFS, sliding window maximum
3. Heap: top K, merge K sorted, median
4. Monotonic Stack/Queue
5. Design problems (MinStack, MaxQueue)
"""

from typing import List, Optional
from collections import deque
import heapq


# ============================================================================
# PATTERN 1: STACK BASICS
# ============================================================================

def is_valid_parentheses(s: str) -> bool:
    """
    LeetCode 20 - Valid parentheses.

    Time: O(n), Space: O(n)
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)

    return not stack


def eval_rpn(tokens: List[str]) -> int:
    """
    LeetCode 150 - Evaluate reverse Polish notation.

    Time: O(n), Space: O(n)
    """
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            else:  # Division
                result = int(a / b)  # Truncate toward zero

            stack.append(result)
        else:
            stack.append(int(token))

    return stack[0]


def simplify_path(path: str) -> str:
    """
    LeetCode 71 - Simplify Unix file path.

    Time: O(n), Space: O(n)
    """
    stack = []

    for component in path.split('/'):
        if component == '..' and stack:
            stack.pop()
        elif component and component not in ('.', '..'):
            stack.append(component)

    return '/' + '/'.join(stack)


# ============================================================================
# PATTERN 2: MONOTONIC STACK
# ============================================================================

def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    LeetCode 496 - Next greater element I.

    Time: O(n), Space: O(n)
    Tricky: Use monotonic decreasing stack
    """
    next_greater = {}
    stack = []

    # Build next greater map for nums2
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)

    return [next_greater.get(num, -1) for num in nums1]


def next_greater_element_ii(nums: List[int]) -> List[int]:
    """
    LeetCode 503 - Next greater element II (circular array).

    Time: O(n), Space: O(n)
    Tricky: Process array twice using modulo
    """
    n = len(nums)
    result = [-1] * n
    stack = []

    # Process array twice to handle circular nature
    for i in range(2 * n):
        idx = i % n

        while stack and nums[stack[-1]] < nums[idx]:
            result[stack.pop()] = nums[idx]

        if i < n:
            stack.append(i)

    return result


def daily_temperatures(temperatures: List[int]) -> List[int]:
    """
    LeetCode 739 - Days until warmer temperature.

    Time: O(n), Space: O(n)
    """
    n = len(temperatures)
    result = [0] * n
    stack = []

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx

        stack.append(i)

    return result


def largest_rectangle_histogram(heights: List[int]) -> int:
    """
    LeetCode 84 - Largest rectangle in histogram.

    Time: O(n), Space: O(n)
    Tricky: Use monotonic increasing stack
    """
    stack = []
    max_area = 0

    for i, h in enumerate(heights):
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


def trap_rain_water(height: List[int]) -> int:
    """
    LeetCode 42 - Trapping rain water using stack.

    Time: O(n), Space: O(n)
    """
    stack = []
    water = 0

    for i, h in enumerate(height):
        while stack and height[stack[-1]] < h:
            bottom = stack.pop()

            if not stack:
                break

            distance = i - stack[-1] - 1
            bounded_height = min(height[stack[-1]], h) - height[bottom]
            water += distance * bounded_height

        stack.append(i)

    return water


# ============================================================================
# PATTERN 3: DESIGN PROBLEMS
# ============================================================================

class MinStack:
    """
    LeetCode 155 - Min stack (get minimum in O(1)).

    Tricky: Use two stacks or store (value, min) pairs
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


class MaxStack:
    """
    Stack that supports push, pop, top, and retrieving max in O(1).
    """
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.max_stack or val >= self.max_stack[-1]:
            self.max_stack.append(val)

    def pop(self) -> int:
        val = self.stack.pop()
        if val == self.max_stack[-1]:
            self.max_stack.pop()
        return val

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1]


# ============================================================================
# PATTERN 4: QUEUE - BFS
# ============================================================================

def level_order_traversal(root):
    """
    BFS using queue for tree level order traversal.

    Time: O(n), Space: O(w) where w is max width
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


# ============================================================================
# PATTERN 5: MONOTONIC QUEUE (Sliding Window Maximum)
# ============================================================================

def max_sliding_window(nums: List[int], k: int) -> List[int]:
    """
    LeetCode 239 - Sliding window maximum.

    Time: O(n), Space: O(k)
    Tricky: Use monotonic decreasing deque
    """
    dq = deque()  # Store indices
    result = []

    for i, num in enumerate(nums):
        # Remove indices outside window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Maintain decreasing order
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        # Add to result when window formed
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


def longest_subarray_limit(nums: List[int], limit: int) -> int:
    """
    LeetCode 1438 - Longest subarray with absolute diff <= limit.

    Time: O(n), Space: O(n)
    Tricky: Use two deques for min and max
    """
    max_dq = deque()  # Decreasing deque
    min_dq = deque()  # Increasing deque
    left = 0
    max_length = 0

    for right, num in enumerate(nums):
        # Maintain decreasing deque for max
        while max_dq and nums[max_dq[-1]] < num:
            max_dq.pop()
        max_dq.append(right)

        # Maintain increasing deque for min
        while min_dq and nums[min_dq[-1]] > num:
            min_dq.pop()
        min_dq.append(right)

        # Shrink window if constraint violated
        while nums[max_dq[0]] - nums[min_dq[0]] > limit:
            left += 1
            if max_dq[0] < left:
                max_dq.popleft()
            if min_dq[0] < left:
                min_dq.popleft()

        max_length = max(max_length, right - left + 1)

    return max_length


# ============================================================================
# PATTERN 6: HEAP (Priority Queue) - TOP K ELEMENTS
# ============================================================================

def kth_largest(nums: List[int], k: int) -> int:
    """
    LeetCode 215 - Kth largest element.

    Time: O(n log k), Space: O(k)
    """
    # Min heap of size k
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    LeetCode 347 - Top k frequent elements.

    Time: O(n log k), Space: O(n)
    """
    from collections import Counter

    count = Counter(nums)

    # Use heap to find top k
    return heapq.nlargest(k, count.keys(), key=count.get)


def k_closest_points(points: List[List[int]], k: int) -> List[List[int]]:
    """
    LeetCode 973 - K closest points to origin.

    Time: O(n log k), Space: O(k)
    Tricky: Use max heap (negate distances) of size k
    """
    heap = []

    for x, y in points:
        dist = -(x*x + y*y)  # Negative for max heap

        heapq.heappush(heap, (dist, x, y))

        if len(heap) > k:
            heapq.heappop(heap)

    return [[x, y] for (_, x, y) in heap]


# ============================================================================
# PATTERN 7: HEAP - MERGE K SORTED
# ============================================================================

def merge_k_sorted_lists(lists):
    """
    LeetCode 23 - Merge k sorted linked lists.

    Time: O(n log k), Space: O(k)
    """
    heap = []
    result_head = result_tail = None

    # Initialize heap with first node from each list
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    counter = len(lists)

    while heap:
        val, list_idx, node = heapq.heappop(heap)

        # Add to result
        if not result_head:
            result_head = result_tail = node
        else:
            result_tail.next = node
            result_tail = node

        # Add next node from same list
        if node.next:
            heapq.heappush(heap, (node.next.val, counter, node.next))
            counter += 1

    return result_head


def smallest_range_k_lists(nums: List[List[int]]) -> List[int]:
    """
    LeetCode 632 - Smallest range covering elements from k lists.

    Time: O(n log k), Space: O(k)
    """
    heap = []
    max_val = float('-inf')

    # Initialize heap with first element from each list
    for i, lst in enumerate(nums):
        heapq.heappush(heap, (lst[0], i, 0))
        max_val = max(max_val, lst[0])

    range_start, range_end = 0, float('inf')

    while len(heap) == len(nums):
        min_val, list_idx, elem_idx = heapq.heappop(heap)

        # Update range if smaller
        if max_val - min_val < range_end - range_start:
            range_start, range_end = min_val, max_val

        # Add next element from same list
        if elem_idx + 1 < len(nums[list_idx]):
            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
            max_val = max(max_val, next_val)

    return [range_start, range_end]


# ============================================================================
# PATTERN 8: HEAP - MEDIAN TRACKING
# ============================================================================

class MedianFinder:
    """
    LeetCode 295 - Find median from data stream.

    Tricky: Use two heaps - max heap for smaller half, min heap for larger half
    """
    def __init__(self):
        self.small = []  # Max heap (negate values)
        self.large = []  # Min heap

    def addNum(self, num: int) -> None:
        # Add to max heap (small)
        heapq.heappush(self.small, -num)

        # Balance: move largest from small to large
        if self.small and self.large and (-self.small[0]) > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        # Maintain size property (small.size >= large.size)
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0


# ============================================================================
# PYTHON HEAP TRICKS
# ============================================================================

def python_heap_operations():
    """Python heapq module operations."""

    # heapq is min heap only!
    heap = []

    # Push
    heapq.heappush(heap, 5)
    heapq.heappush(heap, 3)

    # Pop minimum
    min_val = heapq.heappop(heap)

    # Peek minimum
    min_val = heap[0]

    # Create heap from list
    arr = [3, 1, 4, 1, 5, 9]
    heapq.heapify(arr)  # O(n)

    # N smallest/largest
    heapq.nsmallest(3, arr)
    heapq.nlargest(3, arr)

    # Max heap - negate values
    max_heap = []
    heapq.heappush(max_heap, -5)
    max_val = -heapq.heappop(max_heap)

    # Heap with custom objects
    heap = []
    heapq.heappush(heap, (priority, item))


# ============================================================================
# PRACTICE PROBLEMS
# ============================================================================
"""
EASY (Stack):
- Valid Parentheses (20)
- Implement Stack using Queues (225)

MEDIUM (Stack):
- Min Stack (155)
- Daily Temperatures (739)
- Evaluate RPN (150)
- Next Greater Element (496, 503)
- Simplify Path (71)

HARD (Stack):
- Largest Rectangle in Histogram (84)
- Maximal Rectangle (85)
- Basic Calculator (224)

EASY (Queue):
- Implement Queue using Stacks (232)

MEDIUM (Queue):
- Sliding Window Maximum (239)
- Design Circular Queue (622)

EASY (Heap):
- Kth Largest Element in Stream (703)
- Last Stone Weight (1046)

MEDIUM (Heap):
- Kth Largest Element (215)
- Top K Frequent Elements (347)
- K Closest Points (973)
- Reorganize String (767)

HARD (Heap):
- Find Median from Data Stream (295)
- Merge k Sorted Lists (23)
- Smallest Range Covering K Lists (632)
- IPO (502)
"""

if __name__ == "__main__":
    # Test Stack
    print("Valid Parentheses:", is_valid_parentheses("()[]{}"))
    print("RPN:", eval_rpn(["2", "1", "+", "3", "*"]))

    # Test Monotonic Stack
    print("Next Greater:", next_greater_element([4, 1, 2], [1, 3, 4, 2]))
    print("Daily Temps:", daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))

    # Test Heap
    print("Kth Largest:", kth_largest([3, 2, 1, 5, 6, 4], 2))
    print("Top K Frequent:", top_k_frequent([1, 1, 1, 2, 2, 3], 2))
