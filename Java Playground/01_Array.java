import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Arrays - Complete Guide for Interview Preparation.
 *
 * <p>Core Concepts:
 * <ul>
 *   <li>Arrays in Java are fixed-size, zero-indexed, stored in contiguous memory.</li>
 *   <li>Use int[] for primitives (no boxing overhead), Integer[] when generics needed.</li>
 *   <li>O(1) access by index, O(n) search/insert/delete.</li>
 *   <li>Dynamic arrays: use ArrayList for resizable behavior.</li>
 * </ul>
 *
 * <p>Tricky Parts (Java-specific):
 * <ul>
 *   <li>Integer overflow in mid: use left + (right - left) / 2, NOT (left + right) / 2.</li>
 *   <li>Arrays.sort() on int[] is dual-pivot quicksort O(n log n), not stable.</li>
 *   <li>int[] cannot be used with generics directly — use Integer[].</li>
 *   <li>Arrays.copyOfRange(arr, from, to) — to is exclusive.</li>
 *   <li>2D arrays: int[m][n] initializes to 0; rows are independent objects.</li>
 * </ul>
 *
 * @author Google Senior SWE Interview Playground
 */
public class Array {

  private static final int DEFAULT_MULTIPLIER = 1;

  /**
   * Two Sum using sorted array with opposite direction pointers.
   *
   * <p>LeetCode 167 - Two Sum II Input Array Is Sorted (Medium)
   *
   * @param numbers sorted array of integers
   * @param target sum to find
   * @return [index1, index2] (1-indexed) or empty array if not found
   * @throws IllegalArgumentException if numbers is null or target validation fails
   */
  public static int[] twoSumSorted(int[] numbers, int target) {
    if (numbers == null || numbers.length < 2) {
      throw new IllegalArgumentException("Input array must contain at least 2 elements");
    }

    int left = 0;
    int right = numbers.length - 1;

    while (left < right) {
      int sum = numbers[left] + numbers[right];
      if (sum == target) {
        return new int[]{left + 1, right + 1};
      } else if (sum < target) {
        left++;
      } else {
        right--;
      }
    }

    return new int[]{};
  }

  /**
   * Three Sum: find all unique triplets that sum to zero.
   *
   * <p>LeetCode 15 - 3Sum (Medium)
   *
   * @param nums array of integers
   * @return list of lists containing unique triplets
   * @throws IllegalArgumentException if nums is null
   */
  public static List<List<Integer>> threeSum(int[] nums) {
    if (nums == null) {
      throw new IllegalArgumentException("Input array cannot be null");
    }

    List<List<Integer>> result = new ArrayList<>();
    if (nums.length < 3) {
      return result;
    }

    Arrays.sort(nums);

    for (int i = 0; i < nums.length - 2; i++) {
      if (nums[i] > 0) {
        break;
      }

      if (i > 0 && nums[i] == nums[i - 1]) {
        continue;
      }

      int left = i + 1;
      int right = nums.length - 1;

      while (left < right) {
        int sum = nums[i] + nums[left] + nums[right];
        if (sum == 0) {
          result.add(Arrays.asList(nums[i], nums[left], nums[right]));
          while (left < right && nums[left] == nums[left + 1]) {
            left++;
          }
          while (left < right && nums[right] == nums[right - 1]) {
            right--;
          }
          left++;
          right--;
        } else if (sum < 0) {
          left++;
        } else {
          right--;
        }
      }
    }

    return result;
  }

  /**
   * Maximum sum of subarray of size k using sliding window.
   *
   * <p>Time Complexity: O(n), Space Complexity: O(1)
   *
   * @param arr input array
   * @param k window size
   * @return maximum sum of any contiguous subarray of size k
   * @throws IllegalArgumentException if arr is null or k is invalid
   */
  public static int maxSumSubarraySizeK(int[] arr, int k) {
    if (arr == null || k <= 0 || k > arr.length) {
      throw new IllegalArgumentException("Invalid array or window size");
    }

    int windowSum = 0;
    for (int i = 0; i < k; i++) {
      windowSum += arr[i];
    }

    int maxSum = windowSum;

    for (int i = k; i < arr.length; i++) {
      windowSum = windowSum - arr[i - k] + arr[i];
      maxSum = Math.max(maxSum, windowSum);
    }

    return maxSum;
  }

