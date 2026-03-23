/// @file 16_AdvancedTopics.cpp
/// @brief Advanced algorithmic patterns: monotonic stack, prefix sum, interval
///        scheduling, LFU cache.
///
/// Monotonic stack/queue: O(n) for problems that naively look O(n²) — each
/// element pushed/popped at most once; 2D prefix sum: build O(mn), query
/// O(1); interval scheduling: sort by end time for min-removal greedy; LFU:
/// three maps + min-frequency pointer → O(1) all ops.
///
/// Time/Space varies per algorithm (see individual functions).

#include <algorithm>
#include <climits>
#include <iostream>
#include <list>
#include <stack>
#include <string>
#include <unordered_map>
#include <vector>

namespace advanced_playground {

// ============================================================================
// SECTION 1 — MONOTONIC STACK
// ============================================================================

/// @brief LC 503: Next greater element in circular array.
/// @param nums Array of integers.
/// @return Array where result[i] = next greater element (circular), or -1.
/// @details Example: nums=[1,2,1] → [2,-1,2].
/// @constraints Time: O(n), Space: O(n).
/// @note Tricky: 2x traversal, push in first pass only.
[[nodiscard]] std::vector<int> NextGreaterElementsCircular(
    const std::vector<int>& nums) noexcept {
  int n = nums.size();
  std::vector<int> result(n, -1);
  std::stack<int> stack;

  for (int i = 0; i < 2 * n; ++i) {
    int idx = i % n;
    while (!stack.empty() && nums[stack.top()] < nums[idx]) {
      result[stack.top()] = nums[idx];
      stack.pop();
    }
    if (i < n) stack.push(idx);
  }
  return result;
}

/// @brief LC 739: Daily temperatures (next warmer day).
/// @param temperatures Daily temperatures.
/// @return Days until warmer temperature (0 if none).
/// @details Example: [73,74,75,71,69,72,76,73] → [1,1,4,2,1,1,0,0].
/// @constraints Time: O(n), Space: O(n).
[[nodiscard]] std::vector<int> DailyTemperatures(
    const std::vector<int>& temperatures) noexcept {
  int n = temperatures.size();
  std::vector<int> result(n, 0);
  std::stack<int> stack;

  for (int i = 0; i < n; ++i) {
    while (!stack.empty() && temperatures[stack.top()] < temperatures[i]) {
      int prev_idx = stack.top();
      stack.pop();
      result[prev_idx] = i - prev_idx;
    }
    stack.push(i);
  }

  return result;
}

/// @brief LC 84: Largest rectangle in histogram.
/// @param heights Heights of bars.
/// @return Maximum rectangle area.
/// @details Example: [2,1,5,6,2,3] → 10 (height 5, width 2).
/// @constraints Time: O(n), Space: O(n).
/// @note Tricky: monotonic increasing stack of indices; sentinel 0.
[[nodiscard]] int LargestRectangleHistogram(
    const std::vector<int>& heights) noexcept {
  std::vector<int> h = heights;
  h.push_back(0);  // Sentinel
  std::stack<int> stack;
  int max_area = 0;

  for (int i = 0; i < static_cast<int>(h.size()); ++i) {
    while (!stack.empty() && h[stack.top()] > h[i]) {
      int height = h[stack.top()];
      stack.pop();
      int width = stack.empty() ? i : i - stack.top() - 1;
      max_area = std::max(max_area, height * width);
    }
    stack.push(i);
  }

  return max_area;
}

/// @brief LC 42: Trap rainwater.
/// @param height Heights of bars.
/// @return Volume of water trapped.
/// @details Example: [0,1,0,2,1,0,1,3,2,1,2,1] → 6.
/// @constraints Time: O(n), Space: O(1) (two-pointer) or O(n) (prefix).
/// @note Tricky: water at position i = min(left_max, right_max) - height[i].
[[nodiscard]] int Trap(const std::vector<int>& height) noexcept {
  if (height.size() < 3) return 0;
  int n = height.size();
  int left_max = 0, right_max = 0;
  int water = 0;
  int left = 0, right = n - 1;

  while (left < right) {
    if (height[left] < height[right]) {
      left_max = std::max(left_max, height[left]);
      water += left_max - height[left];
      ++left;
    } else {
      right_max = std::max(right_max, height[right]);
      water += right_max - height[right];
      --right;
    }
  }

  return water;
}

/// @brief LC 901: Stock Spanner (price span query).
/// @details Query: price and # consecutive days with price ≤ current.
class StockSpanner {
 public:
  StockSpanner() noexcept = default;

