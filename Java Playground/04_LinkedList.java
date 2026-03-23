import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Set;

/**
 * Linked List Problems - Complete Guide for Interview Preparation.
 *
 * <p>Core Concepts:
 * <ul>
 *   <li>Always check head == null and head.next == null edge cases.</li>
 *   <li>Dummy head node pattern eliminates special-casing of head modifications.</li>
 *   <li>Fast/slow pointer: fast moves 2 steps, slow moves 1 step (cycle, middle).</li>
 *   <li>Draw pointer diagrams mentally before coding in-place reversals.</li>
 *   <li>Time Complexity: O(n) traversal, O(n^2) nested loops. Space: O(1) for
 *       in-place, O(n) for recursion.</li>
 * </ul>
 *
 * <p>Tricky Parts:
 * <ul>
 *   <li>In-place reversal: maintain prev, curr, next pointers carefully.</li>
 *   <li>Cycle detection: Floyd's algorithm uses slow/fast pointers.</li>
 *   <li>Random pointer copy: HashMap to map original nodes to copies.</li>
 *   <li>Palindrome: find middle, reverse second half, then compare.</li>
 * </ul>
 *
 * @author Google Senior SWE Interview Playground
 */
public class LinkedList {

  /**
   * Definition for singly-linked list node.
   */
  public static class ListNode {
    int val;
    ListNode next;

    /**
     * Constructor with value only.
     *
     * @param val node value
     */
    public ListNode(int val) {
      this.val = val;
    }

    /**
     * Constructor with value and next pointer.
     *
     * @param val node value
     * @param next next node
     */
    public ListNode(int val, ListNode next) {
      this.val = val;
      this.next = next;
    }
  }

  /**
   * Definition for linked list node with random pointer (LC 138).
   */
  public static class RandomNode {
    int val;
    RandomNode next;
    RandomNode random;

    /**
     * Constructor for RandomNode.
     *
     * @param val node value
     */
    public RandomNode(int val) {
      this.val = val;
      this.next = null;
      this.random = null;
    }
  }

  /**
   * Detect if linked list has a cycle using Floyd's algorithm.
   *
   * <p>LeetCode 141 - Linked List Cycle (Easy)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(1)
   *
   * @param head head of linked list
   * @return true if cycle exists, false otherwise
   * @throws IllegalArgumentException if head is null
   */
  public static boolean hasCycle(ListNode head) {
    if (head == null || head.next == null) {
      return false;
    }

    ListNode slow = head;
    ListNode fast = head;

    while (fast != null && fast.next != null) {
      slow = slow.next;
      fast = fast.next.next;

      if (slow == fast) {
        return true;
      }
    }

    return false;
  }

  /**
   * Detect cycle and return node where cycle begins.
   *
   * <p>LeetCode 142 - Linked List Cycle II (Medium)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(1)
   *
   * <p>Pattern: Find meeting point with slow/fast pointers. Then reset one pointer to
   * head and move both one step at a time until they meet at cycle start.
   *
   * @param head head of linked list
   * @return node where cycle begins, or null if no cycle
   */
  public static ListNode detectCycle(ListNode head) {
    if (head == null || head.next == null) {
      return null;
    }

    ListNode slow = head;
    ListNode fast = head;

    while (fast != null && fast.next != null) {
      slow = slow.next;
      fast = fast.next.next;

      if (slow == fast) {
        ListNode ptr1 = head;
        ListNode ptr2 = slow;

        while (ptr1 != ptr2) {
          ptr1 = ptr1.next;
          ptr2 = ptr2.next;
        }

        return ptr1;
      }
    }

    return null;
  }

  /**
   * Find middle of linked list using slow/fast pointers.
   *
   * <p>Time Complexity: O(n), Space Complexity: O(1)
   *
   * @param head head of linked list
   * @return middle node (or first of two middle nodes if even length)
   */
  public static ListNode findMiddle(ListNode head) {
    if (head == null || head.next == null) {
      return head;
    }

    ListNode slow = head;
    ListNode fast = head;

    while (fast != null && fast.next != null) {
      slow = slow.next;
      fast = fast.next.next;
    }

    return slow;
  }

