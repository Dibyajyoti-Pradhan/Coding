import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Union-Find (Disjoint Set Union) problems and implementations.
 *
 * <p>Union-Find is a data structure that efficiently handles dynamic connectivity queries
 * and supports two main operations:
 * <ul>
 *   <li><b>find(x):</b> Determines the representative (root) of the set containing x.
 *   <li><b>union(x, y):</b> Merges the sets containing x and y.
 * </ul>
 *
 * <p><b>Key Optimizations:</b>
 * <ul>
 *   <li><b>Path Compression:</b> In find(), set each traversed node's parent directly to root.
 *   <li><b>Union by Rank:</b> In union(), attach shorter tree under taller tree.
 *   <li><b>Time Complexity:</b> O(α(n)) amortized per operation, where α is inverse Ackermann
 *       (practically constant for all real-world input sizes).
 * </ul>
 *
 * <p><b>Common Use Cases:</b>
 * <ul>
 *   <li>Connected components in undirected graphs
 *   <li>Cycle detection
 *   <li>Kruskal's Minimum Spanning Tree algorithm
 *   <li>Dynamic connectivity queries
 *   <li>Account merging with transitive relations
 * </ul>
 */
public class UnionFind {

  private static final String COMPONENT_COUNT_FORMAT = "Components: %d%n";
  private static final String ISLAND_COUNT_FORMAT = "Islands: %d%n";

  /**
   * Basic Union-Find implementation with path compression and union by rank.
   *
   * <p>Supports efficient find and union operations on disjoint sets.
   */
  public static class UnionFindBasic {
    private int[] parent;
    private int[] rank;
    private int componentCount;

    /**
     * Initializes a Union-Find structure for n elements.
     *
     * @param n number of elements (0 to n-1)
     */
    public UnionFindBasic(int n) {
      if (n <= 0) {
        throw new IllegalArgumentException("n must be positive");
      }
      this.parent = new int[n];
      this.rank = new int[n];
      this.componentCount = n;
      for (int i = 0; i < n; i++) {
        this.parent[i] = i;
        this.rank[i] = 0;
      }
    }

    /**
     * Finds the root representative of the element x with path compression.
     *
     * <p>Path compression: updates each traversed node's parent directly to the root,
     * flattening the tree structure.
     *
     * @param x the element to find
     * @return the root of the set containing x
     * @throws IndexOutOfBoundsException if x is out of bounds
     */
    public int find(int x) {
      if (x < 0 || x >= parent.length) {
        throw new IndexOutOfBoundsException("Index out of bounds: " + x);
      }
      if (parent[x] != x) {
        parent[x] = find(parent[x]); // Path compression
      }
      return parent[x];
    }

    /**
     * Unions the sets containing x and y using union by rank.
     *
     * <p>Union by rank: attaches the smaller tree under the larger tree to keep depth
     * logarithmic.
     *
     * @param x first element
     * @param y second element
     * @return true if x and y were in different sets and are now unioned, false otherwise
     */
    public boolean union(int x, int y) {
      int rootX = find(x);
      int rootY = find(y);

      if (rootX == rootY) {
        return false;
      }

      if (rank[rootX] < rank[rootY]) {
        parent[rootX] = rootY;
      } else if (rank[rootX] > rank[rootY]) {
        parent[rootY] = rootX;
      } else {
        parent[rootY] = rootX;
        rank[rootX]++;
      }

      componentCount--;
      return true;
    }

    /**
     * Checks if two elements are in the same set.
     *
     * @param x first element
     * @param y second element
     * @return true if x and y have the same root
     */
    public boolean connected(int x, int y) {
      return find(x) == find(y);
    }

    /**
     * Returns the number of disjoint sets (components).
     *
     * @return component count
     */
    public int getComponentCount() {
      return componentCount;
    }
  }

  /**
   * Union-Find variant that tracks component sizes.
   *
   * <p>Useful for problems requiring knowledge of component sizes, such as merging accounts
   * and finding largest connected components.
   */
  public static class UnionFindWithSize {
    private int[] parent;
    private int[] rank;
    private int[] size;
    private int componentCount;

    /**
     * Initializes Union-Find with size tracking.
     *
     * @param n number of elements
     */
    public UnionFindWithSize(int n) {
      if (n <= 0) {
        throw new IllegalArgumentException("n must be positive");
      }
      this.parent = new int[n];
      this.rank = new int[n];
      this.size = new int[n];
      this.componentCount = n;
      for (int i = 0; i < n; i++) {
        this.parent[i] = i;
        this.rank[i] = 0;
        this.size[i] = 1;
      }
    }

    /**
     * Finds the root representative with path compression.
     *
     * @param x the element to find
     * @return the root of the set containing x
     */
    public int find(int x) {
      if (parent[x] != x) {
        parent[x] = find(parent[x]);
      }
      return parent[x];
    }