  /// @brief Process price and return span.
  /// @param price Current stock price.
  /// @return Number of consecutive days (including today) with price ≤
  ///         current.
  /// @details Time: O(1) amortised per call.
  /// @note Tricky: stack of {price, span} pairs; span accumulates.
  [[nodiscard]] int Next(int price) noexcept {
    int span = 1;
    while (!stack_.empty() && stack_.back().first <= price) {
      span += stack_.back().second;
      stack_.pop_back();
    }
    stack_.emplace_back(price, span);
    return span;
  }

 private:
  std::vector<std::pair<int, int>> stack_;  ///< {price, span}
};

// ============================================================================
// SECTION 2 — ADVANCED PREFIX SUM
// ============================================================================

/// @brief LC 238: Product of array except self (no division).
/// @param nums Array of integers (no zeros).
/// @return result[i] = product of all elements except nums[i].
/// @details Example: [1,2,3,4] → [24,12,8,6].
/// @constraints Time: O(n), Space: O(1) (output array not counted).
/// @note Tricky: left pass [1,1,2,6]; right pass to accumulate.
[[nodiscard]] std::vector<int> ProductExceptSelf(
    const std::vector<int>& nums) noexcept {
  int n = nums.size();
  std::vector<int> result(n, 1);

  // Left pass: result[i] = product of all left
  for (int i = 1; i < n; ++i) {
    result[i] = result[i - 1] * nums[i - 1];
  }

  // Right pass: multiply by product of all right
  int right_prod = 1;
  for (int i = n - 1; i >= 0; --i) {
    result[i] *= right_prod;
    right_prod *= nums[i];
  }

  return result;
}

/// @brief LC 974: Subarrays divisible by K.
/// @param nums Array of integers.
/// @param k Divisor.
/// @return Count of subarrays with sum divisible by k.
/// @details Example: [4,5,0,-2,-3,1], k=5 → 7.
/// @constraints Time: O(n), Space: O(k).
/// @note Tricky: (a-b) divisible by k iff (a%k == b%k); handle negative mod.
[[nodiscard]] int SubarraysDivByK(const std::vector<int>& nums,
                                   int k) noexcept {
  std::unordered_map<int, int> mod_count;
  mod_count[0] = 1;
  int prefix_sum = 0, count = 0;

  for (int num : nums) {
    prefix_sum += num;
    int mod = ((prefix_sum % k) + k) % k;
    if (mod_count.count(mod)) {
      count += mod_count[mod];
    }
    ++mod_count[mod];
  }

  return count;
}

/// @brief LC 523: Continuous subarray sum.
/// @param nums Array of integers.
/// @param k Divisor.
/// @return true if subarray of length ≥2 with sum divisible by k exists.
/// @details Example: [23,2,4,6,13], k=6 → true (2+4=6).
/// @constraints Time: O(n), Space: O(k).
/// @note Tricky: track first index of each remainder; require length ≥ 2.
[[nodiscard]] bool ContinuousSubarraySum(const std::vector<int>& nums,
                                         int k) noexcept {
  std::unordered_map<int, int> mod_index;
  mod_index[0] = -1;
  int prefix_sum = 0;

  for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
    prefix_sum += nums[i];
    int mod = ((prefix_sum % k) + k) % k;

    if (mod_index.count(mod)) {
      if (i - mod_index[mod] >= 2) {
        return true;
      }
    } else {
      mod_index[mod] = i;
    }
  }

  return false;
}

/// @brief LC 304: 2D range sum query (immutable).
/// @details Precompute 2D prefix sum; query O(1).
class NumMatrix {
 public:
  /// @brief Initialize with matrix.
  /// @param matrix Grid of integers.
  /// @details Time: O(mn), Space: O(mn).
  explicit NumMatrix(const std::vector<std::vector<int>>& matrix) noexcept {
    if (matrix.empty()) return;
    int m = matrix.size(), n = matrix[0].size();
    prefix_sum_.assign(m + 1, std::vector<int>(n + 1, 0));

    for (int i = 1; i <= m; ++i) {
      for (int j = 1; j <= n; ++j) {
        prefix_sum_[i][j] = matrix[i - 1][j - 1] +
                            prefix_sum_[i - 1][j] +
                            prefix_sum_[i][j - 1] -
                            prefix_sum_[i - 1][j - 1];
      }
    }
  }

