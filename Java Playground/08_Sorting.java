import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

/**
 * Sorting Algorithms & Techniques.
 *
 * <p><b>MERGE SORT:</b> Stable, O(n log n) time, O(n) space. Good for linked
 * lists, guaranteed O(n log n). Recursive divide-and-merge.
 *
 * <p><b>QUICK SORT:</b> In-place (O(log n) space for recursion), O(n log n) avg,
 * O(n²) worst. Good for arrays. Partition around pivot.
 *
 * <p><b>QUICK SELECT:</b> Find kth smallest/largest in O(n) average without
 * full sort. Use quick sort partition.
 *
 * <p><b>JAVA ARRAYS.SORT:</b> Dual-pivot quicksort for primitives, timsort for
 * objects. Use Integer.compare for safe comparisons (avoid a-b overflow).
 *
 * <p><b>CUSTOM COMPARATOR:</b> For objects, use explicit comparator. Common
 * pattern: (a, b) -> Integer.compare(a, b) for ascending.
 *
 * <p><b>INTERVAL PROBLEMS:</b> Sort by start, use greedy or heap for
 * overlaps/merges.
 *
 * <p>Time varies by algorithm. Space: O(n) for merge, O(log n) for quick.
 */
public class Sorting {

  /**
   * Merge Sort - Stable, divide-and-conquer.
   *
   * @param arr input array to sort
   * @throws NullPointerException if arr is null
   *
   *         <p>Time: O(n log n). Space: O(n) for merge buffer.
   *
   *         <p>Recursively divide array in half, merge sorted halves. Stable
   *         sorting maintains original order of equal elements.
   */
  public static void mergeSort(int[] arr) {
    if (arr == null || arr.length == 0) {
      return;
    }

    mergeSortHelper(arr, 0, arr.length - 1);
  }

  /**
   * Helper: recursively sort arr[left..right].
   *
   * @param arr input array
   * @param left left boundary
   * @param right right boundary
   */
  private static void mergeSortHelper(int[] arr, int left, int right) {
    if (left < right) {
      int mid = left + (right - left) / 2;

      mergeSortHelper(arr, left, mid);
      mergeSortHelper(arr, mid + 1, right);

      merge(arr, left, mid, right);
    }
  }

  /**
   * Helper: merge two sorted subarrays arr[left..mid] and arr[mid+1..right].
   *
   * @param arr input array
   * @param left left boundary
   * @param mid middle boundary
   * @param right right boundary
   */
  private static void merge(int[] arr, int left, int mid, int right) {
    int[] temp = new int[right - left + 1];
    int i = left;
    int j = mid + 1;
    int k = 0;

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

    for (int idx = left, t = 0; idx <= right; idx++, t++) {
      arr[idx] = temp[t];
    }
  }

  /**
   * Quick Sort - In-place, average O(n log n).
   *
   * @param arr input array to sort
   * @throws NullPointerException if arr is null
   *
   *         <p>Time: O(n log n) avg, O(n²) worst. Space: O(log n) recursion.
   *
   *         <p>Partition around pivot, recursively sort left and right. Use
   *         Hoare or Lomuto partition scheme. Here: Lomuto (simpler).
   */
  public static void quickSort(int[] arr) {
    if (arr == null || arr.length == 0) {
      return;
    }

    quickSortHelper(arr, 0, arr.length - 1);
  }

  /**
   * Helper: recursively sort arr[left..right].
   *
   * @param arr input array
   * @param left left boundary
   * @param right right boundary
   */
  private static void quickSortHelper(int[] arr, int left, int right) {
    if (left < right) {
      int pivotIdx = partition(arr, left, right);

      quickSortHelper(arr, left, pivotIdx - 1);
      quickSortHelper(arr, pivotIdx + 1, right);
    }
  }

  /**
   * Helper: Lomuto partition scheme. Pivot is rightmost element.
   *
   * @param arr input array
   * @param left left boundary
   * @param right right boundary
   * @return index of pivot after partitioning
   */
  private static int partition(int[] arr, int left, int right) {
    int pivot = arr[right];
    int i = left;

    for (int j = left; j < right; j++) {
      if (arr[j] < pivot) {
        swap(arr, i, j);
        i++;
      }
    }

    swap(arr, i, right);
    return i;
  }