    /**
     * Unions two sets and updates their combined size.
     *
     * @param x first element
     * @param y second element
     * @return true if union occurred, false if already connected
     */
    public boolean union(int x, int y) {
      int rootX = find(x);
      int rootY = find(y);

      if (rootX == rootY) {
        return false;
      }

      if (rank[rootX] < rank[rootY]) {
        parent[rootX] = rootY;
        size[rootY] += size[rootX];
      } else if (rank[rootX] > rank[rootY]) {
        parent[rootY] = rootX;
        size[rootX] += size[rootY];
      } else {
        parent[rootY] = rootX;
        size[rootX] += size[rootY];
        rank[rootX]++;
      }

      componentCount--;
      return true;
    }

    /**
     * Gets the size of the component containing element x.
     *
     * @param x the element
     * @return the size of its component
     */
    public int getComponentSize(int x) {
      return size[find(x)];
    }

    /**
     * Gets the largest component size.
     *
     * @return the maximum component size
     */
    public int getMaxComponentSize() {
      int maxSize = 0;
      for (int s : size) {
        maxSize = Math.max(maxSize, s);
      }
      return maxSize;
    }

    /**
     * Returns the number of disjoint components.
     *
     * @return component count
     */
    public int getComponentCount() {
      return componentCount;
    }
  }

  /**
   * Counts the number of connected components in an undirected graph.
   *
   * <p><b>LeetCode 323 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * n = 5, edges = [[0,1],[1,2],[3,4]]
   * Output: 2
   * Explanation: {0, 1, 2} and {3, 4}
   * </pre>
   *
   * <p><b>Constraints:</b> 1 ≤ n ≤ 2000, 0 ≤ edges.length ≤ 10000
   *
   * <p><b>Time:</b> O(n + m·α(n)) where m = edges.length
   * <b>Space:</b> O(n)
   *
   * <p><b>Tricky:</b> Each union decreases component count by 1. Start with n components,
   * then count decreases with each successful union.
   *
   * @param n number of nodes (0-indexed)
   * @param edges array of [u, v] representing edges
   * @return number of connected components
   */
  public static int countComponents(int n, int[][] edges) {
    if (n <= 0) {
      throw new IllegalArgumentException("n must be positive");
    }
    if (edges == null) {
      edges = new int[0][0];
    }

    UnionFindBasic uf = new UnionFindBasic(n);
    for (int[] edge : edges) {
      uf.union(edge[0], edge[1]);
    }
    return uf.getComponentCount();
  }

  /**
   * Validates if the given edges form a tree.
   *
   * <p><b>LeetCode 261 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
   * Output: true (connected, no cycle)
   * </pre>
   *
   * <p><b>Constraints:</b> 1 ≤ n ≤ 2000, 0 ≤ edges.length ≤ 10000
   *
   * <p><b>Time:</b> O((n + m)·α(n)) <b>Space:</b> O(n)
   *
   * <p><b>Tricky:</b> A valid tree has exactly n-1 edges and no cycles. If union returns
   * false (already connected), a cycle exists. Check both conditions.
   *
   * @param n number of nodes
   * @param edges array of [u, v] edges
   * @return true if edges form a valid tree
   */
  public static boolean validTree(int n, int[][] edges) {
    if (n <= 0) {
      throw new IllegalArgumentException("n must be positive");
    }
    if (edges == null) {
      edges = new int[0][0];
    }

    // Valid tree must have exactly n-1 edges
    if (edges.length != n - 1) {
      return false;
    }

    UnionFindBasic uf = new UnionFindBasic(n);
    for (int[] edge : edges) {
      if (!uf.union(edge[0], edge[1])) {
        // Cycle detected
        return false;
      }
    }

    return uf.getComponentCount() == 1;
  }

  /**
   * Finds a redundant edge that creates a cycle in an undirected graph.
   *
   * <p><b>LeetCode 684 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * edges = [[1,2],[1,3],[2,3]]
   * Output: [2, 3] (last edge creating the cycle)
   * </pre>
   *
   * <p><b>Constraints:</b> n = edges.length, 3 ≤ n ≤ 1000
   *
   * <p><b>Time:</b> O(n·α(n)) <b>Space:</b> O(n)
   *
   * <p><b>Tricky:</b> Process edges sequentially; the first edge whose union fails (both
   * endpoints already connected) is the redundant edge.
   *
   * @param edges array of [u, v] edges (1-indexed nodes)
   * @return the redundant edge causing the cycle
   */
  public static int[] findRedundantConnection(int[][] edges) {
    if (edges == null || edges.length == 0) {
      return new int[0];
    }

    int n = edges.length;
    UnionFindBasic uf = new UnionFindBasic(n + 1);

    for (int[] edge : edges) {
      if (!uf.union(edge[0], edge[1])) {
        return edge;
      }
    }

    return new int[0];
  }