  /// @brief Query sum of rectangle [row1, col1] to [row2, col2].
  /// @param row1 Top row.
  /// @param col1 Left column.
  /// @param row2 Bottom row.
  /// @param col2 Right column.
  /// @return Sum of rectangle.
  /// @details Time: O(1).
  [[nodiscard]] int SumRegion(int row1, int col1, int row2,
                               int col2) const noexcept {
    return prefix_sum_[row2 + 1][col2 + 1] -
           prefix_sum_[row1][col2 + 1] -
           prefix_sum_[row2 + 1][col1] +
           prefix_sum_[row1][col1];
  }

 private:
  std::vector<std::vector<int>> prefix_sum_;
};

// ============================================================================
// SECTION 3 — INTERVAL SCHEDULING
// ============================================================================

/// @brief LC 57: Insert interval into sorted list.
/// @param intervals Sorted list of non-overlapping intervals.
/// @param new_interval Interval to insert.
/// @return Updated list with new_interval merged.
/// @details Example: intervals=[[1,2],[3,5],[6,9]], new=[4,8]
///          → [[1,2],[3,8],[6,9]].
/// @constraints Time: O(n), Space: O(n).
[[nodiscard]] std::vector<std::vector<int>> InsertInterval(
    std::vector<std::vector<int>> intervals,
    std::vector<int> new_interval) noexcept {
  std::vector<std::vector<int>> result;
  int i = 0;
  int n = intervals.size();

  // Add all intervals ending before new_interval starts
  while (i < n && intervals[i][1] < new_interval[0]) {
    result.emplace_back(intervals[i]);
    ++i;
  }

  // Merge overlapping intervals
  int start = new_interval[0], end = new_interval[1];
  while (i < n && intervals[i][0] <= end) {
    start = std::min(start, intervals[i][0]);
    end = std::max(end, intervals[i][1]);
    ++i;
  }
  result.emplace_back(std::vector<int>{start, end});

  // Add remaining intervals
  while (i < n) {
    result.emplace_back(intervals[i]);
    ++i;
  }

  return result;
}

/// @brief LC 253: Minimum meeting rooms.
/// @param intervals List of [start, end] times.
/// @return Minimum number of rooms needed.
/// @details Example: [[0,30],[5,10],[15,20]] → 2.
/// @constraints Time: O(n log n), Space: O(n).
/// @note Tricky: sort starts and ends separately; two-pointer.
[[nodiscard]] int MinMeetingRooms(
    std::vector<std::vector<int>> intervals) noexcept {
  std::vector<int> starts, ends;
  for (const auto& iv : intervals) {
    starts.emplace_back(iv[0]);
    ends.emplace_back(iv[1]);
  }

  std::sort(starts.begin(), starts.end());
  std::sort(ends.begin(), ends.end());

  int rooms = 0, end_idx = 0;
  for (int start : starts) {
    if (start < ends[end_idx]) {
      ++rooms;
    } else {
      ++end_idx;
    }
  }

  return rooms;
}

/// @brief LC 435: Non-overlapping intervals (greedy removal).
/// @param intervals List of [start, end] intervals.
/// @return Minimum intervals to remove for non-overlapping.
/// @details Example: [[1,2],[2,3],[3,4],[1,3]] → 1.
/// @constraints Time: O(n log n), Space: O(1).
/// @note Tricky: sort by end time; greedy keeps earliest-ending.
[[nodiscard]] int NonOverlappingIntervals(
    std::vector<std::vector<int>> intervals) noexcept {
  std::sort(intervals.begin(), intervals.end(),
            [](const std::vector<int>& a, const std::vector<int>& b) {
              return a[1] < b[1];
            });

  int count = 0;
  int prev_end = INT_MIN;
  for (const auto& iv : intervals) {
    if (iv[0] >= prev_end) {
      prev_end = iv[1];
    } else {
      ++count;
    }
  }

  return count;
}

/// @brief LC 452: Minimum arrows to burst balloons.
/// @param points List of [x_start, x_end] balloon ranges.
/// @return Minimum arrows needed.
/// @details Example: [[10,16],[2,8],[1,6],[7,12],[4,9]] → 2.
/// @constraints Time: O(n log n), Space: O(1).
/// @note Tricky: sort by end; cast to long long to avoid overflow.
[[nodiscard]] int MinArrowsBurstBalloons(
    std::vector<std::vector<int>> points) noexcept {
  if (points.empty()) return 0;
  std::sort(points.begin(), points.end(),
            [](const std::vector<int>& a, const std::vector<int>& b) {
              return static_cast<long long>(a[1]) <
                     static_cast<long long>(b[1]);
            });

  int arrows = 1;
  long long prev_end = static_cast<long long>(points[0][1]);
  for (int i = 1; i < static_cast<int>(points.size()); ++i) {
    if (static_cast<long long>(points[i][0]) > prev_end) {
      ++arrows;
      prev_end = static_cast<long long>(points[i][1]);
    }
  }

  return arrows;
}

