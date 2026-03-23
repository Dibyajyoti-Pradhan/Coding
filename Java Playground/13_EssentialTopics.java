import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Essential advanced topics: greedy, backtracking, bit manipulation, Trie, math.
 *
 * Covers: greedy interval problems (jump game, gas station, partition labels),
 * backtracking (permutations, combinations, subsets, N-Queens, word search),
 * bit manipulation (XOR, bit counting, reverse bits), Trie data structure,
 * and mathematical algorithms (GCD, primes, fast exponentiation).
 *
 * KEY INSIGHTS:
 * - Greedy: prove correctness before using; usually one pass
 * - Backtracking: explore all possibilities with pruning (DFS)
 * - Bit manipulation: XOR = toggle/find missing, AND = common bits
 * - Trie: O(L) search/insert where L = word length
 * - Prime: Sieve of Eratosthenes O(n log log n) finds all primes ≤ n
 * - All methods include input validation; null inputs throw IllegalArgumentException
 */
public final class EssentialTopics {

  private EssentialTopics() {
    // Utility class; prevent instantiation
  }

  // ============================================================================
  // GREEDY
  // ============================================================================

  /**
   * Check if we can reach the last index (greedy jump game).
   *
   * @param nums array where nums[i] = max jump length (may not be null)
   * @return true if last index is reachable from index 0
   *
   * LeetCode 55, Medium. Example: [2,3,1,1,4] → true; [3,2,1,0,4] → false
   *
   * Time: O(n), Space: O(1).
   * Tricky: Track max reachable index; can jump if current index ≤ max.
   */
  public static boolean canJump(int[] nums) {
    if (nums == null || nums.length == 0) {
      throw new IllegalArgumentException("nums must be non-null and non-empty");
    }

    int maxReach = 0;
    for (int i = 0; i < nums.length; i++) {
      if (i > maxReach) {
        return false;
      }
      maxReach = Math.max(maxReach, i + nums[i]);
    }

    return true;
  }

  /**
   * Minimum number of jumps to reach last index.
   *
   * @param nums array of positive integers (may not be null)
   * @return minimum jumps needed
   *
   * LeetCode 45, Medium. Example: [2,3,1,1,4] → 2 (jump 1 step, then 3)
   *
   * Time: O(n), Space: O(1).
   * Tricky: Track current and next max range; jump when at boundary.
   */
  public static int jump(int[] nums) {
    if (nums == null || nums.length < 2) {
      throw new IllegalArgumentException("nums must have ≥ 2 elements");
    }

    int jumps = 0;
    int currentMax = 0;
    int nextMax = 0;

    for (int i = 0; i < nums.length - 1; i++) {
      nextMax = Math.max(nextMax, i + nums[i]);

      if (i == currentMax) {
        jumps++;
        currentMax = nextMax;
      }
    }

    return jumps;
  }

  /**
   * Gas station: starting position to complete circuit exactly once.
   *
   * @param gas array of gas at each station (may not be null)
   * @param cost array of cost to travel to next station (may not be null)
   * @return starting station index; -1 if impossible
   *
   * LeetCode 134, Medium. Example: gas=[1,2,3,4,5], cost=[3,4,5,1,2] → 3
   *
   * Time: O(n), Space: O(1).
   * Tricky: If total gas < total cost, return -1. Otherwise, unique answer.
   */
  public static int canCompleteCircuit(int[] gas, int[] cost) {
    if (gas == null || cost == null || gas.length != cost.length) {
      throw new IllegalArgumentException("gas and cost must be non-null and equal length");
    }

    int totalGas = 0;
    int totalCost = 0;
    int currentGas = 0;
    int start = 0;

    for (int i = 0; i < gas.length; i++) {
      totalGas += gas[i];
      totalCost += cost[i];
      currentGas += gas[i] - cost[i];

      if (currentGas < 0) {
        start = i + 1;
        currentGas = 0;
      }
    }

    return totalGas >= totalCost ? start : -1;
  }

