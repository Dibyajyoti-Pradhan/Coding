/// Two Pointers Playground
/// Opposite direction for sorted/palindrome problems; same direction for
/// in-place removal/partition; sort first for k-sum; use while guards to
/// skip duplicates; avoid off-by-one in bounds.

#include <algorithm>
#include <cctype>
#include <iostream>
#include <vector>
#include <string>
#include <string_view>

namespace two_pointers_playground {

// ============================================================================
// OPPOSITE DIRECTION
// ============================================================================

/// @brief Find two numbers that add up to target in sorted array.
/// @param nums Sorted array of integers
/// @param target Sum to find
/// @return [index1, index2] 1-indexed, index1 < index2
/// @example TwoSumSorted({2,7,11,15}, 9) -> {1,2}
/// @constraints Array is sorted; exactly one solution
/// @time O(n) @space O(1)
[[nodiscard]] std::vector<int>
TwoSumSorted(const std::vector<int>& nums, int target) noexcept {
  int left = 0;
  int right = static_cast<int>(nums.size()) - 1;
  while (left < right) {
    int sum = nums[left] + nums[right];
    if (sum == target) {
      return {left + 1, right + 1};
    }
    if (sum < target) {
      ++left;
    } else {
      --right;
    }
  }
  return {};
}

/// @brief Find all unique triplets summing to target.
/// @param nums Array of integers
/// @param target Sum to find
/// @return Vector of unique triplets
/// @example ThreeSum({-1,0,1,2,-1,-4}, 0) -> {[-1,-1,2], [-1,0,1]}
/// @constraints O(n²) time required; handle duplicates
/// @time O(n²) @space O(1) excluding output
/// Tricky: Sort first; skip duplicates carefully in outer loop
[[nodiscard]] std::vector<std::vector<int>>
ThreeSum(std::vector<int> nums) noexcept {
  std::vector<std::vector<int>> result;
  std::sort(nums.begin(), nums.end());

  for (size_t i = 0; i < nums.size(); ++i) {
    if (nums[i] > 0) break;
    if (i > 0 && nums[i] == nums[i - 1]) continue;

    int left = i + 1;
    int right = nums.size() - 1;
    int target = -nums[i];

    while (left < right) {
      int sum = nums[left] + nums[right];
      if (sum == target) {
        result.emplace_back(
            std::vector<int>{nums[i], nums[left], nums[right]});
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
  return result;
}

/// @brief Find all unique quadruplets summing to target.
/// @param nums Array of integers
/// @param target Sum to find
/// @return Vector of unique quadruplets
/// @example FourSum({1000000000,1000000000,1000000000,1000000000}, -294967296)
/// @constraints Handle overflow; two nested sorted iterations
/// @time O(n³) @space O(1) excluding output
/// Tricky: Use long long to avoid integer overflow in sum
[[nodiscard]] std::vector<std::vector<int>>
FourSum(std::vector<int> nums, long long target) noexcept {
  std::vector<std::vector<int>> result;
  if (nums.size() < 4) return result;

  std::sort(nums.begin(), nums.end());

  for (size_t i = 0; i < nums.size() - 3; ++i) {
    if (i > 0 && nums[i] == nums[i - 1]) continue;
    long long first = nums[i];
    if (first + nums[i + 1] + nums[i + 2] + nums[i + 3] > target) break;
    if (first + nums[nums.size() - 3] + nums[nums.size() - 2] +
            nums[nums.size() - 1] <
        target)
      continue;

    for (size_t j = i + 1; j < nums.size() - 2; ++j) {
      if (j > i + 1 && nums[j] == nums[j - 1]) continue;
      long long second = nums[j];
      if (first + second + nums[j + 1] + nums[j + 2] > target) break;
      if (first + second + nums[nums.size() - 2] + nums[nums.size() - 1] <
          target)
        continue;

      int left = j + 1;
      int right = nums.size() - 1;
      while (left < right) {
        long long sum = first + second + nums[left] + nums[right];
        if (sum == target) {
          result.emplace_back(std::vector<int>{
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

/// @brief Maximum water area between two lines.
/// @param height Heights at each index
/// @return Maximum container area
/// @example ContainerWithMostWater({1,8,6,2,5,4,8,3,7}) -> 49
/// @constraints Height >= 0
/// @time O(n) @space O(1)
/// Tricky: Area = min(h[i], h[j]) * (j-i); move inward from smaller
[[nodiscard]] int
ContainerWithMostWater(const std::vector<int>& height) noexcept {
  int left = 0;
  int right = height.size() - 1;
  int max_area = 0;

  while (left < right) {
    int width = right - left;
    int h = std::min(height[left], height[right]);
    int area = width * h;
    max_area = std::max(max_area, area);

    if (height[left] < height[right]) {
      ++left;
    } else {
      --right;
    }
  }
  return max_area;
}

// ============================================================================
// SAME DIRECTION
// ============================================================================

/// @brief Remove duplicates in-place from sorted array.
/// @param nums Sorted array, modified in-place
/// @return Number of unique elements
/// @example RemoveDuplicates({1,1,2}) -> 2, nums becomes {1,2,...}
/// @constraints Array is sorted; at most one instance retained per value
/// @time O(n) @space O(1)
[[nodiscard]] int RemoveDuplicates(std::vector<int>& nums) noexcept {
  if (nums.empty()) return 0;

  int write = 0;
  for (int read = 1; read < static_cast<int>(nums.size()); ++read) {
    if (nums[read] != nums[write]) {
      ++write;
      nums[write] = nums[read];
    }
  }
  return write + 1;
}

/// @brief Remove all instances of val in-place.
/// @param nums Array to modify
/// @param val Value to remove
/// @return Count of remaining elements
/// @example RemoveElement({0,1,2,2,3,0,4}, 2) -> 5
/// @constraints Order of remaining elements doesn't matter
/// @time O(n) @space O(1)
[[nodiscard]] int RemoveElement(std::vector<int>& nums,
                                 int val) noexcept {
  int write = 0;
  for (int read = 0; read < static_cast<int>(nums.size()); ++read) {
    if (nums[read] != val) {
      nums[write] = nums[read];
      ++write;
    }
  }
  return write;
}

/// @brief Move all zeros to end, preserve relative order of non-zero.
/// @param nums Array to modify in-place
/// @example MoveZeroes({0,1,0,3,12}) -> {1,3,12,0,0}
/// @constraints O(n) time, O(1) space required
/// @time O(n) @space O(1)
void MoveZeroes(std::vector<int>& nums) noexcept {
  int write = 0;
  for (int read = 0; read < static_cast<int>(nums.size()); ++read) {
    if (nums[read] != 0) {
      if (write != read) {
        nums[write] = nums[read];
      }
      ++write;
    }
  }
  while (write < static_cast<int>(nums.size())) {
    nums[write] = 0;
    ++write;
  }
}

// ============================================================================
// PARTITION (THREE-WAY)
// ============================================================================

/// @brief Sort array with 0, 1, 2 in-place (Dutch National Flag).
/// @param nums Array containing only 0, 1, 2; modified in-place
/// @example SortColors({2,0,1}) -> {0,1,2}
/// @constraints One pass required; O(1) space
/// @time O(n) @space O(1)
/// Tricky: Maintain three pointers: low (0 boundary), mid (current),
/// high (2 boundary)
void SortColors(std::vector<int>& nums) noexcept {
  int low = 0;
  int mid = 0;
  int high = nums.size() - 1;

  while (mid <= high) {
    if (nums[mid] == 0) {
      std::swap(nums[low], nums[mid]);
      ++low;
      ++mid;
    } else if (nums[mid] == 1) {
      ++mid;
    } else {
      std::swap(nums[mid], nums[high]);
      --high;
    }
  }
}

// ============================================================================
// PALINDROME
// ============================================================================

/// @brief Check if string is palindrome ignoring non-alphanumeric.
/// @param s Input string
/// @return true if palindrome (case-insensitive alphanumeric only)
/// @example ValidPalindrome("A man, a plan, a canal: Panama") -> true
/// @constraints O(n) time, O(1) space required
/// @time O(n) @space O(1)
[[nodiscard]] bool ValidPalindrome(std::string_view s) noexcept {
  int left = 0;
  int right = s.size() - 1;

  while (left < right) {
    while (left < right && !std::isalnum(s[left])) {
      ++left;
    }
    while (left < right && !std::isalnum(s[right])) {
      --right;
    }
    if (std::tolower(s[left]) != std::tolower(s[right])) {
      return false;
    }
    ++left;
    --right;
  }
  return true;
}

/// @brief Check if palindrome with at most one character deletion allowed.
/// @param s Input string
/// @return true if can be palindrome by deleting at most one char
/// @example ValidPalindromeII("abca") -> true (delete 'b')
/// @constraints Helper checks palindrome range
/// @time O(n) @space O(1)
[[nodiscard]] bool ValidPalindromeII(std::string_view s) noexcept {
  auto is_palindrome = [](std::string_view str, int left,
                          int right) noexcept {
    while (left < right) {
      if (str[left] != str[right]) return false;
      ++left;
      --right;
    }
    return true;
  };

  int left = 0;
  int right = s.size() - 1;

  while (left < right) {
    if (s[left] != s[right]) {
      return is_palindrome(s, left + 1, right) ||
             is_palindrome(s, left, right - 1);
    }
    ++left;
    --right;
  }
  return true;
}

// ============================================================================
// RAIN WATER TRAPPING
// ============================================================================

/// @brief Calculate trapped rainwater given elevation map.
/// @param height Elevation at each position
/// @return Total water trapped
/// @example Trap({0,1,0,2,1,0,1,3,2,1,2,1}) -> 6
/// @constraints O(1) space solution; track left/right max
/// @time O(n) @space O(1)
/// Tricky: Process from side with smaller max; water level = min(left_max,
/// right_max) - height[i]
[[nodiscard]] int Trap(const std::vector<int>& height) noexcept {
  if (height.empty()) return 0;

  int left = 0;
  int right = height.size() - 1;
  int left_max = 0;
  int right_max = 0;
  int water = 0;

  while (left < right) {
    if (height[left] < height[right]) {
      if (height[left] >= left_max) {
        left_max = height[left];
      } else {
        water += left_max - height[left];
      }
      ++left;
    } else {
      if (height[right] >= right_max) {
        right_max = height[right];
      } else {
        water += right_max - height[right];
      }
      --right;
    }
  }
  return water;
}

}  // namespace two_pointers_playground

// ============================================================================
// TESTS
// ============================================================================

int main() {
  using namespace two_pointers_playground;

  std::cout << "=== Two Pointers Playground ===\n\n";

  std::cout << "TwoSumSorted({2,7,11,15}, 9): ";
  {
    auto result = TwoSumSorted({2, 7, 11, 15}, 9);
    std::cout << "[" << result[0] << ", " << result[1] << "]\n";
  }

  std::cout << "ThreeSum({-1,0,1,2,-1,-4}, 0): ";
  {
    auto result = ThreeSum({-1, 0, 1, 2, -1, -4});
    for (const auto& triplet : result) {
      std::cout << "[" << triplet[0] << "," << triplet[1] << ","
                << triplet[2] << "] ";
    }
    std::cout << "\n";
  }

  std::cout << "ContainerWithMostWater({1,8,6,2,5,4,8,3,7}): ";
  {
    auto result = ContainerWithMostWater({1, 8, 6, 2, 5, 4, 8, 3, 7});
    std::cout << result << "\n";
  }

  std::cout << "RemoveDuplicates({1,1,2}): ";
  {
    std::vector<int> nums = {1, 1, 2};
    int len = RemoveDuplicates(nums);
    std::cout << "len=" << len << "\n";
  }

  std::cout << "RemoveElement({0,1,2,2,3,0,4}, 2): ";
  {
    std::vector<int> nums = {0, 1, 2, 2, 3, 0, 4};
    int len = RemoveElement(nums, 2);
    std::cout << "len=" << len << "\n";
  }

  std::cout << "MoveZeroes({0,1,0,3,12}): ";
  {
    std::vector<int> nums = {0, 1, 0, 3, 12};
    MoveZeroes(nums);
    for (int x : nums) std::cout << x << " ";
    std::cout << "\n";
  }

  std::cout << "SortColors({2,0,1}): ";
  {
    std::vector<int> nums = {2, 0, 1};
    SortColors(nums);
    for (int x : nums) std::cout << x << " ";
    std::cout << "\n";
  }

  std::cout << "ValidPalindrome(\"A man, a plan, a canal: Panama\"): ";
  {
    bool result = ValidPalindrome("A man, a plan, a canal: Panama");
    std::cout << (result ? "true" : "false") << "\n";
  }

  std::cout << "ValidPalindromeII(\"abca\"): ";
  {
    bool result = ValidPalindromeII("abca");
    std::cout << (result ? "true" : "false") << "\n";
  }

  std::cout << "Trap({0,1,0,2,1,0,1,3,2,1,2,1}): ";
  {
    auto result = Trap({0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1});
    std::cout << result << "\n";
  }

  return 0;
}