  /**
   * Find Kth Largest Element using Quick Select.
   *
   * @param nums input array
   * @param k kth largest (1-indexed: 1 = largest, 2 = 2nd largest, etc)
   * @return kth largest element
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 215 (Medium). Time: O(n) avg, O(n²) worst.
   *         Space: O(log n).
   *
   *         <p>Quick select finds kth smallest/largest without full sort.
   *         Use partition, recursively search left or right half.
   */
  public static int findKthLargest(int[] nums, int k) {
    if (nums == null || nums.length == 0 || k <= 0 || k > nums.length) {
      return Integer.MIN_VALUE;
    }

    // Convert kth largest to kth smallest (0-indexed)
    int target = nums.length - k;
    return quickSelect(nums, 0, nums.length - 1, target);
  }

  /**
   * Helper: quick select to find element at index target.
   *
   * @param arr input array
   * @param left left boundary
   * @param right right boundary
   * @param target 0-indexed target position
   * @return element at target position in sorted order
   */
  private static int quickSelect(int[] arr, int left, int right, int target) {
    if (left == right) {
      return arr[left];
    }

    int pivotIdx = partition(arr, left, right);

    if (target == pivotIdx) {
      return arr[target];
    } else if (target < pivotIdx) {
      return quickSelect(arr, left, pivotIdx - 1, target);
    } else {
      return quickSelect(arr, pivotIdx + 1, right, target);
    }
  }

  /**
   * Largest Number - Arrange numbers to form largest possible number.
   *
   * @param nums input array of non-negative integers
   * @return string representation of largest number
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 179 (Medium). Time: O(n log n). Space: O(n).
   *
   *         <p>Custom comparator: for two numbers a, b, compare (a+b) vs (b+a).
   *         If ab > ba, a should come first. Handle edge case of all zeros.
   */
  public static String largestNumber(int[] nums) {
    if (nums == null || nums.length == 0) {
      return "";
    }

    String[] strs = new String[nums.length];
    for (int i = 0; i < nums.length; i++) {
      strs[i] = String.valueOf(nums[i]);
    }

    // Custom comparator: sort so ab > ba for max result
    Arrays.sort(strs, new Comparator<String>() {
      @Override
      public int compare(String a, String b) {
        String ab = a + b;
        String ba = b + a;
        return ba.compareTo(ab); // Descending: ba > ab
      }
    });

    // Edge case: if first element is "0", entire result is "0"
    if (strs[0].equals("0")) {
      return "0";
    }

    StringBuilder result = new StringBuilder();
    for (String s : strs) {
      result.append(s);
    }

    return result.toString();
  }

  /**
   * Sort by Frequency then Value.
   *
   * @param nums input array
   * @return sorted array: ascending by frequency, then by value (if same
   *     frequency)
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 1636 (Medium). Time: O(n log n).
   *         Space: O(n).
   *
   *         <p>Count frequencies, use custom comparator: sort by frequency
   *         ascending, then by value descending.
   */
  public static int[] sortByFrequencyThenValue(int[] nums) {
    if (nums == null) {
      return new int[0];
    }

    Map<Integer, Integer> freqMap = new HashMap<>();
    for (int num : nums) {
      freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
    }

    Integer[] arr = new Integer[nums.length];
    for (int i = 0; i < nums.length; i++) {
      arr[i] = nums[i];
    }

    Arrays.sort(arr, new Comparator<Integer>() {
      @Override
      public int compare(Integer a, Integer b) {
        int freqA = freqMap.get(a);
        int freqB = freqMap.get(b);

        if (freqA != freqB) {
          return Integer.compare(freqA, freqB); // Ascending frequency
        }
        return Integer.compare(b, a); // Descending value (if same freq)
      }
    });

    int[] result = new int[arr.length];
    for (int i = 0; i < arr.length; i++) {
      result[i] = arr[i];
    }

    return result;
  }

