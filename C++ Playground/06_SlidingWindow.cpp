/// Sliding Window Playground
/// Expand right, shrink left; int freq[128]{} for ASCII (faster than
/// unordered_map); at-most-K trick: ExactK(k) = AtMostK(k) - AtMostK(k-1);
/// monotonic deque stores indices (not values) — front is always max; when
/// window slides past front, pop it.

#include <algorithm>
#include <climits>
#include <deque>
#include <iostream>
#include <string>
#include <string_view>
#include <unordered_map>
#include <vector>

namespace sliding_window_playground {

constexpr int kAsciiSize = 128;

// ============================================================================
// FIXED SIZE WINDOW
// ============================================================================

/// @brief Maximum sum of subarray of size k.
/// @param nums Array of integers
/// @param k Window size
/// @return Maximum sum in any k-length subarray
/// @example MaxSumSubarraySizeK({1,3,-1,-3,5,3,6,7}, 3) -> 16
/// @constraints k >= 1, k <= nums.size()
/// @time O(n) @space O(1)
[[nodiscard]] int MaxSumSubarraySizeK(const std::vector<int>& nums,
                                       int k) noexcept {
  if (nums.empty() || k > static_cast<int>(nums.size())) {
    return 0;
  }

  int window_sum = 0;
  for (int i = 0; i < k; ++i) {
    window_sum += nums[i];
  }
  int max_sum = window_sum;

  for (size_t i = k; i < nums.size(); ++i) {
    window_sum = window_sum - nums[i - k] + nums[i];
    max_sum = std::max(max_sum, window_sum);
  }
  return max_sum;
}

/// @brief Find all anagram start indices of p in s.
/// @param s Haystack string
/// @param p Needle pattern (anagram target)
/// @return Indices where anagram of p starts in s
/// @example FindAnagrams("cbaebabacd", "abc") -> {0,6}
/// @constraints Use freq array for O(1) comparison
/// @time O(n) @space O(1) [26 letters]
[[nodiscard]] std::vector<int> FindAnagrams(std::string_view s,
                                             std::string_view p) noexcept {
  if (p.size() > s.size()) return {};

  std::vector<int> p_freq(26, 0);
  std::vector<int> window_freq(26, 0);

  for (char c : p) {
    ++p_freq[c - 'a'];
  }

  std::vector<int> result;
  for (size_t i = 0; i < s.size(); ++i) {
    ++window_freq[s[i] - 'a'];

    if (i >= p.size()) {
      --window_freq[s[i - p.size()] - 'a'];
    }

    if (window_freq == p_freq) {
      result.emplace_back(i - p.size() + 1);
    }
  }
  return result;
}

/// @brief Check if duplicates exist within distance k.
/// @param nums Array of integers
/// @param k Maximum distance between duplicates
/// @return true if duplicate found within distance k
/// @example ContainsNearbyDuplicate({99,99}, 2) -> true
/// @constraints Window size = k
/// @time O(n) @space O(min(n,k))
[[nodiscard]] bool ContainsNearbyDuplicate(const std::vector<int>& nums,
                                            int k) noexcept {
  std::unordered_map<int, int> window;

  for (size_t i = 0; i < nums.size(); ++i) {
    if (window.find(nums[i]) != window.end()) {
      return true;
    }
    window[nums[i]] = i;

    if (static_cast<int>(window.size()) > k) {
      window.erase(nums[i - k]);
    }
  }
  return false;
}

// ============================================================================
// VARIABLE WINDOW — MAXIMUM LENGTH
// ============================================================================

/// @brief Longest substring without repeating characters.
/// @param s Input string
/// @return Length of longest substring with all distinct chars
/// @example LengthOfLongestSubstring("abcabcbb") -> 3 ("abc")
/// @constraints Two-pointer, char freq tracking
/// @time O(n) @space O(min(n,128))
[[nodiscard]] int LengthOfLongestSubstring(std::string_view s) noexcept {
  int char_freq[kAsciiSize]{};
  int left = 0;
  int max_len = 0;

  for (size_t right = 0; right < s.size(); ++right) {
    ++char_freq[static_cast<unsigned char>(s[right])];

    while (char_freq[static_cast<unsigned char>(s[right])] > 1) {
      --char_freq[static_cast<unsigned char>(s[left])];
      ++left;
    }

    max_len = std::max(max_len, static_cast<int>(right - left + 1));
  }
  return max_len;
}

/// @brief Longest substring with at most k distinct characters.
/// @param s Input string
/// @param k Max distinct characters allowed
/// @return Length of longest substring
/// @example LongestSubstringKDistinct("eceba", 2) -> 3 ("ece")
/// @constraints Maintain char count in window
/// @time O(n) @space O(min(n,128))
[[nodiscard]] int LongestSubstringKDistinct(std::string_view s,
                                             int k) noexcept {
  if (k <= 0 || s.empty()) return 0;

  int char_freq[kAsciiSize]{};
  int left = 0;
  int max_len = 0;
  int distinct = 0;

  for (size_t right = 0; right < s.size(); ++right) {
    if (char_freq[static_cast<unsigned char>(s[right])] == 0) {
      ++distinct;
    }
    ++char_freq[static_cast<unsigned char>(s[right])];

    while (distinct > k) {
      --char_freq[static_cast<unsigned char>(s[left])];
      if (char_freq[static_cast<unsigned char>(s[left])] == 0) {
        --distinct;
      }
      ++left;
    }

    max_len = std::max(max_len, static_cast<int>(right - left + 1));
  }
  return max_len;
}

/// @brief Longest substring with at most k character replacements.
/// @param s String with uppercase letters
/// @param k Max replacements allowed
/// @return Length of longest substring with same char after k replacements
/// @example CharacterReplacement("ABAB", 2) -> 4 ("ABAB"->all A or all B)
/// @constraints Track max freq in window; expand if replacements OK
/// @time O(n) @space O(26)
[[nodiscard]] int CharacterReplacement(std::string_view s, int k) noexcept {
  int char_freq[26]{};
  int left = 0;
  int max_freq = 0;
  int max_len = 0;

  for (size_t right = 0; right < s.size(); ++right) {
    ++char_freq[s[right] - 'A'];
    max_freq = std::max(max_freq, char_freq[s[right] - 'A']);

    int window_len = right - left + 1;
    int replacements_needed = window_len - max_freq;

    while (replacements_needed > k) {
      --char_freq[s[left] - 'A'];
      ++left;
      window_len = right - left + 1;
      max_freq = *std::max_element(char_freq, char_freq + 26);
      replacements_needed = window_len - max_freq;
    }

    max_len = std::max(max_len, static_cast<int>(right - left + 1));
  }
  return max_len;
}

// ============================================================================
// VARIABLE WINDOW — MINIMUM LENGTH
// ============================================================================

/// @brief Minimum window substring containing all chars of t.
/// @param s Haystack string
/// @param t Needle characters (must all appear in result)
/// @return Shortest substring of s containing all chars from t
/// @example MinWindowSubstring("ADOBECODEBANC", "ABC") -> "BANC"
/// @constraints Track required chars and formed chars
/// @time O(n+m) @space O(128)
[[nodiscard]] std::string MinWindowSubstring(std::string_view s,
                                              std::string_view t) noexcept {
  if (s.empty() || t.empty() || t.size() > s.size()) return "";

  int required[kAsciiSize]{};
  int window[kAsciiSize]{};

  for (char c : t) {
    ++required[static_cast<unsigned char>(c)];
  }

  int left = 0;
  int formed = 0;
  int required_count = 0;

  for (char c : t) {
    if (required[static_cast<unsigned char>(c)] > 0) {
      ++required_count;
      required[static_cast<unsigned char>(c)] =
          -required[static_cast<unsigned char>(c)];
    }
  }

  int min_len = INT_MAX;
  int min_left = 0;
  int min_right = 0;

  for (size_t right = 0; right < s.size(); ++right) {
    ++window[static_cast<unsigned char>(s[right])];

    if (required[static_cast<unsigned char>(s[right])] < 0 &&
        window[static_cast<unsigned char>(s[right])] <=
            -required[static_cast<unsigned char>(s[right])]) {
      ++formed;
    }

    while (left <= right && formed == required_count) {
      if (static_cast<int>(right - left + 1) < min_len) {
        min_len = right - left + 1;
        min_left = left;
        min_right = right;
      }

      --window[static_cast<unsigned char>(s[left])];
      if (required[static_cast<unsigned char>(s[left])] < 0 &&
          window[static_cast<unsigned char>(s[left])] <
              -required[static_cast<unsigned char>(s[left])]) {
        --formed;
      }
      ++left;
    }
  }

  return min_len == INT_MAX ? ""
                            : std::string(s.substr(min_left, min_len));
}

/// @brief Minimum subarray length with sum >= target.
/// @param target Minimum sum required
/// @param nums Array of positive integers
/// @return Length of minimum subarray, 0 if impossible
/// @example MinSizeSubarraySum(7, {2,3,1,2,4,3}) -> 2 ([4,3])
/// @constraints Two-pointer expansion and contraction
/// @time O(n) @space O(1)
[[nodiscard]] int MinSizeSubarraySum(int target,
                                      const std::vector<int>& nums) noexcept {
  int left = 0;
  int window_sum = 0;
  int min_len = INT_MAX;

  for (size_t right = 0; right < nums.size(); ++right) {
    window_sum += nums[right];

    while (window_sum >= target) {
      min_len = std::min(min_len, static_cast<int>(right - left + 1));
      window_sum -= nums[left];
      ++left;
    }
  }

  return min_len == INT_MAX ? 0 : min_len;
}

// ============================================================================
// AT-MOST-K DISTINCT
// ============================================================================

/// @brief Helper: count subarrays with at most k distinct integers.
/// @param nums Array of integers
/// @param k Maximum distinct integers allowed
/// @return Count of subarrays with <= k distinct
static [[nodiscard]] int AtMostKDistinct(const std::vector<int>& nums,
                                          int k) noexcept {
  std::unordered_map<int, int> freq;
  int left = 0;
  int count = 0;

  for (size_t right = 0; right < nums.size(); ++right) {
    ++freq[nums[right]];

    while (freq.size() > static_cast<size_t>(k)) {
      --freq[nums[left]];
      if (freq[nums[left]] == 0) {
        freq.erase(nums[left]);
      }
      ++left;
    }

    count += right - left + 1;
  }
  return count;
}

/// @brief Subarrays with exactly k distinct integers.
/// @param nums Array of integers
/// @param k Exact count of distinct integers
/// @return Count of subarrays with exactly k distinct
/// @example SubarraysWithKDistinct({1,2,1,2,3}, 2) -> 7
/// @constraints Use at-most-k trick: exactly(k) = atMost(k) - atMost(k-1)
/// @time O(n) @space O(n)
[[nodiscard]] int SubarraysWithKDistinct(const std::vector<int>& nums,
                                          int k) noexcept {
  return AtMostKDistinct(nums, k) - AtMostKDistinct(nums, k - 1);
}

// ============================================================================
// SLIDING WINDOW MAXIMUM
// ============================================================================

/// @brief Maximum element in each sliding window.
/// @param nums Array of integers
/// @param k Window size
/// @return Vector of maximum values for each k-size window
/// @example MaxSlidingWindow({1,3,-1,-3,5,3,6,7}, 3) -> {3,3,5,5,6,7}
/// @constraints Monotonic deque stores indices; O(n) time
/// @time O(n) @space O(k)
/// Tricky: Deque maintains indices in decreasing value order; remove old
/// indices outside window; remove smaller values when new element comes
[[nodiscard]] std::vector<int>
MaxSlidingWindow(const std::vector<int>& nums, int k) noexcept {
  std::vector<int> result;
  if (nums.empty() || k <= 0) return result;

  std::deque<int> dq;

  for (size_t i = 0; i < nums.size(); ++i) {
    // Remove indices outside current window
    while (!dq.empty() && dq.front() <= static_cast<int>(i) - k) {
      dq.pop_front();
    }

    // Remove elements smaller than current element (maintain decreasing order)
    while (!dq.empty() && nums[dq.back()] <= nums[i]) {
      dq.pop_back();
    }

    dq.push_back(i);

    // Add to result when window is full
    if (i >= static_cast<size_t>(k) - 1) {
      result.emplace_back(nums[dq.front()]);
    }
  }
  return result;
}

}  // namespace sliding_window_playground

