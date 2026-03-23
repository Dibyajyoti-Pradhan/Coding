/// @file 04_LinkedList.cpp
/// @brief Linked Lists Playground — reversal, cycle detection, merge,
///        reorder, copy with random, palindrome.
///
/// LINKED LISTS GUIDE:
/// - Define ListNode struct at top with constructor (val, next, NOT val_, next_)
/// - Always check for nullptr before dereferencing next or random pointers
/// - Use dummy head node to simplify edge cases (ListNode dummy(0); ...)
/// - Fast-and-slow pointer: fast jumps 2, slow jumps 1, meet at cycle/middle
/// - Reversal: track prev, curr, next; prev follows curr; curr follows next
/// - Merge with heap: use priority_queue<ListNode*> with custom comparator
/// - Copy with random: interleave original and copy, then separate
/// - LeetCode struct names: ListNode uses val, next, RandomNode uses val,
///   next, random (NO trailing underscores)

#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>

namespace linkedlist_playground {

/// @brief Singly-linked list node (LeetCode API compatible).
struct ListNode {
  int val;
  ListNode* next;
  explicit ListNode(int x) : val(x), next(nullptr) {}
};

/// @brief Node with random pointer (LC 138, LeetCode API compatible).
struct RandomNode {
  int val;
  RandomNode* next;
  RandomNode* random;
  explicit RandomNode(int x) : val(x), next(nullptr), random(nullptr) {}
};

/// @brief Detect cycle in linked list using fast-slow pointers (LC 141 Easy).
/// @param head Head of linked list.
/// @return true if cycle exists, false otherwise.
///
/// Example: 1→2→3→4→2 (cycle) → true; 1→2→3 (no cycle) → false
/// Constraints: 0 ≤ n ≤ 10⁴; −10⁵ ≤ val ≤ 10⁵.
/// Time: O(n), Space: O(1)
/// Tricky: Fast pointer jumps 2 steps, slow jumps 1. If they meet, cycle.
///         If fast reaches nullptr, no cycle.
[[nodiscard]] bool HasCycle(ListNode* head) noexcept {
  ListNode* slow = head;
  ListNode* fast = head;
  while (fast && fast->next) {
    slow = slow->next;
    fast = fast->next->next;
    if (slow == fast) return true;
  }
  return false;
}

/// @brief Detect and return node where cycle begins (LC 142 Medium).
/// @param head Head of linked list.
/// @return Pointer to cycle node, or nullptr if no cycle.
///
/// Example: 1→2→3→4→2 (cycle at 2) → pointer to node with val=2
/// Constraints: 0 ≤ n ≤ 10⁴.
/// Time: O(n), Space: O(1)
/// Tricky: Meet point = fast and slow collide. Then move slow to head,
///         fast stays; move both 1 step at a time; meet at cycle start.
[[nodiscard]] ListNode* DetectCycle(ListNode* head) noexcept {
  ListNode* slow = head;
  ListNode* fast = head;

  while (fast && fast->next) {
    slow = slow->next;
    fast = fast->next->next;
    if (slow == fast) break;
  }

  if (!fast || !fast->next) return nullptr;

  slow = head;
  while (slow != fast) {
    slow = slow->next;
    fast = fast->next;
  }
  return slow;
}

/// @brief Find middle of linked list using fast-slow pointers.
/// @param head Head of linked list.
/// @return Middle node (for even length, return second middle).
///
/// Example: 1→2→3→4→5 → 3; 1→2→3→4 → 3
/// Constraints: 1 ≤ n ≤ 500.
/// Time: O(n), Space: O(1)
/// Tricky: Fast reaches end, slow at middle.
[[nodiscard]] ListNode* FindMiddle(ListNode* head) noexcept {
  ListNode* slow = head;
  ListNode* fast = head;

  while (fast && fast->next) {
    slow = slow->next;
    fast = fast->next->next;
  }
  return slow;
}

/// @brief Remove Nth node from end of list (LC 19 Medium).
/// @param head Head of linked list.
/// @param n Position from end (1-indexed).
/// @return Head of modified list.
///
/// Example: 1→2→3→4→5, n=2 → 1→2→3→5
/// Constraints: 1 ≤ n ≤ list length; may remove head.
/// Time: O(n), Space: O(1)
/// Tricky: Use dummy head; two pointers n steps apart; move both until
///         first reaches end; remove by skipping.
[[nodiscard]] ListNode* RemoveNthFromEnd(ListNode* head, int n) noexcept {
  ListNode dummy(0);
  dummy.next = head;
  ListNode* first = &dummy;
  ListNode* second = &dummy;

  for (int i = 0; i <= n; ++i) {
    if (!first) return head;
    first = first->next;
  }

  while (first) {
    first = first->next;
    second = second->next;
  }

  second->next = second->next->next;
  return dummy.next;
}

/// @brief Reverse linked list (LC 206 Easy).
/// @param head Head of linked list.
/// @return Head of reversed list.
///
/// Example: 1→2→3→4→5 → 5→4→3→2→1
/// Constraints: 0 ≤ n ≤ 5000.
/// Time: O(n), Space: O(1)
/// Tricky: Track prev, curr, next. Reverse link from curr→prev. Move all
///         forward.
[[nodiscard]] ListNode* ReverseList(ListNode* head) noexcept {
  ListNode* prev = nullptr;
  ListNode* curr = head;

  while (curr) {
    ListNode* next = curr->next;
    curr->next = prev;
    prev = curr;
    curr = next;
  }
  return prev;
}

/// @brief Reverse list between positions left and right (LC 92 Medium).
/// @param head Head of linked list.
/// @param left Start position (1-indexed).
/// @param right End position (1-indexed).
/// @return Head of modified list.
///
/// Example: 1→2→3→4→5, left=2, right=4 → 1→4→3→2→5
/// Constraints: 1 ≤ left ≤ right ≤ n.
/// Time: O(n), Space: O(1)
/// Tricky: Find node before left; reverse [left..right] using standard
///         reversal; connect back.
[[nodiscard]] ListNode* ReverseBetween(ListNode* head, int left,
                                        int right) noexcept {
  ListNode dummy(0);
  dummy.next = head;
  ListNode* prev_left = &dummy;

  for (int i = 0; i < left - 1; ++i) {
    prev_left = prev_left->next;
  }

  ListNode* curr = prev_left->next;
  for (int i = 0; i < right - left; ++i) {
    ListNode* next = curr->next;
    curr->next = next->next;
    next->next = prev_left->next;
    prev_left->next = next;
  }

  return dummy.next;
}

/// @brief Reverse k group: reverse every k elements (LC 25 Hard).
/// @param head Head of linked list.
/// @param k Group size.
/// @return Head of modified list.
///
/// Example: 1→2→3→4→5, k=2 → 2→1→4→3→5
/// Constraints: 1 ≤ n ≤ 5000; 1 ≤ k ≤ n.
/// Time: O(n), Space: O(1)
/// Tricky: Check if k nodes available; reverse them; reconnect groups.
[[nodiscard]] ListNode* ReverseKGroup(ListNode* head, int k) noexcept {
  ListNode dummy(0);
  dummy.next = head;
  ListNode* prev_group = &dummy;

  while (true) {
    ListNode* kth = prev_group;
    for (int i = 0; i < k; ++i) {
      if (!kth->next) return dummy.next;
      kth = kth->next;
    }

    ListNode* next_group = kth->next;
    ListNode* prev = next_group;
    ListNode* curr = prev_group->next;

    for (int i = 0; i < k; ++i) {
      ListNode* next = curr->next;
      curr->next = prev;
      prev = curr;
      curr = next;
    }

    ListNode* temp = prev_group->next;
    prev_group->next = kth;
    prev_group = temp;
  }
}

/// @brief Merge two sorted linked lists (LC 21 Easy).
/// @param list1 Head of first sorted list.
/// @param list2 Head of second sorted list.
/// @return Head of merged sorted list.
///
/// Example: 1→2→4, 1→3→4 → 1→1→2→3→4→4
/// Constraints: 0 ≤ n, m ≤ 50.
/// Time: O(n + m), Space: O(1)
/// Tricky: Use dummy head; compare nodes, append smaller; advance that
///         pointer.
[[nodiscard]] ListNode* MergeTwoLists(ListNode* list1,
                                       ListNode* list2) noexcept {
  ListNode dummy(0);
  ListNode* curr = &dummy;

  while (list1 && list2) {
    if (list1->val <= list2->val) {
      curr->next = list1;
      list1 = list1->next;
    } else {
      curr->next = list2;
      list2 = list2->next;
    }
    curr = curr->next;
  }

  curr->next = list1 ? list1 : list2;
  return dummy.next;
}

/// @brief Merge k sorted linked lists (LC 23 Hard).
/// @param lists Vector of k sorted list heads.
/// @return Head of merged sorted list.
///
/// Example: [[1,4,5],[1,3,4],[2,6]] → [1,1,2,1,3,4,4,5,6]
/// Constraints: 0 ≤ k ≤ 10⁴; 0 ≤ n_i ≤ 500.
/// Time: O(n log k) where n = total nodes, k = number of lists
/// Space: O(k) for heap
/// Tricky: Use min-heap to always get smallest node; pop, add its next.
[[nodiscard]] ListNode* MergeKLists(std::vector<ListNode*>& lists) {
  auto cmp = [](ListNode* a, ListNode* b) {
    return a->val > b->val;
  };
  std::priority_queue<ListNode*, std::vector<ListNode*>, decltype(cmp)>
      min_heap(cmp);

  for (ListNode* head : lists) {
    if (head) min_heap.push(head);
  }

  ListNode dummy(0);
  ListNode* curr = &dummy;

  while (!min_heap.empty()) {
    ListNode* node = min_heap.top();
    min_heap.pop();
    curr->next = node;
    curr = curr->next;
    if (node->next) {
      min_heap.push(node->next);
    }
  }

  return dummy.next;
}

/// @brief Reorder list: 1→2→3→4→5 becomes 1→5→2→4→3 (LC 143 Medium).
/// @param head Head of linked list (modified in-place).
///
/// Example: 1→2→3→4→5 → 1→5→2→4→3
/// Constraints: 1 ≤ n ≤ 5×10⁴; n ≥ 2.
/// Time: O(n), Space: O(1)
/// Tricky: Find middle; reverse second half; merge two halves.
void ReorderList(ListNode* head) noexcept {
  ListNode* slow = head;
  ListNode* fast = head;
  while (fast && fast->next) {
    slow = slow->next;
    fast = fast->next->next;
  }

  ListNode* prev = nullptr;
  ListNode* curr = slow;
  while (curr) {
    ListNode* next = curr->next;
    curr->next = prev;
    prev = curr;
    curr = next;
  }

  ListNode* first = head;
  ListNode* second = prev;
  while (second->next) {
    ListNode* next_first = first->next;
    ListNode* next_second = second->next;
    first->next = second;
    second->next = next_first;
    first = next_first;
    second = next_second;
  }
}

/// @brief Odd-even linked list: group odd-indexed, then even-indexed
///        (LC 328 Med).
/// @param head Head of linked list (modified in-place).
/// @return Head of reordered list.
///
/// Example: 1→2→3→4→5 → 1→3→5→2→4
/// Constraints: 0 ≤ n ≤ 10⁴.
/// Time: O(n), Space: O(1)
/// Tricky: Two pointers for odd/even chains; interleave.
[[nodiscard]] ListNode* OddEvenList(ListNode* head) noexcept {
  if (!head || !head->next) return head;

  ListNode* odd = head;
  ListNode* even = head->next;
  ListNode* even_head = even;

  while (even && even->next) {
    odd->next = odd->next->next;
    even->next = even->next->next;
    odd = odd->next;
    even = even->next;
  }

  odd->next = even_head;
  return head;
}

/// @brief Copy list with random pointer: deep copy (LC 138 Medium).
/// @param head Head of RandomNode list.
/// @return Head of deep copied list.
///
/// Example: 1(random→3)→2(random→1)→3(random→3) →
///          deep copy with same structure
/// Constraints: 0 ≤ n ≤ 100; next and random can point anywhere.
/// Time: O(n), Space: O(n) for copy
/// Tricky: Interleave: insert copy right after original in original list;
///         set random pointers on copy; then separate lists.
[[nodiscard]] RandomNode* CopyRandomList(RandomNode* head) {
  if (!head) return nullptr;

  for (RandomNode* curr = head; curr; curr = curr->next->next) {
    RandomNode* copy = new RandomNode(curr->val);
    copy->next = curr->next;
    curr->next = copy;
  }

  for (RandomNode* curr = head; curr; curr = curr->next->next) {
    RandomNode* copy = curr->next;
    if (curr->random) {
      copy->random = curr->random->next;
    }
  }

  RandomNode dummy(0);
  RandomNode* copy_prev = &dummy;
  for (RandomNode* curr = head; curr; curr = curr->next) {
    RandomNode* copy = curr->next;
    copy_prev->next = copy;
    copy_prev = copy;
    curr->next = curr->next->next;
  }

  return dummy.next;
}

/// @brief Check if linked list is palindrome (LC 234 Easy).
/// @param head Head of linked list.
/// @return true if list is palindrome, false otherwise.
///
/// Example: 1→2→2→1 → true; 1→2 → false
/// Constraints: 1 ≤ n ≤ 10⁵; −10⁵ ≤ val ≤ 10⁵.
/// Time: O(n), Space: O(1)
/// Tricky: Find middle; reverse second half in-place; compare.
[[nodiscard]] bool IsPalindrome(ListNode* head) noexcept {
  ListNode* slow = head;
  ListNode* fast = head;
  while (fast && fast->next) {
    slow = slow->next;
    fast = fast->next->next;
  }

  ListNode* prev = nullptr;
  ListNode* curr = slow;
  while (curr) {
    ListNode* next = curr->next;
    curr->next = prev;
    prev = curr;
    curr = next;
  }

  ListNode* left = head;
  ListNode* right = prev;
  while (right) {
    if (left->val != right->val) return false;
    left = left->next;
    right = right->next;
  }
  return true;
}

}  // namespace linkedlist_playground

