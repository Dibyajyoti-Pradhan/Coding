import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedHashSet;
import java.util.Map;
import java.util.Stack;

/**
 * Advanced algorithmic patterns appearing frequently in medium/hard level interviews.
 *
 * <p>This class covers:
 * <ul>
 *   <li><b>Monotonic Stack/Queue:</b> Maintain increasing/decreasing order for next/previous
 *       greater element problems
 *   <li><b>Advanced Prefix Sum:</b> Optimize space and handle negative numbers
 *   <li><b>Interval Scheduling:</b> Greedy strategies for overlapping intervals
 *   <li><b>System Design Caching:</b> LFU Cache with O(1) operations
 * </ul>
 */
public class AdvancedTopics {

  private static final int NEGATIVE_INFINITY = -1;
  private static final int CACHE_SIZE_EXAMPLE = 2;

  // ===================== SECTION 1: MONOTONIC STACK =====================

  /**
   * Monotonic Stack Pattern: Maintain increasing/decreasing order of elements.
   *
   * <p>Key insights:
   * <ul>
   *   <li>Each element is pushed and popped exactly once → O(n) time
   *   <li>Store indices, not values, to handle duplicates and construct results
   *   <li>Use stack for previous/next greater/smaller element problems
   * </ul>
   */

  /**
   * Finds the next greater element in a circular array.
   *
   * <p><b>LeetCode 503 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * nums = [1,2,1]
   * Output: [2,-1,2]
   * </pre>
   *
   * <p><b>Constraints:</b> 1 ≤ nums.length ≤ 10^4
   *
   * <p><b>Time:</b> O(n) <b>Space:</b> O(n)
   *
   * <p><b>Tricky:</b> Iterate twice through array to simulate circularity. Use monotonic
   * decreasing stack to handle wrap-around.
   *
   * @param nums input array
   * @return array where result[i] = next greater element or -1
   */
  public static int[] nextGreaterElementsCircular(int[] nums) {
    if (nums == null || nums.length == 0) {
      return new int[0];
    }

    int n = nums.length;
    int[] result = new int[n];
    java.util.Arrays.fill(result, NEGATIVE_INFINITY);

    Stack<Integer> stack = new Stack<>();

    // Iterate twice to handle circular nature
    for (int i = 0; i < 2 * n; i++) {
      int num = nums[i % n];

      // Pop elements smaller than current
      while (!stack.isEmpty() && nums[stack.peek()] < num) {
        result[stack.pop()] = num;
      }

      // Only push first occurrence
      if (i < n) {
        stack.push(i);
      }
    }

    return result;
  }

  /**
   * Finds the number of days to wait for a warmer temperature.
   *
   * <p><b>LeetCode 739 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * temperatures = [73,74,75,71,69,72,76,73]
   * Output: [1,1,4,2,1,1,0,0]
   * </pre>
   *
   * <p><b>Constraints:</b> 1 ≤ temperatures.length ≤ 10^5, 30 ≤ temp ≤ 100
   *
   * <p><b>Time:</b> O(n) <b>Space:</b> O(n)
   *
   * <p><b>Tricky:</b> Use monotonic decreasing stack of indices. When current temperature
   * is higher, pop and calculate distance.
   *
   * @param temperatures daily temperatures
   * @return array where result[i] = days until warmer temperature
   */
  public static int[] dailyTemperatures(int[] temperatures) {
    if (temperatures == null || temperatures.length == 0) {
      return new int[0];
    }

    int n = temperatures.length;
    int[] result = new int[n];
    Stack<Integer> stack = new Stack<>();

    for (int i = 0; i < n; i++) {
      while (!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]) {
        int prevIndex = stack.pop();
        result[prevIndex] = i - prevIndex;
      }
      stack.push(i);
    }

