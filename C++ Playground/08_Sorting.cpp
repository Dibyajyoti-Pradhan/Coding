/// Sorting Playground
/// std::sort is introsort — O(n log n) worst; custom comparator must be
/// strict weak ordering (irreflexive, asymmetric, transitive) — undefined
/// behaviour if not; quick-select expected O(n) but O(n²) worst — use random
/// pivot; std::nth_element for O(n) avg Kth in practice; std::stable_sort
/// for stable O(n log n).

#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <numeric>
#include <string>
#include <unordered_map>
#include <vector>

namespace sorting_playground {

// ============================================================================
// MERGE SORT
// ============================================================================

/// @brief Merge sort implementation using auxiliary space.
/// @param arr Array to sort in-place
/// @example MergeSort({38,27,43,3,9,82,10}); arr -> {3,9,10,27,38,43,82}
/// @constraints O(n) space for temp array
/// @time O(n log n) @space O(n)
void MergeSortHelper(std::vector<int>& arr, int left, int right,
                     std::vector<int>& temp) noexcept;

void Merge(std::vector<int>& arr, int left, int mid, int right,
           std::vector<int>& temp) noexcept;

void MergeSort(std::vector<int>& arr) noexcept {
  if (arr.empty()) return;
  std::vector<int> temp(arr.size());
  MergeSortHelper(arr, 0, arr.size() - 1, temp);
}

void MergeSortHelper(std::vector<int>& arr, int left, int right,
                     std::vector<int>& temp) noexcept {
  if (left < right) {
    int mid = left + (right - left) / 2;
    MergeSortHelper(arr, left, mid, temp);
    MergeSortHelper(arr, mid + 1, right, temp);
    Merge(arr, left, mid, right, temp);
  }
}

void Merge(std::vector<int>& arr, int left, int mid, int right,
           std::vector<int>& temp) noexcept {
  int i = left;
  int j = mid + 1;
  int k = left;

  while (i <= mid && j <= right) {
    if (arr[i] <= arr[j]) {
      temp[k++] = arr[i++];
    } else {
      temp[k++] = arr[j++];
    }
  }

  while (i <= mid) {
    temp[k++] = arr[i++];
  }
  while (j <= right) {
    temp[k++] = arr[j++];
  }

  for (i = left; i <= right; ++i) {
    arr[i] = temp[i];
  }
}

// ============================================================================
// QUICK SORT + QUICK SELECT
// ============================================================================

/// @brief Quick sort with random pivot selection.
/// @param arr Array to sort in-place
/// @example QuickSort({38,27,43,3,9,82,10}); arr -> {3,9,10,27,38,43,82}
/// @constraints Random pivot mitigates worst-case O(n²) behavior
/// @time O(n log n) avg, O(n²) worst @space O(log n) recursion
int Partition(std::vector<int>& arr, int left, int right) noexcept;

void QuickSort(std::vector<int>& arr) noexcept {
  if (arr.empty()) return;
  std::srand(std::time(nullptr));
  int left = 0;
  int right = arr.size() - 1;

  auto quick_sort_helper = [&](auto& self, int lo, int hi) noexcept -> void {
    if (lo < hi) {
      int pi = Partition(arr, lo, hi);
      self(self, lo, pi - 1);
      self(self, pi + 1, hi);
    }
  };

  quick_sort_helper(quick_sort_helper, left, right);
}

int Partition(std::vector<int>& arr, int left, int right) noexcept {
  int random_idx = left + std::rand() % (right - left + 1);
  std::swap(arr[random_idx], arr[right]);

  int pivot = arr[right];
  int i = left - 1;

  for (int j = left; j < right; ++j) {
    if (arr[j] < pivot) {
      ++i;
      std::swap(arr[i], arr[j]);
    }
  }
  std::swap(arr[i + 1], arr[right]);
  return i + 1;
}

/// @brief Find kth largest element using quick-select.
/// @param nums Array of integers
/// @param k Position (1-indexed) from largest
/// @return kth largest value
/// @example FindKthLargest({3,2,1,5,6,4}, 2) -> 5
/// @constraints In-place; expected O(n) with random pivot
/// @time O(n) avg, O(n²) worst @space O(1) avg
[[nodiscard]] int FindKthLargest(std::vector<int> nums, int k) noexcept {
  std::srand(std::time(nullptr));
  int target_idx = k - 1;  // 0-indexed
  int left = 0;
  int right = nums.size() - 1;

  while (true) {
    if (left == right) return nums[left];

    int random_idx = left + std::rand() % (right - left + 1);
    std::swap(nums[random_idx], nums[right]);

    int pivot = nums[right];
    int i = left - 1;

    for (int j = left; j < right; ++j) {
      if (nums[j] > pivot) {  // Descending for kth largest
        ++i;
        std::swap(nums[i], nums[j]);
      }
    }
    std::swap(nums[i + 1], nums[right]);
    int pi = i + 1;

    if (pi == target_idx) {
      return nums[pi];
    }
    if (pi < target_idx) {
      left = pi + 1;
    } else {
      right = pi - 1;
    }
  }
}

// ============================================================================
// CUSTOM COMPARATOR
// ============================================================================

/// @brief Largest number by concatenation.
/// @param nums Array of integers
/// @return String form of largest concatenation
/// @example LargestNumber({3,30,34,5,9}) -> "9534330"
/// @constraints Custom comparator: a+b > b+a lexicographically
/// @time O(n log n) @space O(n)
[[nodiscard]] std::string LargestNumber(std::vector<int> nums) noexcept {
  std::sort(nums.begin(), nums.end(), [](int a, int b) noexcept {
    std::string ab = std::to_string(a) + std::to_string(b);
    std::string ba = std::to_string(b) + std::to_string(a);
    return ab > ba;
  });

  if (nums[0] == 0) return "0";

  std::string result;
  for (int num : nums) {
    result += std::to_string(num);
  }
  return result;
}

/// @brief Sort array by frequency, then by value.
/// @param nums Array of integers
/// @return Sorted array by (freq desc, then val asc)
/// @example SortByFrequency({1,1,1,2,2,3}) -> {3,2,2,1,1,1}
/// @constraints Build freq map; sort with custom comparator
/// @time O(n log n) @space O(n)
[[nodiscard]] std::vector<int> SortByFrequency(std::vector<int> nums) noexcept {
  std::unordered_map<int, int> freq;
  for (int num : nums) {
    ++freq[num];
  }

  std::sort(nums.begin(), nums.end(), [&freq](int a, int b) noexcept {
    if (freq[a] != freq[b]) {
      return freq[a] > freq[b];  // Higher freq first
    }
    return a < b;  // Lower value first if same freq
  });

  return nums;
}

// ============================================================================
// INTERVAL PROBLEMS
// ============================================================================

/// @brief Merge overlapping intervals.
/// @param intervals List of [start, end] intervals
/// @return Merged non-overlapping intervals
/// @example MergeIntervals({{1,3},{2,6},{8,10},{15,18}}) ->
/// {{1,6},{8,10},{15,18}}
/// @constraints Sort by start; merge if overlap
/// @time O(n log n) @space O(1) excluding output
[[nodiscard]] std::vector<std::vector<int>>
MergeIntervals(std::vector<std::vector<int>> intervals) noexcept {
  if (intervals.empty()) return {};

  std::sort(intervals.begin(), intervals.end());

  std::vector<std::vector<int>> result;
  result.emplace_back(intervals[0]);

  for (size_t i = 1; i < intervals.size(); ++i) {
    if (intervals[i][0] <= result.back()[1]) {
      result.back()[1] = std::max(result.back()[1], intervals[i][1]);
    } else {
      result.emplace_back(intervals[i]);
    }
  }
  return result;
}

/// @brief Insert interval into list of merged intervals.
/// @param intervals Sorted list of non-overlapping intervals
/// @param new_interval Interval to insert and merge
/// @return Updated merged list
/// @example InsertInterval({{1,2},{3,5},{6,9}}, {4,8}) -> {{1,2},{3,8},{6,9}}
/// @constraints More efficient than insert+merge
/// @time O(n) @space O(n)
[[nodiscard]] std::vector<std::vector<int>>
InsertInterval(std::vector<std::vector<int>> intervals,
               std::vector<int> new_interval) noexcept {
  std::vector<std::vector<int>> result;
  size_t i = 0;

  // Add all intervals before new_interval
  while (i < intervals.size() && intervals[i][1] < new_interval[0]) {
    result.emplace_back(intervals[i]);
    ++i;
  }

  // Merge overlapping intervals
  while (i < intervals.size() && intervals[i][0] <= new_interval[1]) {
    new_interval[0] = std::min(new_interval[0], intervals[i][0]);
    new_interval[1] = std::max(new_interval[1], intervals[i][1]);
    ++i;
  }
  result.emplace_back(new_interval);

  // Add remaining intervals
  while (i < intervals.size()) {
    result.emplace_back(intervals[i]);
    ++i;
  }

  return result;
}

/// @brief Minimum rooms needed for meetings.
/// @param intervals Meeting times [[start, end], ...]
/// @return Minimum number of rooms required
/// @example MeetingRoomsII({{0,30},{5,10},{15,20}}) -> 2
/// @constraints Two-pointer over sorted starts and ends
/// @time O(n log n) @space O(n)
/// Tricky: Sort starts and ends separately; if start < end, need new room
[[nodiscard]] int
MeetingRoomsII(std::vector<std::vector<int>> intervals) noexcept {
  if (intervals.empty()) return 0;

  std::vector<int> starts, ends;
  for (const auto& interval : intervals) {
    starts.emplace_back(interval[0]);
    ends.emplace_back(interval[1]);
  }

  std::sort(starts.begin(), starts.end());
  std::sort(ends.begin(), ends.end());

  int rooms = 0;
  int available = 0;
  size_t i = 0;
  size_t j = 0;

  while (i < starts.size()) {
    if (starts[i] < ends[j]) {
      ++rooms;
      ++i;
    } else {
      ++available;
      ++j;
    }
  }

  return rooms;
}

// ============================================================================
// BUCKET / COUNTING SORT
// ============================================================================

/// @brief Top k frequent elements using bucket sort.
/// @param nums Array of integers
/// @param k Number of top elements to return
/// @return k most frequent elements
/// @example TopKFrequentBucket({1,1,1,2,2,3}, 2) -> {1,2}
/// @constraints Freq array as keys; bucket index = frequency
/// @time O(n) @space O(n)
[[nodiscard]] std::vector<int> TopKFrequentBucket(const std::vector<int>& nums,
                                                   int k) noexcept {
  std::unordered_map<int, int> freq;
  for (int num : nums) {
    ++freq[num];
  }

  std::vector<std::vector<int>> buckets(nums.size() + 1);
  for (const auto& [num, count] : freq) {
    buckets[count].emplace_back(num);
  }

  std::vector<int> result;
  for (int i = buckets.size() - 1; i >= 0 && result.size() < static_cast<size_t>(k);
       --i) {
    for (int num : buckets[i]) {
      result.emplace_back(num);
      if (result.size() == static_cast<size_t>(k)) break;
    }
  }
  return result;
}

// ============================================================================
// CYCLE SORT / INDEX TRICKS
// ============================================================================

/// @brief Find missing number in [0,n] using XOR.
/// @param nums Array with n unique numbers from [0,n]
/// @return The one missing number
/// @example FindMissingNumber({3,0,1}) -> 2
/// @constraints XOR trick: a XOR a = 0; a XOR 0 = a
/// @time O(n) @space O(1)
[[nodiscard]] int FindMissingNumber(const std::vector<int>& nums) noexcept {
  int xor_all = 0;
  int xor_nums = 0;

  for (size_t i = 0; i < nums.size(); ++i) {
    xor_all ^= i;
    xor_nums ^= nums[i];
  }
  xor_all ^= nums.size();

  return xor_all ^ xor_nums;
}

/// @brief Find duplicate using Floyd's cycle detection.
/// @param nums Array with one duplicate, range [1,n], length n+1
/// @return The duplicate number
/// @example FindDuplicate({1,3,4,2,2}) -> 2
/// @constraints Treat as linked list where nums[i] -> index nums[i]
/// @time O(n) @space O(1)
/// Tricky: Slow and fast pointers; detect cycle; find cycle entrance
[[nodiscard]] int FindDuplicate(const std::vector<int>& nums) noexcept {
  int slow = nums[0];
  int fast = nums[0];

  do {
    slow = nums[slow];
    fast = nums[nums[fast]];
  } while (slow != fast);

  slow = nums[0];
  while (slow != fast) {
    slow = nums[slow];
    fast = nums[fast];
  }

  return slow;
}

}  // namespace sorting_playground

