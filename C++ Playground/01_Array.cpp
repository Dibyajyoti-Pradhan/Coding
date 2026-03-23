/// @file 01_Array.cpp
/// @brief Arrays Playground — vectors, two-pointers, sliding window, prefix sum,
///        Kadane's algorithm, Dutch National Flag, merge intervals, binary search.
///
/// ARRAYS GUIDE:
/// - std::vector<int> is dynamic array with O(1) index access
/// - Iterator invalidation: push_back/erase/resize can invalidate iterators
/// - static_cast<int>(vec.size()) needed for signed/unsigned comparison safety
/// - Avoid (left+right)/2 overflow: use left + (right-left)/2 instead
/// - Reserve capacity if size known upfront: vec.reserve(n)
/// - Two-pointers: opposite direction for sorted; same direction for removal
/// - Sliding window: expand right, shrink left when constraint broken
/// - Prefix sum: PS[i] = arr[0..i-1]; query [l,r] = PS[r+1] - PS[l]
/// - [[nodiscard]] on all query/read functions
/// - noexcept on algorithmic functions that never throw

#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <vector>

namespace array_playground {

/// @brief Two-pointer opposite direction: sorted array, find pair summing
///        to target (LC 167 Easy).
/// @param nums Sorted vector of integers.
/// @param target Sum to find.
/// @return Vector [i, j] where i < j and nums[i] + nums[j] == target
///         (1-indexed in LC, 0-indexed here).
///
/// Example: nums=[2,7,11,15], target=9 → [0,1]
/// Constraints: sorted, exactly one solution, no re-using element.
/// Time: O(n), Space: O(1)
/// Tricky: Use left+right from opposite ends; no extra space needed.
[[nodiscard]] std::vector<int> TwoSumSorted(
    const std::vector<int>& nums, int target) noexcept {
  int left = 0, right = static_cast<int>(nums.size()) - 1;
  while (left < right) {
    int sum = nums[left] + nums[right];
    if (sum == target) {
      return {left, right};
    } else if (sum < target) {
      ++left;
    } else {
      --right;
    }
  }
  return {};
}

/// @brief Two-pointer: find all triplets summing to target (LC 15 Medium).
/// @param nums Unsorted vector.
/// @param target Sum to find.
/// @return Vector of vectors, each triplet unique (no duplicates).
///
/// Example: nums=[−1,0,1,2,−1,−2], target=0 → [[-2,-1,1],[-2,0,2],[-1,0,1]]
/// Constraints: 3 ≤ n ≤ 3000; no re-use; sort first.
/// Time: O(n²), Space: O(1) (sorting in-place)
/// Tricky: Sort first; skip duplicates with while loops; fix first, two-sum
///         rest with opposite pointers.
[[nodiscard]] std::vector<std::vector<int>> ThreeSum(
    std::vector<int> nums) noexcept {
  std::vector<std::vector<int>> result;
  std::sort(nums.begin(), nums.end());
  int n = static_cast<int>(nums.size());

  for (int i = 0; i < n - 2; ++i) {
    if (nums[i] > 0) break;
    if (i > 0 && nums[i] == nums[i - 1]) continue;

    int left = i + 1, right = n - 1;
    while (left < right) {
      int sum = nums[i] + nums[left] + nums[right];
      if (sum == 0) {
        result.emplace_back(
            std::initializer_list<int>{nums[i], nums[left], nums[right]});
        while (left < right && nums[left] == nums[left + 1]) ++left;
        while (left < right && nums[right] == nums[right - 1]) --right;
        ++left;
        --right;
      } else if (sum < 0) {
        ++left;
      } else {
        --right;
      }
    }
  }
  return result;
}

/// @brief Two-pointer: find all quadruplets summing to target (LC 18 Medium).
/// @param nums Unsorted vector.
/// @param target Sum to find.
/// @return Vector of vectors, each quadruplet unique.
///
/// Example: nums=[1,0,-1,0,-2,2], target=0 →
///          [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
/// Constraints: 4 ≤ n ≤ 150; avoid duplicates; sort first.
/// Time: O(n³), Space: O(1)
/// Tricky: Fix first two, two-sum rest; skip duplicates at all levels.
[[nodiscard]] std::vector<std::vector<int>> FourSum(
    std::vector<int> nums, int target) noexcept {
  std::vector<std::vector<int>> result;
  std::sort(nums.begin(), nums.end());
  int n = static_cast<int>(nums.size());

  for (int i = 0; i < n - 3; ++i) {
    if (i > 0 && nums[i] == nums[i - 1]) continue;
    for (int j = i + 1; j < n - 2; ++j) {
      if (j > i + 1 && nums[j] == nums[j - 1]) continue;

      int left = j + 1, right = n - 1;
      while (left < right) {
        long long sum = static_cast<long long>(nums[i]) + nums[j] +
                        nums[left] + nums[right];
        if (sum == target) {
          result.emplace_back(std::initializer_list<int>{
              nums[i], nums[j], nums[left], nums[right]});
          while (left < right && nums[left] == nums[left + 1]) ++left;
          while (left < right && nums[right] == nums[right - 1]) --right;
          ++left;
          --right;
        } else if (sum < target) {
          ++left;
        } else {
          --right;
        }
      }
    }
  }
  return result;
}

/// @brief Container with most water: find two lines with max area (LC 11 Med).
/// @param height Vector of heights.
/// @return Maximum area between two lines.
///
/// Example: height=[1,8,6,2,5,4,8,3,7] → 49 (lines at i=1, j=8)
/// Constraints: 2 ≤ n ≤ 10⁵; area = min(h[i], h[j]) * (j - i).
/// Time: O(n), Space: O(1)
/// Tricky: Greed: always move inward from the shorter line (might find taller).
[[nodiscard]] int ContainerWithMostWater(
    const std::vector<int>& height) noexcept {
  int left = 0, right = static_cast<int>(height.size()) - 1;
  int max_area = 0;
  while (left < right) {
    int current_area =
        std::min(height[left], height[right]) * (right - left);
    max_area = std::max(max_area, current_area);
    if (height[left] < height[right]) {
      ++left;
    } else {
      --right;
    }
  }
  return max_area;
}

/// @brief Sliding window (fixed size k): max sum of subarray of size k.
/// @param nums Vector of integers.
/// @param k Window size.
/// @return Maximum sum of any contiguous subarray of size k.
///
/// Example: nums=[1,3,-1,-3,5,3,6,7], k=3 → 16 (subarray [6,7])
/// Constraints: k ≤ nums.size(); k > 0.
/// Time: O(n), Space: O(1)
/// Tricky: Maintain running sum; subtract leaving element, add entering.
[[nodiscard]] int MaxSumSubarraySizeK(const std::vector<int>& nums,
                                       int k) noexcept {
  if (static_cast<int>(nums.size()) < k) return 0;
  int current_sum = 0, max_sum = 0;

  for (int i = 0; i < k; ++i) {
    current_sum += nums[i];
  }
  max_sum = current_sum;

  for (int i = k; i < static_cast<int>(nums.size()); ++i) {
    current_sum = current_sum + nums[i] - nums[i - k];
    max_sum = std::max(max_sum, current_sum);
  }
  return max_sum;
}

/// @brief Sliding window (variable): longest substring with at most k
///        distinct characters.
/// @param s Input string.
/// @param k Maximum distinct characters allowed.
/// @return Length of longest valid substring.
///
/// Example: s="eceba", k=2 → 3 ("ece" or "ceb")
/// Constraints: 1 ≤ n ≤ 10⁵; k ≥ 1.
/// Time: O(n), Space: O(k)
/// Tricky: Use hashmap of char→count; track distinct count separately.
[[nodiscard]] int LongestSubstringKDistinct(std::string_view s,
                                             int k) noexcept {
  if (k <= 0 || s.empty()) return 0;

  std::unordered_map<char, int> char_count;
  int left = 0, max_len = 0;

  for (int right = 0; right < static_cast<int>(s.length()); ++right) {
    ++char_count[s[right]];

    while (static_cast<int>(char_count.size()) > k) {
      --char_count[s[left]];
      if (char_count[s[left]] == 0) {
        char_count.erase(s[left]);
      }
      ++left;
    }
    max_len = std::max(max_len, right - left + 1);
  }
  return max_len;
}

/// @brief Prefix sum: find count of subarrays with sum == k (LC 560 Medium).
/// @param nums Vector of integers (can be negative).
/// @param k Target sum.
/// @return Count of subarrays with sum == k.
///
/// Example: nums=[1,1,1], k=2 → 2 (subarrays [1,1] at indices 0-1 and 1-2)
/// Constraints: −10⁴ ≤ nums[i] ≤ 10⁴; −10⁷ ≤ k ≤ 10⁷; 1 ≤ n ≤ 2×10⁴.
/// Time: O(n), Space: O(n)
/// Tricky: Use prefix sum + hashmap; if prefix_sum[j] - prefix_sum[i] == k
///         then k appears. Store running prefix_sum with counts.
[[nodiscard]] int SubarraySumEqualsK(const std::vector<int>& nums,
                                      int k) noexcept {
  std::unordered_map<int, int> prefix_sum_count;
  prefix_sum_count[0] = 1;
  int current_sum = 0, count = 0;

  for (int num : nums) {
    current_sum += num;
    if (prefix_sum_count.count(current_sum - k)) {
      count += prefix_sum_count[current_sum - k];
    }
    ++prefix_sum_count[current_sum];
  }
  return count;
}

/// @brief Range sum query: precompute prefix sums, answer range queries O(1).
class RangeSum {
 public:
  /// @brief Constructor: precompute prefix sum array.
  /// @param nums Immutable input array.
  explicit RangeSum(const std::vector<int>& nums) {
    prefix_.resize(nums.size() + 1, 0);
    for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
      prefix_[i + 1] = prefix_[i] + nums[i];
    }
  }