  /**
   * Longest substring with at most k distinct characters.
   *
   * <p>Time Complexity: O(n), Space Complexity: O(k)
   *
   * @param s input string
   * @param k maximum number of distinct characters
   * @return length of longest substring with at most k distinct chars
   * @throws IllegalArgumentException if s is null or k is negative
   */
  public static int longestSubstringWithKDistinct(String s, int k) {
    if (s == null || k < 0) {
      throw new IllegalArgumentException("Invalid string or k value");
    }

    Map<Character, Integer> charCount = new HashMap<>();
    int left = 0;
    int maxLength = 0;

    for (int right = 0; right < s.length(); right++) {
      char rightChar = s.charAt(right);
      charCount.put(rightChar, charCount.getOrDefault(rightChar, 0) + 1);

      while (charCount.size() > k) {
        char leftChar = s.charAt(left);
        charCount.put(leftChar, charCount.get(leftChar) - 1);
        if (charCount.get(leftChar) == 0) {
          charCount.remove(leftChar);
        }
        left++;
      }

      maxLength = Math.max(maxLength, right - left + 1);
    }

    return maxLength;
  }

  /**
   * Subarray sum equals k using prefix sum and hashmap.
   *
   * <p>LeetCode 560 - Subarray Sum Equals K (Medium)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(n)
   *
   * @param nums input array
   * @param k target sum
   * @return count of subarrays with sum equal to k
   * @throws IllegalArgumentException if nums is null
   */
  public static int subarraySumEqualsK(int[] nums, int k) {
    if (nums == null) {
      throw new IllegalArgumentException("Input array cannot be null");
    }

    Map<Integer, Integer> prefixSumCount = new HashMap<>();
    prefixSumCount.put(0, 1);
    int currentSum = 0;
    int count = 0;

    for (int num : nums) {
      currentSum += num;
      int targetPrefix = currentSum - k;

      if (prefixSumCount.containsKey(targetPrefix)) {
        count += prefixSumCount.get(targetPrefix);
      }

      prefixSumCount.put(currentSum, prefixSumCount.getOrDefault(currentSum, 0) + 1);
    }

    return count;
  }

  /**
   * Range sum query using prefix sum inner class.
   *
   * <p>LeetCode 303 - Range Sum Query - Immutable (Easy)
   */
  public static class RangeSum {
    private final int[] prefixSum;

    /**
     * Constructor to preprocess array for range sum queries.
     *
     * @param nums input array
     * @throws IllegalArgumentException if nums is null
     */
    public RangeSum(int[] nums) {
      if (nums == null) {
        throw new IllegalArgumentException("Input array cannot be null");
      }
      this.prefixSum = new int[nums.length + 1];
      for (int i = 0; i < nums.length; i++) {
        this.prefixSum[i + 1] = this.prefixSum[i] + nums[i];
      }
    }

    /**
     * Sum of elements from index left to right (inclusive).
     *
     * @param left left boundary (inclusive)
     * @param right right boundary (inclusive)
     * @return sum of elements in range [left, right]
     */
    public int sumRange(int left, int right) {
      return this.prefixSum[right + 1] - this.prefixSum[left];
    }
  }

  /**
   * Maximum subarray sum using Kadane's Algorithm.
   *
   * <p>LeetCode 53 - Maximum Subarray (Medium)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(1)
   *
   * @param nums input array
   * @return maximum sum of any contiguous subarray
   * @throws IllegalArgumentException if nums is null or empty
   */
  public static int maxSubarraySum(int[] nums) {
    if (nums == null || nums.length == 0) {
      throw new IllegalArgumentException("Input array cannot be null or empty");
    }

    int maxSoFar = nums[0];
    int maxEndingHere = nums[0];

    for (int i = 1; i < nums.length; i++) {
      maxEndingHere = Math.max(nums[i], maxEndingHere + nums[i]);
      maxSoFar = Math.max(maxSoFar, maxEndingHere);
    }

    return maxSoFar;
  }

  /**
   * Maximum product subarray using Kadane's with tracking max/min.
   *
   * <p>LeetCode 152 - Maximum Product Subarray (Medium)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(1)
   *
   * <p>Tricky: Negative numbers can flip max to min, so track both.
   *
   * @param nums input array
   * @return maximum product of any contiguous subarray
   * @throws IllegalArgumentException if nums is null or empty
   */
  public static int maxProductSubarray(int[] nums) {
    if (nums == null || nums.length == 0) {
      throw new IllegalArgumentException("Input array cannot be null or empty");
    }

    int maxSoFar = nums[0];
    int maxEndingHere = nums[0];
    int minEndingHere = nums[0];

    for (int i = 1; i < nums.length; i++) {
      int newMax = Math.max(nums[i], Math.max(maxEndingHere * nums[i],
          minEndingHere * nums[i]));
      int newMin = Math.min(nums[i], Math.min(maxEndingHere * nums[i],
          minEndingHere * nums[i]));

      maxEndingHere = newMax;
      minEndingHere = newMin;
      maxSoFar = Math.max(maxSoFar, maxEndingHere);
    }

    return maxSoFar;
  }