  /**
   * Remove Nth node from end of list.
   *
   * <p>LeetCode 19 - Remove Nth Node From End of List (Medium)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(1)
   *
   * <p>Pattern: Use dummy head. Two-pointer technique with n-step gap.
   *
   * @param head head of linked list
   * @param n position from end to remove (1-indexed)
   * @return new head after removal
   * @throws IllegalArgumentException if head is null or n is invalid
   */
  public static ListNode removeNthFromEnd(ListNode head, int n) {
    if (head == null || n < 1) {
      throw new IllegalArgumentException("Invalid input");
    }

    ListNode dummy = new ListNode(0, head);
    ListNode first = dummy;
    ListNode second = dummy;

    for (int i = 0; i <= n; i++) {
      if (first == null) {
        throw new IllegalArgumentException("n is greater than list length");
      }
      first = first.next;
    }

    while (first != null) {
      first = first.next;
      second = second.next;
    }

    second.next = second.next.next;
    return dummy.next;
  }

  /**
   * Reverse entire linked list.
   *
   * <p>LeetCode 206 - Reverse Linked List (Easy)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(1)
   *
   * @param head head of linked list
   * @return new head of reversed list
   */
  public static ListNode reverseList(ListNode head) {
    ListNode prev = null;
    ListNode curr = head;

    while (curr != null) {
      ListNode nextTemp = curr.next;
      curr.next = prev;
      prev = curr;
      curr = nextTemp;
    }

    return prev;
  }

  /**
   * Reverse linked list between positions left and right.
   *
   * <p>LeetCode 92 - Reverse Linked List II (Medium)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(1)
   *
   * @param head head of linked list
   * @param left start position (1-indexed)
   * @param right end position (1-indexed)
   * @return head of modified list
   * @throws IllegalArgumentException if left or right invalid
   */
  public static ListNode reverseBetween(ListNode head, int left, int right) {
    if (head == null || left < 1 || left > right) {
      throw new IllegalArgumentException("Invalid left or right position");
    }

    ListNode dummy = new ListNode(0, head);
    ListNode prevLeft = dummy;

    for (int i = 1; i < left; i++) {
      if (prevLeft.next == null) {
        throw new IllegalArgumentException("Left position exceeds list length");
      }
      prevLeft = prevLeft.next;
    }

    ListNode leftNode = prevLeft.next;
    ListNode prevCurr = leftNode;
    ListNode curr = leftNode.next;

    for (int i = 0; i < right - left; i++) {
      if (curr == null) {
        throw new IllegalArgumentException("Right position exceeds list length");
      }
      ListNode nextTemp = curr.next;
      curr.next = prevCurr;
      prevCurr = curr;
      curr = nextTemp;
    }

    leftNode.next = curr;
    prevLeft.next = prevCurr;

    return dummy.next;
  }

  /**
   * Reverse nodes of k group.
   *
   * <p>LeetCode 25 - Reverse Nodes in k-Group (Hard)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(1)
   *
   * @param head head of linked list
   * @param k group size
   * @return head of modified list
   * @throws IllegalArgumentException if head is null or k invalid
   */
  public static ListNode reverseKGroup(ListNode head, int k) {
    if (head == null || k < 1) {
      throw new IllegalArgumentException("Invalid input");
    }

    ListNode dummy = new ListNode(0, head);
    ListNode prevGroup = dummy;

    while (true) {
      ListNode groupEnd = prevGroup;
      for (int i = 0; i < k; i++) {
        groupEnd = groupEnd.next;
        if (groupEnd == null) {
          return dummy.next;
        }
      }

      ListNode nextGroup = groupEnd.next;
      ListNode curr = prevGroup.next;
      ListNode prev = nextGroup;

      for (int i = 0; i < k; i++) {
        ListNode nextTemp = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nextTemp;
      }

      ListNode temp = prevGroup.next;
      prevGroup.next = groupEnd;
      prevGroup = temp;
    }
  }