// ============================================================================
// SECTION 4 — LFU CACHE
// ============================================================================

/// @brief LC 460: LFU Cache (Least Frequently Used).
/// @details Get: O(1), Put: O(1); evicts LFU key with earliest insertion.
class LFUCache {
 public:
  /// @brief Initialize cache with capacity.
  /// @param capacity Maximum items to store.
  explicit LFUCache(int capacity) noexcept
      : capacity_(capacity), min_freq_(0) {}

  /// @brief Get value for key.
  /// @param key Cache key.
  /// @return Value if exists, -1 otherwise.
  /// @details Time: O(1).
  [[nodiscard]] int Get(int key) noexcept {
    if (key_to_val_.find(key) == key_to_val_.end()) {
      return -1;
    }
    UpdateFreq(key);
    return key_to_val_[key];
  }

  /// @brief Put key-value pair into cache.
  /// @param key Cache key.
  /// @param value Value to store.
  /// @return void
  /// @details Time: O(1). Evicts LFU key if capacity exceeded.
  void Put(int key, int value) noexcept {
    if (capacity_ == 0) return;

    if (key_to_val_.find(key) != key_to_val_.end()) {
      key_to_val_[key] = value;
      UpdateFreq(key);
      return;
    }

    if (static_cast<int>(key_to_val_.size()) == capacity_) {
      // Evict LFU key (earliest inserted at min_freq)
      int lfu_key = freq_to_keys_[min_freq_].front();
      freq_to_keys_[min_freq_].pop_front();
      key_to_val_.erase(lfu_key);
      key_to_freq_.erase(lfu_key);
      key_to_iter_.erase(lfu_key);
    }

    key_to_val_[key] = value;
    key_to_freq_[key] = 1;
    freq_to_keys_[1].emplace_back(key);
    key_to_iter_[key] = std::prev(freq_to_keys_[1].end());
    min_freq_ = 1;
  }

 private:
  int capacity_;
  int min_freq_;
  std::unordered_map<int, int> key_to_val_;
  std::unordered_map<int, int> key_to_freq_;
  std::unordered_map<int, std::list<int>> freq_to_keys_;
  std::unordered_map<int, std::list<int>::iterator> key_to_iter_;

  /// @brief Update frequency of key.
  /// @param key Key whose frequency to update.
  /// @return void
  /// @details Moves key from freq→freq+1 list; updates min_freq if needed.
  void UpdateFreq(int key) noexcept {
    int freq = key_to_freq_[key];
    ++key_to_freq_[key];

    freq_to_keys_[freq].erase(key_to_iter_[key]);
    if (freq_to_keys_[freq].empty()) {
      freq_to_keys_.erase(freq);
      if (freq == min_freq_) {
        ++min_freq_;
      }
    }

    freq_to_keys_[freq + 1].emplace_back(key);
    key_to_iter_[key] = std::prev(freq_to_keys_[freq + 1].end());
  }
};

}  // namespace advanced_playground