  /**
   * Dutch National Flag: partition array with 0, 1, 2 values.
   *
   * <p>LeetCode 75 - Sort Colors (Medium)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(1)
   *
   * @param nums array containing only 0, 1, 2 values
   * @throws IllegalArgumentException if nums is null
   */
  public static void sortColors(int[] nums) {
    if (nums == null) {
      throw new IllegalArgumentException("Input array cannot be null");
    }

    int low = 0;
    int mid = 0;
    int high = nums.length - 1;

    while (mid <= high) {
      if (nums[mid] == 0) {
        int temp = nums[low];
        nums[low] = nums[mid];
        nums[mid] = temp;
        low++;
        mid++;
      } else if (nums[mid] == 1) {
        mid++;
      } else {
        int temp = nums[mid];
        nums[mid] = nums[high];
        nums[high] = temp;
        high--;
      }
    }
  }

  /**
   * Merge intervals: combine overlapping intervals.
   *
   * <p>LeetCode 56 - Merge Intervals (Medium)
   *
   * <p>Time Complexity: O(n log n), Space Complexity: O(n)
   *
   * @param intervals array of [start, end] intervals
   * @return merged intervals list
   * @throws IllegalArgumentException if intervals is null
   */
  public static int[][] mergeIntervals(int[][] intervals) {
    if (intervals == null || intervals.length == 0) {
      throw new IllegalArgumentException("Input intervals array cannot be null or empty");
    }

    Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

    List<int[]> merged = new ArrayList<>();
    int[] currentInterval = intervals[0];

    for (int i = 1; i < intervals.length; i++) {
      if (intervals[i][0] <= currentInterval[1]) {
        currentInterval[1] = Math.max(currentInterval[1], intervals[i][1]);
      } else {
        merged.add(currentInterval);
        currentInterval = intervals[i];
      }
    }

    merged.add(currentInterval);
    return merged.toArray(new int[0][]);
  }

  /**
   * Binary search on sorted array.
   *
   * <p>Time Complexity: O(log n), Space Complexity: O(1)
   *
   * @param arr sorted array
   * @param target value to find
   * @return index of target or -1 if not found
   * @throws IllegalArgumentException if arr is null
   */
  public static int binarySearch(int[] arr, int target) {
    if (arr == null) {
      throw new IllegalArgumentException("Input array cannot be null");
    }

    int left = 0;
    int right = arr.length - 1;

    while (left <= right) {
      int mid = left + (right - left) / 2;
      if (arr[mid] == target) {
        return mid;
      } else if (arr[mid] < target) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }

    return -1;
  }

  /**
   * Search in rotated sorted array.
   *
   * <p>LeetCode 33 - Search in Rotated Sorted Array (Medium)
   *
   * <p>Time Complexity: O(log n), Space Complexity: O(1)
   *
   * <p>Tricky: Determine which half is sorted, then search accordingly.
   *
   * @param nums rotated sorted array
   * @param target value to find
   * @return index of target or -1 if not found
   * @throws IllegalArgumentException if nums is null
   */
  public static int searchInRotatedSortedArray(int[] nums, int target) {
    if (nums == null) {
      throw new IllegalArgumentException("Input array cannot be null");
    }

    int left = 0;
    int right = nums.length - 1;

    while (left <= right) {
      int mid = left + (right - left) / 2;
      if (nums[mid] == target) {
        return mid;
      }

      if (nums[left] <= nums[mid]) {
        if (target >= nums[left] && target < nums[mid]) {
          right = mid - 1;
        } else {
          left = mid + 1;
        }
      } else {
        if (target > nums[mid] && target <= nums[right]) {
          left = mid + 1;
        } else {
          right = mid - 1;
        }
      }
    }

    return -1;
  }

