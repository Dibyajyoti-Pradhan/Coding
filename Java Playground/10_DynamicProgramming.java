import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Dynamic Programming patterns: memoization, tabulation, space optimization.
 *
 * Covers linear DP (climbing stairs, house robber), grid DP (unique paths,
 * min path sum), knapsack variants (unbounded coin change, 0/1 subset
 * partition), LIS/LCS, palindromic DP, string DP, and stock trading.
 *
 * KEY INSIGHTS:
 * - Memoization (top-down): recursion + cache, intuitive
 * - Tabulation (bottom-up): iterative, no stack overflow, easy space optimize
 * - Space optimization: often reduce 2D DP to 1D (e.g., O(n²) → O(n))
 * - LIS O(n log n) via binary search (patience sorting)
 * - Stock problems: track states (buy, sell, cooldown)
 * - All methods include input validation; null inputs throw IllegalArgumentException
 */
public final class DynamicProgramming {

  private DynamicProgramming() {
    // Utility class; prevent instantiation
  }

  // ============================================================================
  // LINEAR DP
  // ============================================================================

  /**
   * Minimum steps to climb n stairs (1 or 2 steps per move).
   *
   * @param n the number of stairs (n >= 1)
   * @return number of unique ways to reach the top
   *
   * LeetCode 70, Easy. Example: n=3 → 3 (1+1+1, 1+2, 2+1)
   *
   * Time: O(n), Space: O(1) optimized (no need for full DP array).
   * Tricky: This is Fibonacci; dp[i] = dp[i-1] + dp[i-2].
   */
  public static int climbingStairs(int n) {
    if (n < 1) {
      throw new IllegalArgumentException("n must be >= 1");
    }
    if (n <= 2) {
      return n;
    }

    int prev = 1, curr = 2;
    for (int i = 3; i <= n; i++) {
      int temp = prev + curr;
      prev = curr;
      curr = temp;
    }
    return curr;
  }

  /**
   * Maximum sum of non-adjacent house robberies.
   *
   * @param nums array of house values (may not be null)
   * @return maximum sum achievable without robbing adjacent houses
   *
   * LeetCode 198, Medium. Example: [1,2,3,1] → 4 (houses 1 and 3)
   *
   * Time: O(n), Space: O(1) optimized.
   * Tricky: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
   */
  public static int houseRobber(int[] nums) {
    if (nums == null || nums.length == 0) {
      throw new IllegalArgumentException("nums must be non-null and non-empty");
    }
    if (nums.length == 1) {
      return nums[0];
    }

    int prev = 0, curr = nums[0];
    for (int i = 1; i < nums.length; i++) {
      int temp = Math.max(curr, prev + nums[i]);
      prev = curr;
      curr = temp;
    }
    return curr;
  }

  /**
   * Maximum sum of non-adjacent houses on a circular street.
   *
   * @param nums array of house values (may not be null)
   * @return maximum sum where houses form a circle (first and last are adjacent)
   *
   * LeetCode 213, Medium. Example: [1,2,3,1] → 3 (houses 1 or 3)
   *
   * Time: O(n), Space: O(1).
   * Tricky: Can't rob both first and last; try two cases and take max.
   */
  public static int houseRobberII(int[] nums) {
    if (nums == null || nums.length == 0) {
      throw new IllegalArgumentException("nums must be non-null and non-empty");
    }
    if (nums.length == 1) {
      return nums[0];
    }

    // Case 1: exclude first house
    int case1 = robLinear(nums, 1, nums.length - 1);
    // Case 2: exclude last house
    int case2 = robLinear(nums, 0, nums.length - 2);

    return Math.max(case1, case2);
  }

  private static int robLinear(int[] nums, int start, int end) {
    int prev = 0, curr = 0;
    for (int i = start; i <= end; i++) {
      int temp = Math.max(curr, prev + nums[i]);
      prev = curr;
      curr = temp;
    }
    return curr;
  }

  // ============================================================================
  // GRID DP
  // ============================================================================