  /// @brief Query sum of range [left, right] inclusive.
  /// @param left Left index (0-indexed).
  /// @param right Right index (0-indexed, inclusive).
  /// @return Sum of nums[left..right].
  ///
  /// Time: O(1), Space: O(n) (precomputed in constructor)
  /// Tricky: prefix_[r+1] - prefix_[l] gives sum [l,r].
  [[nodiscard]] int SumRange(int left, int right) const noexcept {
    return prefix_[right + 1] - prefix_[left];
  }

 private:
  std::vector<int> prefix_;
};

/// @brief Kadane's algorithm: max sum of any contiguous subarray (LC 53 Med).
/// @param nums Vector of integers (can contain negatives).
/// @return Maximum subarray sum.
///
/// Example: nums=[-2,1,-3,4,-1,2,1,-5,4] → 6 (subarray [4,-1,2,1])
/// Constraints: 1 ≤ n ≤ 10⁵; −10⁴ ≤ nums[i] ≤ 10⁴.
/// Time: O(n), Space: O(1)
/// Tricky: Track current_max (best ending at i) and global_max. If current
///         becomes negative and remaining elements could be better, reset.
[[nodiscard]] int MaxSubarraySum(const std::vector<int>& nums) noexcept {
  int current_max = nums[0], global_max = nums[0];
  for (int i = 1; i < static_cast<int>(nums.size()); ++i) {
    current_max = std::max(nums[i], current_max + nums[i]);
    global_max = std::max(global_max, current_max);
  }
  return global_max;
}

