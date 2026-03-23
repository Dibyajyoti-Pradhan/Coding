import java.util.ArrayList;
import java.util.Comparator;
import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Stack;

/**
 * Stack, Queue, Deque, and Heap patterns.
 *
 * Covers: basic stack (parentheses, string decoding), monotonic stack
 * (temperature, next greater, histogram, rain water), min stack with O(1)
 * getMin, monotonic deque for sliding window, heaps for top-k, kth largest,
 * and median finding.
 *
 * KEY INSIGHTS:
 * - Stack: LIFO, useful for balancing, precedence, backtracking
 * - Deque: bidirectional, great for sliding windows (monotonic)
 * - Monotonic stack: maintain increasing/decreasing invariant
 * - Heap (PriorityQueue): O(log n) insert/remove, not sorted
 * - Min heap for max problems (invert), max heap for min problems
 * - Two heaps for median: max heap ≤ min heap
 * - All methods include input validation; null inputs throw IllegalArgumentException
 */
public final class StackQueueHeap {

  private StackQueueHeap() {
    // Utility class; prevent instantiation
  }

  // ============================================================================
  // STACK - BASIC
  // ============================================================================

  /**
   * Validate parentheses/brackets/braces are properly balanced.
   *
   * @param s input string (may not be null)
   * @return true if valid, false otherwise
   *
   * LeetCode 20, Easy. Example: s="()" → true; s="([)]" → false
   *
   * Time: O(n), Space: O(n) stack.
   */
  public static boolean isValid(String s) {
    if (s == null) {
      throw new IllegalArgumentException("s must be non-null");
    }

    Stack<Character> stack = new Stack<>();
    Map<Character, Character> pairs = new HashMap<>();
    pairs.put(')', '(');
    pairs.put(']', '[');
    pairs.put('}', '{');

    for (char c : s.toCharArray()) {
      if (pairs.containsKey(c)) {
        if (stack.isEmpty() || stack.pop() != pairs.get(c)) {
          return false;
        }
      } else {
        stack.push(c);
      }
    }

    return stack.isEmpty();
  }

  /**
   * Decode string with patterns like "2[abc]3[cd]" → "abcabcdcdcd".
   *
   * @param s encoded string with integers and brackets (may not be null)
   * @return decoded string
   *
   * LeetCode 394, Medium. Example: "3[a2[c]]" → "accaccacc"
   *
   * Time: O(n + output length), Space: O(depth of nesting).
   * Tricky: Use stack to track numbers and strings at each nesting level.
   */
  public static String decodeString(String s) {
    if (s == null) {
      throw new IllegalArgumentException("s must be non-null");
    }

    Stack<Integer> numStack = new Stack<>();
    Stack<String> strStack = new Stack<>();
    StringBuilder current = new StringBuilder();
    int num = 0;

    for (char c : s.toCharArray()) {
      if (Character.isDigit(c)) {
        num = num * 10 + (c - '0');
      } else if (c == '[') {
        numStack.push(num);
        strStack.push(current.toString());
        current = new StringBuilder();
        num = 0;
      } else if (c == ']') {
        String prev = strStack.pop();
        int count = numStack.pop();
        StringBuilder temp = new StringBuilder(prev);
        for (int i = 0; i < count; i++) {
          temp.append(current);
        }
        current = temp;
      } else {
        current.append(c);
      }
    }

    return current.toString();
  }

  // ============================================================================
  // MONOTONIC STACK
  // ============================================================================

  /**
   * For each temperature, find days until a warmer day.
   *
   * @param temperatures array of daily temperatures (may not be null)
   * @return array where result[i] = days to wait for warmer (0 if none)
   *
   * LeetCode 739, Medium. Example: [73,74,75,71,69,72,76,73] → [1,1,4,2,1,1,0,0]
   *
   * Time: O(n), Space: O(n) for monotonic stack.
   * Tricky: Maintain decreasing stack of indices; pop when temp increases.
   */
  public static int[] dailyTemperatures(int[] temperatures) {
    if (temperatures == null || temperatures.length == 0) {
      throw new IllegalArgumentException(
          "temperatures must be non-null and non-empty");
    }

    int n = temperatures.length;
    int[] result = new int[n];
    Stack<Integer> stack = new Stack<>();

    for (int i = 0; i < n; i++) {
      while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
        int idx = stack.pop();
        result[idx] = i - idx;
      }
      stack.push(i);
    }

