import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Set;

/**
 * Hash Table Problems - Complete Guide for Interview Preparation.
 *
 * <p>Core Concepts:
 * <ul>
 *   <li>HashMap O(1) average get/put, O(n) worst case (hash collision).</li>
 *   <li>Use getOrDefault(key, defaultValue) and
 *       computeIfAbsent(key, k -> new ArrayList()).</li>
 *   <li>LinkedHashMap for insertion-order iteration (useful for LRU Cache).</li>
 *   <li>HashSet for O(1) contains checks, unordered set.</li>
 *   <li>Always check containsKey before get() or use getOrDefault().</li>
 * </ul>
 *
 * <p>Tricky Parts:
 * <ul>
 *   <li>Hash collisions resolved via chaining (linked list) in Java HashMap.</li>
 *   <li>Initial capacity must be power of 2 for efficient rehashing.</li>
 *   <li>equals() and hashCode() contract: if a.equals(b), then a.hashCode() ==
 *       b.hashCode().</li>
 *   <li>LinkedHashMap.removeEldestEntry() for automatic LRU eviction.</li>
 * </ul>
 *
 * @author Google Senior SWE Interview Playground
 */
public class HashTable {

  /**
   * Two Sum: find two numbers that add up to target.
   *
   * <p>LeetCode 1 - Two Sum (Easy)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(n)
   *
   * @param nums input array
   * @param target sum to find
   * @return [index1, index2] or empty array if not found
   * @throws IllegalArgumentException if nums is null
   */
  public static int[] twoSum(int[] nums, int target) {
    if (nums == null || nums.length < 2) {
      throw new IllegalArgumentException("Input array must contain at least 2 elements");
    }

    Map<Integer, Integer> seen = new HashMap<>();

    for (int i = 0; i < nums.length; i++) {
      int complement = target - nums[i];

      if (seen.containsKey(complement)) {
        return new int[]{seen.get(complement), i};
      }

      seen.put(nums[i], i);
    }

    return new int[]{};
  }

  /**
   * Two Sum All Pairs: find all unique pairs that sum to target.
   *
   * <p>Time Complexity: O(n), Space Complexity: O(n)
   *
   * @param nums input array
   * @param target sum to find
   * @return list of unique pairs [a, b] where a + b = target
   * @throws IllegalArgumentException if nums is null
   */
  public static List<List<Integer>> twoSumAllPairs(int[] nums, int target) {
    if (nums == null) {
      throw new IllegalArgumentException("Input array cannot be null");
    }

    Set<List<Integer>> pairs = new HashSet<>();
    Set<Integer> seen = new HashSet<>();

    for (int num : nums) {
      int complement = target - num;

      if (seen.contains(complement)) {
        List<Integer> pair = new ArrayList<>();
        pair.add(Math.min(num, complement));
        pair.add(Math.max(num, complement));
        pairs.add(pair);
      }

      seen.add(num);
    }

    return new ArrayList<>(pairs);
  }

  /**
   * Top K Frequent Elements.
   *
   * <p>LeetCode 347 - Top K Frequent Elements (Medium)
   *
   * <p>Time Complexity: O(n log k), Space Complexity: O(n)
   *
   * @param nums input array
   * @param k number of top frequent elements
   * @return list of k most frequent elements
   * @throws IllegalArgumentException if nums is null or k is invalid
   */
  public static List<Integer> topKFrequent(int[] nums, int k) {
    if (nums == null || k < 1 || k > nums.length) {
      throw new IllegalArgumentException("Invalid input array or k value");
    }

    Map<Integer, Integer> freqMap = new HashMap<>();
    for (int num : nums) {
      freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
    }

    PriorityQueue<Integer> minHeap = new PriorityQueue<>((a, b) ->
        Integer.compare(freqMap.get(a), freqMap.get(b)));

    for (int num : freqMap.keySet()) {
      minHeap.offer(num);
      if (minHeap.size() > k) {
        minHeap.poll();
      }
    }

    return new ArrayList<>(minHeap);
  }

  /**
   * First Unique Character in String.
   *
   * <p>LeetCode 387 - First Unique Character in a String (Easy)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(1) (fixed 26-char alphabet)
   *
   * @param s input string
   * @return index of first unique character or -1 if none
   * @throws IllegalArgumentException if s is null
   */
  public static int firstUniqueChar(String s) {
    if (s == null) {
      throw new IllegalArgumentException("Input string cannot be null");
    }

    Map<Character, Integer> charCount = new HashMap<>();

    for (char c : s.toCharArray()) {
      charCount.put(c, charCount.getOrDefault(c, 0) + 1);
    }

    for (int i = 0; i < s.length(); i++) {
      if (charCount.get(s.charAt(i)) == 1) {
        return i;
      }
    }

    return -1;
  }

