import java.util.Arrays;

/**
 * Binary Search Template & Variants.
 *
 * <p><b>CORE INVARIANT:</b> Maintain arr[left..mid-1] < target ≤ arr[mid..right]
 * (or similar depending on search type).
 *
 * <p><b>LOOP CONDITION:</b>
 * - Use `left < right` when searching for a boundary (first/last occurrence).
 * - Use `left <= right` when searching for exact match and returning -1 if not found.
 *
 * <p><b>MID CALCULATION:</b> Always use `mid = left + (right - left) / 2` to avoid
 * integer overflow. NEVER use `(left + right) / 2`.
 *
 * <p><b>BINARY SEARCH ON ANSWER:</b> Instead of searching array, define feasibility
 * function and binary search on answer space (e.g., min eating speed, min allocation).
 *
 * <p>Time: O(log n) for standard, O(log n * check) for answer space. Space: O(1).
 */
public class BinarySearch {

  /**
   * Standard Binary Search - Find exact match.
   *
   * @param nums sorted array
   * @param target value to find
   * @return index of target if found, -1 otherwise
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 704 (Easy). Time: O(log n). Space: O(1).
   *
   *         <p>Use `left <= right` for exact match. Return immediately when
   *         found.
   */
  public static int search(int[] nums, int target) {
    if (nums == null) {
      return -1;
    }

    int left = 0;
    int right = nums.length - 1;

    while (left <= right) {
      int mid = left + (right - left) / 2;

      if (nums[mid] == target) {
        return mid;
      } else if (nums[mid] < target) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }

    return -1;
  }

  /**
   * Search Insert Position.
   *
   * @param nums sorted array
   * @param target value to find or insert
   * @return index where target is found, or where it should be inserted to
   *     maintain sorted order
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 35 (Easy). Time: O(log n). Space: O(1).
   *
   *         <p>Use `left < right` to find left boundary. At end, left is
   *         insertion position.
   */
  public static int searchInsertPosition(int[] nums, int target) {
    if (nums == null) {
      return 0;
    }

    int left = 0;
    int right = nums.length;

    while (left < right) {
      int mid = left + (right - left) / 2;

      if (nums[mid] < target) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }

    return left;
  }

  /**
   * Find First Occurrence of target (smallest index).
   *
   * @param nums sorted array (may have duplicates)
   * @param target value to find
   * @return smallest index where nums[i] == target, or -1 if not found
   * @throws NullPointerException if nums is null
   *
   *         <p>Time: O(log n). Space: O(1).
   *
   *         <p>Use `left < right` to find boundary. When nums[mid] == target,
   *         move right = mid to keep searching left. At end, check if nums[left]
   *         == target.
   */
  public static int findFirstOccurrence(int[] nums, int target) {
    if (nums == null || nums.length == 0) {
      return -1;
    }

    int left = 0;
    int right = nums.length;

    while (left < right) {
      int mid = left + (right - left) / 2;

      if (nums[mid] < target) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }

    return left < nums.length && nums[left] == target ? left : -1;
  }

  /**
   * Find Last Occurrence of target (largest index).
   *
   * @param nums sorted array (may have duplicates)
   * @param target value to find
   * @return largest index where nums[i] == target, or -1 if not found
   * @throws NullPointerException if nums is null
   *
   *         <p>Time: O(log n). Space: O(1).
   *
   *         <p>Use `left < right` to find boundary. When nums[mid] == target,
   *         move left = mid + 1 to keep searching right. At end, check if
   *         nums[right - 1] == target.
   */
  public static int findLastOccurrence(int[] nums, int target) {
    if (nums == null || nums.length == 0) {
      return -1;
    }

    int left = 0;
    int right = nums.length;

    while (left < right) {
      int mid = left + (right - left) / 2;

      if (nums[mid] <= target) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }

    return left > 0 && nums[left - 1] == target ? left - 1 : -1;
  }

