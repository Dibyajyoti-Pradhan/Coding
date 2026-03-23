/// @file 03_HashTable.cpp
/// @brief Hash Tables Playground — two sum, frequency, grouping, LRU cache,
///        two sum design.
///
/// HASH TABLES GUIDE:
/// - unordered_map<K,V>: O(1) average, O(n) worst case on hash collision
/// - map<K,V>: O(log n) guaranteed, uses red-black tree, keeps sorted order
/// - Use .count(k) or .find(k) to check membership on const maps
/// - Default [] initializes missing key to default value (0 for int, "" for
///   string)
/// - Frequency counting: unordered_map<int, int> or int[26] for chars
/// - LRU Cache: combine doubly-linked-list + unordered_map for O(1) Get/Put
/// - Two pointers on hash: find unique pairs or track indices efficiently

#include <algorithm>
#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

namespace hashtable_playground {

/// @brief Two Sum: find two indices where nums[i] + nums[j] == target
///        (LC 1 Easy).
/// @param nums Vector of integers (may have duplicates).
/// @param target Sum to find.
/// @return Vector [i, j] of indices, or empty if not found.
///
/// Example: nums=[2,7,11,15], target=9 → [0,1]
/// Constraints: 2 ≤ n ≤ 10³; exactly one solution.
/// Time: O(n), Space: O(n)
/// Tricky: Store num→index in map; for each num, check if (target - num)
///         exists. Avoid re-using same element.
[[nodiscard]] std::vector<int> TwoSum(const std::vector<int>& nums,
                                       int target) {
  std::unordered_map<int, int> num_index;
  for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
    int complement = target - nums[i];
    if (num_index.count(complement)) {
      return {num_index[complement], i};
    }
    num_index[nums[i]] = i;
  }
  return {};
}

