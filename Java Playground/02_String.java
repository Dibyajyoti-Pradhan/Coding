import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Stack;

/**
 * String Problems - Complete Guide for Interview Preparation.
 *
 * <p>Core Concepts:
 * <ul>
 *   <li>Java String immutability — always use StringBuilder for concatenation in loops.</li>
 *   <li>s.charAt(i) not s[i]; String comparison: equals() not ==.</li>
 *   <li>int[26] for lowercase letter frequencies (faster than HashMap).</li>
 *   <li>Character.isLetterOrDigit(), Character.toLowerCase().</li>
 *   <li>Two-pointer technique for palindromes and validation.</li>
 * </ul>
 *
 * <p>Tricky Parts:
 * <ul>
 *   <li>String.substring(start, end) — end is exclusive.</li>
 *   <li>Anagrams: same character frequencies, not same order.</li>
 *   <li>Palindrome check: ignore non-alphanumeric and case-insensitive.</li>
 *   <li>KMP failure function prevents redundant character comparisons.</li>
 * </ul>
 *
 * @author Google Senior SWE Interview Playground
 */
public class String {

  private static final int ALPHABET_SIZE = 26;

  /**
   * Check if two strings are anagrams.
   *
   * <p>LeetCode 242 - Valid Anagram (Easy)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(1) (fixed 26-char alphabet)
   *
   * @param s first string
   * @param t second string
   * @return true if t is an anagram of s
   * @throws IllegalArgumentException if either string is null
   */
  public static boolean isAnagram(java.lang.String s, java.lang.String t) {
    if (s == null || t == null) {
      throw new IllegalArgumentException("Input strings cannot be null");
    }

    if (s.length() != t.length()) {
      return false;
    }

    int[] charCount = new int[ALPHABET_SIZE];
    for (int i = 0; i < s.length(); i++) {
      charCount[s.charAt(i) - 'a']++;
      charCount[t.charAt(i) - 'a']--;
    }

    for (int count : charCount) {
      if (count != 0) {
        return false;
      }
    }

    return true;
  }

  /**
   * Group anagrams together.
   *
   * <p>LeetCode 49 - Group Anagrams (Medium)
   *
   * <p>Time Complexity: O(n * k log k) where k is max string length
   *
   * <p>Space Complexity: O(n * k)
   *
   * @param strs array of strings
   * @return list of anagram groups
   * @throws IllegalArgumentException if strs is null
   */
  public static List<List<java.lang.String>> groupAnagrams(java.lang.String[] strs) {
    if (strs == null) {
      throw new IllegalArgumentException("Input array cannot be null");
    }

    Map<java.lang.String, List<java.lang.String>> anagramMap = new HashMap<>();

    for (java.lang.String word : strs) {
      char[] chars = word.toCharArray();
      Arrays.sort(chars);
      java.lang.String key = new java.lang.String(chars);

      anagramMap.computeIfAbsent(key, k -> new ArrayList<>()).add(word);
    }

    return new ArrayList<>(anagramMap.values());
  }

  /**
   * Find the length of longest substring without repeating characters.
   *
   * <p>LeetCode 3 - Longest Substring Without Repeating Characters (Medium)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(min(n, 26))
   *
   * @param s input string
   * @return length of longest substring without repeating chars
   * @throws IllegalArgumentException if s is null
   */
  public static int lengthOfLongestSubstring(java.lang.String s) {
    if (s == null) {
      throw new IllegalArgumentException("Input string cannot be null");
    }

    Map<Character, Integer> lastSeen = new HashMap<>();
    int maxLength = 0;
    int left = 0;

    for (int right = 0; right < s.length(); right++) {
      char rightChar = s.charAt(right);

      if (lastSeen.containsKey(rightChar)) {
        left = Math.max(left, lastSeen.get(rightChar) + 1);
      }

      lastSeen.put(rightChar, right);
      maxLength = Math.max(maxLength, right - left + 1);
    }

    return maxLength;
  }