  /**
   * Rotate array in-place.
   *
   * <p>LeetCode 189 - Rotate Array (Medium)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(1)
   *
   * <p>Pattern: reverse(0, n-1) -> reverse(0, k-1) -> reverse(k, n-1)
   *
   * @param nums array to rotate
   * @param k number of steps to rotate right
   * @throws IllegalArgumentException if nums is null
   */
  public static void rotateArray(int[] nums, int k) {
    if (nums == null) {
      throw new IllegalArgumentException("Input array cannot be null");
    }

    k = k % nums.length;
    reverse(nums, 0, nums.length - 1);
    reverse(nums, 0, k - 1);
    reverse(nums, k, nums.length - 1);
  }

  /**
   * Helper method to reverse array in-place.
   *
   * @param nums array to reverse
   * @param start start index
   * @param end end index
   */
  private static void reverse(int[] nums, int start, int end) {
    while (start < end) {
      int temp = nums[start];
      nums[start] = nums[end];
      nums[end] = temp;
      start++;
      end--;
    }
  }

  /**
   * Next permutation: modify array to next lexicographic permutation.
   *
   * <p>LeetCode 31 - Next Permutation (Medium)
   *
   * <p>Time Complexity: O(n), Space Complexity: O(1)
   *
   * <p>Pattern: 1) Find rightmost i where nums[i] < nums[i+1] 2) Find rightmost j where
   * nums[j] > nums[i] 3) Swap i and j 4) Reverse from i+1 to end
   *
   * @param nums array to modify in-place
   * @throws IllegalArgumentException if nums is null
   */
  public static void nextPermutation(int[] nums) {
    if (nums == null) {
      throw new IllegalArgumentException("Input array cannot be null");
    }

    int i = nums.length - 2;
    while (i >= 0 && nums[i] >= nums[i + 1]) {
      i--;
    }

    if (i >= 0) {
      int j = nums.length - 1;
      while (j > i && nums[j] <= nums[i]) {
        j--;
      }

      int temp = nums[i];
      nums[i] = nums[j];
      nums[j] = temp;
    }

    reverse(nums, i + 1, nums.length - 1);
  }

  /**
   * Main method with comprehensive test cases.
   *
   * @param args command-line arguments (unused)
   */
  public static void main(String[] args) {
    System.out.println("=== Array Problems ===\n");

    // Test twoSumSorted
    System.out.println("1. Two Sum (Sorted):");
    int[] numbers = {2, 7, 11, 15};
    int[] result = twoSumSorted(numbers, 9);
    System.out.println("  Input: [2,7,11,15], target=9");
    System.out.println("  Output: [" + result[0] + "," + result[1] + "]\n");

    // Test threeSum
    System.out.println("2. Three Sum:");
    int[] nums1 = {-1, 0, 1, 2, -1, -4};
    List<List<Integer>> threeResult = threeSum(nums1);
    System.out.println("  Input: [-1,0,1,2,-1,-4]");
    System.out.println("  Output: " + threeResult + "\n");

    // Test maxSumSubarraySizeK
    System.out.println("3. Max Sum Subarray Size K:");
    int[] arr = {1, 4, 2, 10, 23, 3, 1, 0, 20};
    int maxSum = maxSumSubarraySizeK(arr, 4);
    System.out.println("  Input: [1,4,2,10,23,3,1,0,20], k=4");
    System.out.println("  Output: " + maxSum + "\n");

    // Test maxSubarraySum
    System.out.println("4. Max Subarray Sum (Kadane's):");
    int[] nums2 = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int kadaneResult = maxSubarraySum(nums2);
    System.out.println("  Input: [-2,1,-3,4,-1,2,1,-5,4]");
    System.out.println("  Output: " + kadaneResult + "\n");

    // Test mergeIntervals
    System.out.println("5. Merge Intervals:");
    int[][] intervals = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
    int[][] mergedIntervals = mergeIntervals(intervals);
    System.out.println("  Input: [[1,3],[2,6],[8,10],[15,18]]");
    System.out.print("  Output: [");
    for (int[] interval : mergedIntervals) {
      System.out.print("[" + interval[0] + "," + interval[1] + "]");
    }
    System.out.println("]\n");

    // Test rotateArray
    System.out.println("6. Rotate Array:");
    int[] rotateNums = {1, 2, 3, 4, 5, 6, 7};
    rotateArray(rotateNums, 3);
    System.out.println("  Input: [1,2,3,4,5,6,7], k=3");
    System.out.print("  Output: [");
    for (int i = 0; i < rotateNums.length; i++) {
      System.out.print(rotateNums[i]);
      if (i < rotateNums.length - 1) {
        System.out.print(",");
      }
    }
    System.out.println("]\n");
  }
}
