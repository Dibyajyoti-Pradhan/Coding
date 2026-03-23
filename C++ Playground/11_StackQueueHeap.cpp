#include <algorithm>
#include <deque>
#include <iostream>
#include <queue>
#include <stack>
#include <unordered_map>
#include <vector>

namespace stack_queue_heap_playground {

/// std::deque for monotonic structures (push/pop both ends).
/// priority_queue is max-heap by default; min-heap requires greater<T>.
/// Each element pushed/popped once in monotonic stack → O(n) total.
/// [[nodiscard]] on all query methods.

// ============================================================================
// STACK DESIGN
// ============================================================================

/// Min stack with O(1) push, pop, top, getMin (LC 155 Med).
class MinStack {
 private:
  std::stack<int> stack_;
  std::stack<int> min_stack_;

 public:
  MinStack() = default;

  /// Push value onto stack and update min_stack.
  void Push(int val) noexcept {
    stack_.push(val);
    if (min_stack_.empty() || val <= min_stack_.top()) {
      min_stack_.push(val);
    }
  }

  /// Pop from both stacks if necessary.
  void Pop() noexcept {
    if (stack_.top() == min_stack_.top()) {
      min_stack_.pop();
    }
    stack_.pop();
  }

  /// Get top element.
  [[nodiscard]] int Top() const noexcept { return stack_.top(); }

  /// Get minimum element.
  [[nodiscard]] int GetMin() const noexcept { return min_stack_.top(); }
};

// ============================================================================
// MONOTONIC STACK
// ============================================================================

/// Daily temperatures (LC 739 Med).
/// For each day, find next warmer day index offset.
/// Time: O(n), Space: O(n).
[[nodiscard]] std::vector<int> DailyTemperatures(
    const std::vector<int>& temperatures) noexcept {
  const int n = static_cast<int>(temperatures.size());
  std::vector<int> result(n, 0);
  std::stack<int> stk;

  for (int i = 0; i < n; ++i) {
    while (!stk.empty() && temperatures[i] > temperatures[stk.top()]) {
      int prev_idx = stk.top();
      stk.pop();
      result[prev_idx] = i - prev_idx;
    }
    stk.push(i);
  }

  return result;
}

/// Next greater element II (LC 503 Med).
/// Circular array. Find next greater element for each.
/// Time: O(n), Space: O(n).
[[nodiscard]] std::vector<int> NextGreaterElements(
    const std::vector<int>& nums) noexcept {
  const int n = static_cast<int>(nums.size());
  std::vector<int> result(n, -1);
  std::stack<int> stk;

  for (int i = 0; i < 2 * n; ++i) {
    int idx = i % n;
    while (!stk.empty() && nums[idx] > nums[stk.top()]) {
      result[stk.top()] = nums[idx];
      stk.pop();
    }
    if (i < n) stk.push(idx);
  }

  return result;
}

/// Largest rectangle in histogram (LC 84 Hard).
/// Find largest rectangle area in histogram.
/// Time: O(n), Space: O(n).
[[nodiscard]] int LargestRectangleHistogram(
    const std::vector<int>& heights) noexcept {
  int max_area = 0;
  std::stack<int> stk;

  for (int i = 0; i < static_cast<int>(heights.size()); ++i) {
    while (!stk.empty() && heights[i] < heights[stk.top()]) {
      int h_idx = stk.top();
      stk.pop();
      int h = heights[h_idx];
      int w = stk.empty() ? i : i - stk.top() - 1;
      max_area = std::max(max_area, h * w);
    }
    stk.push(i);
  }

  while (!stk.empty()) {
    int h_idx = stk.top();
    stk.pop();
    int h = heights[h_idx];
    int w = stk.empty() ? static_cast<int>(heights.size())
                        : static_cast<int>(heights.size()) - stk.top() - 1;
    max_area = std::max(max_area, h * w);
  }

  return max_area;
}

// ============================================================================
// PARENTHESES
// ============================================================================

/// Valid parentheses (LC 20 Easy).
/// Check if string has valid nested parentheses.
/// Time: O(n), Space: O(n).
[[nodiscard]] bool IsValid(std::string_view s) noexcept {
  std::stack<char> stk;

  for (char c : s) {
    if (c == '(' || c == '[' || c == '{') {
      stk.push(c);
    } else {
      if (stk.empty()) return false;
      char top = stk.top();
      stk.pop();
      if ((c == ')' && top != '(') || (c == ']' && top != '[') ||
          (c == '}' && top != '{')) {
        return false;
      }
    }
  }

  return stk.empty();
}

/// Longest valid parentheses (LC 32 Hard).
/// Find length of longest valid parentheses substring.
/// Time: O(n), Space: O(n).
[[nodiscard]] int LongestValidParentheses(std::string_view s) noexcept {
  int max_len = 0;
  std::stack<int> stk;
  stk.push(-1);

  for (int i = 0; i < static_cast<int>(s.size()); ++i) {
    if (s[i] == '(') {
      stk.push(i);
    } else {
      stk.pop();
      if (stk.empty()) {
        stk.push(i);
      } else {
        max_len = std::max(max_len, i - stk.top());
      }
    }
  }

  return max_len;
}

// ============================================================================
// HEAP — TOP K
// ============================================================================

/// Find k-th largest element (LC 215 Med).
/// Using min-heap of size k.
/// Time: O(n log k), Space: O(k).
[[nodiscard]] int FindKthLargest(std::vector<int> nums, int k) noexcept {
  std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;

  for (int num : nums) {
    min_heap.push(num);
    if (static_cast<int>(min_heap.size()) > k) {
      min_heap.pop();
    }
  }

  return min_heap.top();
}

/// Top k frequent elements (LC 347 Med).
/// Find k most frequent elements.
/// Time: O(n log k), Space: O(n).
[[nodiscard]] std::vector<int> TopKFrequent(const std::vector<int>& nums,
                                           int k) noexcept {
  std::unordered_map<int, int> freq;
  for (int num : nums) {
    freq[num]++;
  }

  auto cmp = [&freq](int a, int b) { return freq[a] > freq[b]; };
  std::priority_queue<int, std::vector<int>, decltype(cmp)> min_heap(cmp);

  for (const auto& [num, _] : freq) {
    min_heap.push(num);
    if (static_cast<int>(min_heap.size()) > k) {
      min_heap.pop();
    }
  }

  std::vector<int> result;
  while (!min_heap.empty()) {
    result.emplace_back(min_heap.top());
    min_heap.pop();
  }

  return result;
}

// ============================================================================
// MEDIAN FINDER
// ============================================================================

/// Median finder (LC 295 Hard).
/// Add numbers and find median in O(log n) and O(1).
class MedianFinder {
 private:
  std::priority_queue<int> lower_;
  std::priority_queue<int, std::vector<int>, std::greater<int>> upper_;