  /**
   * Merge Intervals - Merge overlapping intervals.
   *
   * @param intervals array of [start, end] intervals
   * @return merged non-overlapping intervals
   * @throws NullPointerException if intervals is null
   *
   *         <p>LeetCode 56 (Medium). Time: O(n log n). Space: O(1) excluding
   *         output.
   *
   *         <p>Sort by start time. Merge if next interval overlaps current.
   *         Overlaps if next.start <= current.end.
   */
  public static int[][] mergeIntervals(int[][] intervals) {
    if (intervals == null || intervals.length == 0) {
      return new int[0][0];
    }

    Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));

    List<int[]> merged = new ArrayList<>();
    int[] current = intervals[0];

    for (int i = 1; i < intervals.length; i++) {
      if (intervals[i][0] <= current[1]) {
        // Overlapping: extend current interval
        current[1] = Math.max(current[1], intervals[i][1]);
      } else {
        // Non-overlapping: save current and start new
        merged.add(current);
        current = intervals[i];
      }
    }

    merged.add(current);

    return merged.toArray(new int[0][0]);
  }

  /**
   * Insert Interval - Insert new interval and merge as needed.
   *
   * @param intervals sorted array of non-overlapping intervals
   * @param newInterval interval to insert
   * @return merged result after insertion
   * @throws NullPointerException if intervals or newInterval is null
   *
   *         <p>LeetCode 57 (Medium). Time: O(n). Space: O(1) excluding output.
   *
   *         <p>Add all non-overlapping intervals before merge, merge overlapping,
   *         add all after. Avoid full sort; linear pass sufficient.
   */
  public static int[][] insertInterval(int[][] intervals,
      int[] newInterval) {
    if (intervals == null || newInterval == null) {
      return new int[0][0];
    }

    List<int[]> result = new ArrayList<>();
    int newStart = newInterval[0];
    int newEnd = newInterval[1];
    int i = 0;

    // Add all intervals before new interval (no overlap)
    while (i < intervals.length && intervals[i][1] < newStart) {
      result.add(intervals[i]);
      i++;
    }

    // Merge overlapping intervals
    while (i < intervals.length && intervals[i][0] <= newEnd) {
      newStart = Math.min(newStart, intervals[i][0]);
      newEnd = Math.max(newEnd, intervals[i][1]);
      i++;
    }

    result.add(new int[]{newStart, newEnd});

    // Add all remaining intervals
    while (i < intervals.length) {
      result.add(intervals[i]);
      i++;
    }

    return result.toArray(new int[0][0]);
  }

  /**
   * Meeting Rooms II - Find minimum meeting rooms needed.
   *
   * @param intervals array of [start, end] meeting times
   * @return minimum number of meeting rooms required
   * @throws NullPointerException if intervals is null
   *
   *         <p>LeetCode 253 (Medium). Time: O(n log n). Space: O(n).
   *
   *         <p>Use min heap of end times. For each meeting, pop room if
   *         earliest end <= current start; else add new room.
   */
  public static int meetingRoomsII(int[][] intervals) {
    if (intervals == null || intervals.length == 0) {
      return 0;
    }

    // Sort by start time
    Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));

    PriorityQueue<Integer> minHeap = new PriorityQueue<>();

    for (int[] interval : intervals) {
      if (!minHeap.isEmpty() && minHeap.peek() <= interval[0]) {
        // Previous meeting ended before this starts; reuse room
        minHeap.poll();
      }

      minHeap.offer(interval[1]);
    }

    return minHeap.size();
  }

  /**
   * Top K Frequent Elements using Bucket Sort.
   *
   * @param nums input array
   * @param k number of most frequent elements to return
   * @return array of k most frequent elements (any order)
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 347 (Medium). Time: O(n). Space: O(n).
   *
   *         <p>Count frequencies, create buckets indexed by frequency. Fill
   *         buckets, collect from highest frequency down. More efficient than
   *         heap for this problem.
   */
  public static int[] topKFrequentBucket(int[] nums, int k) {
    if (nums == null || k <= 0) {
      return new int[0];
    }

    Map<Integer, Integer> freqMap = new HashMap<>();
    for (int num : nums) {
      freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
    }

    // Buckets: bucket[i] = list of numbers with frequency i
    List<Integer>[] buckets = new List[nums.length + 1];
    for (int i = 0; i < buckets.length; i++) {
      buckets[i] = new ArrayList<>();
    }

    for (Map.Entry<Integer, Integer> entry : freqMap.entrySet()) {
      buckets[entry.getValue()].add(entry.getKey());
    }

    int[] result = new int[k];
    int idx = 0;

    // Collect from highest frequency bucket downward
    for (int i = buckets.length - 1; i >= 0 && idx < k; i--) {
      for (int num : buckets[i]) {
        result[idx++] = num;
        if (idx == k) {
          break;
        }
      }
    }

    return result;
  }

  /**
   * Find Missing Number (multiple approaches demonstrated).
   *
   * @param nums input array containing n-1 unique integers from 0 to n
   * @return missing integer
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 268 (Easy). Time: O(n). Space: O(1).
   *
   *         <p>Approach: XOR all nums and all expected values. XOR of same
   *         values = 0, so result is missing number.
   */
  public static int findMissingNumber(int[] nums) {
    if (nums == null) {
      return -1;
    }

    int xorNums = 0;
    int xorExpected = 0;

    for (int i = 0; i < nums.length; i++) {
      xorNums ^= nums[i];
      xorExpected ^= i;
    }

    // XOR with n (missing range endpoint)
    xorExpected ^= nums.length;

    return xorNums ^ xorExpected;
  }

  /**
   * Find Duplicate Number using Floyd's Cycle Detection.
   *
   * @param nums array where 1 <= nums[i] <= n-1, n = nums.length, with at
   *     least one duplicate
   * @return duplicate number (may appear more than once)
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 287 (Medium). Time: O(n). Space: O(1).
   *
   *         <p>Treat array as linked list where nums[i] = next node index.
   *         Detect cycle with Floyd's tortoise-hare algorithm, then find cycle
   *         entrance (the duplicate).
   */
  public static int findDuplicateNumber(int[] nums) {
    if (nums == null || nums.length <= 1) {
      return -1;
    }

    int slow = nums[0];
    int fast = nums[0];

    // Phase 1: detect cycle
    do {
      slow = nums[slow];
      fast = nums[nums[fast]];
    } while (slow != fast);

    // Phase 2: find cycle entrance
    slow = nums[0];
    while (slow != fast) {
      slow = nums[slow];
      fast = nums[fast];
    }

    return slow;
  }

  /**
   * Helper: swap two elements in array.
   *
   * @param arr input array
   * @param i first index
   * @param j second index
   */
  private static void swap(int[] arr, int i, int j) {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }

  /**
   * Main method demonstrating all sorting techniques.
   */
  public static void main(String[] args) {
    System.out.println("=== SORTING ALGORITHMS & TECHNIQUES ===\n");

    // Merge Sort
    int[] arr1 = {38, 27, 43, 3, 9, 82, 10};
    mergeSort(arr1);
    System.out.println("Merge Sort: " + Arrays.toString(arr1));

    // Quick Sort
    int[] arr2 = {64, 34, 25, 12, 22, 11, 90};
    quickSort(arr2);
    System.out.println("Quick Sort: " + Arrays.toString(arr2));

    // Find Kth Largest
    int[] arr3 = {3, 2, 1, 5, 6, 4};
    System.out.println("Kth Largest (k=2): " + findKthLargest(arr3, 2));

    // Largest Number
    int[] arr4 = {3, 30, 34, 5, 9};
    System.out.println("Largest Number: " + largestNumber(arr4));

    // Sort by Frequency
    int[] arr5 = {1, 1, 1, 2, 2, 3, 3, 3, 3};
    System.out.println("Sort by Frequency: " +
        Arrays.toString(sortByFrequencyThenValue(arr5)));

    // Merge Intervals
    int[][] intervals1 = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
    int[][] merged = mergeIntervals(intervals1);
    System.out.println("Merge Intervals:");
    for (int[] interval : merged) {
      System.out.println("  " + Arrays.toString(interval));
    }

    // Insert Interval
    int[][] intervals2 = {{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}};
    int[][] inserted = insertInterval(intervals2, new int[]{4, 8});
    System.out.println("Insert Interval [4,8]:");
    for (int[] interval : inserted) {
      System.out.println("  " + Arrays.toString(interval));
    }

    // Meeting Rooms II
    int[][] intervals3 = {{0, 30}, {5, 10}, {15, 20}};
    System.out.println("Meeting Rooms: " + meetingRoomsII(intervals3));

    // Top K Frequent
    int[] arr6 = {1, 1, 1, 2, 2, 3};
    System.out.println("Top K Frequent (k=2): " +
        Arrays.toString(topKFrequentBucket(arr6, 2)));

    // Find Missing Number
    int[] arr7 = {3, 0, 1};
    System.out.println("Find Missing Number: " + findMissingNumber(arr7));

    // Find Duplicate
    int[] arr8 = {1, 3, 4, 2, 2};
    System.out.println("Find Duplicate: " + findDuplicateNumber(arr8));
  }
}