/// @brief Two Sum with all pairs: return all unique pairs.
/// @param nums Vector of integers.
/// @param target Sum to find.
/// @return Vector of unique pairs [a, b] where a ≤ b.
///
/// Example: nums=[1,5,7,−1,5], target=6 → [[1,5]]
/// Constraints: duplicates possible.
/// Time: O(n), Space: O(n)
/// Tricky: Use set to track seen pairs and avoid duplicates.
[[nodiscard]] std::vector<std::pair<int, int>> TwoSumAllPairs(
    std::vector<int> nums, int target) noexcept {
  std::sort(nums.begin(), nums.end());
  std::vector<std::pair<int, int>> result;
  int left = 0, right = static_cast<int>(nums.size()) - 1;

  while (left < right) {
    int sum = nums[left] + nums[right];
    if (sum == target) {
      result.emplace_back(nums[left], nums[right]);
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
  return result;
}

/// @brief Top K frequent elements: return k most frequent elements
///        (LC 347 Medium).
/// @param nums Vector of integers.
/// @param k Number of top elements to return.
/// @return Vector of k most frequent elements (order doesn't matter).
///
/// Example: nums=[1,1,1,2,2,3], k=2 → [1,2]
/// Constraints: 1 ≤ n ≤ 10⁵; 1 ≤ k ≤ unique elements.
/// Time: O(n log k) using min-heap, or O(n) using bucket sort
/// Space: O(k) for heap
/// Tricky: Use min-heap of size k with custom comparator; or bucket sort
///         by frequency.
[[nodiscard]] std::vector<int> TopKFrequent(const std::vector<int>& nums,
                                             int k) {
  std::unordered_map<int, int> freq;
  for (int num : nums) {
    ++freq[num];
  }

  auto cmp = [](const std::pair<int, int>& a,
                const std::pair<int, int>& b) {
    return a.first > b.first;
  };
  std::priority_queue<std::pair<int, int>,
                      std::vector<std::pair<int, int>>,
                      decltype(cmp)> min_heap(cmp);

  for (const auto& [num, count] : freq) {
    min_heap.emplace(count, num);
    if (static_cast<int>(min_heap.size()) > k) {
      min_heap.pop();
    }
  }

  std::vector<int> result;
  while (!min_heap.empty()) {
    result.emplace_back(min_heap.top().second);
    min_heap.pop();
  }
  return result;
}

/// @brief First unique character in string: find index of first char
///        appearing once (LC 387 Easy).
/// @param s Input string.
/// @return Index of first unique char, or -1 if none.
///
/// Example: s="leetcode" → 0 (l); s="loveleetcode" → 2 (v)
/// Constraints: 1 ≤ s.length ≤ 10⁵; lowercase English.
/// Time: O(n), Space: O(1) (26 chars)
/// Tricky: Count frequencies first; second pass find first char with count 1.
[[nodiscard]] int FirstUniqueChar(std::string_view s) noexcept {
  int char_count[26] = {0};
  for (char c : s) {
    ++char_count[c - 'a'];
  }
  for (int i = 0; i < static_cast<int>(s.length()); ++i) {
    if (char_count[s[i] - 'a'] == 1) {
      return i;
    }
  }
  return -1;
}

/// @brief Group anagrams (LC 49 Medium).
/// @param strs Vector of strings.
/// @return Vector of vectors, grouped by canonical form.
///
/// Time: O(n * k log k) where k = avg string length
/// Space: O(n * k)
/// Tricky: Sort chars in each string to get canonical form.
[[nodiscard]] std::vector<std::vector<std::string>> GroupAnagrams(
    const std::vector<std::string>& strs) {
  std::unordered_map<std::string, std::vector<std::string>> groups;
  for (const auto& str : strs) {
    std::string sorted_str = str;
    std::sort(sorted_str.begin(), sorted_str.end());
    groups[sorted_str].emplace_back(str);
  }
  std::vector<std::vector<std::string>> result;
  for (auto& group : groups) {
    result.emplace_back(std::move(group.second));
  }
  return result;
}

/// @brief Group shifted strings: group strings with same shift pattern
///        (LC 1061 Easy).
/// @param strs Vector of strings.
/// @return Vector of vectors, grouped by shift pattern.
///
/// Example: strs=["abc","bcd","acef","xyz","az","ba","a","z"] →
///          [["abc","bcd","xyz"],["az","ba"],["acef"],["a","z"]]
/// Constraints: 1 ≤ n ≤ 200; 1 ≤ strs[i].length ≤ 100.
/// Time: O(n * k) where k = avg string length
/// Space: O(n * k)
/// Tricky: Shift pattern = sequence of (char[i+1] - char[i]) mod 26.
[[nodiscard]] std::vector<std::vector<std::string>> GroupShiftedStrings(
    const std::vector<std::string>& strs) {
  std::unordered_map<std::string, std::vector<std::string>> groups;

  for (const auto& str : strs) {
    std::string pattern;
    for (int i = 1; i < static_cast<int>(str.length()); ++i) {
      int diff = (str[i] - str[i - 1] + 26) % 26;
      pattern += std::to_string(diff) + ",";
    }
    groups[pattern].emplace_back(str);
  }

  std::vector<std::vector<std::string>> result;
  for (auto& group : groups) {
    result.emplace_back(std::move(group.second));
  }
  return result;
}

/// @brief Subarray sum equals k: count subarrays summing to k (LC 560 Med).
/// @param nums Vector of integers.
/// @param k Target sum.
/// @return Count of subarrays.
///
/// Example: nums=[1,1,1], k=2 → 2
/// Constraints: −10⁴ ≤ nums[i] ≤ 10⁴; 1 ≤ n ≤ 2×10⁴.
/// Time: O(n), Space: O(n)
/// Tricky: Prefix sum + hashmap; if prefix[j] - prefix[i] == k, then
///         subarray [i+1..j] sums to k. Increment count of prefix[j] - k.
[[nodiscard]] int SubarraySumEqualsK(const std::vector<int>& nums,
                                      int k) noexcept {
  std::unordered_map<int, int> prefix_count;
  prefix_count[0] = 1;
  int current_sum = 0, count = 0;

  for (int num : nums) {
    current_sum += num;
    if (prefix_count.count(current_sum - k)) {
      count += prefix_count[current_sum - k];
    }
    ++prefix_count[current_sum];
  }
  return count;
}

/// @brief Longest consecutive sequence (LC 128 Medium).
/// @param nums Vector of integers (unsorted, may have duplicates).
/// @return Length of longest consecutive elements sequence.
///
/// Example: nums=[100,4,200,1,3,2] → 4 (sequence 1,2,3,4)
/// Constraints: 0 ≤ n ≤ 10⁵; −10⁹ ≤ nums[i] ≤ 10⁹.
/// Time: O(n), Space: O(n)
/// Tricky: Store all nums in set; for each num, if (num-1) not in set, it's
///         a sequence start; count consecutive.
[[nodiscard]] int LongestConsecutiveSequence(
    const std::vector<int>& nums) {
  std::unordered_set<int> num_set(nums.begin(), nums.end());
  int max_length = 0;

  for (int num : num_set) {
    if (num_set.find(num - 1) == num_set.end()) {
      int current_num = num, current_length = 1;
      while (num_set.find(current_num + 1) != num_set.end()) {
        ++current_num;
        ++current_length;
      }
      max_length = std::max(max_length, current_length);
    }
  }
  return max_length;
}

/// @brief LRU Cache: Least Recently Used eviction policy (LC 146 Medium).
/// - Get(key) returns value in O(1), marks as recently used
/// - Put(key, val) sets value in O(1), evicts least recently used if full
/// - Both operations must be O(1)
///
/// Implementation: doubly-linked-list + unordered_map
/// Tricky: Node order in DLL: most recent at end, least recent at head
/// (after dummy head). Move accessed node to end. Evict head.next.
class LRUCache {
 private:
  struct Node {
    int key;
    int val;
    Node* prev;
    Node* next;
    Node(int k, int v) : key(k), val(v), prev(nullptr), next(nullptr) {}
  };

  int capacity_;
  Node* head_;
  Node* tail_;
  std::unordered_map<int, Node*> cache_;

  void RemoveNode(Node* node) noexcept {
    node->prev->next = node->next;
    node->next->prev = node->prev;
  }

  void AddToEnd(Node* node) noexcept {
    node->prev = tail_->prev;
    node->next = tail_;
    tail_->prev->next = node;
    tail_->prev = node;
  }

 public:
  explicit LRUCache(int capacity) noexcept : capacity_(capacity) {
    head_ = new Node(0, 0);
    tail_ = new Node(0, 0);
    head_->next = tail_;
    tail_->prev = head_;
  }

  ~LRUCache() {
    Node* curr = head_;
    while (curr) {
      Node* temp = curr;
      curr = curr->next;
      delete temp;
    }
  }

  /// @brief Get value by key, mark as recently used.
  /// @param key Key to retrieve.
  /// @return Value associated with key, or -1 if not found.
  /// Time: O(1)
  [[nodiscard]] int Get(int key) noexcept {
    if (!cache_.count(key)) {
      return -1;
    }
    Node* node = cache_[key];
    RemoveNode(node);
    AddToEnd(node);
    return node->val;
  }

  /// @brief Put key-value pair; evict LRU if at capacity.
  /// @param key Key to insert.
  /// @param value Value to associate.
  /// Time: O(1)
  void Put(int key, int value) noexcept {
    if (cache_.count(key)) {
      Node* node = cache_[key];
      node->val = value;
      RemoveNode(node);
      AddToEnd(node);
    } else {
      Node* new_node = new Node(key, value);
      cache_[key] = new_node;
      AddToEnd(new_node);
      if (static_cast<int>(cache_.size()) > capacity_) {
        Node* lru = head_->next;
        RemoveNode(lru);
        cache_.erase(lru->key);
        delete lru;
      }
    }
  }
};

/// @brief Two Sum Design: Add numbers and check if any two sum equals target
///        (LC 170 Easy).
class TwoSumDS {
 private:
  std::unordered_map<int, int> num_count_;

 public:
  /// @brief Add a number to the data structure.
  /// @param number Number to add.
  /// Time: O(1)
  void Add(int number) noexcept { ++num_count_[number]; }

  /// @brief Check if any two numbers sum to target.
  /// @param target Sum to find.
  /// @return true if two numbers (possibly same) sum to target.
  /// Time: O(n) where n = unique numbers
  /// Tricky: If target is even and target/2 exists with count ≥ 2, return
  ///         true. Otherwise need two different numbers.
  [[nodiscard]] bool Find(int target) const noexcept {
    for (const auto& [num, count] : num_count_) {
      int complement = target - num;
      if (complement == num) {
        return count >= 2;
      }
      if (num_count_.count(complement)) {
        return true;
      }
    }
    return false;
  }
};

}  // namespace hashtable_playground

int main() {
  std::cout << "=== HASH TABLE PLAYGROUND ===\n\n";

  std::vector<int> nums_2sum = {2, 7, 11, 15};
  auto result_2sum = hashtable_playground::TwoSum(nums_2sum, 9);
  std::cout << "TwoSum([2,7,11,15], 9): [" << result_2sum[0] << ","
            << result_2sum[1] << "]\n";

  std::vector<int> nums_freq = {1, 1, 1, 2, 2, 3};
  auto top_k = hashtable_playground::TopKFrequent(nums_freq, 2);
  std::cout << "TopKFrequent([1,1,1,2,2,3], 2): ";
  for (int n : top_k) std::cout << n << " ";
  std::cout << "\n";

  int first_unique = hashtable_playground::FirstUniqueChar("leetcode");
  std::cout << "FirstUniqueChar(\"leetcode\"): " << first_unique << "\n";

  std::vector<std::string> words = {"eat", "tea", "tan", "ate", "nat", "bat"};
  auto grouped = hashtable_playground::GroupAnagrams(words);
  std::cout << "GroupAnagrams(...): " << grouped.size() << " groups\n";

  std::vector<int> nums_subarray = {1, 1, 1};
  int subarray_count =
      hashtable_playground::SubarraySumEqualsK(nums_subarray, 2);
  std::cout << "SubarraySumEqualsK([1,1,1], 2): " << subarray_count << "\n";

  std::vector<int> nums_consecutive = {100, 4, 200, 1, 3, 2};
  int longest_consec =
      hashtable_playground::LongestConsecutiveSequence(nums_consecutive);
  std::cout << "LongestConsecutiveSequence([100,4,200,1,3,2]): "
            << longest_consec << "\n";

  hashtable_playground::LRUCache lru_cache(2);
  lru_cache.Put(1, 1);
  lru_cache.Put(2, 2);
  std::cout << "LRUCache: Put(1,1), Put(2,2), Get(1)=" << lru_cache.Get(1)
            << "\n";

  hashtable_playground::TwoSumDS two_sum_ds;
  two_sum_ds.Add(1);
  two_sum_ds.Add(5);
  bool found = two_sum_ds.Find(6);
  std::cout << "TwoSumDS: Add(1), Add(5), Find(6)=" << (found ? "true" : "false")
            << "\n";

  return 0;
}
