"""
LINKED LIST - Complete Guide for Interview Preparation
=======================================================

CORE CONCEPTS:
--------------
1. Singly linked list: node with value and next pointer
2. Doubly linked list: node with value, next, and prev pointers
3. No random access - O(n) to access element by index
4. O(1) insertion/deletion if pointer available
5. Python doesn't have built-in linked list (use class)

TRICKY PARTS:
-------------
1. Always check for null/None pointers!
2. Drawing diagrams helps visualize pointer manipulation
3. Edge cases: empty list, single node, two nodes
4. Dummy head node simplifies many operations
5. Fast & slow pointers (Floyd's cycle detection)
6. Reversing links: need to keep track of prev, curr, next

COMMON PATTERNS:
----------------
1. Fast & Slow Pointers (cycle, middle, nth from end)
2. Dummy Head (simplify edge cases)
3. In-place Reversal
4. Merge sorted lists
5. Recursion (elegant but O(n) space)
"""

from typing import Optional, List


class ListNode:
    """Standard singly linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    """Doubly linked list or list with random pointer."""
    def __init__(self, val=0, next=None, prev=None, random=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.random = random


# ============================================================================
# PATTERN 1: FAST & SLOW POINTERS
# ============================================================================

def has_cycle(head: Optional[ListNode]) -> bool:
    """
    LeetCode 141 - Detect cycle in linked list.

    Time: O(n), Space: O(1)
    Tricky: Floyd's cycle detection - fast moves 2x, slow moves 1x
    """
    if not head:
        return False

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def detect_cycle_start(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    LeetCode 142 - Find the node where cycle begins.

    Time: O(n), Space: O(1)
    Tricky: After detecting cycle, reset slow to head and move both at same speed
    """
    if not head:
        return None

    slow = fast = head

    # Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        # No cycle
        return None

    # Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


def find_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    LeetCode 876 - Find middle node of linked list.

    Time: O(n), Space: O(1)
    Tricky: When fast reaches end, slow is at middle
    """
    if not head:
        return None

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    LeetCode 19 - Remove nth node from end.

    Time: O(n), Space: O(1)
    Tricky: Use two pointers with n gap between them
    """
    dummy = ListNode(0, head)
    fast = slow = dummy

    # Move fast n+1 steps ahead
    for _ in range(n + 1):
        if not fast:
            return head  # n is larger than list length
        fast = fast.next

    # Move both until fast reaches end
    while fast:
        slow = slow.next
        fast = fast.next

    # Remove nth node
    slow.next = slow.next.next

    return dummy.next


def is_palindrome(head: Optional[ListNode]) -> bool:
    """
    LeetCode 234 - Check if linked list is palindrome.

    Time: O(n), Space: O(1)
    Tricky: Find middle, reverse second half, compare
    """
    if not head or not head.next:
        return True

    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev = None
    curr = slow
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    # Compare first and second half
    left, right = head, prev
    while right:  # Only need to check second half
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True


# ============================================================================
# PATTERN 2: IN-PLACE REVERSAL
# ============================================================================

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    LeetCode 206 - Reverse linked list iteratively.

    Time: O(n), Space: O(1)
    Tricky: Keep track of prev, curr, next
    """
    prev = None
    curr = head

    while curr:
        next_temp = curr.next  # Save next
        curr.next = prev       # Reverse link
        prev = curr           # Move prev forward
        curr = next_temp      # Move curr forward

    return prev


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse linked list recursively.

    Time: O(n), Space: O(n) for recursion stack
    """
    if not head or not head.next:
        return head

    # Reverse rest of the list
    new_head = reverse_list_recursive(head.next)

    # Fix current node
    head.next.next = head
    head.next = None

    return new_head


def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    """
    LeetCode 92 - Reverse sublist from position left to right.

    Time: O(n), Space: O(1)
    Tricky: Keep track of connections before and after reversed portion
    """
    if not head or left == right:
        return head

    dummy = ListNode(0, head)
    prev = dummy

    # Move to position before left
    for _ in range(left - 1):
        prev = prev.next

    # Reverse from left to right
    curr = prev.next
    for _ in range(right - left):
        next_temp = curr.next
        curr.next = next_temp.next
        next_temp.next = prev.next
        prev.next = next_temp

    return dummy.next


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    LeetCode 25 - Reverse nodes in k-group.

    Time: O(n), Space: O(1)
    Tricky: Complex pointer manipulation
    """
    def reverse_segment(start: ListNode, end: ListNode) -> ListNode:
        """Reverse nodes from start to end (exclusive)."""
        prev = None
        curr = start

        while curr != end:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        return prev

    dummy = ListNode(0, head)
    prev_group_end = dummy

    while True:
        # Find k nodes
        kth_node = prev_group_end
        for _ in range(k):
            kth_node = kth_node.next
            if not kth_node:
                return dummy.next

        next_group_start = kth_node.next

        # Reverse current group
        first = prev_group_end.next
        prev_group_end.next = reverse_segment(first, next_group_start)

        # Connect to next group
        first.next = next_group_start

        # Move to next group
        prev_group_end = first

    return dummy.next


# ============================================================================
# PATTERN 3: MERGE / SORT
# ============================================================================

def merge_two_sorted_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    LeetCode 21 - Merge two sorted linked lists.

    Time: O(n + m), Space: O(1)
    """
    dummy = ListNode(0)
    curr = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    # Attach remaining nodes
    curr.next = l1 if l1 else l2

    return dummy.next