  /**
   * Number of unique paths in m×n grid (move right or down only).
   *
   * @param m number of rows (m >= 1)
   * @param n number of columns (n >= 1)
   * @return number of unique paths from top-left to bottom-right
   *
   * LeetCode 62, Medium. Example: m=3, n=3 → 6
   *
   * Time: O(m*n), Space: O(m*n) or O(min(m,n)) optimized.
   * Tricky: Combinatorial solution is C(m+n-2, m-1); DP is intuitive.
   */
  public static int uniquePaths(int m, int n) {
    if (m < 1 || n < 1) {
      throw new IllegalArgumentException("m and n must be >= 1");
    }

    int[] dp = new int[n];
    Arrays.fill(dp, 1);

    for (int i = 1; i < m; i++) {
      for (int j = 1; j < n; j++) {
        dp[j] += dp[j - 1];
      }
    }

    return dp[n - 1];
  }

  /**
   * Minimum path sum from top-left to bottom-right in grid.
   *
   * @param grid integer grid (may not be null; all positive)
   * @return minimum sum path from [0][0] to [m-1][n-1]
   *
   * LeetCode 64, Medium. Example: [[1,3,1],[1,5,1],[4,2,1]] → 7
   *
   * Time: O(m*n), Space: O(m*n) or O(n) optimized.
   */
  public static int minPathSum(int[][] grid) {
    if (grid == null || grid.length == 0 || grid[0].length == 0) {
      throw new IllegalArgumentException("grid must be non-null and non-empty");
    }

    int m = grid.length;
    int n = grid[0].length;
    int[] dp = new int[n];

    dp[0] = grid[0][0];
    for (int j = 1; j < n; j++) {
      dp[j] = dp[j - 1] + grid[0][j];
    }

    for (int i = 1; i < m; i++) {
      dp[0] += grid[i][0];
      for (int j = 1; j < n; j++) {
        dp[j] = Math.min(dp[j], dp[j - 1]) + grid[i][j];
      }
    }

    return dp[n - 1];
  }

  // ============================================================================
  // KNAPSACK VARIANTS
  // ============================================================================

  /**
   * Minimum number of coins to make amount (unbounded knapsack).
   *
   * @param coins array of coin denominations (may not be null)
   * @param amount target amount (>= 0)
   * @return minimum coins needed; -1 if impossible
   *
   * LeetCode 322, Medium. Example: coins=[1,2,5], amount=5 → 1
   *
   * Time: O(amount * coins.length), Space: O(amount).
   * Tricky: Each coin can be used unlimited times.
   */
  public static int coinChange(int[] coins, int amount) {
    if (coins == null) {
      throw new IllegalArgumentException("coins must be non-null");
    }
    if (amount < 0) {
      throw new IllegalArgumentException("amount must be >= 0");
    }

    int[] dp = new int[amount + 1];
    Arrays.fill(dp, amount + 1);
    dp[0] = 0;

    for (int i = 1; i <= amount; i++) {
      for (int coin : coins) {
        if (coin <= i) {
          dp[i] = Math.min(dp[i], dp[i - coin] + 1);
        }
      }
    }

    return dp[amount] > amount ? -1 : dp[amount];
  }

  /**
   * Partition equal sum subsets (0/1 knapsack variant).
   *
   * @param nums array of integers (may not be null)
   * @return true if nums can be partitioned into two equal-sum subsets
   *
   * LeetCode 416, Medium. Example: [1,5,11,5] → true (5+5+1=11)
   *
   * Time: O(n * sum/2), Space: O(sum/2).
   * Tricky: If sum is odd, impossible. Use 1D DP for space.
   */
  public static boolean canPartitionEqualSubset(int[] nums) {
    if (nums == null || nums.length == 0) {
      throw new IllegalArgumentException("nums must be non-null and non-empty");
    }

    int sum = 0;
    for (int num : nums) {
      sum += num;
    }

    if (sum % 2 != 0) {
      return false;
    }

    int target = sum / 2;
    boolean[] dp = new boolean[target + 1];
    dp[0] = true;

    for (int num : nums) {
      for (int j = target; j >= num; j--) {
        dp[j] = dp[j] || dp[j - num];
      }
    }

    return dp[target];
  }

  // ============================================================================
  // LIS / LCS
  // ============================================================================