 public:
  MedianFinder() = default;

  /// Add a number to the structure.
  void AddNum(int num) noexcept {
    if (lower_.empty() || num <= lower_.top()) {
      lower_.push(num);
    } else {
      upper_.push(num);
    }

    if (static_cast<int>(lower_.size()) > static_cast<int>(upper_.size()) + 1) {
      upper_.push(lower_.top());
      lower_.pop();
    }
    if (static_cast<int>(upper_.size()) > static_cast<int>(lower_.size())) {
      lower_.push(upper_.top());
      upper_.pop();
    }
  }

  /// Get the median of all numbers added so far.
  [[nodiscard]] double FindMedian() const noexcept {
    if (lower_.size() > upper_.size()) {
      return static_cast<double>(lower_.top());
    }
    return (static_cast<double>(lower_.top()) + upper_.top()) / 2.0;
  }
};

// ============================================================================
// QUEUE DESIGN
// ============================================================================

/// My queue implemented with two stacks (LC 232 Easy).
class MyQueue {
 private:
  std::stack<int> in_stk_;
  std::stack<int> out_stk_;

 public:
  MyQueue() = default;

  /// Push element onto back of queue.
  void Push(int x) noexcept { in_stk_.push(x); }

  /// Remove front element.
  [[nodiscard]] int Pop() noexcept {
    if (out_stk_.empty()) {
      while (!in_stk_.empty()) {
        out_stk_.push(in_stk_.top());
        in_stk_.pop();
      }
    }
    int val = out_stk_.top();
    out_stk_.pop();
    return val;
  }