  /**
   * Partition labels: group characters into fewest partitions.
   *
   * @param s input string (may not be null)
   * @return list of partition sizes
   *
   * LeetCode 763, Medium. Example: "ababcbacaddefegdehijhijk" →
   * [9,7,8] (each char appears within one partition)
   *
   * Time: O(n), Space: O(1) (at most 26 chars).
   * Tricky: Track last occurrence of each char; partition when reach it.
   */
  public static List<Integer> partitionLabels(String s) {
    if (s == null) {
      throw new IllegalArgumentException("s must be non-null");
    }

    List<Integer> result = new ArrayList<>();
    int[] lastIndex = new int[26];

    // Map each char to its last occurrence
    for (int i = 0; i < s.length(); i++) {
      lastIndex[s.charAt(i) - 'a'] = i;
    }

    int start = 0;
    int maxEnd = 0;

    for (int i = 0; i < s.length(); i++) {
      maxEnd = Math.max(maxEnd, lastIndex[s.charAt(i) - 'a']);

      if (i == maxEnd) {
        result.add(i - start + 1);
        start = i + 1;
      }
    }

    return result;
  }

  // ============================================================================
  // BACKTRACKING
  // ============================================================================

  /**
   * Generate all permutations of an array.
   *
   * @param nums input array (may not be null)
   * @return list of all permutations
   *
   * LeetCode 46, Medium. Example: [1,2,3] → [[1,2,3],[1,3,2],...] (6 total)
   *
   * Time: O(n! * n), Space: O(n! * n) output + O(n) recursion stack.
   */
  public static List<List<Integer>> permutations(int[] nums) {
    if (nums == null) {
      throw new IllegalArgumentException("nums must be non-null");
    }

    List<List<Integer>> result = new ArrayList<>();
    List<Integer> current = new ArrayList<>();

    boolean[] used = new boolean[nums.length];
    backtrackPermute(nums, used, current, result);

    return result;
  }

  private static void backtrackPermute(int[] nums, boolean[] used,
      List<Integer> current, List<List<Integer>> result) {
    if (current.size() == nums.length) {
      result.add(new ArrayList<>(current));
      return;
    }

    for (int i = 0; i < nums.length; i++) {
      if (!used[i]) {
        used[i] = true;
        current.add(nums[i]);

        backtrackPermute(nums, used, current, result);

        current.remove(current.size() - 1);
        used[i] = false;
      }
    }
  }

  /**
   * Generate all subsets (power set).
   *
   * @param nums input array (may not be null)
   * @return list of all subsets
   *
   * LeetCode 78, Medium. Example: [1,2,3] → [[],[1],[2],[3],[1,2],[1,3],
   * [2,3],[1,2,3]]
   *
   * Time: O(2^n * n), Space: O(2^n * n).
   */
  public static List<List<Integer>> subsets(int[] nums) {
    if (nums == null) {
      throw new IllegalArgumentException("nums must be non-null");
    }

    List<List<Integer>> result = new ArrayList<>();
    backtrackSubsets(nums, 0, new ArrayList<>(), result);

    return result;
  }

  private static void backtrackSubsets(int[] nums, int start,
      List<Integer> current, List<List<Integer>> result) {
    result.add(new ArrayList<>(current));

    for (int i = start; i < nums.length; i++) {
      current.add(nums[i]);
      backtrackSubsets(nums, i + 1, current, result);
      current.remove(current.size() - 1);
    }
  }

  /**
   * Combination sum: all unique combinations that sum to target.
   *
   * @param candidates array of candidates (may not be null)
   * @param target goal sum
   * @return list of combinations (unbounded: each candidate reusable)
   *
   * LeetCode 39, Medium. Example: candidates=[2,3,6,7], target=7 →
   * [[2,2,3],[7]]
   *
   * Time: O(4^(t/m) * k) where t=target, m=min candidate, k=avg combo length,
   * Space: O(t/m) recursion depth.
   */
  public static List<List<Integer>> combinationSum(int[] candidates,
      int target) {
    if (candidates == null) {
      throw new IllegalArgumentException("candidates must be non-null");
    }

    List<List<Integer>> result = new ArrayList<>();
    Arrays.sort(candidates);

    backtrackCombination(candidates, target, 0, new ArrayList<>(), result);

    return result;
  }