    return result;
  }

  /**
   * Next greater element in second array for each element in first array.
   *
   * @param nums1 subset array (may not be null)
   * @param nums2 source array (may not be null)
   * @return array of next greater elements for nums1; -1 if not found
   *
   * LeetCode 496, Easy. Example: nums1=[4,1,2], nums2=[1,3,4,2] →
   * [-1,3,-1]
   *
   * Time: O(n), Space: O(n).
   */
  public static int[] nextGreaterElement(int[] nums1, int[] nums2) {
    if (nums1 == null || nums2 == null) {
      throw new IllegalArgumentException(
          "nums1 and nums2 must be non-null");
    }

    Map<Integer, Integer> nextGreater = new HashMap<>();
    Stack<Integer> stack = new Stack<>();

    for (int num : nums2) {
      while (!stack.isEmpty() && stack.peek() < num) {
        nextGreater.put(stack.pop(), num);
      }
      stack.push(num);
    }

    int[] result = new int[nums1.length];
    for (int i = 0; i < nums1.length; i++) {
      result[i] = nextGreater.getOrDefault(nums1[i], -1);
    }

    return result;
  }

  /**
   * Largest rectangle in histogram.
   *
   * @param heights array of histogram bar heights (may not be null)
   * @return maximum area rectangle
   *
   * LeetCode 84, Hard. Example: [2,1,5,6,2,3] → 10 (bars 5 and 6)
   *
   * Time: O(n), Space: O(n) monotonic stack.
   * Tricky: For each bar, find left/right boundaries using stack.
   */
  public static int largestRectangleInHistogram(int[] heights) {
    if (heights == null || heights.length == 0) {
      throw new IllegalArgumentException("heights must be non-null and non-empty");
    }

    int maxArea = 0;
    Stack<Integer> stack = new Stack<>();

    for (int i = 0; i < heights.length; i++) {
      while (!stack.isEmpty() && heights[i] < heights[stack.peek()]) {
        int h = heights[stack.pop()];
        int width = stack.isEmpty() ? i : i - stack.peek() - 1;
        maxArea = Math.max(maxArea, h * width);
      }
      stack.push(i);
    }

    while (!stack.isEmpty()) {
      int h = heights[stack.pop()];
      int width = stack.isEmpty() ? heights.length : heights.length
          - stack.peek() - 1;
      maxArea = Math.max(maxArea, h * width);
    }

    return maxArea;
  }

  /**
   * Trapping rain water using stack approach.
   *
   * @param height array of elevation heights (may not be null)
   * @return total units of water trapped
   *
   * LeetCode 42, Hard. Example: [0,1,0,2,1,0,1,3,2,1,2,1] → 6
   *
   * Time: O(n), Space: O(n) stack.
   * Tricky: Use monotonic decreasing stack; pop when height increases.
   */
  public static int trappingRainWater(int[] height) {
    if (height == null || height.length == 0) {
      throw new IllegalArgumentException("height must be non-null and non-empty");
    }

    int water = 0;
    Stack<Integer> stack = new Stack<>();

    for (int i = 0; i < height.length; i++) {
      int h = height[i];
      while (!stack.isEmpty() && h > height[stack.peek()]) {
        int top = stack.pop();
        if (stack.isEmpty()) {
          break;
        }
        int boundedHeight = Math.min(h, height[stack.peek()]) - height[top];
        int width = i - stack.peek() - 1;
        water += boundedHeight * width;
      }
      stack.push(i);
    }

    return water;
  }

  // ============================================================================
  // DESIGN - MIN STACK
  // ============================================================================

  /**
   * Stack with O(1) getMin operation. Public for testing.
   */
  public static class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> minStack;

    /**
     * Initialize MinStack.
     */
    public MinStack() {
      this.stack = new Stack<>();
      this.minStack = new Stack<>();
    }

    /**
     * Push value onto stack.
     *
     * @param val the value to push
     */
    public void push(int val) {
      stack.push(val);
      if (minStack.isEmpty() || val <= minStack.peek()) {
        minStack.push(val);
      }
    }

    /**
     * Pop from stack.
     */
    public void pop() {
      if (stack.isEmpty()) {
        throw new IllegalStateException("Stack is empty");
      }
      int val = stack.pop();
      if (val == minStack.peek()) {
        minStack.pop();
      }
    }

    /**
     * Get top of stack.
     *
     * @return top value
     */
    public int top() {
      if (stack.isEmpty()) {
        throw new IllegalStateException("Stack is empty");
      }
      return stack.peek();
    }

    /**
     * Get minimum value in stack in O(1).
     *
     * @return the minimum value
     */
    public int getMin() {
      if (minStack.isEmpty()) {
        throw new IllegalStateException("Stack is empty");
      }
      return minStack.peek();
    }
  }

  // ============================================================================
  // DEQUE - SLIDING WINDOW MAXIMUM
  // ============================================================================

  /**
   * Maximum element in every sliding window of size k.
   *
   * @param nums array of integers (may not be null)
   * @param k window size (k >= 1)
   * @return array of maximum values for each window
   *
   * LeetCode 239, Hard. Example: nums=[1,3,-1,-3,5,3,6,7], k=3 →
   * [3,3,5,5,6,7]
   *
   * Time: O(n), Space: O(k) monotonic deque.
   * Tricky: Deque stores indices in decreasing order of values.
   */
  public static int[] maxSlidingWindow(int[] nums, int k) {
    if (nums == null || nums.length == 0 || k < 1 || k > nums.length) {
      throw new IllegalArgumentException("Invalid input");
    }

    int n = nums.length;
    int[] result = new int[n - k + 1];
    Deque<Integer> deque = new LinkedList<>();

    for (int i = 0; i < n; i++) {
      // Remove indices outside window
      if (!deque.isEmpty() && deque.peekFirst() < i - k + 1) {
        deque.pollFirst();
      }

      // Remove smaller elements from back
      while (!deque.isEmpty() && nums[deque.peekLast()] < nums[i]) {
        deque.pollLast();
      }

      deque.addLast(i);

      // Store max when window is full
      if (i >= k - 1) {
        result[i - k + 1] = nums[deque.peekFirst()];
      }
    }

    return result;
  }

  // ============================================================================
  // HEAP - TOP K
  // ============================================================================

  /**
   * Top k most frequent elements.
   *
   * @param nums array of integers (may not be null)
   * @param k number of top frequent elements to return (k >= 1)
   * @return array of k most frequent elements
   *
   * LeetCode 347, Medium. Example: nums=[1,1,1,2,2,3], k=2 → [1,2]
   *
   * Time: O(n + k log n), Space: O(n).
   * Tricky: Use min heap of size k; track by frequency.
   */
  public static int[] topKFrequent(int[] nums, int k) {
    if (nums == null || nums.length == 0 || k < 1) {
      throw new IllegalArgumentException("Invalid input");
    }

    Map<Integer, Integer> frequency = new HashMap<>();
    for (int num : nums) {
      frequency.put(num, frequency.getOrDefault(num, 0) + 1);
    }

    PriorityQueue<Integer> minHeap = new PriorityQueue<>(
        (a, b) -> frequency.get(a) - frequency.get(b));

    for (int num : frequency.keySet()) {
      minHeap.offer(num);
      if (minHeap.size() > k) {
        minHeap.poll();
      }
    }

    int[] result = new int[k];
    int idx = k - 1;
    while (!minHeap.isEmpty()) {
      result[idx--] = minHeap.poll();
    }

    return result;
  }

  /**
   * Kth largest element in array.
   *
   * @param nums array of integers (may not be null)
   * @param k rank (1-indexed; k=1 is maximum)
   * @return the kth largest value
   *
   * LeetCode 215, Medium. Example: nums=[3,2,1,5,6,4], k=2 → 5
   *
   * Time: O(n + k log n), Space: O(k).
   * Tricky: Use min heap of size k.
   */
  public static int kthLargest(int[] nums, int k) {
    if (nums == null || nums.length == 0 || k < 1 || k > nums.length) {
      throw new IllegalArgumentException("Invalid input");
    }

    PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    for (int num : nums) {
      minHeap.offer(num);
      if (minHeap.size() > k) {
        minHeap.poll();
      }
    }

    return minHeap.peek();
  }

  /**
   * K closest points to origin.
   *
   * @param points array of [x, y] coordinates (may not be null)
   * @param k number of closest points (k >= 1)
   * @return array of k closest points
   *
   * LeetCode 973, Medium. Example: points=[[1,3],[-2,2]], k=1 → [[-2,2]]
   *
   * Time: O(n + k log n), Space: O(k).
   */
  public static int[][] kClosestPoints(int[][] points, int k) {
    if (points == null || points.length == 0 || k < 1) {
      throw new IllegalArgumentException("Invalid input");
    }

    PriorityQueue<int[]> maxHeap = new PriorityQueue<>(
        (a, b) -> (b[0] * b[0] + b[1] * b[1])
            - (a[0] * a[0] + a[1] * a[1]));

    for (int[] point : points) {
      maxHeap.offer(point);
      if (maxHeap.size() > k) {
        maxHeap.poll();
      }
    }

    int[][] result = new int[k][2];
    int idx = 0;
    while (!maxHeap.isEmpty()) {
      result[idx++] = maxHeap.poll();
    }

    return result;
  }

  // ============================================================================
  // DESIGN - MEDIAN FINDER
  // ============================================================================

  /**
   * Find median dynamically as numbers are added. Public for testing.
   */
  public static class MedianFinder {
    private PriorityQueue<Integer> maxHeap;  // ≤ median
    private PriorityQueue<Integer> minHeap;  // ≥ median

    /**
     * Initialize MedianFinder.
     */
    public MedianFinder() {
      this.maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
      this.minHeap = new PriorityQueue<>();
    }

    /**
     * Add a number to the data structure.
     *
     * @param num the number to add
     */
    public void addNum(int num) {
      // Add to max heap first
      maxHeap.offer(num);

      // Ensure max heap <= min heap
      if (!maxHeap.isEmpty() && !minHeap.isEmpty()
          && maxHeap.peek() > minHeap.peek()) {
        int val = maxHeap.poll();
        minHeap.offer(val);
      }

      // Balance: minHeap can have at most 1 more element
      if (maxHeap.size() > minHeap.size() + 1) {
        int val = maxHeap.poll();
        minHeap.offer(val);
      }
    }

    /**
     * Return the median of all numbers added so far.
     *
     * @return the median
     */
    public double findMedian() {
      if (maxHeap.isEmpty()) {
        throw new IllegalStateException("No elements added");
      }

      if (maxHeap.size() == minHeap.size()) {
        return (maxHeap.peek() + minHeap.peek()) / 2.0;
      }
      return (double) maxHeap.peek();
    }
  }

  // ============================================================================
  // MAIN: Test cases for all methods
  // ============================================================================

  /**
   * Main method demonstrating all stack/queue/heap operations.
   *
   * @param args not used
   */
  public static void main(String[] args) {
    System.out.println("=== Stack, Queue, Heap ===\n");

    System.out.println("BASIC STACK:");
    System.out.println("Is Valid '()': " + isValid("()"));
    System.out.println("Is Valid '([)]': " + isValid("([)]"));
    System.out.println("Decode '3[a2[c]]': " + decodeString("3[a2[c]]"));

    System.out.println("\nMONOTONIC STACK:");
    System.out.println("Daily Temperatures [73,74,75,71,69,72,76,73]: "
        + java.util.Arrays.toString(
            dailyTemperatures(new int[]{73, 74, 75, 71, 69, 72, 76, 73})));

    System.out.println("Next Greater Element:");
    System.out.println(java.util.Arrays.toString(
        nextGreaterElement(new int[]{4, 1, 2}, new int[]{1, 3, 4, 2})));

    System.out.println("Largest Rectangle [2,1,5,6,2,3]: "
        + largestRectangleInHistogram(new int[]{2, 1, 5, 6, 2, 3}));

    System.out.println("Trapping Rain Water [0,1,0,2,1,0,1,3,2,1,2,1]: "
        + trappingRainWater(new int[]{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}));

    System.out.println("\nMIN STACK:");
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    System.out.println("Min: " + minStack.getMin());
    minStack.pop();
    System.out.println("Top: " + minStack.top());
    System.out.println("Min: " + minStack.getMin());

    System.out.println("\nSLIDING WINDOW MAX:");
    System.out.println("Max Sliding Window [1,3,-1,-3,5,3,6,7] k=3: "
        + java.util.Arrays.toString(maxSlidingWindow(
            new int[]{1, 3, -1, -3, 5, 3, 6, 7}, 3)));

    System.out.println("\nHEAP:");
    System.out.println("Top K Frequent [1,1,1,2,2,3] k=2: "
        + java.util.Arrays.toString(topKFrequent(new int[]{1, 1, 1, 2, 2, 3}, 2)));

    System.out.println("Kth Largest [3,2,1,5,6,4] k=2: "
        + kthLargest(new int[]{3, 2, 1, 5, 6, 4}, 2));

    System.out.println("\nMEDIAN FINDER:");
    MedianFinder mf = new MedianFinder();
    mf.addNum(1);
    System.out.println("Median after adding 1: " + mf.findMedian());
    mf.addNum(2);
    System.out.println("Median after adding 1,2: " + mf.findMedian());
    mf.addNum(3);
    System.out.println("Median after adding 1,2,3: " + mf.findMedian());
  }
}