  /**
   * Merges email accounts that share common emails.
   *
   * <p><b>LeetCode 721 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * accounts = [["John", "johnsmith@example.com", "john_newyork@example.com"],
   *             ["John", "johnsmith@example.com", "john00@example.com"],
   *             ["Mary", "mary@example.com"]]
   * Output: [["John", "john00@example.com", "john_newyork@example.com", "johnsmith@example.com"],
   *          ["Mary", "mary@example.com"]]
   * </pre>
   *
   * <p><b>Constraints:</b> 1 ≤ accounts.length ≤ 1000
   *
   * <p><b>Time:</b> O(n·k·log(k)) where n = accounts, k = emails <b>Space:</b> O(n·k)
   *
   * <p><b>Tricky:</b> Map each email to an account index, union accounts sharing emails,
   * then group by root and sort emails per account.
   *
   * @param accounts list of [name, email1, email2, ...]
   * @return merged accounts grouped by root
   */
  public static List<List<String>> accountsMerge(List<List<String>> accounts) {
    if (accounts == null || accounts.isEmpty()) {
      return new ArrayList<>();
    }

    int n = accounts.size();
    UnionFindBasic uf = new UnionFindBasic(n);

    // Map email to account index
    Map<String, Integer> emailToAccount = new HashMap<>();
    for (int i = 0; i < n; i++) {
      List<String> account = accounts.get(i);
      for (int j = 1; j < account.size(); j++) {
        String email = account.get(j);
        if (emailToAccount.containsKey(email)) {
          uf.union(i, emailToAccount.get(email));
        } else {
          emailToAccount.put(email, i);
        }
      }
    }

    // Group emails by root account
    Map<Integer, List<String>> rootToEmails = new HashMap<>();
    for (String email : emailToAccount.keySet()) {
      int root = uf.find(emailToAccount.get(email));
      rootToEmails.computeIfAbsent(root, k -> new ArrayList<>()).add(email);
    }

    // Build result
    List<List<String>> result = new ArrayList<>();
    for (int i = 0; i < n; i++) {
      int root = uf.find(i);
      if (rootToEmails.containsKey(root)) {
        List<String> mergedAccount = new ArrayList<>();
        mergedAccount.add(accounts.get(i).get(0)); // Account name
        List<String> emails = rootToEmails.get(root);
        emails.sort(String::compareTo);
        mergedAccount.addAll(emails);
        result.add(mergedAccount);
        rootToEmails.remove(root); // Avoid duplicates
      }
    }

    return result;
  }

  /**
   * Finds islands dynamically as points are added to a grid.
   *
   * <p><b>LeetCode 305 (Hard)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * m = 3, n = 3, positions = [[0,0],[0,1],[2,2],[2,1]]
   * Output: [1, 1, 2, 3]
   * </pre>
   *
   * <p><b>Constraints:</b> m, n ≤ 100, positions.length ≤ 4900
   *
   * <p><b>Time:</b> O(k·α(k)) where k = positions.length <b>Space:</b> O(k)
   *
   * <p><b>Tricky:</b> Flatten 2D coordinates to 1D (row * n + col), maintain a set of
   * existing positions, union with adjacent land cells only.
   *
   * @param m number of rows
   * @param n number of columns
   * @param positions array of [row, col] positions to add land
   * @return array of island counts after each addition
   */
  public static int[] numIslandsII(int m, int n, int[][] positions) {
    if (m <= 0 || n <= 0 || positions == null || positions.length == 0) {
      return new int[0];
    }

    int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    UnionFindBasic uf = new UnionFindBasic(m * n);
    Set<Integer> land = new HashSet<>();
    int[] result = new int[positions.length];

    for (int i = 0; i < positions.length; i++) {
      int row = positions[i][0];
      int col = positions[i][1];
      int index = row * n + col;

      if (land.contains(index)) {
        result[i] = uf.getComponentCount();
        continue;
      }

      land.add(index);
      uf.componentCount--; // Add new island initially

      for (int[] dir : directions) {
        int newRow = row + dir[0];
        int newCol = col + dir[1];
        int newIndex = newRow * n + newCol;

        if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n
            && land.contains(newIndex)) {
          if (uf.union(index, newIndex)) {
            uf.componentCount++; // union already decremented, but we need net effect
          }
        }
      }

      result[i] = uf.getComponentCount();
    }