// ============================================================================
// TESTS
// ============================================================================

int main() {
  using namespace sliding_window_playground;

  std::cout << "=== Sliding Window Playground ===\n\n";

  std::cout << "MaxSumSubarraySizeK({1,3,-1,-3,5,3,6,7}, 3): ";
  {
    auto result = MaxSumSubarraySizeK({1, 3, -1, -3, 5, 3, 6, 7}, 3);
    std::cout << result << "\n";
  }

  std::cout << "FindAnagrams(\"cbaebabacd\", \"abc\"): ";
  {
    auto result = FindAnagrams("cbaebabacd", "abc");
    for (int idx : result) std::cout << idx << " ";
    std::cout << "\n";
  }

  std::cout << "ContainsNearbyDuplicate({99,99}, 2): ";
  {
    bool result = ContainsNearbyDuplicate({99, 99}, 2);
    std::cout << (result ? "true" : "false") << "\n";
  }

  std::cout << "LengthOfLongestSubstring(\"abcabcbb\"): ";
  {
    auto result = LengthOfLongestSubstring("abcabcbb");
    std::cout << result << "\n";
  }

  std::cout << "LongestSubstringKDistinct(\"eceba\", 2): ";
  {
    auto result = LongestSubstringKDistinct("eceba", 2);
    std::cout << result << "\n";
  }

  std::cout << "CharacterReplacement(\"ABAB\", 2): ";
  {
    auto result = CharacterReplacement("ABAB", 2);
    std::cout << result << "\n";
  }

  std::cout << "MinWindowSubstring(\"ADOBECODEBANC\", \"ABC\"): ";
  {
    auto result = MinWindowSubstring("ADOBECODEBANC", "ABC");
    std::cout << "\"" << result << "\"\n";
  }

  std::cout << "MinSizeSubarraySum(7, {2,3,1,2,4,3}): ";
  {
    auto result = MinSizeSubarraySum(7, {2, 3, 1, 2, 4, 3});
    std::cout << result << "\n";
  }

  std::cout << "SubarraysWithKDistinct({1,2,1,2,3}, 2): ";
  {
    auto result = SubarraysWithKDistinct({1, 2, 1, 2, 3}, 2);
    std::cout << result << "\n";
  }

  std::cout << "MaxSlidingWindow({1,3,-1,-3,5,3,6,7}, 3): ";
  {
    auto result = MaxSlidingWindow({1, 3, -1, -3, 5, 3, 6, 7}, 3);
    for (int x : result) std::cout << x << " ";
    std::cout << "\n";
  }

  return 0;
}