/// @brief Kadane variant: max product of contiguous subarray (LC 152 Medium).
/// @param nums Vector of integers (can be negative/zero).
/// @return Maximum product subarray.
///
/// Example: nums=[2,3,-2,4] → 6 (subarray [2,3])
/// Constraints: 1 ≤ n ≤ 2×10⁴; −10 ≤ nums[i] ≤ 10.
/// Time: O(n), Space: O(1)
/// Tricky: Track both max and min ending at i (min can become max after
///         negative number); negative × negative = positive.
[[nodiscard]] int MaxProductSubarray(const std::vector<int>& nums) noexcept {
  int current_max = nums[0], current_min = nums[0], global_max = nums[0];
  for (int i = 1; i < static_cast<int>(nums.size()); ++i) {
    int temp_max = current_max;
    current_max = std::max({nums[i], nums[i] * current_max,
                            nums[i] * current_min});
    current_min = std::min({nums[i], nums[i] * temp_max,
                            nums[i] * current_min});
    global_max = std::max(global_max, current_max);
  }
  return global_max;
}

/// @brief Dutch National Flag: sort array of 0s, 1s, 2s in-place (LC 75 Med).
/// @param nums Vector of 0s, 1s, 2s (modified in-place).
///
/// Example: nums=[2,0,2,1,1,0] → [0,0,1,1,2,2]
/// Constraints: 1 ≤ n ≤ 300; nums[i] ∈ {0,1,2}.
/// Time: O(n), Space: O(1)
/// Tricky: Three pointers: left for 0s, right for 2s, mid for 1s. Swap and
///         adjust accordingly. Keep mid moving forward until all 2s pushed.
void SortColors(std::vector<int>& nums) noexcept {
  int left = 0, mid = 0, right = static_cast<int>(nums.size()) - 1;
  while (mid <= right) {
    if (nums[mid] == 0) {
      std::swap(nums[left], nums[mid]);
      ++left;
      ++mid;
    } else if (nums[mid] == 1) {
      ++mid;
    } else {
      std::swap(nums[mid], nums[right]);
      --right;
    }
  }
}