  /**
   * Group Anagrams using HashMap.
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
  public static List<List<String>> groupAnagrams(String[] strs) {
    if (strs == null) {
      throw new IllegalArgumentException("Input array cannot be null");
    }

    Map<String, List<String>> anagramMap = new HashMap<>();

    for (String word : strs) {
      char[] chars = word.toCharArray();
      java.util.Arrays.sort(chars);
      String key = new String(chars);

      anagramMap.computeIfAbsent(key, k -> new ArrayList<>()).add(word);
    }

    return new ArrayList<>(anagramMap.values());
  }

  /**
   * Group Shifted Strings.
   *
   * <p>LeetCode 249 - Group Shifted Strings (Medium)
   *
   * <p>Time Complexity: O(n * k) where k is max string length
   *
   * <p>Space Complexity: O(n)
   *
   * @param strings array of strings
   * @return list of shifted string groups
   * @throws IllegalArgumentException if strings is null
   */
  public static List<List<String>> groupShiftedStrings(String[] strings) {
    if (strings == null) {
      throw new IllegalArgumentException("Input array cannot be null");
    }

    Map<String, List<String>> shiftMap = new HashMap<>();

    for (String str : strings) {
      String key = getShiftKey(str);
      shiftMap.computeIfAbsent(key, k -> new ArrayList<>()).add(str);
    }

    return new ArrayList<>(shiftMap.values());
  }

  /**
   * Helper to compute shift pattern for a string.
   *
   * @param str input string
   * @return shift pattern key
   */
  private static String getShiftKey(String str) {
    StringBuilder key = new StringBuilder();

    for (int i = 1; i < str.length(); i++) {
      int shift = (str.charAt(i) - str.charAt(i - 1) + 26) % 26;
      key.append(shift).append(",");
    }

    return key.toString();
  }

  /**
   * Longest Consecutive Sequence using HashSet.
   *
   * <p>LeetCode 128 - Longest Consecutive Sequence (Medium)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(n)
   *
   * <p>Pattern: Use set for O(1) lookups, find sequence streaks.
   *
   * @param nums input array
   * @return length of longest consecutive elements sequence
   * @throws IllegalArgumentException if nums is null
   */
  public static int longestConsecutiveSequence(int[] nums) {
    if (nums == null) {
      throw new IllegalArgumentException("Input array cannot be null");
    }

    if (nums.length == 0) {
      return 0;
    }

    Set<Integer> numSet = new HashSet<>();
    for (int num : nums) {
      numSet.add(num);
    }

    int longestStreak = 0;

    for (int num : numSet) {
      if (!numSet.contains(num - 1)) {
        int currentNum = num;
        int currentStreak = 1;

        while (numSet.contains(currentNum + 1)) {
          currentNum++;
          currentStreak++;
        }

        longestStreak = Math.max(longestStreak, currentStreak);
      }
    }

    return longestStreak;
  }

  /**
   * LRU (Least Recently Used) Cache implementation.
   *
   * <p>LeetCode 146 - LRU Cache (Medium)
   *
   * <p>Time Complexity: get/put O(1), Space Complexity: O(capacity)
   */
  public static class LRUCache extends LinkedHashMap<Integer, Integer> {
    private final int capacity;

    /**
     * Constructor for LRU Cache.
     *
     * @param capacity maximum number of items in cache
     * @throws IllegalArgumentException if capacity is invalid
     */
    public LRUCache(int capacity) {
      super(capacity, 0.75f, true);
      if (capacity <= 0) {
        throw new IllegalArgumentException("Capacity must be positive");
      }
      this.capacity = capacity;
    }

    /**
     * Override to remove eldest entry when capacity exceeded.
     *
     * @return true if eldest entry should be removed
     */
    @Override
    protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
      return size() > this.capacity;
    }

    /**
     * Get value for key, return -1 if not found.
     *
     * @param key lookup key
     * @return value or -1
     */
    public int get(int key) {
      return super.getOrDefault(key, -1);
    }