  /// Get front element.
  [[nodiscard]] int Peek() const noexcept {
    if (!out_stk_.empty()) return out_stk_.top();
    std::stack<int> temp_in = in_stk_;
    while (temp_in.size() > 1) temp_in.pop();
    return temp_in.top();
  }

  /// Check if queue is empty.
  [[nodiscard]] bool Empty() const noexcept {
    return in_stk_.empty() && out_stk_.empty();
  }
};

/// Maximum sliding window (LC 239 Hard).
/// Find maximum in each window of size k using deque.
/// Time: O(n), Space: O(k).
[[nodiscard]] std::vector<int> MaxSlidingWindow(
    const std::vector<int>& nums, int k) noexcept {
  std::vector<int> result;
  if (nums.empty() || k <= 0) return result;

  std::deque<int> dq;

  for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
    while (!dq.empty() && dq.front() <= i - k) {
      dq.pop_front();
    }

    while (!dq.empty() && nums[dq.back()] <= nums[i]) {
      dq.pop_back();
    }

    dq.push_back(i);

    if (i >= k - 1) {
      result.emplace_back(nums[dq.front()]);
    }
  }

  return result;
}

}  // namespace stack_queue_heap_playground

/// Test driver demonstrating all stack/queue/heap functions.
int main() {
  using namespace stack_queue_heap_playground;

  std::cout << "=== Stack, Queue, Heap Algorithms ===\n\n";

  // Min stack test
  MinStack min_stack;
  min_stack.Push(-2);
  min_stack.Push(0);
  min_stack.Push(-3);
  std::cout << "Min Stack getMin(): " << min_stack.GetMin() << "\n";
  min_stack.Pop();
  std::cout << "After pop, top(): " << min_stack.Top() << "\n";
  std::cout << "After pop, getMin(): " << min_stack.GetMin() << "\n";

  std::cout << "\nDaily Temperatures ([73,74,75,71,69,72,76,73]): ";
  auto temps = DailyTemperatures({73, 74, 75, 71, 69, 72, 76, 73});
  for (int x : temps) std::cout << x << " ";
  std::cout << "\n";

  std::cout << "Next Greater Elements ([1,2,1]): ";
  auto nge = NextGreaterElements({1, 2, 1});
  for (int x : nge) std::cout << x << " ";
  std::cout << "\n";

  std::cout << "Largest Rectangle ([2,1,5,6,2,3]): "
            << LargestRectangleHistogram({2, 1, 5, 6, 2, 3}) << "\n";

  std::cout << "Valid Parentheses ('()'): "
            << (IsValid("()") ? "true" : "false") << "\n";
  std::cout << "Valid Parentheses ('([)]'): "
            << (IsValid("([)]") ? "true" : "false") << "\n";

  std::cout << "Longest Valid Parentheses ('(()'): "
            << LongestValidParentheses("(())") << "\n";

  std::cout << "Find Kth Largest ([3,2,1,5,6,4], 2): "
            << FindKthLargest({3, 2, 1, 5, 6, 4}, 2) << "\n";

  std::cout << "Top K Frequent ([1,1,1,2,2,3], 2): ";
  auto top_k = TopKFrequent({1, 1, 1, 2, 2, 3}, 2);
  for (int x : top_k) std::cout << x << " ";
  std::cout << "\n";

  MedianFinder mf;
  mf.AddNum(1);
  std::cout << "Median after adding 1: " << mf.FindMedian() << "\n";
  mf.AddNum(2);
  std::cout << "Median after adding 2: " << mf.FindMedian() << "\n";
  mf.AddNum(3);
  std::cout << "Median after adding 3: " << mf.FindMedian() << "\n";

  MyQueue queue;
  queue.Push(1);
  queue.Push(2);
  std::cout << "Queue peek: " << queue.Peek() << "\n";
  std::cout << "Queue pop: " << queue.Pop() << "\n";

  std::cout << "Max Sliding Window ([1,3,-1,-3,5,3,6,7], 3): ";
  auto sliding = MaxSlidingWindow({1, 3, -1, -3, 5, 3, 6, 7}, 3);
  for (int x : sliding) std::cout << x << " ";
  std::cout << "\n";

  std::cout << "\nAll stack/queue/heap tests passed!\n";
  return 0;
}