  /**
   * Minimum window substring containing all target characters.
   *
   * <p>LeetCode 76 - Minimum Window Substring (Hard)
   *
   * <p>Time Complexity: O(s + t), Space Complexity: O(1) (fixed ASCII)
   *
   * @param s haystack string
   * @param t needle string
   * @return minimum window substring or empty string if not found
   * @throws IllegalArgumentException if either string is null
   */
  public static java.lang.String minWindowSubstring(java.lang.String s,
      java.lang.String t) {
    if (s == null || t == null) {
      throw new IllegalArgumentException("Input strings cannot be null");
    }

    if (t.length() > s.length()) {
      return "";
    }

    Map<Character, Integer> targetCount = new HashMap<>();
    for (char c : t.toCharArray()) {
      targetCount.put(c, targetCount.getOrDefault(c, 0) + 1);
    }

    Map<Character, Integer> windowCount = new HashMap<>();
    int required = targetCount.size();
    int formed = 0;
    int left = 0;
    int minLength = Integer.MAX_VALUE;
    int minStart = 0;

    for (int right = 0; right < s.length(); right++) {
      char rightChar = s.charAt(right);
      windowCount.put(rightChar, windowCount.getOrDefault(rightChar, 0) + 1);

      if (targetCount.containsKey(rightChar) &&
          windowCount.get(rightChar).equals(targetCount.get(rightChar))) {
        formed++;
      }

      while (formed == required && left <= right) {
        if (right - left + 1 < minLength) {
          minLength = right - left + 1;
          minStart = left;
        }

        char leftChar = s.charAt(left);
        windowCount.put(leftChar, windowCount.get(leftChar) - 1);
        if (targetCount.containsKey(leftChar) &&
            windowCount.get(leftChar) < targetCount.get(leftChar)) {
          formed--;
        }

        left++;
      }
    }

    return minLength == Integer.MAX_VALUE ? "" : s.substring(minStart,
        minStart + minLength);
  }

  /**
   * Check if string is a valid palindrome (ignoring non-alphanumeric).
   *
   * <p>LeetCode 125 - Valid Palindrome (Easy)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(1)
   *
   * @param s input string
   * @return true if s is a valid palindrome
   * @throws IllegalArgumentException if s is null
   */
  public static boolean isPalindrome(java.lang.String s) {
    if (s == null) {
      throw new IllegalArgumentException("Input string cannot be null");
    }

    int left = 0;
    int right = s.length() - 1;

    while (left < right) {
      while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
        left++;
      }

      while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
        right--;
      }

      char leftChar = Character.toLowerCase(s.charAt(left));
      char rightChar = Character.toLowerCase(s.charAt(right));

      if (leftChar != rightChar) {
        return false;
      }