  /**
   * Merge two sorted linked lists.
   *
   * <p>LeetCode 21 - Merge Two Sorted Lists (Easy)
   *
   * <p>Time Complexity: O(n + m), Space Complexity: O(1)
   *
   * @param list1 first sorted list
   * @param list2 second sorted list
   * @return merged sorted list
   */
  public static ListNode mergeTwoLists(ListNode list1, ListNode list2) {
    ListNode dummy = new ListNode(0);
    ListNode curr = dummy;

    while (list1 != null && list2 != null) {
      if (list1.val <= list2.val) {
        curr.next = list1;
        list1 = list1.next;
      } else {
        curr.next = list2;
        list2 = list2.next;
      }
      curr = curr.next;
    }

    if (list1 != null) {
      curr.next = list1;
    } else {
      curr.next = list2;
    }

    return dummy.next;
  }

  /**
   * Merge K sorted linked lists.
   *
   * <p>LeetCode 23 - Merge k Sorted Lists (Hard)
   *
   * <p>Time Complexity: O(n log k) where k is number of lists
   *
   * <p>Space Complexity: O(k) for priority queue
   *
   * @param lists array of sorted lists
   * @return merged sorted list
   * @throws IllegalArgumentException if lists is null
   */
  public static ListNode mergeKLists(ListNode[] lists) {
    if (lists == null || lists.length == 0) {
      throw new IllegalArgumentException("Input lists cannot be null or empty");
    }

    PriorityQueue<ListNode> minHeap = new PriorityQueue<>((a, b) ->
        Integer.compare(a.val, b.val));

    for (ListNode list : lists) {
      if (list != null) {
        minHeap.offer(list);
      }
    }

    ListNode dummy = new ListNode(0);
    ListNode curr = dummy;

    while (!minHeap.isEmpty()) {
      ListNode node = minHeap.poll();
      curr.next = node;
      curr = curr.next;

      if (node.next != null) {
        minHeap.offer(node.next);
      }
    }

    return dummy.next;
  }

  /**
   * Reorder list: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2.
   *
   * <p>LeetCode 143 - Reorder List (Medium)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(1)
   *
   * <p>Pattern: Find middle, reverse second half, merge two halves.
   *
   * @param head head of linked list
   * @throws IllegalArgumentException if head is null
   */
  public static void reorderList(ListNode head) {
    if (head == null || head.next == null) {
      return;
    }

    ListNode middle = findMiddle(head);
    ListNode secondHalf = middle.next;
    middle.next = null;

    secondHalf = reverseList(secondHalf);

    ListNode first = head;
    ListNode second = secondHalf;

    while (second != null) {
      ListNode firstNext = first.next;
      ListNode secondNext = second.next;

      first.next = second;
      second.next = firstNext;

      first = firstNext;
      second = secondNext;
    }
  }

  /**
   * Odd-Even Linked List: separate odd and even positioned nodes.
   *
   * <p>LeetCode 328 - Odd Even Linked List (Medium)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(1)
   *
   * @param head head of linked list
   * @return head of modified list (odd nodes first, then even nodes)
   */
  public static ListNode oddEvenList(ListNode head) {
    if (head == null || head.next == null) {
      return head;
    }

    ListNode oddHead = head;
    ListNode evenHead = head.next;
    ListNode oddTail = oddHead;
    ListNode evenTail = evenHead;

    ListNode curr = head.next.next;
    boolean isOdd = true;

    while (curr != null) {
      if (isOdd) {
        oddTail.next = curr;
        oddTail = oddTail.next;
      } else {
        evenTail.next = curr;
        evenTail = evenTail.next;
      }

      curr = curr.next;
      isOdd = !isOdd;
    }

    oddTail.next = evenHead;
    evenTail.next = null;

    return oddHead;
  }

  /**
   * Copy list with random pointer.
   *
   * <p>LeetCode 138 - Copy List with Random Pointer (Medium)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(n)
   *
   * <p>Pattern: First pass create copies and store in map. Second pass set next/random
   * pointers using map.
   *
   * @param head head of list with random pointers
   * @return deep copy of list
   */
  public static RandomNode copyRandomList(RandomNode head) {
    if (head == null) {
      return null;
    }

    Map<RandomNode, RandomNode> nodeMap = new HashMap<>();
    RandomNode curr = head;

    while (curr != null) {
      nodeMap.put(curr, new RandomNode(curr.val));
      curr = curr.next;
    }

    curr = head;
    while (curr != null) {
      RandomNode copy = nodeMap.get(curr);
      copy.next = nodeMap.get(curr.next);
      copy.random = nodeMap.get(curr.random);
      curr = curr.next;
    }

    return nodeMap.get(head);
  }

