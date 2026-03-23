import java.util.ArrayList;
import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Graph DFS/BFS, topological sort, bipartite detection, and Union Find.
 *
 * Covers: DFS on grids and adjacency lists, BFS for shortest paths,
 * cycle detection with color-based DFS, topological sort (Kahn's BFS),
 * bipartite validation, graph cloning with HashMap, Union Find with path
 * compression and union by rank.
 *
 * KEY INSIGHTS:
 * - DFS: stack-based or recursion, detect cycles, explore deeply
 * - BFS: queue-based, shortest path in unweighted graphs
 * - Topological sort: Kahn's (BFS) or DFS finish times
 * - Union Find: nearly O(1) amortized with path compression + union by rank
 * - Color: 0=unvisited, 1=visiting (in current DFS), 2=visited
 * - All methods include input validation; null inputs throw IllegalArgumentException
 */
public final class GraphDfsBfs {

  private GraphDfsBfs() {
    // Utility class; prevent instantiation
  }

  // ============================================================================
  // DFS - GRID PROBLEMS
  // ============================================================================

  /**
   * Count number of islands (connected 1s) in a grid.
   *
   * @param grid 2D char array with '0' (water) and '1' (land)
   * @return number of islands
   *
   * LeetCode 200, Medium. Example: [["1","1"],["0","1"]] → 1
   *
   * Time: O(m*n), Space: O(m*n) for visited + recursion stack.
   */
  public static int numIslands(char[][] grid) {
    if (grid == null || grid.length == 0 || grid[0].length == 0) {
      throw new IllegalArgumentException(
          "grid must be non-null and non-empty");
    }

    int m = grid.length;
    int n = grid[0].length;
    boolean[][] visited = new boolean[m][n];
    int count = 0;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == '1' && !visited[i][j]) {
          dfsIsland(grid, visited, i, j);
          count++;
        }
      }
    }

    return count;
  }

  private static void dfsIsland(char[][] grid, boolean[][] visited,
      int i, int j) {
    if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length
        || visited[i][j] || grid[i][j] == '0') {
      return;
    }

    visited[i][j] = true;
    dfsIsland(grid, visited, i + 1, j);
    dfsIsland(grid, visited, i - 1, j);
    dfsIsland(grid, visited, i, j + 1);
    dfsIsland(grid, visited, i, j - 1);
  }

  /**
   * Maximum area of an island (largest connected component of 1s).
   *
   * @param grid 2D int array with 0 (water) and 1 (land)
   * @return maximum area
   *
   * LeetCode 695, Medium. Example: [[1,1,0],[1,1,0],[0,0,1]] → 4
   *
   * Time: O(m*n), Space: O(m*n).
   */
  public static int maxAreaOfIsland(int[][] grid) {
    if (grid == null || grid.length == 0 || grid[0].length == 0) {
      throw new IllegalArgumentException(
          "grid must be non-null and non-empty");
    }

    int m = grid.length;
    int n = grid[0].length;
    boolean[][] visited = new boolean[m][n];
    int maxArea = 0;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == 1 && !visited[i][j]) {
          int area = dfsArea(grid, visited, i, j);
          maxArea = Math.max(maxArea, area);
        }
      }
    }

    return maxArea;
  }

  private static int dfsArea(int[][] grid, boolean[][] visited,
      int i, int j) {
    if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length
        || visited[i][j] || grid[i][j] == 0) {
      return 0;
    }

    visited[i][j] = true;
    int area = 1;
    area += dfsArea(grid, visited, i + 1, j);
    area += dfsArea(grid, visited, i - 1, j);
    area += dfsArea(grid, visited, i, j + 1);
    area += dfsArea(grid, visited, i, j - 1);

    return area;
  }

  /**
   * Pacific Atlantic water flow: find cells where water flows to both oceans.
   *
   * @param heights 2D elevation grid (may not be null)
   * @return List of [row, col] where water reaches both oceans
   *
   * LeetCode 417, Medium. Pacific = top/left edge, Atlantic = bottom/right edge.
   *
   * Time: O(m*n), Space: O(m*n).
   * Tricky: Run DFS from all edges to find reachable cells.
   */
  public static List<List<Integer>> pacificAtlanticWaterFlow(
      int[][] heights) {
    if (heights == null || heights.length == 0 || heights[0].length == 0) {
      throw new IllegalArgumentException(
          "heights must be non-null and non-empty");
    }

    List<List<Integer>> result = new ArrayList<>();
    int m = heights.length;
    int n = heights[0].length;
    boolean[][] pacific = new boolean[m][n];
    boolean[][] atlantic = new boolean[m][n];

    // Run DFS from Pacific edges (top and left)
    for (int i = 0; i < m; i++) {
      dfsFlow(heights, pacific, i, 0, heights[i][0]);
    }
    for (int j = 0; j < n; j++) {
      dfsFlow(heights, pacific, 0, j, heights[0][j]);
    }

    // Run DFS from Atlantic edges (bottom and right)
    for (int i = 0; i < m; i++) {
      dfsFlow(heights, atlantic, i, n - 1, heights[i][n - 1]);
    }
    for (int j = 0; j < n; j++) {
      dfsFlow(heights, atlantic, m - 1, j, heights[m - 1][j]);
    }

    // Collect cells reachable from both oceans
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (pacific[i][j] && atlantic[i][j]) {
          result.add(List.of(i, j));
        }
      }
    }

    return result;
  }

  private static void dfsFlow(int[][] heights, boolean[][] visited,
      int i, int j, int prevHeight) {
    if (i < 0 || i >= heights.length || j < 0 || j >= heights[0].length
        || visited[i][j] || heights[i][j] < prevHeight) {
      return;
    }

    visited[i][j] = true;
    dfsFlow(heights, visited, i + 1, j, heights[i][j]);
    dfsFlow(heights, visited, i - 1, j, heights[i][j]);
    dfsFlow(heights, visited, i, j + 1, heights[i][j]);
    dfsFlow(heights, visited, i, j - 1, heights[i][j]);
  }

  // ============================================================================
  // BFS - SHORTEST PATH
  // ============================================================================

  /**
   * Shortest path in binary matrix (0 = passable, 1 = blocked).
   *
   * @param grid 2D binary grid (may not be null)
   * @return shortest path length; -1 if no path
   *
   * LeetCode 1091, Medium. Example: [[0,1],[1,0]] → 2
   *
   * Time: O(m*n), Space: O(m*n) queue.
   * Tricky: 8 directions (including diagonals).
   */
  public static int shortestPathBinaryMatrix(int[][] grid) {
    if (grid == null || grid.length == 0 || grid[0].length == 0) {
      throw new IllegalArgumentException(
          "grid must be non-null and non-empty");
    }

    if (grid[0][0] == 1) {
      return -1;
    }

    int m = grid.length;
    int n = grid[0].length;
    int[][] dirs = {
        {-1, -1}, {-1, 0}, {-1, 1},
        {0, -1}, {0, 1},
        {1, -1}, {1, 0}, {1, 1}
    };

    Deque<int[]> queue = new LinkedList<>();
    queue.add(new int[]{0, 0});
    grid[0][0] = 1;

    int dist = 1;
    while (!queue.isEmpty()) {
      int size = queue.size();
      for (int i = 0; i < size; i++) {
        int[] curr = queue.removeFirst();
        int r = curr[0];
        int c = curr[1];

        if (r == m - 1 && c == n - 1) {
          return dist;
        }

        for (int[] dir : dirs) {
          int nr = r + dir[0];
          int nc = c + dir[1];

          if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 0) {
            grid[nr][nc] = 1;
            queue.add(new int[]{nr, nc});
          }
        }
      }
      dist++;
    }

    return -1;
  }

  /**
   * Word ladder: shortest transformation from begin to end word.
   *
   * @param beginWord starting word (may not be null)
   * @param endWord target word (may not be null)
   * @param wordList available words (may not be null)
   * @return shortest path length; 0 if impossible
   *
   * LeetCode 127, Hard. Example: begin="hit", end="cog", list=["hot","dot",
   * "dog","lot","log","cog"] → 5
   *
   * Time: O(n * l²) where n=wordList size, l=word length, Space: O(n).
   * Tricky: Build graph by finding neighbors (1 char difference).
   */
  public static int wordLadder(String beginWord, String endWord,
      List<String> wordList) {
    if (beginWord == null || endWord == null || wordList == null) {
      throw new IllegalArgumentException("inputs must be non-null");
    }

    Set<String> dict = new HashSet<>(wordList);
    if (!dict.contains(endWord)) {
      return 0;
    }

    Deque<String> queue = new LinkedList<>();
    queue.add(beginWord);
    int dist = 1;

    while (!queue.isEmpty()) {
      int size = queue.size();
      for (int i = 0; i < size; i++) {
        String word = queue.removeFirst();

        if (word.equals(endWord)) {
          return dist;
        }

        // Generate neighbors (change 1 char at a time)
        List<String> neighbors = getNeighbors(word, dict);
        for (String neighbor : neighbors) {
          queue.add(neighbor);
          dict.remove(neighbor); // Mark as visited
        }
      }
      dist++;
    }

    return 0;
  }

  private static List<String> getNeighbors(String word, Set<String> dict) {
    List<String> neighbors = new ArrayList<>();
    char[] chars = word.toCharArray();

    for (int i = 0; i < chars.length; i++) {
      char old = chars[i];
      for (char c = 'a'; c <= 'z'; c++) {
        if (c == old) {
          continue;
        }
        chars[i] = c;
        String newWord = new String(chars);
        if (dict.contains(newWord)) {
          neighbors.add(newWord);
        }
      }
      chars[i] = old;
    }

    return neighbors;
  }

  /**
   * Rotting oranges: minimum time until all oranges rot or return -1.
   *
   * @param grid 2D grid with 0 (empty), 1 (fresh), 2 (rotten)
   * @return minimum time; -1 if impossible
   *
   * LeetCode 994, Medium. Example: [[2,1,1],[1,1,0],[0,1,1]] → 4
   *
   * Time: O(m*n), Space: O(m*n).
   */
  public static int rottingOranges(int[][] grid) {
    if (grid == null || grid.length == 0 || grid[0].length == 0) {
      throw new IllegalArgumentException(
          "grid must be non-null and non-empty");
    }

    int m = grid.length;
    int n = grid[0].length;
    Deque<int[]> queue = new LinkedList<>();
    int fresh = 0;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == 2) {
          queue.add(new int[]{i, j});
        } else if (grid[i][j] == 1) {
          fresh++;
        }
      }
    }

    if (fresh == 0) {
      return 0;
    }

    int[][] dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    int time = 0;

    while (!queue.isEmpty() && fresh > 0) {
      int size = queue.size();
      for (int i = 0; i < size; i++) {
        int[] curr = queue.removeFirst();
        int r = curr[0];
        int c = curr[1];

        for (int[] dir : dirs) {
          int nr = r + dir[0];
          int nc = c + dir[1];

          if (nr >= 0 && nr < m && nc >= 0 && nc < n
              && grid[nr][nc] == 1) {
            grid[nr][nc] = 2;
            queue.add(new int[]{nr, nc});
            fresh--;
          }
        }
      }
      time++;
    }

    return fresh > 0 ? -1 : time;
  }

  // ============================================================================
  // GRAPH - ADJACENCY LIST / CLONING / PROVINCES
  // ============================================================================

  /**
   * Represents an undirected graph node (public for LeetCode).
   */
  public static class Node {
    public int val;
    public List<Node> neighbors;

    /**
     * Constructs a graph node.
     *
     * @param val the node value
     */
    public Node(int val) {
      this.val = val;
      this.neighbors = new ArrayList<>();
    }
  }

  /**
   * Clone a graph node and all its neighbors.
   *
   * @param node the root node to clone (may be null)
   * @return the cloned graph
   *
   * LeetCode 133, Medium. Graph can have cycles.
   *
   * Time: O(n + e) where n=nodes, e=edges, Space: O(n).
   */
  public static Node cloneGraph(Node node) {
    if (node == null) {
      return null;
    }

    Map<Node, Node> visited = new HashMap<>();
    dfsClone(node, visited);
    return visited.get(node);
  }

  private static void dfsClone(Node node, Map<Node, Node> visited) {
    if (visited.containsKey(node)) {
      return;
    }

    Node cloned = new Node(node.val);
    visited.put(node, cloned);

    for (Node neighbor : node.neighbors) {
      dfsClone(neighbor, visited);
      cloned.neighbors.add(visited.get(neighbor));
    }
  }

  /**
   * Number of connected provinces (components).
   *
   * @param isConnected 2D adjacency matrix (may not be null)
   * @return number of provinces
   *
   * LeetCode 547, Medium. Example: [[1,0,1],[0,1,0],[1,0,1]] → 2
   *
   * Time: O(n²), Space: O(n).
   */
  public static int numProvinces(int[][] isConnected) {
    if (isConnected == null || isConnected.length == 0) {
      throw new IllegalArgumentException(
          "isConnected must be non-null and non-empty");
    }

    int n = isConnected.length;
    boolean[] visited = new boolean[n];
    int provinces = 0;

    for (int i = 0; i < n; i++) {
      if (!visited[i]) {
        dfsProvince(isConnected, visited, i);
        provinces++;
      }
    }

    return provinces;
  }

  private static void dfsProvince(int[][] isConnected,
      boolean[] visited, int i) {
    visited[i] = true;
    for (int j = 0; j < isConnected.length; j++) {
      if (isConnected[i][j] == 1 && !visited[j]) {
        dfsProvince(isConnected, visited, j);
      }
    }
  }

  // ============================================================================
  // CYCLE DETECTION & TOPOLOGICAL SORT
  // ============================================================================

  /**
   * Check if courses can be finished (no circular dependencies).
   *
   * @param numCourses total courses (0 to numCourses-1)
   * @param prerequisites [course, prerequisite] pairs
   * @return true if all courses can be finished
   *
   * LeetCode 207, Medium. Example: numCourses=2, prerequisites=[[1,0]] →
   * true
   *
   * Time: O(n + e), Space: O(n + e).
   * Tricky: DFS with 3 colors: 0=unvisited, 1=visiting, 2=visited.
   */
  public static boolean canFinishCourses(int numCourses,
      int[][] prerequisites) {
    if (prerequisites == null) {
      throw new IllegalArgumentException("prerequisites must be non-null");
    }

    List<Integer>[] adj = new ArrayList[numCourses];
    for (int i = 0; i < numCourses; i++) {
      adj[i] = new ArrayList<>();
    }

    for (int[] pre : prerequisites) {
      adj[pre[1]].add(pre[0]);
    }

    int[] color = new int[numCourses];

    for (int i = 0; i < numCourses; i++) {
      if (color[i] == 0 && hasCycleDFS(adj, color, i)) {
        return false;
      }
    }

    return true;
  }

  private static boolean hasCycleDFS(List<Integer>[] adj, int[] color,
      int node) {
    if (color[node] == 1) {
      return true; // Back edge found
    }
    if (color[node] == 2) {
      return false; // Already processed
    }

    color[node] = 1; // Visiting

    for (int neighbor : adj[node]) {
      if (hasCycleDFS(adj, color, neighbor)) {
        return true;
      }
    }

    color[node] = 2; // Visited

    return false;
  }

  /**
   * Find a valid course order (topological sort via Kahn's BFS).
   *
   * @param numCourses total courses
   * @param prerequisites [course, prerequisite] pairs
   * @return valid order; empty array if impossible
   *
   * LeetCode 210, Medium. Example: numCourses=4,
   * prerequisites=[[1,0],[2,0],[3,1],[3,2]] → [0,1,2,3] or [0,2,1,3]
   *
   * Time: O(n + e), Space: O(n + e).
   */
  public static int[] findCourseOrder(int numCourses,
      int[][] prerequisites) {
    if (prerequisites == null) {
      throw new IllegalArgumentException("prerequisites must be non-null");
    }

    List<Integer>[] adj = new ArrayList[numCourses];
    int[] indegree = new int[numCourses];

    for (int i = 0; i < numCourses; i++) {
      adj[i] = new ArrayList<>();
    }

    for (int[] pre : prerequisites) {
      adj[pre[1]].add(pre[0]);
      indegree[pre[0]]++;
    }

    Deque<Integer> queue = new LinkedList<>();
    for (int i = 0; i < numCourses; i++) {
      if (indegree[i] == 0) {
        queue.add(i);
      }
    }

    int[] order = new int[numCourses];
    int idx = 0;

    while (!queue.isEmpty()) {
      int node = queue.removeFirst();
      order[idx++] = node;

      for (int neighbor : adj[node]) {
        indegree[neighbor]--;
        if (indegree[neighbor] == 0) {
          queue.add(neighbor);
        }
      }
    }

    return idx == numCourses ? order : new int[0];
  }

  // ============================================================================
  // BIPARTITE CHECK
  // ============================================================================

  /**
   * Check if graph is bipartite (2-colorable).
   *
   * @param graph adjacency list (may not be null)
   * @return true if bipartite, false otherwise
   *
   * LeetCode 785, Medium. Example: [[1,3],[0,2],[1,3],[0,2]] → true
   *
   * Time: O(n + e), Space: O(n).
   * Tricky: Color nodes 0 or 1; adjacent nodes must differ.
   */
  public static boolean isBipartite(int[][] graph) {
    if (graph == null) {
      throw new IllegalArgumentException("graph must be non-null");
    }

    int n = graph.length;
    int[] color = new int[n];
    java.util.Arrays.fill(color, -1);

    for (int i = 0; i < n; i++) {
      if (color[i] == -1) {
        if (!dfsBipartite(graph, color, i, 0)) {
          return false;
        }
      }
    }

    return true;
  }

  private static boolean dfsBipartite(int[][] graph, int[] color, int node,
      int nodeColor) {
    if (color[node] != -1) {
      return color[node] == nodeColor;
    }

    color[node] = nodeColor;

    for (int neighbor : graph[node]) {
      if (!dfsBipartite(graph, color, neighbor, 1 - nodeColor)) {
        return false;
      }
    }

    return true;
  }

  // ============================================================================
  // UNION FIND
  // ============================================================================

  /**
   * Union Find data structure with path compression and union by rank.
   */
  public static class UnionFind {
    private int[] parent;
    private int[] rank;

    /**
     * Initialize union find for n elements (0 to n-1).
     *
     * @param n the number of elements
     */
    public UnionFind(int n) {
      this.parent = new int[n];
      this.rank = new int[n];
      for (int i = 0; i < n; i++) {
        parent[i] = i;
        rank[i] = 0;
      }
    }

    /**
     * Find root with path compression.
     *
     * @param x element index
     * @return root of x
     */
    public int find(int x) {
      if (parent[x] != x) {
        parent[x] = find(parent[x]);
      }
      return parent[x];
    }

    /**
     * Union two elements by rank.
     *
     * @param x first element
     * @param y second element
     * @return true if union happened, false if already connected
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

      return true;
    }
  }

  /**
   * Number of connected components.
   *
   * @param n total nodes (0 to n-1)
   * @param edges edges [u, v] (may not be null)
   * @return number of connected components
   *
   * LeetCode 323, Medium. Example: n=5, edges=[[0,1],[1,2],[3,4]] → 2
   *
   * Time: O(n + e * α(n)), Space: O(n).
   */
  public static int numConnectedComponents(int n, int[][] edges) {
    if (edges == null) {
      throw new IllegalArgumentException("edges must be non-null");
    }

    UnionFind uf = new UnionFind(n);

    for (int[] edge : edges) {
      uf.union(edge[0], edge[1]);
    }

    Set<Integer> roots = new HashSet<>();
    for (int i = 0; i < n; i++) {
      roots.add(uf.find(i));
    }

    return roots.size();
  }

  /**
   * Merge accounts by email addresses.
   *
   * @param accounts List of [name, email1, email2, ...] (may not be null)
   * @return merged accounts grouped by person
   *
   * LeetCode 721, Medium. Example: accounts=[["John","john@example.com",
   * "john00@example.com"],["John","john0@example.com"],
   * ["Mary","mary@example.com"]] → merged correctly
   *
   * Time: O(n * k log(n*k)) where n=accounts, k=emails/account,
   * Space: O(n*k).
   */
  public static List<List<String>> accountsMerge(
      List<List<String>> accounts) {
    if (accounts == null) {
      throw new IllegalArgumentException("accounts must be non-null");
    }

    Map<String, Integer> emailToAccount = new HashMap<>();
    UnionFind uf = new UnionFind(accounts.size());

    // Union accounts by email
    for (int i = 0; i < accounts.size(); i++) {
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
    for (int root : rootToEmails.keySet()) {
      List<String> merged = new ArrayList<>();
      merged.add(accounts.get(root).get(0)); // Name
      java.util.Collections.sort(rootToEmails.get(root));
      merged.addAll(rootToEmails.get(root));
      result.add(merged);
    }

    return result;
  }

  // ============================================================================
  // MAIN: Test cases
  // ============================================================================

  /**
   * Main method demonstrating graph operations.
   *
   * @param args not used
   */
  public static void main(String[] args) {
    System.out.println("=== Graph DFS/BFS ===\n");

    System.out.println("GRID DFS:");
    char[][] grid1 = {{'1', '1'}, {'0', '1'}};
    System.out.println("Num Islands: " + numIslands(grid1));

    int[][] grid2 = {{1, 1, 0}, {1, 1, 0}, {0, 0, 1}};
    System.out.println("Max Area of Island: " + maxAreaOfIsland(grid2));

    System.out.println("\nBFS:");
    int[][] path = {{0, 1}, {1, 0}};
    System.out.println("Shortest Path Binary Matrix: " + shortestPathBinaryMatrix(path));

    System.out.println("\nTOPOLOGICAL SORT:");
    int[][] pre = {{1, 0}};
    System.out.println("Can Finish: " + canFinishCourses(2, pre));

    int[][] pre2 = {{1, 0}, {2, 0}, {3, 1}, {3, 2}};
    System.out.println("Course Order: " + java.util.Arrays.toString(
        findCourseOrder(4, pre2)));

    System.out.println("\nBIPARTITE:");
    int[][] graph = {{1, 3}, {0, 2}, {1, 3}, {0, 2}};
    System.out.println("Is Bipartite: " + isBipartite(graph));

    System.out.println("\nUNION FIND:");
    int[][] edges = {{0, 1}, {1, 2}, {3, 4}};
    System.out.println("Connected Components: " + numConnectedComponents(5, edges));
  }
}