    return result;
  }

  /**
   * Determines if an equation relationship is satisfiable using variables.
   *
   * <p><b>LeetCode 990 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * equations = ["a==b","b!=ac","b==c"]
   * Output: false (b==c but a==b and b!=ac contradict)
   * </pre>
   *
   * <p><b>Constraints:</b> 1 ≤ equations.length ≤ 500
   *
   * <p><b>Time:</b> O(n·α(26)) = O(n) <b>Space:</b> O(1) (26 letters)
   *
   * <p><b>Tricky:</b> Process all "==" equations first to union equivalent variables,
   * then check all "!=" equations. If any "!=" connects equal variables, it's impossible.
   *
   * @param equations array of equations like "a==b" or "a!=b"
   * @return true if all equations can be satisfied
   */
  public static boolean equationsPossible(String[] equations) {
    if (equations == null || equations.length == 0) {
      return true;
    }

    UnionFindBasic uf = new UnionFindBasic(26);

    // First pass: process all equality equations
    for (String eq : equations) {
      if (eq.charAt(1) == '=') {
        int a = eq.charAt(0) - 'a';
        int b = eq.charAt(3) - 'a';
        uf.union(a, b);
      }
    }

    // Second pass: check all inequality equations
    for (String eq : equations) {
      if (eq.charAt(1) == '!') {
        int a = eq.charAt(0) - 'a';
        int b = eq.charAt(3) - 'a';
        if (uf.connected(a, b)) {
          return false;
        }
      }
    }

    return true;
  }

  /**
   * Removes stones such that we can remove as many stones as possible where two stones
   * are removable if in the same row or column.
   *
   * <p><b>LeetCode 947 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
   * Output: 5 (remove all but one per connected component)
   * </pre>
   *
   * <p><b>Constraints:</b> 1 ≤ stones.length ≤ 104
   *
   * <p><b>Time:</b> O(n·α(n)) <b>Space:</b> O(n)
   *
   * <p><b>Tricky:</b> Stones in the same row or column form a connected component. Answer
   * = total stones - number of components (each component leaves 1 stone).
   *
   * @param stones array of [row, col] positions
   * @return maximum number of stones that can be removed
   */
  public static int removeStones(int[][] stones) {
    if (stones == null || stones.length == 0) {
      return 0;
    }

    int n = stones.length;
    UnionFindBasic uf = new UnionFindBasic(n);

    // Union stones sharing row or column
    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        if (stones[i][0] == stones[j][0] || stones[i][1] == stones[j][1]) {
          uf.union(i, j);
        }
      }
    }

    return n - uf.getComponentCount();
  }

  /**
   * Main method demonstrating all Union-Find problems with test cases.
   *
   * @param args unused
   */
  public static void main(String[] args) {
    System.out.println("=== Union-Find Problems ===\n");

    // countComponents
    System.out.println("1. Count Components:");
    int n = 5;
    int[][] edges = {{0, 1}, {1, 2}, {3, 4}};
    System.out.printf(COMPONENT_COUNT_FORMAT, countComponents(n, edges));

    // validTree
    System.out.println("2. Valid Tree:");
    n = 5;
    edges = new int[][]{{0, 1}, {0, 2}, {0, 3}, {1, 4}};
    System.out.println("Is valid tree: " + validTree(n, edges));

    // findRedundantConnection
    System.out.println("3. Redundant Connection:");
    edges = new int[][]{{1, 2}, {1, 3}, {2, 3}};
    int[] redundant = findRedundantConnection(edges);
    System.out.println("Redundant edge: [" + redundant[0] + ", " + redundant[1] + "]");

    // accountsMerge
    System.out.println("4. Account Merge:");
    List<List<String>> accounts = new ArrayList<>();
    accounts.add(List.of("John", "johnsmith@example.com", "john_newyork@example.com"));
    accounts.add(List.of("John", "johnsmith@example.com", "john00@example.com"));
    accounts.add(List.of("Mary", "mary@example.com"));
    List<List<String>> merged = accountsMerge(accounts);
    for (List<String> account : merged) {
      System.out.println(account);
    }

    // numIslandsII
    System.out.println("\n5. Islands II:");
    int[][] positions = {{0, 0}, {0, 1}, {2, 2}, {2, 1}};
    int[] islandCounts = numIslandsII(4, 3, positions);
    for (int count : islandCounts) {
      System.out.print(count + " ");
    }
    System.out.println();

    // equationsPossible
    System.out.println("\n6. Equations Possible:");
    String[] equations = {"a==b", "b==c", "c==d", "x!=y"};
    System.out.println("Is satisfiable: " + equationsPossible(equations));

    // removeStones
    System.out.println("\n7. Remove Stones:");
    int[][] stones = {{0, 0}, {0, 1}, {1, 0}, {1, 2}, {2, 1}, {2, 2}};
    System.out.println("Stones removed: " + removeStones(stones));
  }
}