  /**
   * Check if linked list is a palindrome using slow/fast pointers.
   *
   * <p>LeetCode 234 - Palindrome Linked List (Easy)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(1)
   *
   * <p>Pattern: Find middle, reverse second half, compare two halves.
   *
   * @param head head of linked list
   * @return true if list is palindrome
   */
  public static boolean isPalindrome(ListNode head) {
    if (head == null || head.next == null) {
      return true;
    }

    ListNode middle = findMiddle(head);
    ListNode secondHalf = reverseList(middle.next);

    ListNode first = head;
    ListNode second = secondHalf;

    while (second != null) {
      if (first.val != second.val) {
        return false;
      }
      first = first.next;
      second = second.next;
    }

    return true;
  }

  /**
   * Helper to print linked list for testing.
   *
   * @param head head of list
   * @return string representation
   */
  private static String printList(ListNode head) {
    StringBuilder sb = new StringBuilder();
    ListNode curr = head;
    while (curr != null) {
      sb.append(curr.val).append(" -> ");
      curr = curr.next;
    }
    sb.append("null");
    return sb.toString();
  }

  /**
   * Main method with comprehensive test cases.
   *
   * @param args command-line arguments (unused)
   */
  public static void main(String[] args) {
    System.out.println("=== Linked List Problems ===\n");

    // Test reverseList
    System.out.println("1. Reverse Linked List:");
    ListNode head1 = new ListNode(1, new ListNode(2, new ListNode(3,
        new ListNode(4))));
    System.out.println("  Input: " + printList(head1));
    ListNode reversed = reverseList(head1);
    System.out.println("  Output: " + printList(reversed) + "\n");

    // Test hasCycle
    System.out.println("2. Detect Cycle:");
    ListNode cycleNode = new ListNode(3);
    ListNode head2 = new ListNode(1, new ListNode(2, cycleNode));
    cycleNode.next = head2.next;
    boolean hasCycle = hasCycle(head2);
    System.out.println("  List with cycle: " + hasCycle + "\n");

    // Test findMiddle
    System.out.println("3. Find Middle:");
    ListNode head3 = new ListNode(1, new ListNode(2, new ListNode(3,
        new ListNode(4, new ListNode(5)))));
    ListNode middle = findMiddle(head3);
    System.out.println("  Input: " + printList(head3));
    System.out.println("  Middle value: " + middle.val + "\n");

    // Test mergeTwoLists
    System.out.println("4. Merge Two Sorted Lists:");
    ListNode list1 = new ListNode(1, new ListNode(2, new ListNode(4)));
    ListNode list2 = new ListNode(1, new ListNode(3, new ListNode(4)));
    ListNode merged = mergeTwoLists(list1, list2);
    System.out.println("  Output: " + printList(merged) + "\n");

    // Test reorderList
    System.out.println("5. Reorder List:");
    ListNode head5 = new ListNode(1, new ListNode(2, new ListNode(3,
        new ListNode(4))));
    System.out.println("  Input: " + printList(head5));
    reorderList(head5);
    System.out.println("  Output: " + printList(head5) + "\n");

    // Test isPalindrome
    System.out.println("6. Palindrome Check:");
    ListNode head6 = new ListNode(1, new ListNode(2, new ListNode(2,
        new ListNode(1))));
    System.out.println("  Input: " + printList(head6));
    boolean isPal = isPalindrome(head6);
    System.out.println("  Is Palindrome: " + isPal + "\n");

    // Test oddEvenList
    System.out.println("7. Odd Even Linked List:");
    ListNode head7 = new ListNode(1, new ListNode(2, new ListNode(3,
        new ListNode(4, new ListNode(5)))));
    System.out.println("  Input: " + printList(head7));
    ListNode oddEven = oddEvenList(head7);
    System.out.println("  Output: " + printList(oddEven) + "\n");
  }
}
