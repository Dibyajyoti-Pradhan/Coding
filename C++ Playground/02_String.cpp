/// @file 02_String.cpp
/// @brief Strings Playground — frequency, sliding window, palindrome,
///        parentheses, word reversal, KMP string matching.
///
/// STRINGS GUIDE:
/// - std::string is mutable in C++; use += not + in loops
/// - std::string_view is non-owning read-only view; use for parameters
/// - Concatenation in loops: += is O(1) amortised; + is O(n)
/// - s[i] accesses char; std::string::npos for not found (size_t, not int)
/// - int[26] frequency array faster than unordered_map for lowercase letters
/// - Sliding window with int[128] for ASCII counts (avoid map overhead)
/// - Palindrome expand-around: check (i, i) and (i, i+1) for odd/even lengths
/// - KMP failure function: LPS[i] = longest proper prefix that is suffix

#include <algorithm>
#include <cctype>
#include <climits>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

namespace string_playground {

/// @brief Check if two strings are anagrams (LC 242 Easy).
/// @param s First string.
/// @param t Second string.
/// @return true if t is anagram of s (same characters, different order).
///
/// Example: s="anagram", t="nagaram" → true; s="ab", t="bb" → false
/// Constraints: 1 ≤ s.length, t.length ≤ 5×10⁴; lowercase English.
/// Time: O(n), Space: O(1) (fixed 26 chars)
/// Tricky: Count frequency of each char; if all match, anagrams.
[[nodiscard]] bool IsAnagram(std::string_view s,
                              std::string_view t) noexcept {
  if (s.length() != t.length()) return false;
  int char_count[26] = {0};
  for (char c : s) ++char_count[c - 'a'];
  for (char c : t) {
    --char_count[c - 'a'];
    if (char_count[c - 'a'] < 0) return false;
  }
  return true;
}

/// @brief Group anagrams together (LC 49 Medium).
/// @param strs Vector of strings.
/// @return Vector of vectors, each subvector contains anagrams of each other.
///
/// Example: strs=["eat","tea","tan","ate","nat","bat"] →
///          [["eat","tea","ate"],["tan","nat"],["bat"]]
/// Constraints: 1 ≤ n ≤ 10⁴; 1 ≤ strs[i].length ≤ 100.
/// Time: O(n * k log k) where k = avg string length (sorting chars).
/// Space: O(n * k) for map
/// Tricky: Sort chars in each string to get canonical form as key.
[[nodiscard]] std::vector<std::vector<std::string>> GroupAnagrams(
    const std::vector<std::string>& strs) {
  std::unordered_map<std::string, std::vector<std::string>> anagram_groups;
  for (const auto& str : strs) {
    std::string sorted_str = str;
    std::sort(sorted_str.begin(), sorted_str.end());
    anagram_groups[sorted_str].emplace_back(str);
  }

  std::vector<std::vector<std::string>> result;
  for (auto& group : anagram_groups) {
    result.emplace_back(std::move(group.second));
  }
  return result;
}

/// @brief Length of longest substring without repeating characters (LC 3 Med).
/// @param s Input string.
/// @return Length of longest substring with all unique characters.
///
/// Example: s="abcabcbb" → 3 (substring "abc"); s="au" → 2; s="dvdf" → 3
/// Constraints: 0 ≤ s.length ≤ 5×10⁴; lowercase, uppercase, digits, symbols.
/// Time: O(n), Space: O(min(n, charset_size))
/// Tricky: Sliding window with char→last_seen_index map; when char repeats,
///         move left past previous occurrence.
[[nodiscard]] int LengthOfLongestSubstring(std::string_view s) noexcept {
  std::unordered_map<char, int> char_index;
  int left = 0, max_len = 0;

  for (int right = 0; right < static_cast<int>(s.length()); ++right) {
    if (char_index.count(s[right]) && char_index[s[right]] >= left) {
      left = char_index[s[right]] + 1;
    }
    char_index[s[right]] = right;
    max_len = std::max(max_len, right - left + 1);
  }
  return max_len;
}

/// @brief Minimum window substring: find smallest substring containing
///        all chars from t (LC 76 Hard).
/// @param s Haystack string.
/// @param t Pattern string.
/// @return Smallest substring of s containing all chars of t (with counts).
///
/// Example: s="ADOBECODEBANC", t="ABC" → "BANC"
/// Constraints: 1 ≤ s.length, t.length ≤ 10⁵; any chars.
/// Time: O(n + m) where n = s.len, m = t.len
/// Space: O(1) (fixed 128 ASCII chars)
/// Tricky: Track required char counts; expand right until window valid;
///         shrink left while valid to minimize size; track best window.
[[nodiscard]] std::string MinWindowSubstring(std::string_view s,
                                              std::string_view t) {
  if (s.length() < t.length()) return "";

  int required[128] = {0}, window[128] = {0};
  for (char c : t) ++required[static_cast<unsigned char>(c)];

  int left = 0, formed = 0, required_count = 0;
  for (int i = 0; i < 128; ++i) {
    if (required[i] > 0) ++required_count;
  }

  int result_len = INT_MAX, result_left = 0;

  for (int right = 0; right < static_cast<int>(s.length()); ++right) {
    unsigned char c = s[right];
    ++window[c];
    if (required[c] > 0 && window[c] == required[c]) {
      --formed;
    }

    while (formed == 0 && left <= right) {
      if (right - left + 1 < result_len) {
        result_len = right - left + 1;
        result_left = left;
      }

      unsigned char left_char = s[left];
      --window[left_char];
      if (required[left_char] > 0 && window[left_char] < required[left_char]) {
        ++formed;
      }
      ++left;
    }
  }

  return result_len == INT_MAX ? ""
                               : std::string(s.substr(result_left, result_len));
}

/// @brief Check if string is valid palindrome (alphanumeric only) (LC 125 Easy).
/// @param s Input string (may contain spaces, punctuation).
/// @return true if alphanumeric chars form palindrome.
///
/// Example: s="A man, a plan, a canal: Panama" → true
/// Constraints: 1 ≤ s.length ≤ 2×10⁵; any ASCII chars.
/// Time: O(n), Space: O(1)
/// Tricky: Skip non-alphanumeric; compare lowercase versions.
[[nodiscard]] bool IsPalindrome(std::string_view s) noexcept {
  int left = 0, right = static_cast<int>(s.length()) - 1;
  while (left < right) {
    while (left < right && !std::isalnum(s[left])) ++left;
    while (left < right && !std::isalnum(s[right])) --right;

    if (std::tolower(s[left]) != std::tolower(s[right])) {
      return false;
    }
    ++left;
    --right;
  }
  return true;
}

/// @brief Longest palindromic substring: expand around center (LC 5 Medium).
/// @param s Input string.
/// @return Longest substring that is palindrome.
///
/// Example: s="babad" → "bab" or "aba"; s="cbbd" → "bb"
/// Constraints: 1 ≤ s.length ≤ 1000; lowercase English.
/// Time: O(n²), Space: O(1)
/// Tricky: For each center (odd-length: single char; even-length: between
///         chars), expand outwards while chars match. Track longest.
[[nodiscard]] std::string LongestPalindromicSubstring(
    std::string_view s) {
  if (s.empty()) return "";

  auto expand_around_center = [&](int left, int right)
      -> std::pair<int, int> {
    while (left >= 0 && right < static_cast<int>(s.length()) &&
           s[left] == s[right]) {
      --left;
      ++right;
    }
    return {left + 1, right - 1};
  };

  int max_start = 0, max_end = 0;
  for (int i = 0; i < static_cast<int>(s.length()); ++i) {
    auto [start1, end1] = expand_around_center(i, i);
    if (end1 - start1 > max_end - max_start) {
      max_start = start1;
      max_end = end1;
    }

    if (i + 1 < static_cast<int>(s.length())) {
      auto [start2, end2] = expand_around_center(i, i + 1);
      if (end2 - start2 > max_end - max_start) {
        max_start = start2;
        max_end = end2;
      }
    }
  }
  return std::string(s.substr(max_start, max_end - max_start + 1));
}

/// @brief Valid parentheses: check balanced brackets (LC 20 Easy).
/// @param s String of parens/brackets/braces.
/// @return true if valid (balanced and properly ordered).
///
/// Example: s="()" → true; s="(){}" → true; s="({[]})" → true; s="({)}" →
///          false
/// Constraints: 1 ≤ s.length ≤ 10⁴; only '(){}[]'.
/// Time: O(n), Space: O(n) (stack)
/// Tricky: Push open chars; pop and match on close; stack empty at end.
[[nodiscard]] bool IsValid(std::string_view s) {
  std::string stack;
  for (char c : s) {
    if (c == '(' || c == '{' || c == '[') {
      stack.push_back(c);
    } else {
      if (stack.empty()) return false;
      char top = stack.back();
      if ((c == ')' && top == '(') || (c == '}' && top == '{') ||
          (c == ']' && top == '[')) {
        stack.pop_back();
      } else {
        return false;
      }
    }
  }
  return stack.empty();
}

/// @brief Reverse words in string: "the sky is blue" → "blue is sky the"
///        (LC 151 Medium).
/// @param s Input string with words separated by spaces.
/// @return String with words in reverse order, single spaces.
///
/// Example: s="  Hello World  " → "World Hello"; s="  Bob    Loves  Alice   "
///          → "Alice Loves Bob"
/// Constraints: 1 ≤ s.length ≤ 10⁴; multiple spaces OK.
/// Time: O(n), Space: O(1) or O(n) depending on string mutability.
/// Tricky: Skip leading/trailing spaces; split by spaces; build result
///         in reverse order.
[[nodiscard]] std::string ReverseWords(std::string_view s) {
  std::vector<std::string> words;
  std::string word;

  for (char c : s) {
    if (c != ' ') {
      word += c;
    } else if (!word.empty()) {
      words.emplace_back(std::move(word));
      word.clear();
    }
  }
  if (!word.empty()) {
    words.emplace_back(std::move(word));
  }

  std::string result;
  for (int i = static_cast<int>(words.size()) - 1; i >= 0; --i) {
    result += words[i];
    if (i > 0) result += " ";
  }
  return result;
}

/// @brief KMP string matching: find pattern in text (LC 28 Medium).
/// @param haystack Text string.
/// @param needle Pattern string.
/// @return Index of first occurrence of needle in haystack, or -1.
///
/// Example: haystack="sadbutsad", needle="sad" → 0
/// Constraints: 1 ≤ needle.length ≤ haystack.length ≤ 10⁴.
/// Time: O(n + m) where n = haystack.len, m = needle.len
/// Space: O(m) for LPS array
/// Tricky: Build LPS (Longest Proper Prefix that is Suffix) array for
///         pattern; use it to skip redundant comparisons.
[[nodiscard]] int StrStr(std::string_view haystack,
                          std::string_view needle) noexcept {
  if (needle.empty()) return 0;
  if (haystack.length() < needle.length()) return -1;

  std::vector<int> lps(needle.length(), 0);
  int j = 0;
  for (int i = 1; i < static_cast<int>(needle.length()); ++i) {
    while (j > 0 && needle[i] != needle[j]) {
      j = lps[j - 1];
    }
    if (needle[i] == needle[j]) {
      ++j;
    }
    lps[i] = j;
  }

  j = 0;
  for (int i = 0; i < static_cast<int>(haystack.length()); ++i) {
    while (j > 0 && haystack[i] != needle[j]) {
      j = lps[j - 1];
    }
    if (haystack[i] == needle[j]) {
      ++j;
    }
    if (j == static_cast<int>(needle.length())) {
      return i - static_cast<int>(needle.length()) + 1;
    }
  }
  return -1;
}

}  // namespace string_playground

