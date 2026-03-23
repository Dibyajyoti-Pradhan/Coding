import java.util.ArrayList;
import java.util.Arrays;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Sliding Window Template & Techniques.
 *
 * <p>Sliding window maintains a contiguous subarray that satisfies a constraint.
 * Move right pointer to expand, left pointer to shrink.
 *
 * <p><b>FIXED SIZE:</b> Window always size k. Expand until full, then slide.
 * Invariant: window always contains exactly k elements.
 *
 * <p><b>VARIABLE - MAXIMUM:</b> Shrink only when constraint violated. Find longest
 * subarray/substring satisfying condition (e.g., longest substring without
 * repeating chars, max length with k distinct chars).
 *
 * <p><b>VARIABLE - MINIMUM:</b> Shrink as much as possible while still valid.
 * Find shortest subarray/substring satisfying condition (e.g., min window with
 * all target chars).
 *
 * <p><b>AT MOST K:</b> Use helper atMostK(k) - atMostK(k-1) pattern for exact k.
 *
 * <p><b>CHARACTER COUNTING:</b> Use int[128] (ASCII) for O(1) lookup vs HashMap.
 * Only use HashMap when needing arbitrary chars (Unicode).
 *
 * <p>Time: O(n) single pass. Space: O(1) for ASCII, O(k) for k distinct chars.
 */
public class SlidingWindow {

  /**
   * Max Sum Subarray of Size K (fixed window).
   *
   * @param nums input array
   * @param k window size
   * @return maximum sum of any contiguous subarray of size k
   * @throws NullPointerException if nums is null
   *
   *         <p>Time: O(n). Space: O(1).
   *
   *         <p>Fixed size window: expand to size k, then slide. On each move,
   *         subtract leftmost, add rightmost.
   */
  public static int maxSumSubarraySizeK(int[] nums, int k) {
    if (nums == null || nums.length < k || k <= 0) {
      return Integer.MIN_VALUE;
    }

    int windowSum = 0;
    // Calculate initial window sum
    for (int i = 0; i < k; i++) {
      windowSum += nums[i];
    }

    int maxSum = windowSum;

    // Slide the window
    for (int i = k; i < nums.length; i++) {
      windowSum = windowSum - nums[i - k] + nums[i];
      maxSum = Math.max(maxSum, windowSum);
    }

    return maxSum;
  }

  /**
   * Find All Anagrams (fixed window).
   *
   * @param s haystack string
   * @param p needle string (pattern to find anagrams of)
   * @return list of starting indices where anagrams of p occur in s
   * @throws NullPointerException if s or p is null
   *
   *         <p>LeetCode 438 (Medium). Time: O(n). Space: O(1) (max 26 chars).
   *
   *         <p>Fixed window size = p.length(). Compare char frequencies using
   *         int[26] array. Maintain count of matching frequencies.
   */
  public static List<Integer> findAnagrams(String s, String p) {
    List<Integer> result = new ArrayList<>();

    if (s == null || p == null || s.length() < p.length()) {
      return result;
    }

    int[] pCount = new int[26];
    int[] windowCount = new int[26];

    // Count chars in pattern
    for (char c : p.toCharArray()) {
      pCount[c - 'a']++;
    }

    int windowSize = p.length();

    for (int i = 0; i < s.length(); i++) {
      // Add right char
      windowCount[s.charAt(i) - 'a']++;

      // Remove left char (when window exceeds size)
      if (i >= windowSize) {
        windowCount[s.charAt(i - windowSize) - 'a']--;
      }

      // Check if window matches pattern
      if (i >= windowSize - 1 && Arrays.equals(pCount, windowCount)) {
        result.add(i - windowSize + 1);
      }
    }

    return result;
  }

