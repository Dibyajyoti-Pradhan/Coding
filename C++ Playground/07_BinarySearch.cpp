/// Binary Search Playground
/// Invariant: arr[0..left-1] < target <= arr[left..n-1];
/// left + (right-left)/2 — NEVER (left+right)/2; left <= right for exact
/// match, left < right for left-boundary; answer-space: feasibility function
/// then binary search over [lo, hi]; Tricky: off-by-one in right = mid vs
/// right = mid-1.

#include <algorithm>
#include <iostream>
#include <vector>

namespace binary_search_playground {

constexpr int kNotFound = -1;

// ============================================================================
// STANDARD BINARY SEARCH
// ============================================================================

/// @brief Find exact target in sorted array.
/// @param nums Sorted array of integers
/// @param target Value to find
/// @return Index of target, or -1 if not found
/// @example Search({-1,0,3,5,9,12}, 9) -> 4
/// @constraints Array is sorted; return any occurrence if duplicates
/// @time O(log n) @space O(1)
[[nodiscard]] int Search(const std::vector<int>& nums,
                          int target) noexcept {
  int left = 0;
  int right = nums.size() - 1;

  while (left <= right) {
    int mid = left + (right - left) / 2;
    if (nums[mid] == target) {
      return mid;
    }
    if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return kNotFound;
}

/// @brief Find insert position to maintain sorted order.
/// @param nums Sorted array
/// @param target Value to insert
/// @return Index where target should be inserted
/// @example SearchInsertPosition({1,3,5,6}, 5) -> 2
/// @example SearchInsertPosition({1,3,5,6}, 7) -> 4
/// @constraints Invariant: result is where target belongs
/// @time O(log n) @space O(1)
[[nodiscard]] int SearchInsertPosition(const std::vector<int>& nums,
                                        int target) noexcept {
  int left = 0;
  int right = nums.size();

  while (left < right) {
    int mid = left + (right - left) / 2;
    if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }
  return left;
}

// ============================================================================
// FIRST/LAST OCCURRENCE
// ============================================================================

/// @brief Find first (leftmost) occurrence of target.
/// @param nums Sorted array with possible duplicates
/// @param target Value to find
/// @return Index of first occurrence, or -1
/// @example FindFirstOccurrence({5,7,7,8,8,10}, 8) -> 3
/// @constraints Invariant: find leftmost equal value
/// @time O(log n) @space O(1)
[[nodiscard]] int FindFirstOccurrence(const std::vector<int>& nums,
                                       int target) noexcept {
  int left = 0;
  int right = nums.size();

  while (left < right) {
    int mid = left + (right - left) / 2;
    if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }

  if (left < nums.size() && nums[left] == target) {
    return left;
  }
  return kNotFound;
}

/// @brief Find last (rightmost) occurrence of target.
/// @param nums Sorted array with possible duplicates
/// @param target Value to find
/// @return Index of last occurrence, or -1
/// @example FindLastOccurrence({5,7,7,8,8,10}, 8) -> 4
/// @constraints Invariant: find rightmost equal value
/// @time O(log n) @space O(1)
[[nodiscard]] int FindLastOccurrence(const std::vector<int>& nums,
                                      int target) noexcept {
  int left = 0;
  int right = nums.size();

  while (left < right) {
    int mid = left + (right - left) / 2;
    if (nums[mid] <= target) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }

  if (left > 0 && nums[left - 1] == target) {
    return left - 1;
  }
  return kNotFound;
}

/// @brief Find first and last occurrence range.
/// @param nums Sorted array with possible duplicates
/// @param target Value to find
/// @return [first_idx, last_idx] or [-1, -1] if not found
/// @example SearchRange({5,7,7,8,8,10}, 8) -> [3,4]
/// @constraints Use first+last occurrence helpers
/// @time O(log n) @space O(1)
[[nodiscard]] std::vector<int>
SearchRange(const std::vector<int>& nums, int target) noexcept {
  int first = FindFirstOccurrence(nums, target);
  if (first == kNotFound) {
    return {-1, -1};
  }
  int last = FindLastOccurrence(nums, target);
  return {first, last};
}

// ============================================================================
// ROTATED SORTED ARRAY
// ============================================================================

/// @brief Search in rotated sorted array.
/// @param nums Rotated sorted array (no duplicates)
/// @param target Value to find
/// @return Index of target, or -1
/// @example SearchInRotatedArray({4,5,6,7,0,1,2}, 0) -> 4
/// @constraints Determine which half is sorted; search accordingly
/// @time O(log n) @space O(1)
/// Tricky: nums[left] <= nums[mid] means left half is sorted; else right
[[nodiscard]] int SearchInRotatedArray(const std::vector<int>& nums,
                                        int target) noexcept {
  int left = 0;
  int right = nums.size() - 1;

  while (left <= right) {
    int mid = left + (right - left) / 2;
    if (nums[mid] == target) {
      return mid;
    }

    if (nums[left] <= nums[mid]) {
      // Left half is sorted
      if (nums[left] <= target && target < nums[mid]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    } else {
      // Right half is sorted
      if (nums[mid] < target && target <= nums[right]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
  }
  return kNotFound;
}

/// @brief Find minimum element in rotated sorted array.
/// @param nums Rotated sorted array
/// @return Minimum value
/// @example FindMinInRotatedArray({3,4,5,1,2}) -> 1
/// @constraints nums[0] != nums[right] guaranteed (no duplicates)
/// @time O(log n) @space O(1)
[[nodiscard]] int FindMinInRotatedArray(const std::vector<int>& nums) noexcept {
  int left = 0;
  int right = nums.size() - 1;

  while (left < right) {
    int mid = left + (right - left) / 2;
    if (nums[mid] > nums[right]) {
      // Min is in right half
      left = mid + 1;
    } else {
      // Min is in left half or is mid
      right = mid;
    }
  }
  return nums[left];
}

// ============================================================================
// ANSWER SPACE (FEASIBILITY + BINARY SEARCH)
// ============================================================================

/// @brief Minimum eating speed for Koko to eat all bananas in h hours.
/// @param piles Pile sizes
/// @param h Hour limit
/// @return Minimum eating speed (bananas per hour)
/// @example KokoEatingBananas({1,1,1,1}, 4) -> 1
/// @example KokoEatingBananas({312884132}, 968709470) -> 1
/// @constraints Binary search on speed [1, max_pile]; feasibility check
/// @time O(n log(max_pile)) @space O(1)
static [[nodiscard]] bool CanEat(const std::vector<int>& piles,
                                  long long speed, int h) noexcept {
  long long hours = 0;
  for (int pile : piles) {
    hours += (pile + speed - 1) / speed;  // Ceiling division
    if (hours > h) return false;
  }
  return true;
}

[[nodiscard]] int KokoEatingBananas(const std::vector<int>& piles,
                                     int h) noexcept {
  int left = 1;
  int right = *std::max_element(piles.begin(), piles.end());

  while (left < right) {
    int mid = left + (right - left) / 2;
    if (CanEat(piles, mid, h)) {
      right = mid;
    } else {
      left = mid + 1;
    }
  }
  return left;
}

/// @brief Minimum largest sum when splitting array into k subarrays.
/// @param nums Array of integers
/// @param k Number of subarrays
/// @return Minimum of maximum subarray sums
/// @example SplitArrayLargestSum({7,2,5,10,8}, 2) -> 18
/// @constraints Binary search on answer [max_single, sum_all]
/// @time O(n log(sum)) @space O(1)
static [[nodiscard]] bool CanSplit(const std::vector<int>& nums, int k,
                                    long long max_sum) noexcept {
  int count = 1;
  long long current_sum = 0;
  for (int num : nums) {
    if (current_sum + num > max_sum) {
      ++count;
      current_sum = num;
      if (count > k) return false;
    } else {
      current_sum += num;
    }
  }
  return true;
}

[[nodiscard]] int SplitArrayLargestSum(const std::vector<int>& nums,
                                        int k) noexcept {
  long long left = *std::max_element(nums.begin(), nums.end());
  long long right = 0;
  for (int num : nums) {
    right += num;
  }

  while (left < right) {
    long long mid = left + (right - left) / 2;
    if (CanSplit(nums, k, mid)) {
      right = mid;
    } else {
      left = mid + 1;
    }
  }
  return left;
}

/// @brief Minimum days to ship all packages within deadline.
/// @param weights Package weights
/// @param days Day limit
/// @return Minimum shipping capacity (kg per day)
/// @example ShipPackages({1,2,3,4,5,6,7,8,9,10}, 5) -> 15
/// @constraints Binary search on capacity; greedy packing
/// @time O(n log(sum)) @space O(1)
[[nodiscard]] int ShipPackages(const std::vector<int>& weights,
                                int days) noexcept {
  long long left = *std::max_element(weights.begin(), weights.end());
  long long right = 0;
  for (int w : weights) {
    right += w;
  }

  while (left < right) {
    long long mid = left + (right - left) / 2;
    int required_days = 1;
    long long current_weight = 0;

    for (int w : weights) {
      if (current_weight + w > mid) {
        ++required_days;
        current_weight = w;
      } else {
        current_weight += w;
      }
    }

    if (required_days <= days) {
      right = mid;
    } else {
      left = mid + 1;
    }
  }
  return left;
}

// ============================================================================
// 2D MATRIX
// ============================================================================

/// @brief Search in 2D matrix (sorted row-wise and col-wise).
/// @param matrix m x n matrix, each row and column sorted
/// @param target Value to find
/// @return true if found, false otherwise
/// @example SearchMatrix({{1,3,5,7},{10,11,16,20},{23,30,34,60}}, 3) -> true
/// @constraints Flatten to 1D indices: row = mid/cols, col = mid%cols
/// @time O(log(m*n)) @space O(1)
[[nodiscard]] bool SearchMatrix(const std::vector<std::vector<int>>& matrix,
                                 int target) noexcept {
  if (matrix.empty() || matrix[0].empty()) return false;

  int m = matrix.size();
  int n = matrix[0].size();
  int left = 0;
  int right = m * n - 1;

  while (left <= right) {
    int mid = left + (right - left) / 2;
    int value = matrix[mid / n][mid % n];

    if (value == target) {
      return true;
    }
    if (value < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return false;
}

/// @brief Search in 2D matrix (sorted rows, but not columns).
/// @param matrix m x n matrix, each row sorted; leftmost of row > rightmost
/// of prev row? No
/// @param target Value to find
/// @return true if found, false otherwise
/// @example SearchMatrixII({{1,4,7,11,15},{2,5,8,12,19},...}, 5) -> true
/// @constraints Start from top-right; move left if too large, down if too
/// small
/// @time O(m+n) @space O(1)
/// Tricky: Top-right pointer strategy (could also use bottom-left)
[[nodiscard]] bool SearchMatrixII(const std::vector<std::vector<int>>& matrix,
                                   int target) noexcept {
  if (matrix.empty() || matrix[0].empty()) return false;

  int row = 0;
  int col = matrix[0].size() - 1;

  while (row < static_cast<int>(matrix.size()) && col >= 0) {
    if (matrix[row][col] == target) {
      return true;
    }
    if (matrix[row][col] > target) {
      --col;
    } else {
      ++row;
    }
  }
  return false;
}

// ============================================================================
// PEAK ELEMENT
// ============================================================================

/// @brief Find peak element (greater than neighbors).
/// @param nums Array where nums[i] != nums[i+1]
/// @return Index of any peak element
/// @example FindPeakElement({1,2,1,3,5,6,4}) -> 1 or 5
/// @constraints Array is finite; ends imply edges are < their single neighbor
/// @time O(log n) @space O(1)
/// Tricky: Compare nums[mid] with nums[mid+1]; if > go left, else go right
[[nodiscard]] int FindPeakElement(const std::vector<int>& nums) noexcept {
  int left = 0;
  int right = nums.size() - 1;

  while (left < right) {
    int mid = left + (right - left) / 2;
    if (nums[mid] > nums[mid + 1]) {
      right = mid;
    } else {
      left = mid + 1;
    }
  }
  return left;
}

}  // namespace binary_search_playground

// ============================================================================
// TESTS
// ============================================================================

int main() {
  using namespace binary_search_playground;

  std::cout << "=== Binary Search Playground ===\n\n";

  std::cout << "Search({-1,0,3,5,9,12}, 9): ";
  {
    auto result = Search({-1, 0, 3, 5, 9, 12}, 9);
    std::cout << result << "\n";
  }

  std::cout << "SearchInsertPosition({1,3,5,6}, 5): ";
  {
    auto result = SearchInsertPosition({1, 3, 5, 6}, 5);
    std::cout << result << "\n";
  }

  std::cout << "FindFirstOccurrence({5,7,7,8,8,10}, 8): ";
  {
    auto result = FindFirstOccurrence({5, 7, 7, 8, 8, 10}, 8);
    std::cout << result << "\n";
  }

  std::cout << "FindLastOccurrence({5,7,7,8,8,10}, 8): ";
  {
    auto result = FindLastOccurrence({5, 7, 7, 8, 8, 10}, 8);
    std::cout << result << "\n";
  }

  std::cout << "SearchRange({5,7,7,8,8,10}, 8): ";
  {
    auto result = SearchRange({5, 7, 7, 8, 8, 10}, 8);
    std::cout << "[" << result[0] << ", " << result[1] << "]\n";
  }

  std::cout << "SearchInRotatedArray({4,5,6,7,0,1,2}, 0): ";
  {
    auto result = SearchInRotatedArray({4, 5, 6, 7, 0, 1, 2}, 0);
    std::cout << result << "\n";
  }

  std::cout << "FindMinInRotatedArray({3,4,5,1,2}): ";
  {
    auto result = FindMinInRotatedArray({3, 4, 5, 1, 2});
    std::cout << result << "\n";
  }

  std::cout << "KokoEatingBananas({1,1,1,1}, 4): ";
  {
    auto result = KokoEatingBananas({1, 1, 1, 1}, 4);
    std::cout << result << "\n";
  }

  std::cout << "SplitArrayLargestSum({7,2,5,10,8}, 2): ";
  {
    auto result = SplitArrayLargestSum({7, 2, 5, 10, 8}, 2);
    std::cout << result << "\n";
  }

  std::cout << "ShipPackages({1,2,3,4,5,6,7,8,9,10}, 5): ";
  {
    auto result = ShipPackages({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 5);
    std::cout << result << "\n";
  }

  std::cout << "SearchMatrix({...}, 3): ";
  {
    auto result = SearchMatrix({{1, 3, 5, 7}, {10, 11, 16, 20}}, 3);
    std::cout << (result ? "true" : "false") << "\n";
  }

  std::cout << "FindPeakElement({1,2,1,3,5,6,4}): ";
  {
    auto result = FindPeakElement({1, 2, 1, 3, 5, 6, 4});
    std::cout << result << "\n";
  }

  return 0;
}