  private static void backtrackCombination(int[] candidates, int target,
      int start, List<Integer> current, List<List<Integer>> result) {
    if (target == 0) {
      result.add(new ArrayList<>(current));
      return;
    }

    if (target < 0) {
      return;
    }

    for (int i = start; i < candidates.length; i++) {
      current.add(candidates[i]);
      // Reuse same index (unbounded)
      backtrackCombination(candidates, target - candidates[i], i, current,
          result);
      current.remove(current.size() - 1);
    }
  }

  /**
   * Solve N-Queens problem: place N queens on N×N board.
   *
   * @param n board size (n >= 1)
   * @return list of valid board configurations
   *
   * LeetCode 51, Hard. Example: n=4 → 2 valid configurations
   *
   * Time: O(N!), Space: O(N) recursion + O(N²) output.
   * Tricky: Track columns, diagonals via sets to check attacks in O(1).
   */
  public static List<List<String>> solveNQueens(int n) {
    if (n < 1) {
      throw new IllegalArgumentException("n must be >= 1");
    }

    List<List<String>> result = new ArrayList<>();
    char[][] board = new char[n][n];

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        board[i][j] = '.';
      }
    }

    Set<Integer> cols = new HashSet<>();
    Set<Integer> diag1 = new HashSet<>(); // row - col
    Set<Integer> diag2 = new HashSet<>(); // row + col

    backtrackNQueens(board, 0, cols, diag1, diag2, result, n);

    return result;
  }

  private static void backtrackNQueens(char[][] board, int row,
      Set<Integer> cols, Set<Integer> diag1, Set<Integer> diag2,
      List<List<String>> result, int n) {
    if (row == n) {
      List<String> config = new ArrayList<>();
      for (int i = 0; i < n; i++) {
        config.add(new String(board[i]));
      }
      result.add(config);
      return;
    }

    for (int col = 0; col < n; col++) {
      int d1 = row - col;
      int d2 = row + col;

      if (cols.contains(col) || diag1.contains(d1) || diag2.contains(d2)) {
        continue;
      }

      board[row][col] = 'Q';
      cols.add(col);
      diag1.add(d1);
      diag2.add(d2);

      backtrackNQueens(board, row + 1, cols, diag1, diag2, result, n);

      board[row][col] = '.';
      cols.remove(col);
      diag1.remove(d1);
      diag2.remove(d2);
    }
  }

  /**
   * Word search: find word in grid (can move up/down/left/right).
   *
   * @param board 2D char grid (may not be null)
   * @param word word to search (may not be null)
   * @return true if word found
   *
   * LeetCode 79, Medium. Example: board=[["A","B"],["C","D"]], word="BA" →
   * true
   *
   * Time: O(m*n * 4^L) where m=rows, n=cols, L=word length,
   * Space: O(L) recursion stack.
   * Tricky: Mark visited cells; use backtracking to undo.
   */
  public static boolean wordSearch(char[][] board, String word) {
    if (board == null || board.length == 0 || board[0].length == 0
        || word == null) {
      throw new IllegalArgumentException("board and word must be non-null");
    }

    int m = board.length;
    int n = board[0].length;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (board[i][j] == word.charAt(0)) {
          if (backtrackWordSearch(board, word, 0, i, j)) {
            return true;
          }
        }
      }
    }

    return false;
  }

  private static boolean backtrackWordSearch(char[][] board, String word,
      int idx, int i, int j) {
    if (idx == word.length()) {
      return true;
    }

    if (i < 0 || i >= board.length || j < 0 || j >= board[0].length
        || board[i][j] != word.charAt(idx)) {
      return false;
    }

    char temp = board[i][j];
    board[i][j] = '#';

    boolean found = backtrackWordSearch(board, word, idx + 1, i + 1, j)
        || backtrackWordSearch(board, word, idx + 1, i - 1, j)
        || backtrackWordSearch(board, word, idx + 1, i, j + 1)
        || backtrackWordSearch(board, word, idx + 1, i, j - 1);

    board[i][j] = temp;

    return found;
  }

  // ============================================================================
  // BIT MANIPULATION
  // ============================================================================

  /**
   * Find single number appearing once (others appear twice).
   *
   * @param nums array where one appears once, rest appear twice
   * @return the single number
   *
   * LeetCode 136, Easy. Example: [2,2,1] → 1; [4,1,2,1,2] → 4
   *
   * Time: O(n), Space: O(1).
   * Tricky: XOR all numbers; duplicates cancel, single remains.
   */
  public static int singleNumber(int[] nums) {
    if (nums == null || nums.length == 0) {
      throw new IllegalArgumentException("nums must be non-null and non-empty");
    }

    int result = 0;
    for (int num : nums) {
      result ^= num;
    }

    return result;
  }

  /**
   * Count number of 1-bits (set bits) for all 0 to n.
   *
   * @param n the upper bound (0 <= n <= 5*10^5)
   * @return array where ans[i] = number of 1-bits in binary of i
   *
   * LeetCode 338, Easy. Example: n=5 → [0,1,1,2,1,2]
   *
   * Time: O(n), Space: O(1) not counting output.
   * Tricky: ans[i] = ans[i >> 1] + (i & 1); or use dp.
   */
  public static int[] countBits(int n) {
    if (n < 0) {
      throw new IllegalArgumentException("n must be >= 0");
    }

    int[] ans = new int[n + 1];

    for (int i = 1; i <= n; i++) {
      ans[i] = ans[i >> 1] + (i & 1);
    }

    return ans;
  }

  /**
   * Reverse bits of an unsigned 32-bit integer.
   *
   * @param n the number to reverse (0 <= n <= 2^32 - 1)
   * @return reversed number
   *
   * LeetCode 190, Easy. Example: n=0b00000010100101000001111010011100 →
   * 0b00111001011110000010100101000000
   *
   * Time: O(1) (32 bits), Space: O(1).
   */
  public static int reverseBits(int n) {
    int result = 0;

    for (int i = 0; i < 32; i++) {
      result = (result << 1) | (n & 1);
      n >>>= 1;
    }

    return result;
  }

  /**
   * Find missing number in array [0, n].
   *
   * @param nums array of n unique numbers in range [0, n]
   * @return the missing number
   *
   * LeetCode 268, Easy. Example: [3,0,1] → 2; [0,1] → 2
   *
   * Time: O(n), Space: O(1).
   * Tricky: XOR approach or sum approach.
   */
  public static int missingNumber(int[] nums) {
    if (nums == null || nums.length == 0) {
      throw new IllegalArgumentException("nums must be non-null and non-empty");
    }

    int xor = 0;
    for (int i = 0; i < nums.length; i++) {
      xor ^= i ^ nums[i];
    }

    return xor ^ nums.length;
  }

  // ============================================================================
  // TRIE
  // ============================================================================

  /**
   * Trie data structure for efficient prefix-based search.
   */
  public static class Trie {
    private TrieNode root;

    /**
     * Trie node.
     */
    private static class TrieNode {
      TrieNode[] children = new TrieNode[26];
      boolean isEnd = false;
    }

    /**
     * Initialize Trie.
     */
    public Trie() {
      this.root = new TrieNode();
    }

    /**
     * Insert a word into Trie.
     *
     * @param word the word to insert (may not be null)
     */
    public void insert(String word) {
      if (word == null) {
        throw new IllegalArgumentException("word must be non-null");
      }

      TrieNode node = root;

      for (char c : word.toCharArray()) {
        int idx = c - 'a';
        if (node.children[idx] == null) {
          node.children[idx] = new TrieNode();
        }
        node = node.children[idx];
      }

      node.isEnd = true;
    }

    /**
     * Search for exact word in Trie.
     *
     * @param word the word to search (may not be null)
     * @return true if word exists
     */
    public boolean search(String word) {
      if (word == null) {
        throw new IllegalArgumentException("word must be non-null");
      }

      TrieNode node = find(word);

      return node != null && node.isEnd;
    }

    /**
     * Search for words with prefix.
     *
     * @param prefix the prefix to search (may not be null)
     * @return true if words with this prefix exist
     */
    public boolean startsWith(String prefix) {
      if (prefix == null) {
        throw new IllegalArgumentException("prefix must be non-null");
      }

      return find(prefix) != null;
    }

    private TrieNode find(String word) {
      TrieNode node = root;

      for (char c : word.toCharArray()) {
        int idx = c - 'a';
        if (node.children[idx] == null) {
          return null;
        }
        node = node.children[idx];
      }

      return node;
    }
  }

  /**
   * Word search II: find all words from board in dictionary.
   *
   * @param board 2D char grid (may not be null)
   * @param words array of words to find (may not be null)
   * @return list of words found in board
   *
   * LeetCode 212, Hard. Example: board=[["o","a","b"],["o","b","a"],
   * ["b","a","b"]], words=["oba","baa"] → ["oba","baa"]
   *
   * Time: O(m*n * 4^L * k) where m=rows, n=cols, L=word length, k=Trie depth,
   * Space: O(k) Trie + O(L) recursion.
   * Tricky: Use Trie to avoid redundant searches; prune dead branches.
   */
  public static List<String> wordSearchII(char[][] board, String[] words) {
    if (board == null || board.length == 0 || board[0].length == 0
        || words == null) {
      throw new IllegalArgumentException("board and words must be non-null");
    }

    Set<String> result = new HashSet<>();
    Trie trie = new Trie();

    for (String word : words) {
      trie.insert(word);
    }

    int m = board.length;
    int n = board[0].length;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        backtrackWordSearchII(board, trie, i, j, new StringBuilder(),
            result);
      }
    }

    return new ArrayList<>(result);
  }

  private static void backtrackWordSearchII(char[][] board, Trie trie,
      int i, int j, StringBuilder current, Set<String> result) {
    if (i < 0 || i >= board.length || j < 0 || j >= board[0].length
        || board[i][j] == '#') {
      return;
    }

    char c = board[i][j];
    current.append(c);

    if (trie.search(current.toString())) {
      result.add(current.toString());
    }

    if (!trie.startsWith(current.toString())) {
      current.deleteCharAt(current.length() - 1);
      return;
    }

    board[i][j] = '#';

    backtrackWordSearchII(board, trie, i + 1, j, current, result);
    backtrackWordSearchII(board, trie, i - 1, j, current, result);
    backtrackWordSearchII(board, trie, i, j + 1, current, result);
    backtrackWordSearchII(board, trie, i, j - 1, current, result);

    board[i][j] = c;
    current.deleteCharAt(current.length() - 1);
  }

  // ============================================================================
  // MATH
  // ============================================================================

  /**
   * Greatest common divisor using Euclidean algorithm.
   *
   * @param a first number (a > 0)
   * @param b second number (b > 0)
   * @return GCD of a and b
   *
   * Time: O(log(min(a, b))), Space: O(log(min(a, b))) recursion.
   */
  public static int gcd(int a, int b) {
    if (a <= 0 || b <= 0) {
      throw new IllegalArgumentException("a and b must be positive");
    }

    if (b == 0) {
      return a;
    }

    return gcd(b, a % b);
  }

  /**
   * Check if a number is prime.
   *
   * @param n the number to check (n >= 2)
   * @return true if prime, false otherwise
   *
   * Time: O(sqrt(n)), Space: O(1).
   */
  public static boolean isPrime(int n) {
    if (n < 2) {
      return false;
    }

    if (n == 2) {
      return true;
    }

    if (n % 2 == 0) {
      return false;
    }

    for (int i = 3; i * i <= n; i += 2) {
      if (n % i == 0) {
        return false;
      }
    }

    return true;
  }

  /**
   * Sieve of Eratosthenes: find all primes up to n.
   *
   * @param n upper bound (n >= 2)
   * @return boolean array where is[i] = true if i is prime
   *
   * Time: O(n log log n), Space: O(n).
   */
  public static boolean[] sieveOfEratosthenes(int n) {
    if (n < 2) {
      throw new IllegalArgumentException("n must be >= 2");
    }

    boolean[] isPrime = new boolean[n + 1];
    Arrays.fill(isPrime, true);
    isPrime[0] = isPrime[1] = false;

    for (int i = 2; i * i <= n; i++) {
      if (isPrime[i]) {
        for (int j = i * i; j <= n; j += i) {
          isPrime[j] = false;
        }
      }
    }

    return isPrime;
  }

  /**
   * x^n using fast exponentiation (binary exponentiation).
   *
   * @param x base (any double)
   * @param n exponent (any int; handles negatives)
   * @return x^n
   *
   * LeetCode 50, Medium. Example: x=2.0, n=10 → 1024.0
   *
   * Time: O(log n), Space: O(log n) recursion or O(1) iterative.
   * Tricky: Use binary representation of exponent; handle overflow for n=INT_MIN.
   */
  public static double myPow(double x, int n) {
    long N = n;

    if (N < 0) {
      x = 1 / x;
      N = -N;
    }

    return powHelper(x, N);
  }

  private static double powHelper(double x, long n) {
    if (n == 0) {
      return 1.0;
    }

    double half = powHelper(x, n / 2);

    if (n % 2 == 0) {
      return half * half;
    } else {
      return half * half * x;
    }
  }

  // ============================================================================
  // MAIN: Test cases for all methods
  // ============================================================================

  /**
   * Main method demonstrating essential topics.
   *
   * @param args not used
   */
  public static void main(String[] args) {
    System.out.println("=== Essential Topics ===\n");

    System.out.println("GREEDY:");
    System.out.println("Can Jump [2,3,1,1,4]: " + canJump(new int[]{2, 3, 1, 1, 4}));
    System.out.println("Jump [2,3,1,1,4]: " + jump(new int[]{2, 3, 1, 1, 4}));
    System.out.println("Gas Station: " + canCompleteCircuit(
        new int[]{1, 2, 3, 4, 5}, new int[]{3, 4, 5, 1, 2}));
    System.out.println("Partition Labels: " + partitionLabels("ababcbacaddefegdehijhijk"));

    System.out.println("\nBACKTRACKING:");
    System.out.println("Permutations [1,2,3]: " + permutations(new int[]{1, 2, 3}));
    System.out.println("Subsets [1,2,3]: " + subsets(new int[]{1, 2, 3}));
    System.out.println("Combination Sum [2,3,6,7] target=7: "
        + combinationSum(new int[]{2, 3, 6, 7}, 7));
    System.out.println("Word Search: " + wordSearch(
        new char[][]{{'A', 'B'}, {'C', 'D'}}, "BA"));

    System.out.println("\nBIT MANIPULATION:");
    System.out.println("Single Number [2,2,1]: " + singleNumber(new int[]{2, 2, 1}));
    System.out.println("Count Bits (n=5): " + Arrays.toString(countBits(5)));
    System.out.println("Missing Number [3,0,1]: " + missingNumber(new int[]{3, 0, 1}));

    System.out.println("\nTRIE:");
    Trie trie = new Trie();
    trie.insert("apple");
    System.out.println("Search 'apple': " + trie.search("apple"));
    System.out.println("StartsWith 'app': " + trie.startsWith("app"));
    System.out.println("Search 'app': " + trie.search("app"));

    System.out.println("\nMATH:");
    System.out.println("GCD(12, 8): " + gcd(12, 8));
    System.out.println("Is Prime (7): " + isPrime(7));
    System.out.println("Is Prime (10): " + isPrime(10));
    System.out.println("Sieve (10): " + Arrays.toString(sieveOfEratosthenes(10)));
    System.out.println("2^10: " + myPow(2.0, 10));
    System.out.println("2^-2: " + myPow(2.0, -2));
  }
}