  /**
   * Contains Duplicate Within Distance K (fixed window).
   *
   * @param nums input array
   * @param k maximum distance between duplicates
   * @return true if any value appears twice within distance k, false otherwise
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 219 (Easy). Time: O(n). Space: O(min(n, k)).
   *
   *         <p>Fixed window of size k. Use set to track elements in current
   *         window. If element already in set, found duplicate within distance.
   */
  public static boolean containsNearbyDuplicate(int[] nums, int k) {
    if (nums == null || k <= 0) {
      return false;
    }

    java.util.Set<Integer> window = new java.util.HashSet<>();

    for (int i = 0; i < nums.length; i++) {
      if (window.contains(nums[i])) {
        return true;
      }

      window.add(nums[i]);

      // Maintain window size <= k
      if (window.size() > k) {
        window.remove(nums[i - k]);
      }
    }

    return false;
  }

  /**
   * Longest Substring Without Repeating Characters.
   *
   * @param s input string
   * @return length of longest substring without repeating characters
   * @throws NullPointerException if s is null
   *
   *         <p>LeetCode 3 (Medium). Time: O(n). Space: O(min(n, 128)).
   *
   *         <p>Variable max window: expand right, shrink left only when constraint
   *         violated (duplicate char found). Track char positions for quick shrink.
   */
  public static int lengthOfLongestSubstring(String s) {
    if (s == null) {
      return 0;
    }

    int[] lastIndex = new int[128];
    Arrays.fill(lastIndex, -1);

    int left = 0;
    int maxLength = 0;

    for (int right = 0; right < s.length(); right++) {
      char c = s.charAt(right);

      // If char seen in current window, shrink left
      if (lastIndex[c] >= left) {
        left = lastIndex[c] + 1;
      }

      // Update last seen position
      lastIndex[c] = right;

      maxLength = Math.max(maxLength, right - left + 1);
    }

    return maxLength;
  }

  /**
   * Longest Substring With At Most K Distinct Characters.
   *
   * @param s input string
   * @param k maximum number of distinct characters allowed
   * @return length of longest substring with at most k distinct characters
   * @throws NullPointerException if s is null
   *
   *         <p>LeetCode 340 (Medium). Time: O(n). Space: O(k).
   *
   *         <p>Variable max window: expand right to add chars, shrink left when
   *         distinct count exceeds k. Track char frequencies.
   */
  public static int longestSubstringWithKDistinct(String s, int k) {
    if (s == null || k <= 0) {
      return 0;
    }

    int[] charCount = new int[128];
    int left = 0;
    int distinctCount = 0;
    int maxLength = 0;

    for (int right = 0; right < s.length(); right++) {
      char rightChar = s.charAt(right);

      if (charCount[rightChar] == 0) {
        distinctCount++;
      }
      charCount[rightChar]++;

      // Shrink window if too many distinct chars
      while (distinctCount > k) {
        char leftChar = s.charAt(left);
        charCount[leftChar]--;

        if (charCount[leftChar] == 0) {
          distinctCount--;
        }
        left++;
      }

      maxLength = Math.max(maxLength, right - left + 1);
    }

    return maxLength;
  }

  /**
   * Character Replacement (variable max with constraint on operations).
   *
   * @param s input string with uppercase letters
   * @param k maximum number of character replacements allowed
   * @return length of longest substring possible after at most k replacements
   * @throws NullPointerException if s is null
   *
   *         <p>LeetCode 424 (Medium). Time: O(n). Space: O(26).
   *
   *         <p>Insight: longest substring where (window_length - max_char_count)
   *         ≤ k. Expand right, shrink left only when constraint violated.
   */
  public static int characterReplacement(String s, int k) {
    if (s == null || k < 0) {
      return 0;
    }

    int[] charCount = new int[26];
    int left = 0;
    int maxCount = 0;
    int maxLength = 0;

    for (int right = 0; right < s.length(); right++) {
      charCount[s.charAt(right) - 'A']++;
      maxCount = Math.max(maxCount, charCount[s.charAt(right) - 'A']);

      // Window size - most frequent char = chars that need replacing
      int windowSize = right - left + 1;
      if (windowSize - maxCount > k) {
        charCount[s.charAt(left) - 'A']--;
        left++;
      }

      maxLength = Math.max(maxLength, right - left + 1);
    }

    return maxLength;
  }