int main() {
  std::cout << "=== STRING PLAYGROUND ===\n\n";

  bool is_anagram =
      string_playground::IsAnagram("anagram", "nagaram");
  std::cout << "IsAnagram(\"anagram\", \"nagaram\"): "
            << (is_anagram ? "true" : "false") << "\n";

  std::vector<std::string> words = {"eat", "tea", "tan", "ate", "nat", "bat"};
  auto grouped = string_playground::GroupAnagrams(words);
  std::cout << "GroupAnagrams(...): " << grouped.size() << " groups\n";

  int longest_substring =
      string_playground::LengthOfLongestSubstring("abcabcbb");
  std::cout << "LengthOfLongestSubstring(\"abcabcbb\"): " << longest_substring
            << "\n";

  std::string min_window =
      string_playground::MinWindowSubstring("ADOBECODEBANC", "ABC");
  std::cout << "MinWindowSubstring(\"ADOBECODEBANC\", \"ABC\"): \"" << min_window
            << "\"\n";

  bool is_palindrome =
      string_playground::IsPalindrome("A man, a plan, a canal: Panama");
  std::cout << "IsPalindrome(\"A man, a plan, a canal: Panama\"): "
            << (is_palindrome ? "true" : "false") << "\n";

  std::string longest_palin =
      string_playground::LongestPalindromicSubstring("babad");
  std::cout << "LongestPalindromicSubstring(\"babad\"): \"" << longest_palin
            << "\"\n";

  bool is_valid = string_playground::IsValid("()[]{}");
  std::cout << "IsValid(\"()[]{}\"); " << (is_valid ? "true" : "false")
            << "\n";

  std::string reversed =
      string_playground::ReverseWords("  Hello World  ");
  std::cout << "ReverseWords(\"  Hello World  \"): \"" << reversed << "\"\n";

  int str_index = string_playground::StrStr("sadbutsad", "sad");
  std::cout << "StrStr(\"sadbutsad\", \"sad\"): " << str_index << "\n";

  return 0;
}