def merge_k_sorted_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    LeetCode 23 - Merge k sorted linked lists.

    Time: O(n log k) where n is total nodes, k is number of lists
    Space: O(k) for heap
    """
    import heapq

    # Min heap: (value, list_index, node)
    heap = []

    # Initialize heap with first node from each list
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode(0)
    curr = dummy

    # Counter for unique list index (in case values are same)
    counter = len(lists)

    while heap:
        val, list_idx, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(heap, (node.next.val, counter, node.next))
            counter += 1

    return dummy.next


def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    LeetCode 148 - Sort linked list using merge sort.

    Time: O(n log n), Space: O(log n) for recursion
    """
    if not head or not head.next:
        return head

    # Find middle using slow-fast pointers
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Split into two halves
    mid = slow.next
    slow.next = None

    # Recursively sort both halves
    left = sort_list(head)
    right = sort_list(mid)

    # Merge sorted halves
    return merge_two_sorted_lists(left, right)


# ============================================================================
# PATTERN 4: REORDER / PARTITION
# ============================================================================

def partition_list(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    """
    LeetCode 86 - Partition list around value x.

    Time: O(n), Space: O(1)
    Tricky: Use two separate lists, then connect
    """
    before_head = ListNode(0)
    after_head = ListNode(0)

    before = before_head
    after = after_head

    while head:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next

        head = head.next

    # Important: terminate after list
    after.next = None

    # Connect two lists
    before.next = after_head.next

    return before_head.next


def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    LeetCode 328 - Group odd and even positioned nodes.

    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = even_head

    return head


def reorder_list(head: Optional[ListNode]) -> None:
    """
    LeetCode 143 - Reorder list: L0→Ln→L1→Ln-1→L2→Ln-2→...

    Time: O(n), Space: O(1)
    Tricky: Find middle, reverse second half, merge alternately
    """
    if not head or not head.next:
        return

    # Find middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev, curr = None, slow
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    # Merge two halves alternately
    first, second = head, prev
    while second.next:
        temp1, temp2 = first.next, second.next

        first.next = second
        second.next = temp1

        first = temp1
        second = temp2


# ============================================================================
# PATTERN 5: INTERSECTION / CYCLE
# ============================================================================

def get_intersection_node(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    """
    LeetCode 160 - Find intersection of two linked lists.

    Time: O(n + m), Space: O(1)
    Tricky: Use two pointers, switch heads when reaching end
    """
    if not headA or not headB:
        return None

    pA, pB = headA, headB

    # When pA reaches end, redirect to headB
    # When pB reaches end, redirect to headA
    # They will meet at intersection or None
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA

    return pA


# ============================================================================
# PATTERN 6: COPY / CLONE
# ============================================================================

def copy_random_list(head: Optional[Node]) -> Optional[Node]:
    """
    LeetCode 138 - Copy list with random pointer.

    Time: O(n), Space: O(n) or O(1) with interweaving
    """
    if not head:
        return None

    # Approach 1: Using hashmap - O(n) space
    old_to_new = {}

    # First pass: create all nodes
    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next

    # Second pass: connect pointers
    curr = head
    while curr:
        if curr.next:
            old_to_new[curr].next = old_to_new[curr.next]
        if curr.random:
            old_to_new[curr].random = old_to_new[curr.random]
        curr = curr.next

    return old_to_new[head]


def copy_random_list_constant_space(head: Optional[Node]) -> Optional[Node]:
    """
    Copy list with random pointer using O(1) space.

    Tricky: Interweave old and new nodes
    """
    if not head:
        return None

    # Step 1: Create new nodes and interweave
    curr = head
    while curr:
        new_node = Node(curr.val)
        new_node.next = curr.next
        curr.next = new_node
        curr = new_node.next

    # Step 2: Set random pointers
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # Step 3: Separate lists
    curr = head
    new_head = head.next
    while curr:
        new_node = curr.next
        curr.next = new_node.next
        curr = curr.next

        if curr:
            new_node.next = curr.next

    return new_head


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def create_linked_list(values: List[int]) -> Optional[ListNode]:
    """Helper: Create linked list from array."""
    if not values:
        return None

    head = ListNode(values[0])
    curr = head

    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    return head


def linked_list_to_array(head: Optional[ListNode]) -> List[int]:
    """Helper: Convert linked list to array."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def print_linked_list(head: Optional[ListNode]) -> None:
    """Helper: Print linked list."""
    values = linked_list_to_array(head)
    print(" -> ".join(map(str, values)))


# ============================================================================
# PRACTICE PROBLEMS
# ============================================================================
"""
EASY:
- Reverse Linked List (206)
- Merge Two Sorted Lists (21)
- Linked List Cycle (141)
- Remove Duplicates from Sorted List (83)
- Intersection of Two Linked Lists (160)

MEDIUM:
- Add Two Numbers (2)
- Remove Nth Node From End (19)
- Reverse Linked List II (92)
- Reorder List (143)
- Odd Even Linked List (328)
- Sort List (148)
- Palindrome Linked List (234)
- Copy List with Random Pointer (138)

HARD:
- Merge k Sorted Lists (23)
- Reverse Nodes in k-Group (25)
"""

if __name__ == "__main__":
    # Test examples
    # Create list: 1 -> 2 -> 3 -> 4 -> 5
    head = create_linked_list([1, 2, 3, 4, 5])
    print("Original:", linked_list_to_array(head))

    # Reverse
    reversed_head = reverse_list(create_linked_list([1, 2, 3, 4, 5]))
    print("Reversed:", linked_list_to_array(reversed_head))

    # Find middle
    middle = find_middle(create_linked_list([1, 2, 3, 4, 5]))
    print("Middle:", middle.val if middle else None)

    # Merge two sorted lists
    l1 = create_linked_list([1, 3, 5])
    l2 = create_linked_list([2, 4, 6])
    merged = merge_two_sorted_lists(l1, l2)
    print("Merged:", linked_list_to_array(merged))