  /**
   * Length of longest increasing subsequence (binary search approach).
   *
   * @param nums array of integers (may not be null)
   * @return length of LIS
   *
   * LeetCode 300, Medium. Example: [10,9,2,5,3,7,101,18] → 4 ([2,3,7,101])
   *
   * Time: O(n log n) via binary search, Space: O(n).
   * Tricky: Maintain sorted tails[] where tails[i] = smallest tail of
   * increasing subsequence of length i+1.
   */
  public static int lengthOfLIS(int[] nums) {
    if (nums == null || nums.length == 0) {
      throw new IllegalArgumentException("nums must be non-null and non-empty");
    }

    int[] tails = new int[nums.length];
    int length = 0;

    for (int num : nums) {
      int pos = Arrays.binarySearch(tails, 0, length, num);
      if (pos < 0) {
        pos = -(pos + 1);
      }
      tails[pos] = num;
      if (pos == length) {
        length++;
      }
    }

    return length;
  }

  /**
   * Length of longest common subsequence between two strings.
   *
   * @param text1 first string (may not be null)
   * @param text2 second string (may not be null)
   * @return length of LCS
   *
   * LeetCode 1143, Medium. Example: text1="abc", text2="abc" → 3
   *
   * Time: O(m*n), Space: O(m*n) or O(n) optimized.
   */
  public static int longestCommonSubsequence(String text1, String text2) {
    if (text1 == null || text2 == null) {
      throw new IllegalArgumentException("texts must be non-null");
    }

    int m = text1.length();
    int n = text2.length();
    int[] prev = new int[n + 1];
    int[] curr = new int[n + 1];

    for (int i = 1; i <= m; i++) {
      for (int j = 1; j <= n; j++) {
        if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
          curr[j] = prev[j - 1] + 1;
        } else {
          curr[j] = Math.max(prev[j], curr[j - 1]);
        }
      }
      int[] temp = prev;
      prev = curr;
      curr = temp;
    }