      left++;
      right--;
    }

    return true;
  }

  /**
   * Find longest palindromic substring using expand-around-center.
   *
   * <p>LeetCode 5 - Longest Palindromic Substring (Medium)
   *
   * <p>Time Complexity: O(n^2), Space Complexity: O(1)
   *
   * <p>Pattern: For each center, expand outward. Centers can be char (odd) or between
   * chars (even).
   *
   * @param s input string
   * @return longest palindromic substring
   * @throws IllegalArgumentException if s is null
   */
  public static java.lang.String longestPalindromicSubstring(java.lang.String s) {
    if (s == null) {
      throw new IllegalArgumentException("Input string cannot be null");
    }

    if (s.length() < 2) {
      return s;
    }

    int maxStart = 0;
    int maxLength = 1;

    for (int i = 0; i < s.length(); i++) {
      int len1 = expandAroundCenter(s, i, i);
      int len2 = expandAroundCenter(s, i, i + 1);

      int len = Math.max(len1, len2);
      if (len > maxLength) {
        maxLength = len;
        maxStart = i - (len - 1) / 2;
      }
    }

    return s.substring(maxStart, maxStart + maxLength);
  }

  /**
   * Helper to expand around center for palindrome detection.
   *
   * @param s input string
   * @param left left center pointer
   * @param right right center pointer
   * @return length of palindrome centered at left/right
   */
  private static int expandAroundCenter(java.lang.String s, int left, int right) {
    while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
      left--;
      right++;
    }

    return right - left - 1;
  }

  /**
   * Check if string contains only valid parentheses.
   *
   * <p>LeetCode 20 - Valid Parentheses (Easy)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(n)
   *
   * @param s string containing parentheses
   * @return true if all parentheses are valid
   * @throws IllegalArgumentException if s is null
   */
  public static boolean isValid(java.lang.String s) {
    if (s == null) {
      throw new IllegalArgumentException("Input string cannot be null");
    }

    Stack<Character> stack = new Stack<>();
    Map<Character, Character> pairs = new HashMap<>();
    pairs.put(')', '(');
    pairs.put('}', '{');
    pairs.put(']', '[');

    for (char c : s.toCharArray()) {
      if (pairs.containsValue(c)) {
        stack.push(c);
      } else if (pairs.containsKey(c)) {
        if (stack.isEmpty() || stack.pop() != pairs.get(c)) {
          return false;
        }
      }
    }

    return stack.isEmpty();
  }

  /**
   * Reverse words in string.
   *
   * <p>LeetCode 151 - Reverse Words in a String (Medium)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(n)
   *
   * @param s input string with words separated by spaces
   * @return string with words in reverse order
   * @throws IllegalArgumentException if s is null
   */
  public static java.lang.String reverseWords(java.lang.String s) {
    if (s == null) {
      throw new IllegalArgumentException("Input string cannot be null");
    }

    java.lang.String[] words = s.trim().split("\\s+");
    Collections.reverse(Arrays.asList(words));

    return java.lang.String.join(" ", words);
  }

  /**
   * Encode string using run-length encoding.
   *
   * <p>Time Complexity: O(n), Space Complexity: O(1) or O(n) for result
   *
   * @param s input string
   * @return encoded string
   * @throws IllegalArgumentException if s is null
   */
  public static java.lang.String encodeString(java.lang.String s) {
    if (s == null) {
      throw new IllegalArgumentException("Input string cannot be null");
    }

    if (s.length() == 0) {
      return "";
    }

    StringBuilder encoded = new StringBuilder();
    int count = 1;

    for (int i = 1; i <= s.length(); i++) {
      if (i < s.length() && s.charAt(i) == s.charAt(i - 1)) {
        count++;
      } else {
        encoded.append(count).append(s.charAt(i - 1));
        count = 1;
      }
    }

    return encoded.toString();
  }

  /**
   * Decode run-length encoded string.
   *
   * <p>Time Complexity: O(n), Space Complexity: O(n)
   *
   * @param s encoded string
   * @return decoded string
   * @throws IllegalArgumentException if s is null
   */
  public static java.lang.String decodeString(java.lang.String s) {
    if (s == null) {
      throw new IllegalArgumentException("Input string cannot be null");
    }

    StringBuilder decoded = new StringBuilder();
    int i = 0;

    while (i < s.length()) {
      StringBuilder count = new StringBuilder();

      while (i < s.length() && Character.isDigit(s.charAt(i))) {
        count.append(s.charAt(i));
        i++;
      }

      int freq = count.length() > 0 ? Integer.parseInt(count.toString()) : 1;
      char c = s.charAt(i);

      for (int j = 0; j < freq; j++) {
        decoded.append(c);
      }

      i++;
    }

    return decoded.toString();
  }

  /**
   * KMP string matching: find first occurrence of pattern in text.
   *
   * <p>LeetCode 28 - Implement strStr() (Easy)
   *
   * <p>Time Complexity: O(m + n) where m is needle, n is haystack
   *
   * <p>Space Complexity: O(m) for failure function
   *
   * @param haystack text to search in
   * @param needle pattern to find
   * @return index of first occurrence or -1 if not found
   * @throws IllegalArgumentException if either argument is null
   */
  public static int strStr(java.lang.String haystack, java.lang.String needle) {
    if (haystack == null || needle == null) {
      throw new IllegalArgumentException("Input strings cannot be null");
    }

    if (needle.length() == 0) {
      return 0;
    }

    if (needle.length() > haystack.length()) {
      return -1;
    }

    int[] failureFunction = buildFailureFunction(needle);
    int needleIdx = 0;

    for (int haystackIdx = 0; haystackIdx < haystack.length(); haystackIdx++) {
      while (needleIdx > 0 && haystack.charAt(haystackIdx) !=
          needle.charAt(needleIdx)) {
        needleIdx = failureFunction[needleIdx - 1];
      }

      if (haystack.charAt(haystackIdx) == needle.charAt(needleIdx)) {
        needleIdx++;
      }

      if (needleIdx == needle.length()) {
        return haystackIdx - needle.length() + 1;
      }
    }

    return -1;
  }

  /**
   * Build KMP failure function (also called prefix function).
   *
   * @param pattern input pattern
   * @return failure function array
   */
  private static int[] buildFailureFunction(java.lang.String pattern) {
    int[] failure = new int[pattern.length()];
    int j = 0;

    for (int i = 1; i < pattern.length(); i++) {
      while (j > 0 && pattern.charAt(i) != pattern.charAt(j)) {
        j = failure[j - 1];
      }

      if (pattern.charAt(i) == pattern.charAt(j)) {
        j++;
      }

      failure[i] = j;
    }

    return failure;
  }

  /**
   * Main method with comprehensive test cases.
   *
   * @param args command-line arguments (unused)
   */
  public static void main(java.lang.String[] args) {
    System.out.println("=== String Problems ===\n");

    // Test isAnagram
    System.out.println("1. Valid Anagram:");
    boolean anagram = isAnagram("anagram", "nagaram");
    System.out.println("  Input: s=\"anagram\", t=\"nagaram\"");
    System.out.println("  Output: " + anagram + "\n");

    // Test groupAnagrams
    System.out.println("2. Group Anagrams:");
    java.lang.String[] strs = {"eat", "tea", "ate", "bat", "tab"};
    List<List<java.lang.String>> groups = groupAnagrams(strs);
    System.out.println("  Input: [\"eat\",\"tea\",\"ate\",\"bat\",\"tab\"]");
    System.out.println("  Output: " + groups + "\n");

    // Test lengthOfLongestSubstring
    System.out.println("3. Longest Substring Without Repeating Characters:");
    int longLen = lengthOfLongestSubstring("abcabcbb");
    System.out.println("  Input: \"abcabcbb\"");
    System.out.println("  Output: " + longLen + "\n");

    // Test isPalindrome
    System.out.println("4. Valid Palindrome:");
    boolean palindrome = isPalindrome("A man, a plan, a canal: Panama");
    System.out.println("  Input: \"A man, a plan, a canal: Panama\"");
    System.out.println("  Output: " + palindrome + "\n");

    // Test longestPalindromicSubstring
    System.out.println("5. Longest Palindromic Substring:");
    java.lang.String longestPal = longestPalindromicSubstring("babad");
    System.out.println("  Input: \"babad\"");
    System.out.println("  Output: \"" + longestPal + "\"\n");

    // Test isValid
    System.out.println("6. Valid Parentheses:");
    boolean valid = isValid("()[]{}");
    System.out.println("  Input: \"()[]{}\"");
    System.out.println("  Output: " + valid + "\n");

    // Test reverseWords
    System.out.println("7. Reverse Words in String:");
    java.lang.String reversed = reverseWords("  the   quick   brown  fox  ");
    System.out.println("  Input: \"  the   quick   brown  fox  \"");
    System.out.println("  Output: \"" + reversed + "\"\n");

    // Test encode/decode
    System.out.println("8. Encode/Decode String:");
    java.lang.String encoded = encodeString("aaabbbccc");
    System.out.println("  Encode \"aaabbbccc\": \"" + encoded + "\"");
    java.lang.String decoded = decodeString(encoded);
    System.out.println("  Decode back: \"" + decoded + "\"\n");

    // Test strStr
    System.out.println("9. String Matching (KMP):");
    int strIdx = strStr("hello", "ll");
    System.out.println("  Input: haystack=\"hello\", needle=\"ll\"");
    System.out.println("  Output: " + strIdx + "\n");
  }
}