/// @brief Merge intervals: combine overlapping intervals (LC 56 Medium).
/// @param intervals Vector of [start, end] pairs.
/// @return Vector of merged, non-overlapping intervals.
///
/// Example: intervals=[[1,3],[2,6],[8,10],[15,18]] →
///          [[1,6],[8,10],[15,18]]
/// Constraints: 1 ≤ n ≤ 10⁴; all well-formed.
/// Time: O(n log n) (sorting), Space: O(1) (output only)
/// Tricky: Sort by start; merge if current.start <= last_merged.end.
[[nodiscard]] std::vector<std::vector<int>> MergeIntervals(
    std::vector<std::vector<int>> intervals) noexcept {
  std::sort(intervals.begin(), intervals.end());
  std::vector<std::vector<int>> result;
  result.emplace_back(intervals[0]);

  for (int i = 1; i < static_cast<int>(intervals.size()); ++i) {
    if (intervals[i][0] <= result.back()[1]) {
      result.back()[1] = std::max(result.back()[1], intervals[i][1]);
    } else {
      result.emplace_back(intervals[i]);
    }
  }
  return result;
}

/// @brief Binary search: find target in sorted array (LC 704 Easy).
/// @param nums Sorted vector (ascending).
/// @param target Value to find.
/// @return Index of target, or -1 if not found.
///
/// Example: nums=[-1,0,3,5,9,12], target=9 → 4
/// Constraints: 1 ≤ n ≤ 10³; nums sorted; unique elements.
/// Time: O(log n), Space: O(1)
/// Tricky: Use left + (right-left)/2 to avoid overflow. Invariant:
///         target only in [left, right].
[[nodiscard]] int BinarySearch(const std::vector<int>& nums,
                                int target) noexcept {
  int left = 0, right = static_cast<int>(nums.size()) - 1;
  while (left <= right) {
    int mid = left + (right - left) / 2;
    if (nums[mid] == target) {
      return mid;
    } else if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return -1;
}

/// @brief Binary search in rotated sorted array (LC 33 Medium).
/// @param nums Rotated sorted vector (no duplicates).
/// @param target Value to find.
/// @return Index of target, or -1 if not found.
///
/// Example: nums=[4,5,6,7,0,1,2], target=0 → 4
/// Constraints: 1 ≤ n ≤ 5000; rotated at pivot.
/// Time: O(log n), Space: O(1)
/// Tricky: Determine which half is sorted; target in sorted half? Search
///         there, else search other half.
[[nodiscard]] int SearchRotatedSortedArray(const std::vector<int>& nums,
                                            int target) noexcept {
  int left = 0, right = static_cast<int>(nums.size()) - 1;
  while (left <= right) {
    int mid = left + (right - left) / 2;
    if (nums[mid] == target) return mid;

    if (nums[left] <= nums[mid]) {
      if (nums[left] <= target && target < nums[mid]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    } else {
      if (nums[mid] < target && target <= nums[right]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
  }
  return -1;
}

/// @brief Rotate array by k steps in-place (LC 189 Medium).
/// @param nums Vector to rotate (modified in-place).
/// @param k Rotation steps (can be > n, wrap around).
///
/// Example: nums=[1,2,3,4,5,6,7], k=3 → [5,6,7,1,2,3,4]
/// Constraints: 1 ≤ n ≤ 10⁵; 0 ≤ k ≤ 10⁹.
/// Time: O(n), Space: O(1)
/// Tricky: Reverse three times: nums[0..n-1], nums[0..k%n-1],
///         nums[k%n..n-1].
void RotateArray(std::vector<int>& nums, int k) noexcept {
  int n = static_cast<int>(nums.size());
  k = k % n;
  std::reverse(nums.begin(), nums.end());
  std::reverse(nums.begin(), nums.begin() + k);
  std::reverse(nums.begin() + k, nums.end());
}

/// @brief Next permutation: rearrange into next lexicographically
///        greater permutation (LC 31 Medium).
/// @param nums Vector to permute in-place.
///
/// Example: nums=[1,2,3] → [1,3,2]; [3,2,1] → [1,2,3] (wrap around)
/// Constraints: 1 ≤ n ≤ 100; modifies in-place.
/// Time: O(n), Space: O(1)
/// Tricky: Find rightmost i where nums[i] < nums[i+1]; swap with smallest
///         nums[j] > nums[i] to right; reverse nums[i+1..n-1].
void NextPermutation(std::vector<int>& nums) noexcept {
  int n = static_cast<int>(nums.size());
  int i = n - 2;
  while (i >= 0 && nums[i] >= nums[i + 1]) --i;

  if (i >= 0) {
    int j = n - 1;
    while (j > i && nums[j] <= nums[i]) --j;
    std::swap(nums[i], nums[j]);
  }
  std::reverse(nums.begin() + i + 1, nums.end());
}

}  // namespace array_playground

int main() {
  std::cout << "=== ARRAY PLAYGROUND ===\n\n";

  std::vector<int> nums_2sum = {2, 7, 11, 15};
  auto result_2sum = array_playground::TwoSumSorted(nums_2sum, 9);
  std::cout << "TwoSumSorted([2,7,11,15], 9): [" << result_2sum[0] << ","
            << result_2sum[1] << "]\n";

  std::vector<int> nums_3sum = {-1, 0, 1, 2, -1, -2};
  auto result_3sum = array_playground::ThreeSum(nums_3sum);
  std::cout << "ThreeSum([-1,0,1,2,-1,-2]): " << result_3sum.size()
            << " triplets found\n";

  std::vector<int> nums_4sum = {1, 0, -1, 0, -2, 2};
  auto result_4sum = array_playground::FourSum(nums_4sum, 0);
  std::cout << "FourSum([1,0,-1,0,-2,2], 0): " << result_4sum.size()
            << " quadruplets found\n";

  std::vector<int> heights = {1, 8, 6, 2, 5, 4, 8, 3, 7};
  int max_area = array_playground::ContainerWithMostWater(heights);
  std::cout << "ContainerWithMostWater([1,8,6,2,5,4,8,3,7]): " << max_area
            << "\n";

  std::vector<int> nums_window = {1, 3, -1, -3, 5, 3, 6, 7};
  int max_sum_k = array_playground::MaxSumSubarraySizeK(nums_window, 3);
  std::cout << "MaxSumSubarraySizeK([1,3,-1,-3,5,3,6,7], 3): " << max_sum_k
            << "\n";

  int longest = array_playground::LongestSubstringKDistinct("eceba", 2);
  std::cout << "LongestSubstringKDistinct(\"eceba\", 2): " << longest << "\n";

  std::vector<int> nums_subarray = {1, 1, 1};
  int subarray_count = array_playground::SubarraySumEqualsK(nums_subarray, 2);
  std::cout << "SubarraySumEqualsK([1,1,1], 2): " << subarray_count << "\n";

  std::vector<int> nums_range = {-2, 0, 3, -5, 2, -1};
  array_playground::RangeSum range_query(nums_range);
  std::cout << "RangeSum([−2,0,3,−5,2,−1]): SumRange(0,2) = "
            << range_query.SumRange(0, 2) << "\n";

  std::vector<int> nums_kadane = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
  int max_subarray = array_playground::MaxSubarraySum(nums_kadane);
  std::cout << "MaxSubarraySum([-2,1,-3,4,-1,2,1,-5,4]): " << max_subarray
            << "\n";

  std::vector<int> nums_product = {2, 3, -2, 4};
  int max_product = array_playground::MaxProductSubarray(nums_product);
  std::cout << "MaxProductSubarray([2,3,-2,4]): " << max_product << "\n";

  std::vector<int> colors = {2, 0, 2, 1, 1, 0};
  array_playground::SortColors(colors);
  std::cout << "SortColors([2,0,2,1,1,0]): [";
  for (int c : colors) std::cout << c << ",";
  std::cout << "\b]\n";

  std::vector<std::vector<int>> intervals = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
  auto merged = array_playground::MergeIntervals(intervals);
  std::cout << "MergeIntervals(...): " << merged.size() << " merged intervals\n";

  std::vector<int> nums_bs = {-1, 0, 3, 5, 9, 12};
  int bs_result = array_playground::BinarySearch(nums_bs, 9);
  std::cout << "BinarySearch([-1,0,3,5,9,12], 9): index " << bs_result << "\n";

  std::vector<int> rotated = {4, 5, 6, 7, 0, 1, 2};
  int rotated_result =
      array_playground::SearchRotatedSortedArray(rotated, 0);
  std::cout << "SearchRotatedSortedArray([4,5,6,7,0,1,2], 0): index "
            << rotated_result << "\n";

  std::vector<int> nums_rotate = {1, 2, 3, 4, 5, 6, 7};
  array_playground::RotateArray(nums_rotate, 3);
  std::cout << "RotateArray([1,2,3,4,5,6,7], 3): [";
  for (int n : nums_rotate) std::cout << n << ",";
  std::cout << "\b]\n";

  std::vector<int> perm = {1, 2, 3};
  array_playground::NextPermutation(perm);
  std::cout << "NextPermutation([1,2,3]): [";
  for (int p : perm) std::cout << p << ",";
  std::cout << "\b]\n";

  return 0;
}