  /**
   * Minimum Window Substring (variable min).
   *
   * @param s source string
   * @param t target string (chars to find)
   * @return shortest substring of s containing all chars in t, empty if
   *     impossible
   * @throws NullPointerException if s or t is null
   *
   *         <p>LeetCode 76 (Hard). Time: O(n + m). Space: O(1) (max 128 chars).
   *
   *         <p>Variable min window: expand right to satisfy constraint, shrink
   *         left as much as possible while maintaining constraint. Track required
   *         and formed char counts.
   */
  public static String minWindowSubstring(String s, String t) {
    if (s == null || t == null || s.length() < t.length()) {
      return "";
    }

    int[] required = new int[128];
    for (char c : t.toCharArray()) {
      required[c]++;
    }

    int left = 0;
    int formed = 0;
    int requiredLen = t.length();
    int minLength = Integer.MAX_VALUE;
    int minLeft = 0;

    int[] window = new int[128];

    for (int right = 0; right < s.length(); right++) {
      char rightChar = s.charAt(right);
      window[rightChar]++;

      // If this char is in t and we have enough of it
      if (required[rightChar] > 0 && window[rightChar] <= required[rightChar]) {
        formed++;
      }

      // Try to shrink window from left
      while (formed == requiredLen && left <= right) {
        char leftChar = s.charAt(left);

        // Update result if this window is smaller
        if (right - left + 1 < minLength) {
          minLength = right - left + 1;
          minLeft = left;
        }

        window[leftChar]--;

        if (required[leftChar] > 0 && window[leftChar] < required[leftChar]) {
          formed--;
        }

        left++;
      }
    }

    return minLength == Integer.MAX_VALUE ? "" :
        s.substring(minLeft, minLeft + minLength);
  }

  /**
   * Minimum Size Subarray Sum (variable min).
   *
   * @param target target sum to reach or exceed
   * @param nums positive integer array
   * @return length of minimum subarray with sum ≥ target, or 0 if impossible
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 209 (Medium). Time: O(n). Space: O(1).
   *
   *         <p>Expand right to accumulate sum, shrink left when sum ≥ target
   *         to find minimum length.
   */
  public static int minSizeSubarraySum(int target, int[] nums) {
    if (nums == null || nums.length == 0) {
      return 0;
    }

    int left = 0;
    int sum = 0;
    int minLength = Integer.MAX_VALUE;

    for (int right = 0; right < nums.length; right++) {
      sum += nums[right];

      while (sum >= target) {
        minLength = Math.min(minLength, right - left + 1);
        sum -= nums[left];
        left++;
      }
    }

    return minLength == Integer.MAX_VALUE ? 0 : minLength;
  }

  /**
   * Subarrays With Exactly K Distinct Integers (at most k trick).
   *
   * @param nums input array
   * @param k exact number of distinct integers required
   * @return count of subarrays with exactly k distinct integers
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 992 (Hard). Time: O(n). Space: O(k).
   *
   *         <p>Key trick: atMostK(k) - atMostK(k-1) gives exactly k. Helper
   *         counts subarrays with at most k distinct.
   */
  public static int subarraysWithKDistinct(int[] nums, int k) {
    if (nums == null || k <= 0) {
      return 0;
    }

    return atMostKDistinct(nums, k) - atMostKDistinct(nums, k - 1);
  }