int main() {
  std::cout << "=== LINKED LIST PLAYGROUND ===\n\n";

  linkedlist_playground::ListNode* head1 =
      new linkedlist_playground::ListNode(1);
  head1->next = new linkedlist_playground::ListNode(2);
  head1->next->next = new linkedlist_playground::ListNode(3);

  bool has_cycle = linkedlist_playground::HasCycle(head1);
  std::cout << "HasCycle(1→2→3): " << (has_cycle ? "true" : "false") << "\n";

  linkedlist_playground::ListNode* middle =
      linkedlist_playground::FindMiddle(head1);
  std::cout << "FindMiddle(1→2→3): val=" << middle->val << "\n";

  linkedlist_playground::ListNode* reversed =
      linkedlist_playground::ReverseList(head1);
  std::cout << "ReverseList(1→2→3): ";
  linkedlist_playground::ListNode* temp = reversed;
  while (temp) {
    std::cout << temp->val << "→";
    temp = temp->next;
  }
  std::cout << "\b\b  \n";

  linkedlist_playground::ListNode* list1 =
      new linkedlist_playground::ListNode(1);
  list1->next = new linkedlist_playground::ListNode(3);
  linkedlist_playground::ListNode* list2 =
      new linkedlist_playground::ListNode(2);
  list2->next = new linkedlist_playground::ListNode(4);
  linkedlist_playground::ListNode* merged =
      linkedlist_playground::MergeTwoLists(list1, list2);
  std::cout << "MergeTwoLists(1→3, 2→4): ";
  temp = merged;
  while (temp) {
    std::cout << temp->val << "→";
    temp = temp->next;
  }
  std::cout << "\b\b  \n";

  linkedlist_playground::ListNode* palin =
      new linkedlist_playground::ListNode(1);
  palin->next = new linkedlist_playground::ListNode(2);
  palin->next->next = new linkedlist_playground::ListNode(2);
  palin->next->next->next = new linkedlist_playground::ListNode(1);
  bool is_palin = linkedlist_playground::IsPalindrome(palin);
  std::cout << "IsPalindrome(1→2→2→1): " << (is_palin ? "true" : "false")
            << "\n";

  return 0;
}