  /**
   * Search Range - Find first and last occurrence in one call.
   *
   * @param nums sorted array
   * @param target value to find
   * @return int[] {first, last} indices, or {-1, -1} if not found
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 34 (Medium). Time: O(log n). Space: O(1).
   *
   *         <p>Call findFirstOccurrence and findLastOccurrence helper functions.
   */
  public static int[] searchRange(int[] nums, int target) {
    if (nums == null || nums.length == 0) {
      return new int[]{-1, -1};
    }

    int first = findFirstOccurrence(nums, target);
    if (first == -1) {
      return new int[]{-1, -1};
    }

    int last = findLastOccurrence(nums, target);
    return new int[]{first, last};
  }

  /**
   * Search in Rotated Sorted Array (unknown pivot).
   *
   * @param nums rotated sorted array with distinct elements
   * @param target value to find
   * @return index of target, or -1 if not found
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 33 (Medium). Time: O(log n). Space: O(1).
   *
   *         <p>Determine which half is sorted, check if target in sorted half.
   *         If yes, search that half; else search other half.
   */
  public static int searchInRotatedArray(int[] nums, int target) {
    if (nums == null || nums.length == 0) {
      return -1;
    }

    int left = 0;
    int right = nums.length - 1;

    while (left <= right) {
      int mid = left + (right - left) / 2;

      if (nums[mid] == target) {
        return mid;
      }

      // Determine which half is sorted
      if (nums[left] <= nums[mid]) {
        // Left half is sorted
        if (nums[left] <= target && target < nums[mid]) {
          // Target in sorted left half
          right = mid - 1;
        } else {
          left = mid + 1;
        }
      } else {
        // Right half is sorted
        if (nums[mid] < target && target <= nums[right]) {
          // Target in sorted right half
          left = mid + 1;
        } else {
          right = mid - 1;
        }
      }
    }

    return -1;
  }

  /**
   * Find Minimum in Rotated Sorted Array.
   *
   * @param nums rotated sorted array with distinct elements
   * @return minimum element
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 153 (Medium). Time: O(log n). Space: O(1).
   *
   *         <p>Rotation point where min occurs. If nums[mid] > nums[right],
   *         min is in right half. If nums[mid] <= nums[right], min is in left
   *         half (including mid).
   */
  public static int findMinInRotatedArray(int[] nums) {
    if (nums == null || nums.length == 0) {
      return Integer.MIN_VALUE;
    }

    int left = 0;
    int right = nums.length - 1;

    // Already sorted (no rotation)
    if (nums[left] <= nums[right]) {
      return nums[left];
    }

    while (left < right) {
      int mid = left + (right - left) / 2;

      if (nums[mid] > nums[right]) {
        // Minimum in right half
        left = mid + 1;
      } else {
        // Minimum in left half or at mid
        right = mid;
      }
    }

    return nums[left];
  }

  /**
   * Koko Eating Bananas (binary search on answer space).
   *
   * @param piles array of pile sizes
   * @param h hours available
   * @return minimum eating speed (bananas per hour) to finish all piles
   * @throws NullPointerException if piles is null
   *
   *         <p>LeetCode 875 (Medium). Time: O(n log m) where m = max pile size.
   *         Space: O(1).
   *
   *         <p>Search on answer space [1, max(piles)]. For each speed, check if
   *         Koko can finish in h hours.
   */
  public static int kokoEatingBananas(int[] piles, int h) {
    if (piles == null || piles.length == 0) {
      return 0;
    }

    int left = 1;
    int right = 0;
    for (int pile : piles) {
      right = Math.max(right, pile);
    }

    while (left < right) {
      int mid = left + (right - left) / 2;

      if (canFinish(piles, mid, h)) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }

    return left;
  }

  /**
   * Helper: can Koko eat all piles at given speed in h hours?
   *
   * @param piles array of pile sizes
   * @param speed eating speed (bananas/hour)
   * @param h available hours
   * @return true if can finish all piles
   */
  private static boolean canFinish(int[] piles, int speed, int h) {
    long hours = 0;
    for (int pile : piles) {
      hours += (pile + speed - 1) / speed; // Ceiling division
    }
    return hours <= h;
  }