int main() {
  using namespace advanced_playground;
  std::cout << "=== Advanced Topics Playground ===\n\n";

  std::cout << "--- Section 1: Monotonic Stack ---\n\n";

  std::cout << "Next Greater Elements (LC 503)\n";
  {
    auto result = NextGreaterElementsCircular({1, 2, 1});
    std::cout << "Input: [1, 2, 1]\nOutput: [";
    for (int i = 0; i < static_cast<int>(result.size()); ++i) {
      if (i > 0) std::cout << ", ";
      std::cout << result[i];
    }
    std::cout << "]\n";
  }

  std::cout << "\nDaily Temperatures (LC 739)\n";
  {
    auto result = DailyTemperatures({73, 74, 75, 71, 69, 72, 76, 73});
    std::cout << "Input: [73, 74, 75, 71, 69, 72, 76, 73]\nOutput: [";
    for (int i = 0; i < static_cast<int>(result.size()); ++i) {
      if (i > 0) std::cout << ", ";
      std::cout << result[i];
    }
    std::cout << "]\n";
  }

  std::cout << "\nLargest Rectangle Histogram (LC 84)\n";
  {
    int result = LargestRectangleHistogram({2, 1, 5, 6, 2, 3});
    std::cout << "Input: [2, 1, 5, 6, 2, 3]\nMax area: " << result << "\n";
  }

  std::cout << "\nTrap Rainwater (LC 42)\n";
  {
    int result = Trap({0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1});
    std::cout << "Input: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]\nWater: "
              << result << "\n";
  }

  std::cout << "\nStock Spanner (LC 901)\n";
  {
    StockSpanner spanner;
    std::cout << "Prices: [100, 80, 60, 70, 60, 75, 85]\n";
    std::cout << "Spans: ";
    for (int price : {100, 80, 60, 70, 60, 75, 85}) {
      std::cout << spanner.Next(price) << " ";
    }
    std::cout << "\n";
  }

  std::cout << "\n--- Section 2: Advanced Prefix Sum ---\n\n";

  std::cout << "Product Except Self (LC 238)\n";
  {
    auto result = ProductExceptSelf({1, 2, 3, 4});
    std::cout << "Input: [1, 2, 3, 4]\nOutput: [";
    for (int i = 0; i < static_cast<int>(result.size()); ++i) {
      if (i > 0) std::cout << ", ";
      std::cout << result[i];
    }
    std::cout << "]\n";
  }

  std::cout << "\nSubarrays Divisible by K (LC 974)\n";
  {
    int result = SubarraysDivByK({4, 5, 0, -2, -3, 1}, 5);
    std::cout << "Input: [4, 5, 0, -2, -3, 1], k=5\nCount: " << result << "\n";
  }

  std::cout << "\nContinuous Subarray Sum (LC 523)\n";
  {
    bool result = ContinuousSubarraySum({23, 2, 4, 6, 13}, 6);
    std::cout << "Input: [23, 2, 4, 6, 13], k=6\nExists: "
              << (result ? "true" : "false") << "\n";
  }

  std::cout << "\n2D Range Sum (LC 304)\n";
  {
    std::vector<std::vector<int>> matrix = {
        {3, 0, 1, 4, 2}, {5, 6, 3, 2, 1}, {1, 2, 0, 1, 5}, {4, 1, 0, 1, 7}, {1, 0, 3, 0, 5}
    };
    NumMatrix nm(matrix);
    std::cout << "Matrix: 5x5\n";
    std::cout << "SumRegion(2, 1, 4, 3): " << nm.SumRegion(2, 1, 4, 3) << "\n";
  }

  std::cout << "\n--- Section 3: Interval Scheduling ---\n\n";

  std::cout << "Insert Interval (LC 57)\n";
  {
    auto result = InsertInterval({{1, 2}, {3, 5}, {6, 9}}, {4, 8});
    std::cout << "Intervals: [[1,2], [3,5], [6,9]], Insert [4,8]\nResult: [";
    for (int i = 0; i < static_cast<int>(result.size()); ++i) {
      if (i > 0) std::cout << ", ";
      std::cout << "[" << result[i][0] << "," << result[i][1] << "]";
    }
    std::cout << "]\n";
  }

  std::cout << "\nMin Meeting Rooms (LC 253)\n";
  {
    int result = MinMeetingRooms({{0, 30}, {5, 10}, {15, 20}});
    std::cout << "Meetings: [[0,30], [5,10], [15,20]]\nRooms: " << result
              << "\n";
  }

  std::cout << "\nNon-overlapping Intervals (LC 435)\n";
  {
    int result = NonOverlappingIntervals({{1, 2}, {2, 3}, {3, 4}, {1, 3}});
    std::cout << "Intervals: [[1,2], [2,3], [3,4], [1,3]]\nRemove: "
              << result << "\n";
  }

  std::cout << "\nMin Arrows Burst Balloons (LC 452)\n";
  {
    int result = MinArrowsBurstBalloons({{10, 16}, {2, 8}, {1, 6}, {7, 12}});
    std::cout << "Balloons: [[10,16], [2,8], [1,6], [7,12]]\nArrows: "
              << result << "\n";
  }

  std::cout << "\n--- Section 4: LFU Cache ---\n\n";

  std::cout << "LFU Cache (LC 460)\n";
  {
    LFUCache cache(2);
    cache.Put(1, 1);
    cache.Put(2, 2);
    std::cout << "Capacity: 2\n";
    std::cout << "Put(1, 1), Put(2, 2)\n";
    std::cout << "Get(1): " << cache.Get(1) << "\n";
    cache.Put(3, 3);
    std::cout << "Put(3, 3)\n";
    std::cout << "Get(2): " << cache.Get(2) << " (evicted, LFU=2)\n";
    cache.Put(4, 4);
    std::cout << "Put(4, 4)\n";
    std::cout << "Get(1): " << cache.Get(1) << " (evicted, LFU=1)\n";
    std::cout << "Get(3): " << cache.Get(3) << "\n";
    std::cout << "Get(4): " << cache.Get(4) << "\n";
  }

  return 0;
}
