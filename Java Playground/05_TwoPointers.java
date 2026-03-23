import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Two-Pointer Template & Techniques.
 *
 * <p>Two pointers is a technique where two pointers traverse an array/string from
 * different positions based on a condition. Key patterns:
 *
 * <p><b>OPPOSITE DIRECTION:</b> Initialize pointers at both ends, converge toward
 * center. Best for sorted arrays, palindromes, container problems. Condition typically
 * checks sum or comparison at current positions.
 *
 * <p><b>SAME DIRECTION:</b> Fast pointer explores, slow pointer builds or maintains
 * result. Common for removals (remove duplicates, remove element), moves (move zeroes).
 * Slower pointer always ≤ faster pointer.
 *
 * <p><b>PARTITION:</b> Rearrange in-place using pointers to mark regions (Dutch Flag).
 *
 * <p><b>VS SLIDING WINDOW:</b> Two pointers ideal for sorted input requiring fixed
 * operations. Sliding window for contiguous subarrays with dynamic window size.
 *
 * <p>Time: O(n) for single pass, O(n log n) with pre-sort. Space: O(1) in-place or
 * O(n) for output.
 */
public class TwoPointers {

  /**
   * Two Sum - Sorted Array.
   *
   * @param numbers sorted array (1-indexed in LeetCode, 0-indexed here)
   * @param target sum to find
   * @return int[] with two indices that sum to target [idx1, idx2] or [-1, -1]
   *     if not found
   * @throws NullPointerException if numbers is null
   *
   *         <p>LeetCode 167 (Medium). Time: O(n). Space: O(1).
   *
   *         <p>Opposite direction: left at start, right at end. If sum too small,
   *         move left right. If sum too large, move right left.
   */
  public static int[] twoSumSorted(int[] numbers, int target) {
    if (numbers == null || numbers.length < 2) {
      return new int[]{-1, -1};
    }

    int left = 0;
    int right = numbers.length - 1;

    while (left < right) {
      int sum = numbers[left] + numbers[right];
      if (sum == target) {
        return new int[]{left + 1, right + 1}; // 1-indexed for LeetCode
      } else if (sum < target) {
        left++;
      } else {
        right--;
      }
    }

    return new int[]{-1, -1};
  }

  /**
   * Three Sum - Find all unique triplets summing to zero.
   *
   * @param nums input array (may contain duplicates)
   * @return List of lists, each containing 3 integers that sum to 0, no duplicates
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 15 (Medium). Time: O(n²). Space: O(1) excluding output.
   *
   *         <p>Sort first O(n log n). For each element, use two-pointer on
   *         remaining to find pairs. Skip duplicates carefully.
   */
  public static List<List<Integer>> threeSum(int[] nums) {
    List<List<Integer>> result = new ArrayList<>();

    if (nums == null || nums.length < 3) {
      return result;
    }

    Arrays.sort(nums);

    for (int i = 0; i < nums.length - 2; i++) {
      // Optimization: if nums[i] > 0, no triplet sums to 0
      if (nums[i] > 0) {
        break;
      }

      // Skip duplicate first element
      if (i > 0 && nums[i] == nums[i - 1]) {
        continue;
      }

      int left = i + 1;
      int right = nums.length - 1;
      int target = -nums[i];

      while (left < right) {
        int sum = nums[left] + nums[right];
        if (sum == target) {
          result.add(Arrays.asList(nums[i], nums[left], nums[right]));

          // Skip duplicates for left
          while (left < right && nums[left] == nums[left + 1]) {
            left++;
          }
          // Skip duplicates for right
          while (left < right && nums[right] == nums[right - 1]) {
            right--;
          }

          left++;
          right--;
        } else if (sum < target) {
          left++;
        } else {
          right--;
        }
      }
    }

    return result;
  }