    /**
     * Put key-value pair in cache.
     *
     * @param key cache key
     * @param value cache value
     */
    public void put(int key, int value) {
      super.put(key, value);
    }
  }

  /**
   * Two Sum Data Structure: Add and Find operations.
   *
   * <p>LeetCode 170 - Two Sum III - Data structure design (Easy)
   *
   * <p>Time Complexity: add O(1), find O(n)
   *
   * <p>Space Complexity: O(n)
   */
  public static class TwoSumDataStructure {
    private final Map<Integer, Integer> numCount;

    /**
     * Constructor for TwoSumDataStructure.
     */
    public TwoSumDataStructure() {
      this.numCount = new HashMap<>();
    }

    /**
     * Add number to data structure.
     *
     * @param number number to add
     */
    public void add(int number) {
      this.numCount.put(number, this.numCount.getOrDefault(number, 0) + 1);
    }

    /**
     * Find if two numbers exist that sum to target value.
     *
     * @param value target sum
     * @return true if two numbers exist that sum to value
     */
    public boolean find(int value) {
      for (int num : this.numCount.keySet()) {
        int complement = value - num;

        if (complement == num) {
          if (this.numCount.get(num) > 1) {
            return true;
          }
        } else if (this.numCount.containsKey(complement)) {
          return true;
        }
      }

      return false;
    }
  }

  /**
   * Main method with comprehensive test cases.
   *
   * @param args command-line arguments (unused)
   */
  public static void main(String[] args) {
    System.out.println("=== Hash Table Problems ===\n");

    // Test twoSum
    System.out.println("1. Two Sum:");
    int[] nums1 = {2, 7, 11, 15};
    int[] twoSumResult = twoSum(nums1, 9);
    System.out.println("  Input: [2,7,11,15], target=9");
    System.out.println("  Output: [" + twoSumResult[0] + "," + twoSumResult[1] + "]\n");

    // Test twoSumAllPairs
    System.out.println("2. Two Sum All Pairs:");
    int[] nums2 = {1, 5, 7, -1};
    List<List<Integer>> allPairs = twoSumAllPairs(nums2, 6);
    System.out.println("  Input: [1,5,7,-1], target=6");
    System.out.println("  Output: " + allPairs + "\n");

    // Test topKFrequent
    System.out.println("3. Top K Frequent Elements:");
    int[] nums3 = {1, 1, 1, 2, 2, 3};
    List<Integer> topK = topKFrequent(nums3, 2);
    System.out.println("  Input: [1,1,1,2,2,3], k=2");
    System.out.println("  Output: " + topK + "\n");

    // Test firstUniqueChar
    System.out.println("4. First Unique Character:");
    int firstUnique = firstUniqueChar("loveleetcode");
    System.out.println("  Input: \"loveleetcode\"");
    System.out.println("  Output: " + firstUnique + "\n");

    // Test groupAnagrams
    System.out.println("5. Group Anagrams:");
    String[] strs = {"eat", "tea", "ate", "bat"};
    List<List<String>> anagrams = groupAnagrams(strs);
    System.out.println("  Input: [\"eat\",\"tea\",\"ate\",\"bat\"]");
    System.out.println("  Output: " + anagrams + "\n");

    // Test longestConsecutiveSequence
    System.out.println("6. Longest Consecutive Sequence:");
    int[] nums4 = {100, 4, 200, 1, 3, 2};
    int longest = longestConsecutiveSequence(nums4);
    System.out.println("  Input: [100,4,200,1,3,2]");
    System.out.println("  Output: " + longest + "\n");

    // Test LRUCache
    System.out.println("7. LRU Cache:");
    LRUCache cache = new LRUCache(2);
    cache.put(1, 1);
    cache.put(2, 2);
    System.out.println("  put(1,1), put(2,2)");
    System.out.println("  get(1) = " + cache.get(1));
    cache.put(3, 3);
    System.out.println("  put(3,3), get(2) = " + cache.get(2) + " (evicted)\n");

    // Test TwoSumDataStructure
    System.out.println("8. Two Sum Data Structure:");
    TwoSumDataStructure twoSumDS = new TwoSumDataStructure();
    twoSumDS.add(1);
    twoSumDS.add(5);
    twoSumDS.add(7);
    System.out.println("  add(1), add(5), add(7)");
    System.out.println("  find(6) = " + twoSumDS.find(6));
    System.out.println("  find(100) = " + twoSumDS.find(100) + "\n");
  }
}