// ============================================================================
// TESTS
// ============================================================================

int main() {
  using namespace sorting_playground;

  std::cout << "=== Sorting Playground ===\n\n";

  std::cout << "MergeSort({38,27,43,3,9,82,10}): ";
  {
    std::vector<int> arr = {38, 27, 43, 3, 9, 82, 10};
    MergeSort(arr);
    for (int x : arr) std::cout << x << " ";
    std::cout << "\n";
  }

  std::cout << "QuickSort({38,27,43,3,9,82,10}): ";
  {
    std::vector<int> arr = {38, 27, 43, 3, 9, 82, 10};
    QuickSort(arr);
    for (int x : arr) std::cout << x << " ";
    std::cout << "\n";
  }

  std::cout << "FindKthLargest({3,2,1,5,6,4}, 2): ";
  {
    auto result = FindKthLargest({3, 2, 1, 5, 6, 4}, 2);
    std::cout << result << "\n";
  }

  std::cout << "LargestNumber({3,30,34,5,9}): ";
  {
    auto result = LargestNumber({3, 30, 34, 5, 9});
    std::cout << result << "\n";
  }

  std::cout << "SortByFrequency({1,1,1,2,2,3}): ";
  {
    auto result = SortByFrequency({1, 1, 1, 2, 2, 3});
    for (int x : result) std::cout << x << " ";
    std::cout << "\n";
  }

  std::cout << "MergeIntervals({{1,3},{2,6},{8,10},{15,18}}): ";
  {
    auto result = MergeIntervals({{1, 3}, {2, 6}, {8, 10}, {15, 18}});
    for (const auto& interval : result) {
      std::cout << "[" << interval[0] << "," << interval[1] << "] ";
    }
    std::cout << "\n";
  }

  std::cout << "InsertInterval({{1,2},{3,5},{6,9}}, {4,8}): ";
  {
    auto result = InsertInterval({{1, 2}, {3, 5}, {6, 9}}, {4, 8});
    for (const auto& interval : result) {
      std::cout << "[" << interval[0] << "," << interval[1] << "] ";
    }
    std::cout << "\n";
  }

  std::cout << "MeetingRoomsII({{0,30},{5,10},{15,20}}): ";
  {
    auto result = MeetingRoomsII({{0, 30}, {5, 10}, {15, 20}});
    std::cout << result << "\n";
  }

  std::cout << "TopKFrequentBucket({1,1,1,2,2,3}, 2): ";
  {
    auto result = TopKFrequentBucket({1, 1, 1, 2, 2, 3}, 2);
    for (int x : result) std::cout << x << " ";
    std::cout << "\n";
  }

  std::cout << "FindMissingNumber({3,0,1}): ";
  {
    auto result = FindMissingNumber({3, 0, 1});
    std::cout << result << "\n";
  }

  std::cout << "FindDuplicate({1,3,4,2,2}): ";
  {
    auto result = FindDuplicate({1, 3, 4, 2, 2});
    std::cout << result << "\n";
  }

  return 0;
}