  /**
   * Four Sum - Find all unique quadruplets summing to target.
   *
   * @param nums input array
   * @param target sum to find
   * @return List of lists, each containing 4 integers that sum to target
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 18 (Medium). Time: O(n³). Space: O(1) excluding output.
   *
   *         <p>Sort, then nested loops. For each pair (i, j), use two-pointer on
   *         remaining. Watch for integer overflow with target.
   */
  public static List<List<Integer>> fourSum(int[] nums, int target) {
    List<List<Integer>> result = new ArrayList<>();

    if (nums == null || nums.length < 4) {
      return result;
    }

    Arrays.sort(nums);

    for (int i = 0; i < nums.length - 3; i++) {
      // Skip duplicate outer element
      if (i > 0 && nums[i] == nums[i - 1]) {
        continue;
      }

      // Optimization: if nums[i] * 4 > target, no quadruplet possible
      if ((long) nums[i] * 4 > target) {
        break;
      }

      for (int j = i + 1; j < nums.length - 2; j++) {
        // Skip duplicate inner element
        if (j > i + 1 && nums[j] == nums[j - 1]) {
          continue;
        }

        // Optimization: if nums[i] + nums[j] * 3 > target, no quadruplet
        if ((long) nums[i] + (long) nums[j] * 3 > target) {
          break;
        }

        int left = j + 1;
        int right = nums.length - 1;
        long twoSum = (long) target - nums[i] - nums[j];

        while (left < right) {
          long sum = (long) nums[left] + nums[right];
          if (sum == twoSum) {
            result.add(
                Arrays.asList(nums[i], nums[j], nums[left], nums[right]));

            // Skip duplicates
            while (left < right && nums[left] == nums[left + 1]) {
              left++;
            }
            while (left < right && nums[right] == nums[right - 1]) {
              right--;
            }

            left++;
            right--;
          } else if (sum < twoSum) {
            left++;
          } else {
            right--;
          }
        }
      }
    }

    return result;
  }

  /**
   * Container With Most Water - Find max area between two vertical lines.
   *
   * @param height array where height[i] is the vertical line at position i
   * @return maximum area of water that can be contained
   * @throws NullPointerException if height is null
   *
   *         <p>LeetCode 11 (Medium). Time: O(n). Space: O(1).
   *
   *         <p>Opposite direction: start with widest container, greedily shrink
   *         from the side with smaller height (it's the limiting factor).
   */
  public static int containerWithMostWater(int[] height) {
    if (height == null || height.length < 2) {
      return 0;
    }

    int maxArea = 0;
    int left = 0;
    int right = height.length - 1;

    while (left < right) {
      int width = right - left;
      int currentHeight = Math.min(height[left], height[right]);
      int area = width * currentHeight;
      maxArea = Math.max(maxArea, area);

      // Move the pointer pointing to smaller height (to find potentially taller
      // line)
      if (height[left] < height[right]) {
        left++;
      } else {
        right--;
      }
    }

    return maxArea;
  }

  /**
   * Remove Duplicates from Sorted Array (in-place).
   *
   * @param nums sorted array with possible duplicates
   * @return count of unique elements; first k elements contain unique values
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 26 (Easy). Time: O(n). Space: O(1).
   *
   *         <p>Same direction: slow pointer (write position), fast pointer
   *         (exploration). When nums[fast] != nums[slow], increment slow and
   *         copy nums[fast] to nums[slow].
   */
  public static int removeDuplicates(int[] nums) {
    if (nums == null || nums.length == 0) {
      return 0;
    }

    int slow = 0;

    for (int fast = 1; fast < nums.length; fast++) {
      if (nums[fast] != nums[slow]) {
        slow++;
        nums[slow] = nums[fast];
      }
    }

    return slow + 1;
  }

  /**
   * Remove Element (in-place).
   *
   * @param nums input array
   * @param val value to remove
   * @return count of elements not equal to val; first k elements don't contain
   *     val
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 27 (Easy). Time: O(n). Space: O(1).
   *
   *         <p>Same direction: slow tracks position for non-val elements. When
   *         nums[fast] != val, copy to nums[slow] and increment slow.
   */
  public static int removeElement(int[] nums, int val) {
    if (nums == null) {
      return 0;
    }

    int slow = 0;

    for (int fast = 0; fast < nums.length; fast++) {
      if (nums[fast] != val) {
        nums[slow] = nums[fast];
        slow++;
      }
    }

    return slow;
  }

  /**
   * Move Zeroes (in-place, maintain relative order).
   *
   * @param nums input array
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 283 (Easy). Time: O(n). Space: O(1).
   *
   *         <p>Same direction: slow tracks non-zero position. Move all non-zeros
   *         to front, then fill rest with zeros.
   */
  public static void moveZeroes(int[] nums) {
    if (nums == null) {
      return;
    }

    int slow = 0;

    // Move all non-zero elements to the front
    for (int fast = 0; fast < nums.length; fast++) {
      if (nums[fast] != 0) {
        nums[slow] = nums[fast];
        slow++;
      }
    }

    // Fill remaining with zeros
    while (slow < nums.length) {
      nums[slow] = 0;
      slow++;
    }
  }