    return result;
  }

  /**
   * Finds the largest rectangle area in a histogram.
   *
   * <p><b>LeetCode 84 (Hard)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * heights = [2,1,5,6,2,3]
   * Output: 10 (rectangle 5x2)
   * </pre>
   *
   * <p><b>Constraints:</b> 1 ≤ heights.length ≤ 10^5, 0 ≤ height ≤ 10^4
   *
   * <p><b>Time:</b> O(n) <b>Space:</b> O(n)
   *
   * <p><b>Tricky:</b> Use monotonic increasing stack. When bar is shorter, pop and
   * calculate area. Height extends from popped element to current.
   *
   * @param heights array of histogram bar heights
   * @return largest rectangle area
   */
  public static int largestRectangleInHistogram(int[] heights) {
    if (heights == null || heights.length == 0) {
      return 0;
    }

    int maxArea = 0;
    Stack<Integer> stack = new Stack<>();

    for (int i = 0; i < heights.length; i++) {
      while (!stack.isEmpty() && heights[stack.peek()] > heights[i]) {
        int h = heights[stack.pop()];
        int w = stack.isEmpty() ? i : i - stack.peek() - 1;
        maxArea = Math.max(maxArea, h * w);
      }
      stack.push(i);
    }

    // Process remaining bars in stack
    while (!stack.isEmpty()) {
      int h = heights[stack.pop()];
      int w = stack.isEmpty() ? heights.length : heights.length - stack.peek() - 1;
      maxArea = Math.max(maxArea, h * w);
    }

    return maxArea;
  }

  /**
   * Traps rainwater between elevation map bars.
   *
   * <p><b>LeetCode 42 (Hard)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * height = [0,1,0,2,1,0,1,4,3,2,1,2,1]
   * Output: 6
   * </pre>
   *
   * <p><b>Constraints:</b> 1 ≤ height.length ≤ 2·10^4
   *
   * <p><b>Time:</b> O(n) <b>Space:</b> O(1)
   *
   * <p><b>Tricky:</b> Two-pointer approach: track max heights from left and right.
   * Water trapped = min(leftMax, rightMax) - current height.
   *
   * @param height elevation map
   * @return units of trapped water
   */
  public static int trap(int[] height) {
    if (height == null || height.length < 2) {
      return 0;
    }

    int left = 0;
    int right = height.length - 1;
    int leftMax = 0;
    int rightMax = 0;
    int water = 0;

    while (left < right) {
      if (height[left] < height[right]) {
        if (height[left] >= leftMax) {
          leftMax = height[left];
        } else {
          water += leftMax - height[left];
        }
        left++;
      } else {
        if (height[right] >= rightMax) {
          rightMax = height[right];
        } else {
          water += rightMax - height[right];
        }
        right--;
      }
    }

    return water;
  }

  /**
   * Online Stock Span Calculator returning span for each price.
   *
   * <p><b>LeetCode 901 (Medium)</b>
   *
   * <p><b>Span:</b> Number of consecutive days before today with price ≤ today's price.
   */
  public static class StockSpanner {
    private Stack<int[]> stack; // [price, span]

    /**
     * Initializes the stock spanner.
     */
    public StockSpanner() {
      this.stack = new Stack<>();
    }

    /**
     * Returns the span for the current price.
     *
     * <p><b>Time:</b> O(1) amortized <b>Space:</b> O(n)
     *
     * <p><b>Tricky:</b> Store [price, span] pairs. When price increases, pop smaller
     * prices and accumulate their spans.
     *
     * @param price current stock price
     * @return span (consecutive days with price ≤ current)
     */
    public int next(int price) {
      int span = 1;

      while (!stack.isEmpty() && stack.peek()[0] <= price) {
        span += stack.pop()[1];
      }

      stack.push(new int[]{price, span});
      return span;
    }
  }

  // ===================== SECTION 2: ADVANCED PREFIX SUM =====================

  /**
   * Computes product of array except self without division.
   *
   * <p><b>LeetCode 238 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * nums = [1,2,3,4]
   * Output: [24,12,8,6]
   * </pre>
   *
   * <p><b>Constraints:</b> 2 ≤ nums.length ≤ 10^5
   *
   * <p><b>Time:</b> O(n) <b>Space:</b> O(1) (output array not counted)
   *
   * <p><b>Tricky:</b> Two-pass approach: compute left products, then multiply by right
   * products. O(1) auxiliary space.
   *
   * @param nums input array
   * @return product of all elements except current
   */
  public static int[] productExceptSelf(int[] nums) {
    if (nums == null || nums.length == 0) {
      return new int[0];
    }

    int n = nums.length;
    int[] result = new int[n];

    // Left pass: result[i] = product of all elements to the left
    result[0] = 1;
    for (int i = 1; i < n; i++) {
      result[i] = result[i - 1] * nums[i - 1];
    }

    // Right pass: multiply by product of all elements to the right
    int rightProduct = 1;
    for (int i = n - 1; i >= 0; i--) {
      result[i] *= rightProduct;
      rightProduct *= nums[i];
    }

    return result;
  }

  /**
   * Counts subarrays with sum divisible by k.
   *
   * <p><b>LeetCode 974 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * nums = [4,5,0,-2,-3,1], k = 5
   * Output: 7
   * </pre>
   *
   * <p><b>Constraints:</b> 1 ≤ nums.length ≤ 10^5, 1 ≤ k ≤ 10^9
   *
   * <p><b>Time:</b> O(n) <b>Space:</b> O(k)
   *
   * <p><b>Tricky:</b> Use prefix sum modulo k. If (prefixSum1 % k) == (prefixSum2 % k),
   * then subarray sum between them is divisible by k. Handle negative modulo carefully.
   *
   * @param nums input array
   * @param k divisor
   * @return count of subarrays with sum % k == 0
   */
  public static int subarraysDivByK(int[] nums, int k) {
    if (nums == null || nums.length == 0 || k == 0) {
      return 0;
    }

    Map<Integer, Integer> modCount = new HashMap<>();
    modCount.put(0, 1);
    int prefixSum = 0;
    int count = 0;

    for (int num : nums) {
      prefixSum += num;
      int mod = ((prefixSum % k) + k) % k; // Handle negative modulo
      count += modCount.getOrDefault(mod, 0);
      modCount.put(mod, modCount.getOrDefault(mod, 0) + 1);
    }

    return count;
  }

  /**
   * Checks if array has continuous subarray with sum divisible by k and length ≥ 2.
   *
   * <p><b>LeetCode 523 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * nums = [23,2,4,6,7], k = 6
   * Output: true (subarray [2,4])
   * </pre>
   *
   * <p><b>Constraints:</b> 1 ≤ nums.length ≤ 10^5
   *
   * <p><b>Time:</b> O(n) <b>Space:</b> O(k)
   *
   * <p><b>Tricky:</b> Track first occurrence of each prefix mod. Length ≥ 2 means
   * prefix indices differ by at least 1.
   *
   * @param nums input array
   * @param k target divisor
   * @return true if such subarray exists
   */
  public static boolean continuousSubarraySum(int[] nums, int k) {
    if (nums == null || nums.length < 2 || k == 0) {
      return false;
    }

    Map<Integer, Integer> modIndex = new HashMap<>();
    modIndex.put(0, -1);
    int prefixSum = 0;

    for (int i = 0; i < nums.length; i++) {
      prefixSum += nums[i];
      int mod = ((prefixSum % k) + k) % k;

      if (modIndex.containsKey(mod)) {
        if (i - modIndex.get(mod) >= 2) {
          return true;
        }
      } else {
        modIndex.put(mod, i);
      }
    }

    return false;
  }

  /**
   * 2D Prefix Sum for fast range sum queries.
   *
   * <p><b>LeetCode 304 (Medium)</b>
   */
  public static class NumMatrix {
    private int[][] prefixSum;

    /**
     * Initializes 2D prefix sum array.
     *
     * <p><b>Time:</b> O(m·n) <b>Space:</b> O(m·n)
     *
     * @param matrix input matrix
     */
    public NumMatrix(int[][] matrix) {
      if (matrix == null || matrix.length == 0) {
        return;
      }

      int m = matrix.length;
      int n = matrix[0].length;
      this.prefixSum = new int[m + 1][n + 1];

      for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
          prefixSum[i][j] =
              matrix[i - 1][j - 1]
                  + prefixSum[i - 1][j]
                  + prefixSum[i][j - 1]
                  - prefixSum[i - 1][j - 1];
        }
      }
    }

    /**
     * Computes sum of rectangle [row1,col1] to [row2,col2].
     *
     * <p><b>Time:</b> O(1) <b>Space:</b> O(1)
     *
     * @param row1 top-left row
     * @param col1 top-left column
     * @param row2 bottom-right row
     * @param col2 bottom-right column
     * @return sum in rectangle
     */
    public int sumRegion(int row1, int col1, int row2, int col2) {
      if (prefixSum == null) {
        return 0;
      }

      return prefixSum[row2 + 1][col2 + 1]
          - prefixSum[row1][col2 + 1]
          - prefixSum[row2 + 1][col1]
          + prefixSum[row1][col1];
    }
  }

  // ===================== SECTION 3: INTERVAL SCHEDULING =====================

  /**
   * Inserts a new interval into non-overlapping intervals.
   *
   * <p><b>LeetCode 57 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * intervals = [[1,5]], newInterval = [2,7]
   * Output: [[1,7]]
   * </pre>
   *
   * <p><b>Constraints:</b> intervals.length ≤ 10^4
   *
   * <p><b>Time:</b> O(n) <b>Space:</b> O(n)
   *
   * <p><b>Tricky:</b> Add non-overlapping intervals before new interval, merge overlapping,
   * then add remaining intervals.
   *
   * @param intervals sorted non-overlapping intervals
   * @param newInterval interval to insert
   * @return merged intervals
   */
  public static int[][] insertInterval(int[][] intervals, int[] newInterval) {
    if (intervals == null || newInterval == null) {
      return intervals;
    }

    java.util.List<int[]> result = new java.util.ArrayList<>();
    int i = 0;

    // Add intervals before newInterval
    while (i < intervals.length && intervals[i][1] < newInterval[0]) {
      result.add(intervals[i]);
      i++;
    }

    // Merge overlapping intervals
    int start = newInterval[0];
    int end = newInterval[1];
    while (i < intervals.length && intervals[i][0] <= end) {
      start = Math.min(start, intervals[i][0]);
      end = Math.max(end, intervals[i][1]);
      i++;
    }
    result.add(new int[]{start, end});

    // Add remaining intervals
    while (i < intervals.length) {
      result.add(intervals[i]);
      i++;
    }

    return result.toArray(new int[0][]);
  }

  /**
   * Finds minimum number of meeting rooms needed.
   *
   * <p><b>LeetCode 253 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * intervals = [[0,30],[5,10],[15,20]]
   * Output: 2
   * </pre>
   *
   * <p><b>Constraints:</b> 1 ≤ intervals.length ≤ 10^4
   *
   * <p><b>Time:</b> O(n log n) <b>Space:</b> O(n)
   *
   * <p><b>Tricky:</b> Two-pointer approach on sorted start/end times. Max concurrent
   * intervals = min rooms needed.
   *
   * @param intervals meeting time intervals
   * @return minimum rooms needed
   */
  public static int minMeetingRooms(int[][] intervals) {
    if (intervals == null || intervals.length == 0) {
      return 0;
    }

    int[] starts = new int[intervals.length];
    int[] ends = new int[intervals.length];
    for (int i = 0; i < intervals.length; i++) {
      starts[i] = intervals[i][0];
      ends[i] = intervals[i][1];
    }

    java.util.Arrays.sort(starts);
    java.util.Arrays.sort(ends);

    int rooms = 0;
    int maxRooms = 0;
    int i = 0;
    int j = 0;

    while (i < starts.length && j < ends.length) {
      if (starts[i] < ends[j]) {
        rooms++;
        i++;
      } else {
        rooms--;
        j++;
      }
      maxRooms = Math.max(maxRooms, rooms);
    }

    return maxRooms;
  }

  /**
   * Erases the minimum number of non-overlapping intervals.
   *
   * <p><b>LeetCode 435 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * intervals = [[1,2],[2,3],[3,4],[1,3]]
   * Output: 1
   * </pre>
   *
   * <p><b>Constraints:</b> 1 ≤ intervals.length ≤ 10^4
   *
   * <p><b>Time:</b> O(n log n) <b>Space:</b> O(1)
   *
   * <p><b>Tricky:</b> Greedy: sort by end time, keep intervals with smallest end.
   * Remove intervals overlapping with last kept interval.
   *
   * @param intervals intervals to prune
   * @return minimum intervals to remove
   */
  public static int nonOverlappingIntervals(int[][] intervals) {
    if (intervals == null || intervals.length <= 1) {
      return 0;
    }

    java.util.Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));

    int count = 0;
    int lastEnd = intervals[0][1];

    for (int i = 1; i < intervals.length; i++) {
      if (intervals[i][0] < lastEnd) {
        count++;
      } else {
        lastEnd = intervals[i][1];
      }
    }

    return count;
  }

  /**
   * Finds minimum arrows to burst overlapping balloons.
   *
   * <p><b>LeetCode 452 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * points = [[10,16],[2,8],[1,6],[7,12]]
   * Output: 2
   * </pre>
   *
   * <p><b>Constraints:</b> 1 ≤ points.length ≤ 10^4
   *
   * <p><b>Time:</b> O(n log n) <b>Space:</b> O(1)
   *
   * <p><b>Tricky:</b> Sort by end point. Greedy: shoot at end of each interval, track
   * last shot position, skip intervals already burst.
   *
   * @param points balloon coordinate intervals
   * @return minimum arrows needed
   */
  public static int minArrowsToBurstBalloons(int[][] points) {
    if (points == null || points.length == 0) {
      return 0;
    }

    java.util.Arrays.sort(
        points,
        (a, b) -> {
          if (a[1] < b[1]) return -1;
          if (a[1] > b[1]) return 1;
          return 0;
        });

    int arrows = 1;
    long lastShot = points[0][1];

    for (int i = 1; i < points.length; i++) {
      if (points[i][0] > lastShot) {
        arrows++;
        lastShot = points[i][1];
      }
    }

    return arrows;
  }

  // ===================== SECTION 4: SYSTEM DESIGN =====================

  /**
   * Least Frequently Used (LFU) Cache with O(1) get and put operations.
   *
   * <p><b>LeetCode 460 (Hard)</b>
   *
   * <p>Evicts least frequently used item when capacity exceeded. Breaks ties by LRU.
   */
  public static class LFUCache {
    private int capacity;
    private int minFrequency;
    private Map<Integer, Integer> keyToValue;
    private Map<Integer, Integer> keyToFreq;
    private Map<Integer, LinkedHashSet<Integer>> freqToKeys;

    /**
     * Initializes LFU cache with given capacity.
     *
     * <p><b>Time:</b> O(1) per operation <b>Space:</b> O(capacity)
     *
     * @param capacity maximum size of cache
     */
    public LFUCache(int capacity) {
      if (capacity <= 0) {
        throw new IllegalArgumentException("Capacity must be positive");
      }
      this.capacity = capacity;
      this.minFrequency = 0;
      this.keyToValue = new HashMap<>();
      this.keyToFreq = new HashMap<>();
      this.freqToKeys = new HashMap<>();
    }

    /**
     * Gets value for key, updating frequency.
     *
     * @param key the key to get
     * @return value if exists, -1 otherwise
     */
    public int get(int key) {
      if (!keyToValue.containsKey(key)) {
        return -1;
      }

      updateFrequency(key);
      return keyToValue.get(key);
    }

    /**
     * Puts key-value pair, evicting LFU item if needed.
     *
     * @param key the key
     * @param value the value
     */
    public void put(int key, int value) {
      if (capacity <= 0) {
        return;
      }

      if (keyToValue.containsKey(key)) {
        keyToValue.put(key, value);
        updateFrequency(key);
        return;
      }

      if (keyToValue.size() >= capacity) {
        evict();
      }

      keyToValue.put(key, value);
      keyToFreq.put(key, 1);
      freqToKeys.computeIfAbsent(1, k -> new LinkedHashSet<>()).add(key);
      minFrequency = 1;
    }

    /**
     * Updates frequency of a key.
     *
     * @param key the key to update
     */
    private void updateFrequency(int key) {
      int freq = keyToFreq.get(key);
      keyToFreq.put(key, freq + 1);

      freqToKeys.get(freq).remove(key);
      if (freqToKeys.get(freq).isEmpty()) {
        freqToKeys.remove(freq);
        if (freq == minFrequency) {
          minFrequency++;
        }
      }

      freqToKeys.computeIfAbsent(freq + 1, k -> new LinkedHashSet<>()).add(key);
    }

    /**
     * Evicts the least frequently used (or least recently used in LRU sense).
     */
    private void evict() {
      LinkedHashSet<Integer> keys = freqToKeys.get(minFrequency);
      int lruKey = keys.iterator().next();
      keys.remove(lruKey);

      keyToValue.remove(lruKey);
      keyToFreq.remove(lruKey);
    }
  }

  /**
   * Main method demonstrating advanced patterns.
   *
   * @param args unused
   */
  public static void main(String[] args) {
    System.out.println("=== Advanced Topics ===\n");

    // Section 1: Monotonic Stack
    System.out.println("1. Next Greater Elements (Circular):");
    int[] nums = {1, 2, 1};
    int[] result = nextGreaterElementsCircular(nums);
    System.out.println(java.util.Arrays.toString(result));

    System.out.println("\n2. Daily Temperatures:");
    int[] temps = {73, 74, 75, 71, 69, 72, 76, 73};
    result = dailyTemperatures(temps);
    System.out.println(java.util.Arrays.toString(result));

    System.out.println("\n3. Largest Rectangle:");
    int[] heights = {2, 1, 5, 6, 2, 3};
    System.out.println("Max area: " + largestRectangleInHistogram(heights));

    System.out.println("\n4. Trapping Rain Water:");
    int[] height = {0, 1, 0, 2, 1, 0, 1, 4, 3, 2, 1, 2, 1};
    System.out.println("Water trapped: " + trap(height));

    // Section 2: Prefix Sum
    System.out.println("\n5. Product Except Self:");
    int[] nums2 = {1, 2, 3, 4};
    result = productExceptSelf(nums2);
    System.out.println(java.util.Arrays.toString(result));

    System.out.println("\n6. Subarrays Divisible by K:");
    int[] nums3 = {4, 5, 0, -2, -3, 1};
    System.out.println("Count: " + subarraysDivByK(nums3, 5));

    // Section 3: Intervals
    System.out.println("\n7. Min Meeting Rooms:");
    int[][] intervals = {{0, 30}, {5, 10}, {15, 20}};
    System.out.println("Rooms needed: " + minMeetingRooms(intervals));

    // Section 4: LFU Cache
    System.out.println("\n8. LFU Cache:");
    LFUCache cache = new LFUCache(CACHE_SIZE_EXAMPLE);
    cache.put(1, 1);
    cache.put(2, 2);
    System.out.println("Get 1: " + cache.get(1));
    cache.put(3, 3);
    System.out.println("Get 2: " + cache.get(2));
  }
}