  /**
   * Helper: count subarrays with at most k distinct integers.
   *
   * @param nums input array
   * @param k at most k distinct integers
   * @return count of subarrays
   */
  private static int atMostKDistinct(int[] nums, int k) {
    if (k <= 0) {
      return 0;
    }

    Map<Integer, Integer> count = new HashMap<>();
    int left = 0;
    int result = 0;

    for (int right = 0; right < nums.length; right++) {
      count.put(nums[right], count.getOrDefault(nums[right], 0) + 1);

      while (count.size() > k) {
        count.put(nums[left], count.get(nums[left]) - 1);
        if (count.get(nums[left]) == 0) {
          count.remove(nums[left]);
        }
        left++;
      }

      // All subarrays ending at right with at most k distinct
      result += right - left + 1;
    }

    return result;
  }

  /**
   * Sliding Window Maximum (hard variant with deque).
   *
   * @param nums input array
   * @param k sliding window size
   * @return array where result[i] = max in window [i, i+k-1]
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 239 (Hard). Time: O(n). Space: O(k).
   *
   *         <p>Use ArrayDeque to maintain indices in decreasing order of values.
   *         Front always holds max in current window. Remove indices outside
   *         window, remove elements smaller than new right element.
   */
  public static int[] maxSlidingWindow(int[] nums, int k) {
    if (nums == null || nums.length == 0 || k <= 0 || k > nums.length) {
      return new int[0];
    }

    int[] result = new int[nums.length - k + 1];
    Deque<Integer> deque = new ArrayDeque<>();

    for (int i = 0; i < nums.length; i++) {
      // Remove indices outside current window
      while (!deque.isEmpty() && deque.peekFirst() < i - k + 1) {
        deque.pollFirst();
      }

      // Remove indices of elements smaller than current
      while (!deque.isEmpty() && nums[deque.peekLast()] < nums[i]) {
        deque.pollLast();
      }

      // Add current index
      deque.addLast(i);

      // Record max when window is full
      if (i >= k - 1) {
        result[i - k + 1] = nums[deque.peekFirst()];
      }
    }

    return result;
  }

  /**
   * Main method demonstrating all sliding window techniques.
   */
  public static void main(String[] args) {
    System.out.println("=== SLIDING WINDOW TECHNIQUES ===\n");

    // Max Sum Subarray Size K
    int[] nums1 = {1, 4, 2, 10, 2, 3, 1, 0, 20};
    System.out.println("Max Sum Subarray (k=4): " + maxSumSubarraySizeK(nums1, 4));

    // Find Anagrams
    String s1 = "cbaebabacd";
    String p1 = "abc";
    System.out.println("Find Anagrams: " + findAnagrams(s1, p1));

    // Contains Nearby Duplicate
    int[] nums2 = {99, 99};
    System.out.println("Contains Nearby Duplicate (k=2): " +
        containsNearbyDuplicate(nums2, 2));

    // Longest Substring Without Repeating
    String s2 = "abcabcbb";
    System.out.println("Longest Substring No Repeating: " +
        lengthOfLongestSubstring(s2));

    // Longest Substring With K Distinct
    String s3 = "ababc";
    System.out.println("Longest Substring (k=2 distinct): " +
        longestSubstringWithKDistinct(s3, 2));

    // Character Replacement
    String s4 = "ABAB";
    System.out.println("Character Replacement (k=2): " +
        characterReplacement(s4, 2));

    // Min Window Substring
    String s5 = "ADOBECODEBANC";
    String t5 = "ABC";
    System.out.println("Min Window Substring: " +
        minWindowSubstring(s5, t5));

    // Min Size Subarray Sum
    int[] nums3 = {1, 4, 4};
    System.out.println("Min Size Subarray Sum (target=4): " +
        minSizeSubarraySum(4, nums3));

    // Subarrays With K Distinct
    int[] nums4 = {1, 2, 1, 2, 3};
    System.out.println("Subarrays With K=2 Distinct: " +
        subarraysWithKDistinct(nums4, 2));

    // Max Sliding Window
    int[] nums5 = {1, 3, 1, 2, 0, 5};
    System.out.println("Max Sliding Window (k=3): " +
        Arrays.toString(maxSlidingWindow(nums5, 3)));
  }
}