  /**
   * Sort Colors (Dutch Flag problem, in-place).
   *
   * @param nums array containing only 0, 1, 2 (representing red, white, blue)
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 75 (Medium). Time: O(n). Space: O(1).
   *
   *         <p>Partition using three pointers: left (0s boundary), right (2s
   *         boundary), mid (current). Swap to maintain invariant:
   *         [0..left-1] = 0, [left..mid-1] = 1, [right+1..end] = 2.
   */
  public static void sortColors(int[] nums) {
    if (nums == null) {
      return;
    }

    int left = 0;   // boundary for 0s
    int mid = 0;    // current position
    int right = nums.length - 1; // boundary for 2s

    while (mid <= right) {
      if (nums[mid] == 0) {
        swap(nums, left, mid);
        left++;
        mid++;
      } else if (nums[mid] == 1) {
        mid++;
      } else { // nums[mid] == 2
        swap(nums, mid, right);
        right--;
      }
    }
  }

  /**
   * Valid Palindrome II (allow one deletion).
   *
   * @param s input string
   * @return true if string is palindrome or can be made palindrome by deleting
   *     at most one character
   * @throws NullPointerException if s is null
   *
   *         <p>LeetCode 680 (Medium). Time: O(n). Space: O(1).
   *
   *         <p>Opposite direction: converge from both ends. On mismatch, try
   *         deleting either left or right character and check if remaining is
   *         valid palindrome.
   */
  public static boolean validPalindrome(String s) {
    if (s == null) {
      return false;
    }

    int left = 0;
    int right = s.length() - 1;

    while (left < right) {
      if (s.charAt(left) != s.charAt(right)) {
        // Try deleting left or right character
        return isPalindrome(s, left + 1, right) ||
               isPalindrome(s, left, right - 1);
      }
      left++;
      right--;
    }

    return true;
  }

  /**
   * Helper: check if s[left..right] is valid palindrome.
   *
   * @param s input string
   * @param left left boundary
   * @param right right boundary
   * @return true if s[left..right] is palindrome
   */
  private static boolean isPalindrome(String s, int left, int right) {
    while (left < right) {
      if (s.charAt(left) != s.charAt(right)) {
        return false;
      }
      left++;
      right--;
    }
    return true;
  }

  /**
   * Trap Rainwater (two-pointer approach).
   *
   * @param height array of bar heights
   * @return total water trapped between bars
   * @throws NullPointerException if height is null
   *
   *         <p>LeetCode 42 (Hard). Time: O(n). Space: O(1).
   *
   *         <p>Key insight: water at position i depends on max height to left
   *         and right. Use two pointers from both ends, maintain max seen so far
   *         on each side. Move pointer pointing to smaller height (limits water
   *         at that position).
   */
  public static int trap(int[] height) {
    if (height == null || height.length == 0) {
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
   * Main method demonstrating all two-pointer techniques.
   */
  public static void main(String[] args) {
    System.out.println("=== TWO POINTERS TECHNIQUES ===\n");

    // Two Sum Sorted
    int[] numbers = {2, 7, 11, 15};
    int[] result = twoSumSorted(numbers, 9);
    System.out.println("Two Sum (Sorted): " + Arrays.toString(result));

    // Three Sum
    int[] nums = {-1, 0, 1, 2, -1, -4};
    List<List<Integer>> triplets = threeSum(nums);
    System.out.println("Three Sum: " + triplets);

    // Four Sum
    int[] nums2 = {1000000000, 1000000000, 1000000000, 1000000000};
    List<List<Integer>> quadruplets = fourSum(nums2, -294967296);
    System.out.println("Four Sum: " + quadruplets);

    // Container With Most Water
    int[] height1 = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    System.out.println("Container Max Area: " + containerWithMostWater(height1));

    // Remove Duplicates
    int[] arr1 = {1, 1, 2};
    int len = removeDuplicates(arr1);
    System.out.println("Remove Duplicates: length=" + len + ", arr=" +
        Arrays.toString(Arrays.copyOf(arr1, len)));

    // Remove Element
    int[] arr2 = {3, 2, 2, 3};
    int len2 = removeElement(arr2, 3);
    System.out.println("Remove Element (val=3): length=" + len2);

    // Move Zeroes
    int[] arr3 = {0, 1, 0, 3, 12};
    moveZeroes(arr3);
    System.out.println("Move Zeroes: " + Arrays.toString(arr3));

    // Sort Colors
    int[] arr4 = {2, 0, 2, 1, 1, 0};
    sortColors(arr4);
    System.out.println("Sort Colors: " + Arrays.toString(arr4));

    // Valid Palindrome II
    String s1 = "abca";
    System.out.println("Valid Palindrome II (abca): " + validPalindrome(s1));

    // Trap Rainwater
    int[] height2 = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    System.out.println("Trap Rainwater: " + trap(height2));
  }
}