    return prev[n];
  }

  // ============================================================================
  // PALINDROME DP
  // ============================================================================

  /**
   * Length of longest palindromic subsequence.
   *
   * @param s input string (may not be null)
   * @return length of longest palindromic subsequence
   *
   * LeetCode 516, Medium. Example: s="bbbab" → 4 ("bbbb")
   *
   * Time: O(n²), Space: O(n²).
   * Tricky: LPS(s) = LCS(s, reverse(s))
   */
  public static int longestPalindromicSubsequence(String s) {
    if (s == null) {
      throw new IllegalArgumentException("s must be non-null");
    }
    if (s.isEmpty()) {
      return 0;
    }

    String reversed = new StringBuilder(s).reverse().toString();
    return longestCommonSubsequence(s, reversed);
  }

  /**
   * Minimum cuts to make string palindromes (hard).
   *
   * @param s input string (may not be null)
   * @return minimum number of cuts to partition s into palindromes
   *
   * LeetCode 132, Hard. Example: s="nitin" → 0 (already palindrome)
   *
   * Time: O(n²), Space: O(n²).
   * Tricky: Precompute palindrome table, then dp[i] = min(dp[j] + 1)
   * for all j < i where s[j+1:i+1] is palindrome.
   */
  public static int minCutsPalindrome(String s) {
    if (s == null) {
      throw new IllegalArgumentException("s must be non-null");
    }
    if (s.isEmpty()) {
      return 0;
    }

    int n = s.length();
    boolean[][] isPalin = new boolean[n][n];

    // Build palindrome table
    for (int i = 0; i < n; i++) {
      isPalin[i][i] = true;
    }
    for (int i = 0; i < n - 1; i++) {
      if (s.charAt(i) == s.charAt(i + 1)) {
        isPalin[i][i + 1] = true;
      }
    }
    for (int len = 3; len <= n; len++) {
      for (int i = 0; i <= n - len; i++) {
        int j = i + len - 1;
        if (s.charAt(i) == s.charAt(j) && isPalin[i + 1][j - 1]) {
          isPalin[i][j] = true;
        }
      }
    }

    // DP for min cuts
    int[] dp = new int[n];
    for (int i = 0; i < n; i++) {
      if (isPalin[0][i]) {
        dp[i] = 0;
      } else {
        dp[i] = i;
        for (int j = 0; j < i; j++) {
          if (isPalin[j + 1][i]) {
            dp[i] = Math.min(dp[i], dp[j] + 1);
          }
        }
      }
    }

    return dp[n - 1];
  }

  // ============================================================================
  // STRING DP
  // ============================================================================

  /**
   * Edit distance (Levenshtein distance) between two strings.
   *
   * @param word1 first word (may not be null)
   * @param word2 second word (may not be null)
   * @return minimum number of operations (insert, delete, replace)
   *
   * LeetCode 72, Hard. Example: word1="horse", word2="ros" → 3
   *
   * Time: O(m*n), Space: O(m*n) or O(n) optimized.
   */
  public static int editDistance(String word1, String word2) {
    if (word1 == null || word2 == null) {
      throw new IllegalArgumentException("words must be non-null");
    }

    int m = word1.length();
    int n = word2.length();
    int[] prev = new int[n + 1];
    int[] curr = new int[n + 1];

    for (int j = 0; j <= n; j++) {
      prev[j] = j;
    }

    for (int i = 1; i <= m; i++) {
      curr[0] = i;
      for (int j = 1; j <= n; j++) {
        if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
          curr[j] = prev[j - 1];
        } else {
          curr[j] = 1 + Math.min(
              prev[j],      // delete
              Math.min(curr[j - 1], prev[j - 1]) // insert or replace
          );
        }
      }
      int[] temp = prev;
      prev = curr;
      curr = temp;
    }

    return prev[n];
  }

  /**
   * Check if word can be segmented using dictionary.
   *
   * @param s input string (may not be null)
   * @param wordDict list of dictionary words (may not be null)
   * @return true if s can be segmented into dictionary words
   *
   * LeetCode 139, Medium. Example: s="leetcode", dict=["leet","code"] →
   * true
   *
   * Time: O(n² * m) where m = avg word length, Space: O(n).
   * Tricky: dp[i] = true if s[0:i] can be segmented.
   */
  public static boolean wordBreak(String s, List<String> wordDict) {
    if (s == null || wordDict == null) {
      throw new IllegalArgumentException("s and wordDict must be non-null");
    }

    Set<String> dict = new HashSet<>(wordDict);
    boolean[] dp = new boolean[s.length() + 1];
    dp[0] = true;

    for (int i = 1; i <= s.length(); i++) {
      for (int j = 0; j < i; j++) {
        if (dp[j] && dict.contains(s.substring(j, i))) {
          dp[i] = true;
          break;
        }
      }
    }

    return dp[s.length()];
  }

  // ============================================================================
  // STOCK TRADING PROBLEMS
  // ============================================================================

  /**
   * Maximum profit with one transaction (buy once, sell once).
   *
   * @param prices array of daily prices (may not be null)
   * @return maximum profit; 0 if no profit possible
   *
   * LeetCode 121, Easy. Example: [7,1,5,3,6,4] → 5 (buy 1, sell 6)
   *
   * Time: O(n), Space: O(1).
   */
  public static int maxProfitOneTransaction(int[] prices) {
    if (prices == null || prices.length < 2) {
      throw new IllegalArgumentException("prices must have at least 2 elements");
    }

    int minPrice = prices[0];
    int maxProfit = 0;

    for (int i = 1; i < prices.length; i++) {
      maxProfit = Math.max(maxProfit, prices[i] - minPrice);
      minPrice = Math.min(minPrice, prices[i]);
    }

    return maxProfit;
  }

  /**
   * Maximum profit with unlimited transactions.
   *
   * @param prices array of daily prices (may not be null)
   * @return maximum profit; 0 if no profit possible
   *
   * LeetCode 122, Medium. Example: [7,1,5,3,6,4] → 7 (buy 1, sell 5,
   * buy 3, sell 6)
   *
   * Time: O(n), Space: O(1).
   * Tricky: Capture every upswing: profit += max(0, prices[i] - prices[i-1])
   */
  public static int maxProfitUnlimited(int[] prices) {
    if (prices == null || prices.length < 2) {
      throw new IllegalArgumentException("prices must have at least 2 elements");
    }

    int profit = 0;
    for (int i = 1; i < prices.length; i++) {
      if (prices[i] > prices[i - 1]) {
        profit += prices[i] - prices[i - 1];
      }
    }

    return profit;
  }

  /**
   * Maximum profit with cooldown (can't buy on next day after selling).
   *
   * @param prices array of daily prices (may not be null)
   * @return maximum profit with cooldown constraint
   *
   * LeetCode 309, Medium. Example: [3,3,5,0,0,3,1,4] → 6 (buy 3, sell 5,
   * cooldown, buy 0, sell 3, buy 1, sell 4)
   *
   * Time: O(n), Space: O(1).
   * Tricky: States: hold, sold, rest. dp transitions between them.
   */
  public static int maxProfitWithCooldown(int[] prices) {
    if (prices == null || prices.length < 2) {
      throw new IllegalArgumentException("prices must have at least 2 elements");
    }

    int hold = Integer.MIN_VALUE;
    int sold = 0;
    int rest = 0;

    for (int price : prices) {
      int prevHold = hold;
      int prevSold = sold;

      hold = Math.max(prevHold, rest - price);
      sold = prevHold + price;
      rest = Math.max(prevSold, rest);
    }

    return Math.max(sold, rest);
  }

  // ============================================================================
  // MAIN: Test cases for all methods
  // ============================================================================

  /**
   * Main method demonstrating all DP solutions.
   *
   * @param args not used
   */
  public static void main(String[] args) {
    System.out.println("=== Dynamic Programming ===\n");

    System.out.println("LINEAR DP:");
    System.out.println("Climbing Stairs (n=5): " + climbingStairs(5));
    System.out.println("House Robber [1,2,3,1]: " + houseRobber(
        new int[]{1, 2, 3, 1}));
    System.out.println("House Robber II (circular) [1,2,3,1]: "
        + houseRobberII(new int[]{1, 2, 3, 1}));

    System.out.println("\nGRID DP:");
    System.out.println("Unique Paths (3x3): " + uniquePaths(3, 3));
    System.out.println("Min Path Sum [[1,3,1],[1,5,1],[4,2,1]]: "
        + minPathSum(new int[][]{{1, 3, 1}, {1, 5, 1}, {4, 2, 1}}));

    System.out.println("\nKNAPSACK:");
    System.out.println("Coin Change [1,2,5], amount=5: " + coinChange(
        new int[]{1, 2, 5}, 5));
    System.out.println("Equal Partition [1,5,11,5]: " + canPartitionEqualSubset(
        new int[]{1, 5, 11, 5}));

    System.out.println("\nLIS / LCS:");
    System.out.println("LIS [10,9,2,5,3,7,101,18]: " + lengthOfLIS(
        new int[]{10, 9, 2, 5, 3, 7, 101, 18}));
    System.out.println("LCS 'abc' and 'abc': " + longestCommonSubsequence(
        "abc", "abc"));

    System.out.println("\nPALINDROME DP:");
    System.out.println("Longest Palindromic Subsequence 'bbbab': "
        + longestPalindromicSubsequence("bbbab"));
    System.out.println("Min Cuts Palindrome 'nitin': " + minCutsPalindrome(
        "nitin"));

    System.out.println("\nSTRING DP:");
    System.out.println("Edit Distance 'horse' -> 'ros': " + editDistance(
        "horse", "ros"));
    System.out.println("Word Break 'leetcode' [leet,code]: " + wordBreak(
        "leetcode", Arrays.asList("leet", "code")));

    System.out.println("\nSTOCK TRADING:");
    System.out.println("Max Profit One [7,1,5,3,6,4]: " + maxProfitOneTransaction(
        new int[]{7, 1, 5, 3, 6, 4}));
    System.out.println("Max Profit Unlimited [7,1,5,3,6,4]: " + maxProfitUnlimited(
        new int[]{7, 1, 5, 3, 6, 4}));
    System.out.println("Max Profit Cooldown [3,3,5,0,0,3,1,4]: "
        + maxProfitWithCooldown(new int[]{3, 3, 5, 0, 0, 3, 1, 4}));
  }
}