  /**
   * Split Array Largest Sum (binary search on answer space).
   *
   * @param nums array to split
   * @param k number of subarrays to split into
   * @return minimized largest sum among all k subarrays
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 410 (Hard). Time: O(n log(sum)).
   *         Space: O(1).
   *
   *         <p>Binary search on answer: largest possible sum. For each sum,
   *         check if can split into k subarrays where each sum ≤ answer.
   */
  public static int splitArrayLargestSum(int[] nums, int k) {
    if (nums == null || nums.length == 0) {
      return 0;
    }

    int left = 0;
    int right = 0;

    for (int num : nums) {
      left = Math.max(left, num);  // At least largest element
      right += num;                // At most total sum
    }

    while (left < right) {
      int mid = left + (right - left) / 2;

      if (canSplit(nums, mid, k)) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }

    return left;
  }

  /**
   * Helper: can split array into k subarrays where each sum ≤ maxSum?
   *
   * @param nums input array
   * @param maxSum maximum allowed sum per subarray
   * @param k number of subarrays
   * @return true if possible
   */
  private static boolean canSplit(int[] nums, int maxSum, int k) {
    int subarrays = 1;
    long currentSum = 0;

    for (int num : nums) {
      if (currentSum + num > maxSum) {
        subarrays++;
        currentSum = num;

        if (subarrays > k) {
          return false;
        }
      } else {
        currentSum += num;
      }
    }

    return true;
  }

  /**
   * Ship Packages Within Days (binary search on answer space).
   *
   * @param weights array of package weights
   * @param days number of days to ship all packages
   * @return minimum capacity (weight per day) required
   * @throws NullPointerException if weights is null
   *
   *         <p>LeetCode 1011 (Medium). Time: O(n log(sum)).
   *         Space: O(1).
   *
   *         <p>Binary search on capacity [max weight, total weight]. Check if
   *         given capacity allows shipping in days.
   */
  public static int shipPackagesWithinDays(int[] weights, int days) {
    if (weights == null || weights.length == 0) {
      return 0;
    }

    int left = 0;
    int right = 0;

    for (int w : weights) {
      left = Math.max(left, w);
      right += w;
    }

    while (left < right) {
      int mid = left + (right - left) / 2;

      if (canShip(weights, mid, days)) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }

    return left;
  }

  /**
   * Helper: can ship all packages in days with given capacity?
   *
   * @param weights array of weights
   * @param capacity capacity per day
   * @param days days available
   * @return true if possible
   */
  private static boolean canShip(int[] weights, int capacity, int days) {
    int daysNeeded = 1;
    long currentWeight = 0;

    for (int w : weights) {
      if (currentWeight + w > capacity) {
        daysNeeded++;
        currentWeight = w;

        if (daysNeeded > days) {
          return false;
        }
      } else {
        currentWeight += w;
      }
    }

    return true;
  }

  /**
   * Search Matrix (2D, treated as 1D sorted array).
   *
   * @param matrix 2D sorted matrix (row-wise and column-wise)
   * @param target value to find
   * @return true if target found, false otherwise
   * @throws NullPointerException if matrix is null
   *
   *         <p>LeetCode 74 (Medium). Time: O(log(m*n)).
   *         Space: O(1).
   *
   *         <p>Treat 2D matrix as flattened 1D array. mid -> [mid/cols][mid%cols].
   */
  public static boolean searchMatrix(int[][] matrix, int target) {
    if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
      return false;
    }

    int rows = matrix.length;
    int cols = matrix[0].length;
    int left = 0;
    int right = rows * cols - 1;

    while (left <= right) {
      int mid = left + (right - left) / 2;
      int val = matrix[mid / cols][mid % cols];

      if (val == target) {
        return true;
      } else if (val < target) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }

    return false;
  }

  /**
   * Search Matrix II (2D, row and column sorted but no overall ordering).
   *
   * @param matrix 2D matrix where each row and column is sorted
   * @param target value to find
   * @return true if target found, false otherwise
   * @throws NullPointerException if matrix is null
   *
   *         <p>LeetCode 240 (Medium). Time: O(m + n).
   *         Space: O(1).
   *
   *         <p>Start at top-right (or bottom-left). Move left if target smaller,
   *         move down if target larger.
   */
  public static boolean searchMatrixII(int[][] matrix, int target) {
    if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
      return false;
    }

    int row = 0;
    int col = matrix[0].length - 1;

    while (row < matrix.length && col >= 0) {
      if (matrix[row][col] == target) {
        return true;
      } else if (matrix[row][col] > target) {
        col--;
      } else {
        row++;
      }
    }

    return false;
  }

  /**
   * Find Peak Element (element greater than neighbors).
   *
   * @param nums input array
   * @return index of a peak element (element > neighbors)
   * @throws NullPointerException if nums is null
   *
   *         <p>LeetCode 162 (Medium). Time: O(log n).
   *         Space: O(1).
   *
   *         <p>Key: nums[-1] = nums[n] = -inf. Compare nums[mid] with
   *         nums[mid+1]: if nums[mid] < nums[mid+1], peak in right half;
   *         else in left half (including mid).
   */
  public static int findPeakElement(int[] nums) {
    if (nums == null || nums.length == 0) {
      return -1;
    }

    int left = 0;
    int right = nums.length - 1;

    while (left < right) {
      int mid = left + (right - left) / 2;

      if (nums[mid] < nums[mid + 1]) {
        // Peak in right half
        left = mid + 1;
      } else {
        // Peak in left half or at mid
        right = mid;
      }
    }

    return left;
  }

  /**
   * Main method demonstrating all binary search variants.
   */
  public static void main(String[] args) {
    System.out.println("=== BINARY SEARCH VARIANTS ===\n");

    // Standard search
    int[] arr1 = {-1, 0, 3, 5, 9, 12};
    System.out.println("Search: " + search(arr1, 9));

    // Search insert position
    int[] arr2 = {1, 3, 5, 6};
    System.out.println("Insert Position (target=5): " +
        searchInsertPosition(arr2, 5));

    // Search range
    int[] arr3 = {5, 7, 7, 8, 8, 10};
    System.out.println("Search Range (target=8): " +
        Arrays.toString(searchRange(arr3, 8)));

    // Rotated array search
    int[] arr4 = {4, 5, 6, 7, 0, 1, 2};
    System.out.println("Rotated Array Search (target=0): " +
        searchInRotatedArray(arr4, 0));

    // Find min in rotated
    int[] arr5 = {3, 4, 5, 1, 2};
    System.out.println("Find Min in Rotated: " +
        findMinInRotatedArray(arr5));

    // Koko eating bananas
    int[] piles = {1, 1, 1, 1};
    System.out.println("Koko Eating (h=4): " +
        kokoEatingBananas(piles, 4));

    // Split array
    int[] nums1 = {1, 2, 3, 4, 5};
    System.out.println("Split Array (k=2): " +
        splitArrayLargestSum(nums1, 2));

    // Ship packages
    int[] weights = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    System.out.println("Ship Packages (days=5): " +
        shipPackagesWithinDays(weights, 5));

    // Search matrix
    int[][] matrix1 = {{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}};
    System.out.println("Search Matrix (target=3): " +
        searchMatrix(matrix1, 3));

    // Search matrix II
    int[][] matrix2 = {{1, 4, 7, 11, 15}, {2, 5, 8, 12, 19},
        {3, 6, 9, 16, 22}, {10, 13, 14, 17, 24}, {18, 21, 23, 26, 30}};
    System.out.println("Search Matrix II (target=13): " +
        searchMatrixII(matrix2, 13));

    // Find peak
    int[] arr6 = {1, 2, 3, 1};
    System.out.println("Find Peak Element: " +
        findPeakElement(arr6));
  }
}
