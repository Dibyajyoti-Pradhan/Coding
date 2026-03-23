import java.util.ArrayList;
import java.util.List;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Matrix manipulation problems covering traversal, transformation, search, and pathfinding.
 *
 * <p>Key patterns:
 * <ul>
 *   <li><b>Traversal:</b> Spiral order, diagonal, layer-by-layer
 *   <li><b>Transformation:</b> Rotation, transpose, zero marking
 *   <li><b>Search:</b> Binary search on sorted matrix, 2D pointer movement
 *   <li><b>DFS/BFS:</b> Islands, regions, flood fill with in-place marking
 *   <li><b>DP:</b> Paths, sums, squares with space optimization
 *   <li><b>Simulation:</b> Game of Life, state transitions
 * </ul>
 */
public class MatrixProblems {

  // Direction vectors for 4-way and 8-way movement
  private static final int[][] DIRECTIONS_4 = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
  private static final int[][] DIRECTIONS_8 = {
    {0, 1}, {1, 0}, {0, -1}, {-1, 0}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}
  };

  private static final char WATER = 'W';
  private static final char LAND = 'L';
  private static final int GATE = 0;
  private static final int EMPTY = Integer.MAX_VALUE;
  private static final int ALIVE = 1;
  private static final int DEAD = 0;

  // ===================== SECTION 1: TRAVERSAL =====================

  /**
   * Returns elements in spiral order (clockwise from outside).
   *
   * <p><b>LeetCode 54 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * matrix = [[1,2,3],[4,5,6],[7,8,9]]
   * Output: [1,2,3,6,9,8,7,4,5]
   * </pre>
   *
   * <p><b>Constraints:</b> m, n ≤ 10
   *
   * <p><b>Time:</b> O(m·n) <b>Space:</b> O(m·n) for output
   *
   * <p><b>Tricky:</b> Maintain 4 boundaries (top, bottom, left, right). After each
   * direction, shrink corresponding boundary.
   *
   * @param matrix input m×n matrix
   * @return list of elements in spiral order
   */
  public static List<Integer> spiralOrder(int[][] matrix) {
    List<Integer> result = new ArrayList<>();

    if (matrix == null || matrix.length == 0) {
      return result;
    }

    int top = 0;
    int bottom = matrix.length - 1;
    int left = 0;
    int right = matrix[0].length - 1;

    while (top <= bottom && left <= right) {
      // Right
      for (int col = left; col <= right; col++) {
        result.add(matrix[top][col]);
      }
      top++;

      // Down
      for (int row = top; row <= bottom; row++) {
        result.add(matrix[row][right]);
      }
      right--;

      // Left
      if (top <= bottom) {
        for (int col = right; col >= left; col--) {
          result.add(matrix[bottom][col]);
        }
        bottom--;
      }

      // Up
      if (left <= right) {
        for (int row = bottom; row >= top; row--) {
          result.add(matrix[row][left]);
        }
        left++;
      }
    }

    return result;
  }

  /**
   * Generates n×n spiral matrix with numbers 1 to n².
   *
   * <p><b>LeetCode 59 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * n = 3
   * Output: [[1,2,3],[8,9,4],[7,6,5]]
   * </pre>
   *
   * <p><b>Constraints:</b> 1 ≤ n ≤ 10
   *
   * <p><b>Time:</b> O(n²) <b>Space:</b> O(n²)
   *
   * <p><b>Tricky:</b> Spiral generation uses same boundary shrinking as spiral extraction.
   *
   * @param n size of matrix
   * @return n×n spiral matrix
   */
  public static int[][] generateSpiralMatrix(int n) {
    int[][] matrix = new int[n][n];

    int top = 0;
    int bottom = n - 1;
    int left = 0;
    int right = n - 1;
    int num = 1;

    while (top <= bottom && left <= right) {
      // Right
      for (int col = left; col <= right; col++) {
        matrix[top][col] = num++;
      }
      top++;

      // Down
      for (int row = top; row <= bottom; row++) {
        matrix[row][right] = num++;
      }
      right--;

      // Left
      if (top <= bottom) {
        for (int col = right; col >= left; col--) {
          matrix[bottom][col] = num++;
        }
        bottom--;
      }

      // Up
      if (left <= right) {
        for (int row = bottom; row >= top; row--) {
          matrix[row][left] = num++;
        }
        left++;
      }
    }

    return matrix;
  }

  /**
   * Returns diagonal elements of matrix alternating direction.
   *
   * <p><b>LeetCode 498 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * matrix = [[1,2,3],[4,5,6],[7,8,9]]
   * Output: [1,2,4,7,5,3,6,8,9]
   * </pre>
   *
   * <p><b>Constraints:</b> m, n ≤ 10^3
   *
   * <p><b>Time:</b> O(m·n) <b>Space:</b> O(m·n)
   *
   * <p><b>Tricky:</b> Diagonals are identified by r+c = k. Direction alternates: go
   * up-right then down-left.
   *
   * @param matrix input matrix
   * @return diagonal elements
   */
  public static int[] diagonalTraverse(int[][] matrix) {
    if (matrix == null || matrix.length == 0) {
      return new int[0];
    }

    int m = matrix.length;
    int n = matrix[0].length;
    int[] result = new int[m * n];
    int index = 0;

    for (int d = 0; d < m + n - 1; d++) {
      if (d % 2 == 0) {
        // Going up-right
        int row = Math.min(d, m - 1);
        int col = d - row;
        while (row >= 0 && col < n) {
          result[index++] = matrix[row][col];
          row--;
          col++;
        }
      } else {
        // Going down-left
        int col = Math.min(d, n - 1);
        int row = d - col;
        while (col >= 0 && row < m) {
          result[index++] = matrix[row][col];
          row++;
          col--;
        }
      }
    }

    return result;
  }

  // ===================== SECTION 2: TRANSFORMATION =====================

  /**
   * Rotates n×n matrix 90 degrees clockwise in-place.
   *
   * <p><b>LeetCode 48 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * matrix = [[1,2,3],[4,5,6],[7,8,9]]
   * After rotation: [[7,4,1],[8,5,2],[9,6,3]]
   * </pre>
   *
   * <p><b>Constraints:</b> n ≤ 500
   *
   * <p><b>Time:</b> O(n²) <b>Space:</b> O(1)
   *
   * <p><b>Tricky:</b> Two-step: 1) Transpose (swap matrix[i][j] with matrix[j][i]),
   * 2) Reverse each row.
   *
   * @param matrix n×n matrix to rotate
   */
  public static void rotateImage(int[][] matrix) {
    if (matrix == null || matrix.length == 0) {
      return;
    }

    int n = matrix.length;

    // Transpose
    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        int temp = matrix[i][j];
        matrix[i][j] = matrix[j][i];
        matrix[j][i] = temp;
      }
    }

    // Reverse each row
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n / 2; j++) {
        int temp = matrix[i][j];
        matrix[i][j] = matrix[i][n - 1 - j];
        matrix[i][n - 1 - j] = temp;
      }
    }
  }

  /**
   * Sets matrix elements to 0 if row or column contains 0.
   *
   * <p><b>LeetCode 73 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * matrix = [[0,1,2],[3,4,5],[1,2,0]]
   * After: [[0,0,0],[0,4,0],[0,0,0]]
   * </pre>
   *
   * <p><b>Constraints:</b> m, n ≤ 300
   *
   * <p><b>Time:</b> O(m·n) <b>Space:</b> O(1) with first row/col markers
   *
   * <p><b>Tricky:</b> Use first row and column as markers. Handle edge case where they
   * themselves need zeroing.
   *
   * @param matrix matrix to modify
   */
  public static void setMatrixZeroes(int[][] matrix) {
    if (matrix == null || matrix.length == 0) {
      return;
    }

    int m = matrix.length;
    int n = matrix[0].length;
    boolean firstRowZero = false;
    boolean firstColZero = false;

    // Check if first row/col need zeroing
    for (int j = 0; j < n; j++) {
      if (matrix[0][j] == 0) {
        firstRowZero = true;
        break;
      }
    }
    for (int i = 0; i < m; i++) {
      if (matrix[i][0] == 0) {
        firstColZero = true;
        break;
      }
    }

    // Mark zeros in first row/col
    for (int i = 1; i < m; i++) {
      for (int j = 1; j < n; j++) {
        if (matrix[i][j] == 0) {
          matrix[i][0] = 0;
          matrix[0][j] = 0;
        }
      }
    }

    // Set zeros
    for (int i = 1; i < m; i++) {
      for (int j = 1; j < n; j++) {
        if (matrix[i][0] == 0 || matrix[0][j] == 0) {
          matrix[i][j] = 0;
        }
      }
    }

    // Handle first row/col
    if (firstRowZero) {
      for (int j = 0; j < n; j++) {
        matrix[0][j] = 0;
      }
    }
    if (firstColZero) {
      for (int i = 0; i < m; i++) {
        matrix[i][0] = 0;
      }
    }
  }

  /**
   * Transposes a matrix.
   *
   * <p><b>LeetCode 867 (Easy)</b>
   *
   * <p><b>Time:</b> O(m·n) <b>Space:</b> O(m·n)
   *
   * @param matrix input matrix
   * @return transposed matrix
   */
  public static int[][] transpose(int[][] matrix) {
    if (matrix == null || matrix.length == 0) {
      return matrix;
    }

    int m = matrix.length;
    int n = matrix[0].length;
    int[][] result = new int[n][m];

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        result[j][i] = matrix[i][j];
      }
    }

    return result;
  }

  // ===================== SECTION 3: SEARCH =====================

  /**
   * Searches for target in a 2D matrix (rows and columns sorted).
   *
   * <p><b>LeetCode 74 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
   * Output: true
   * </pre>
   *
   * <p><b>Constraints:</b> m, n ≤ 100
   *
   * <p><b>Time:</b> O(log(m·n)) <b>Space:</b> O(1)
   *
   * <p><b>Tricky:</b> Treat 2D matrix as 1D sorted array. Map 1D index to 2D: row =
   * idx / n, col = idx % n.
   *
   * @param matrix sorted m×n matrix
   * @param target value to search
   * @return true if target found
   */
  public static boolean searchMatrix(int[][] matrix, int target) {
    if (matrix == null || matrix.length == 0) {
      return false;
    }

    int m = matrix.length;
    int n = matrix[0].length;
    int left = 0;
    int right = m * n - 1;

    while (left <= right) {
      int mid = left + (right - left) / 2;
      int val = matrix[mid / n][mid % n];

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
   * Searches for target in matrix (each row and column sorted).
   *
   * <p><b>LeetCode 240 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * matrix = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]], target = 5
   * Output: true
   * </pre>
   *
   * <p><b>Constraints:</b> m, n ≤ 500
   *
   * <p><b>Time:</b> O(m + n) <b>Space:</b> O(1)
   *
   * <p><b>Tricky:</b> Start from top-right (or bottom-left). Move left if current >
   * target, down if current < target.
   *
   * @param matrix sorted by rows and columns
   * @param target value to search
   * @return true if target found
   */
  public static boolean searchMatrixII(int[][] matrix, int target) {
    if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
      return false;
    }

    int m = matrix.length;
    int n = matrix[0].length;
    int row = 0;
    int col = n - 1;

    while (row < m && col >= 0) {
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

  // ===================== SECTION 4: DFS/BFS ISLANDS =====================

  /**
   * Counts number of islands (connected 1s) in grid.
   *
   * <p><b>LeetCode 200 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * grid = [['1','1','0'],['1','0','0'],['0','0','1']]
   * Output: 2
   * </pre>
   *
   * <p><b>Constraints:</b> m, n ≤ 300
   *
   * <p><b>Time:</b> O(m·n) <b>Space:</b> O(m·n) for recursion
   *
   * <p><b>Tricky:</b> DFS with in-place marking (set visited cells to '0'). No need
   * for separate visited array.
   *
   * @param grid 2D char grid with '0' and '1'
   * @return number of islands
   */
  public static int numIslands(char[][] grid) {
    if (grid == null || grid.length == 0) {
      return 0;
    }

    int m = grid.length;
    int n = grid[0].length;
    int islandCount = 0;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == '1') {
          islandCount++;
          dfsIslands(grid, i, j, m, n);
        }
      }
    }

    return islandCount;
  }

  /**
   * DFS helper to mark connected land cells.
   *
   * @param grid the grid
   * @param row current row
   * @param col current column
   * @param m total rows
   * @param n total columns
   */
  private static void dfsIslands(char[][] grid, int row, int col, int m, int n) {
    if (row < 0 || row >= m || col < 0 || col >= n || grid[row][col] != '1') {
      return;
    }

    grid[row][col] = '0'; // Mark as visited
    for (int[] dir : DIRECTIONS_4) {
      dfsIslands(grid, row + dir[0], col + dir[1], m, n);
    }
  }

  /**
   * Finds maximum area of island.
   *
   * <p><b>LeetCode 695 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * grid = [[0,0,1,0],[1,0,1,0],[1,1,1,0],[1,0,0,0]]
   * Output: 6
   * </pre>
   *
   * <p><b>Time:</b> O(m·n) <b>Space:</b> O(m·n)
   *
   * @param grid 2D int grid
   * @return maximum island area
   */
  public static int maxAreaOfIsland(int[][] grid) {
    if (grid == null || grid.length == 0) {
      return 0;
    }

    int m = grid.length;
    int n = grid[0].length;
    int maxArea = 0;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == 1) {
          maxArea = Math.max(maxArea, dfsArea(grid, i, j, m, n));
        }
      }
    }

    return maxArea;
  }

  /**
   * DFS to calculate island area.
   *
   * @param grid the grid
   * @param row current row
   * @param col current column
   * @param m total rows
   * @param n total columns
   * @return area of connected land
   */
  private static int dfsArea(int[][] grid, int row, int col, int m, int n) {
    if (row < 0 || row >= m || col < 0 || col >= n || grid[row][col] != 1) {
      return 0;
    }

    grid[row][col] = 0;
    int area = 1;
    for (int[] dir : DIRECTIONS_4) {
      area += dfsArea(grid, row + dir[0], col + dir[1], m, n);
    }
    return area;
  }

  /**
   * Surrounds regions of '0's with 'X', marking border-connected '0's safe first.
   *
   * <p><b>LeetCode 130 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * board = [['X','X','X'],['X','O','X'],['X','X','X']]
   * After: [['X','X','X'],['X','X','X'],['X','X','X']]
   * </pre>
   *
   * <p><b>Constraints:</b> m, n ≤ 200
   *
   * <p><b>Time:</b> O(m·n) <b>Space:</b> O(m·n)
   *
   * <p><b>Tricky:</b> Reverse logic: mark border-reachable O's safe first, then flip
   * remaining O's to X's.
   *
   * @param board 2D char board
   */
  public static void surroundedRegions(char[][] board) {
    if (board == null || board.length == 0) {
      return;
    }

    int m = board.length;
    int n = board[0].length;

    // Mark border-reachable O's as safe (#)
    for (int i = 0; i < m; i++) {
      if (board[i][0] == 'O') dfsSurrounded(board, i, 0, m, n);
      if (board[i][n - 1] == 'O') dfsSurrounded(board, i, n - 1, m, n);
    }
    for (int j = 0; j < n; j++) {
      if (board[0][j] == 'O') dfsSurrounded(board, 0, j, m, n);
      if (board[m - 1][j] == 'O') dfsSurrounded(board, m - 1, j, m, n);
    }

    // Flip remaining O's to X's and restore safe O's
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (board[i][j] == 'O') {
          board[i][j] = 'X';
        } else if (board[i][j] == '#') {
          board[i][j] = 'O';
        }
      }
    }
  }

  /**
   * DFS to mark border-reachable O's.
   */
  private static void dfsSurrounded(char[][] board, int row, int col, int m, int n) {
    if (row < 0 || row >= m || col < 0 || col >= n || board[row][col] != 'O') {
      return;
    }

    board[row][col] = '#';
    for (int[] dir : DIRECTIONS_4) {
      dfsSurrounded(board, row + dir[0], col + dir[1], m, n);
    }
  }

  /**
   * Finds pacific/atlantic water flow cells via reverse BFS from borders.
   *
   * <p><b>LeetCode 417 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * heights = [[1,2,2,3],[5,5,4,3],[3,2,3,1]]
   * Output: [[0,2],[1,0],[1,1],[2,0],[2,1],[2,2]]
   * </pre>
   *
   * <p><b>Constraints:</b> m, n ≤ 150
   *
   * <p><b>Time:</b> O(m·n) <b>Space:</b> O(m·n)
   *
   * <p><b>Tricky:</b> Reverse logic: BFS from ocean borders (edges). Water flows from
   * high to low, so traverse from low to high (backwards).
   *
   * @param heights elevation map
   * @return list of cells flowing to both oceans
   */
  public static List<List<Integer>> pacificAtlanticWaterFlow(int[][] heights) {
    List<List<Integer>> result = new ArrayList<>();

    if (heights == null || heights.length == 0) {
      return result;
    }

    int m = heights.length;
    int n = heights[0].length;
    boolean[][] pacificReach = new boolean[m][n];
    boolean[][] atlanticReach = new boolean[m][n];

    // BFS from pacific (top/left) and atlantic (bottom/right) borders
    for (int i = 0; i < m; i++) {
      bfsWaterFlow(heights, i, 0, pacificReach, m, n);
      bfsWaterFlow(heights, i, n - 1, atlanticReach, m, n);
    }
    for (int j = 0; j < n; j++) {
      bfsWaterFlow(heights, 0, j, pacificReach, m, n);
      bfsWaterFlow(heights, m - 1, j, atlanticReach, m, n);
    }

    // Collect cells reachable by both
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (pacificReach[i][j] && atlanticReach[i][j]) {
          result.add(List.of(i, j));
        }
      }
    }

    return result;
  }

  /**
   * BFS for water flow (reverse direction).
   */
  private static void bfsWaterFlow(
      int[][] heights, int row, int col, boolean[][] reach, int m, int n) {
    Queue<int[]> queue = new LinkedList<>();
    queue.offer(new int[]{row, col});
    reach[row][col] = true;

    while (!queue.isEmpty()) {
      int[] pos = queue.poll();
      int r = pos[0];
      int c = pos[1];

      for (int[] dir : DIRECTIONS_4) {
        int newR = r + dir[0];
        int newC = c + dir[1];

        if (newR >= 0 && newR < m && newC >= 0 && newC < n && !reach[newR][newC]
            && heights[newR][newC] >= heights[r][c]) {
          reach[newR][newC] = true;
          queue.offer(new int[]{newR, newC});
        }
      }
    }
  }

  // ===================== SECTION 5: SHORTEST PATH BFS =====================

  /**
   * Shortest path in binary matrix (8-directional BFS).
   *
   * <p><b>LeetCode 1091 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * grid = [[0,1],[1,0]]
   * Output: 2
   * </pre>
   *
   * <p><b>Constraints:</b> n ≤ 100
   *
   * <p><b>Time:</b> O(n²) <b>Space:</b> O(n²)
   *
   * <p><b>Tricky:</b> 8-directional movement (including diagonals). BFS guarantees
   * shortest path.
   *
   * @param grid binary matrix (0=free, 1=obstacle)
   * @return shortest path length or -1 if impossible
   */
  public static int shortestPathBinaryMatrix(int[][] grid) {
    if (grid == null || grid.length == 0 || grid[0][0] == 1) {
      return -1;
    }

    int n = grid.length;
    Queue<int[]> queue = new LinkedList<>();
    queue.offer(new int[]{0, 0});
    grid[0][0] = 1; // Mark visited

    int distance = 1;

    while (!queue.isEmpty()) {
      int size = queue.size();
      for (int i = 0; i < size; i++) {
        int[] pos = queue.poll();
        int row = pos[0];
        int col = pos[1];

        if (row == n - 1 && col == n - 1) {
          return distance;
        }

        for (int[] dir : DIRECTIONS_8) {
          int newRow = row + dir[0];
          int newCol = col + dir[1];

          if (newRow >= 0 && newRow < n && newCol >= 0 && newCol < n
              && grid[newRow][newCol] == 0) {
            grid[newRow][newCol] = 1;
            queue.offer(new int[]{newRow, newCol});
          }
        }
      }
      distance++;
    }

    return -1;
  }

  /**
   * Minimum time for oranges to rot (multi-source BFS).
   *
   * <p><b>LeetCode 994 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * grid = [[2,1,1],[1,1,0],[0,1,1]]
   * Output: 4
   * </pre>
   *
   * <p><b>Constraints:</b> m, n ≤ 10
   *
   * <p><b>Time:</b> O(m·n) <b>Space:</b> O(m·n)
   *
   * <p><b>Tricky:</b> Multi-source BFS: add all rotten oranges to queue first, then
   * spread simultaneously.
   *
   * @param grid orange grid (0=empty, 1=fresh, 2=rotten)
   * @return minutes until all oranges rotten, or -1
   */
  public static int rottingOranges(int[][] grid) {
    if (grid == null || grid.length == 0) {
      return -1;
    }

    int m = grid.length;
    int n = grid[0].length;
    Queue<int[]> queue = new LinkedList<>();
    int freshCount = 0;

    // Find all rotten oranges and count fresh
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == 2) {
          queue.offer(new int[]{i, j});
        } else if (grid[i][j] == 1) {
          freshCount++;
        }
      }
    }

    if (freshCount == 0) {
      return 0;
    }

    int minutes = 0;
    while (!queue.isEmpty() && freshCount > 0) {
      int size = queue.size();
      for (int i = 0; i < size; i++) {
        int[] pos = queue.poll();
        int row = pos[0];
        int col = pos[1];

        for (int[] dir : DIRECTIONS_4) {
          int newRow = row + dir[0];
          int newCol = col + dir[1];

          if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n
              && grid[newRow][newCol] == 1) {
            grid[newRow][newCol] = 2;
            freshCount--;
            queue.offer(new int[]{newRow, newCol});
          }
        }
      }
      minutes++;
    }

    return freshCount == 0 ? minutes : -1;
  }

  /**
   * Updates matrix: distance to nearest 0 for each cell.
   *
   * <p><b>LeetCode 286 (Medium)</b>
   *
   * <p><b>Time:</b> O(m·n) <b>Space:</b> O(m·n)
   *
   * @param rooms matrix (0=gate, MAX=room)
   */
  public static void wallsAndGates(int[][] rooms) {
    if (rooms == null || rooms.length == 0) {
      return;
    }

    int m = rooms.length;
    int n = rooms[0].length;
    Queue<int[]> queue = new LinkedList<>();

    // Add all gates to queue
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (rooms[i][j] == GATE) {
          queue.offer(new int[]{i, j});
        }
      }
    }

    // Multi-source BFS
    while (!queue.isEmpty()) {
      int[] pos = queue.poll();
      int row = pos[0];
      int col = pos[1];

      for (int[] dir : DIRECTIONS_4) {
        int newRow = row + dir[0];
        int newCol = col + dir[1];

        if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n
            && rooms[newRow][newCol] == EMPTY) {
          rooms[newRow][newCol] = rooms[row][col] + 1;
          queue.offer(new int[]{newRow, newCol});
        }
      }
    }
  }

  // ===================== SECTION 6: MATRIX DP =====================

  /**
   * Number of unique paths in m×n grid (move right or down only).
   *
   * <p><b>LeetCode 62 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * m = 3, n = 7
   * Output: 28
   * </pre>
   *
   * <p><b>Constraints:</b> 1 ≤ m, n ≤ 100
   *
   * <p><b>Time:</b> O(m·n) <b>Space:</b> O(n) with optimization
   *
   * <p><b>Tricky:</b> DP with space optimization: use 1D array, update from left to right.
   *
   * @param m number of rows
   * @param n number of columns
   * @return number of unique paths
   */
  public static int uniquePaths(int m, int n) {
    if (m <= 0 || n <= 0) {
      return 0;
    }

    int[] dp = new int[n];
    dp[0] = 1;

    for (int i = 0; i < m; i++) {
      for (int j = 1; j < n; j++) {
        dp[j] += dp[j - 1];
      }
    }

    return dp[n - 1];
  }

  /**
   * Minimum path sum in grid (grid[i][j] >= 0, move right or down).
   *
   * <p><b>LeetCode 64 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * grid = [[1,3,1],[1,5,1],[4,2,1]]
   * Output: 7 (path: 1->3->1->1->1)
   * </pre>
   *
   * <p><b>Constraints:</b> m, n ≤ 200
   *
   * <p><b>Time:</b> O(m·n) <b>Space:</b> O(m·n) for in-place
   *
   * @param grid input grid
   * @return minimum path sum
   */
  public static int minPathSum(int[][] grid) {
    if (grid == null || grid.length == 0) {
      return 0;
    }

    int m = grid.length;
    int n = grid[0].length;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (i == 0 && j == 0) continue;
        if (i == 0) {
          grid[i][j] += grid[i][j - 1];
        } else if (j == 0) {
          grid[i][j] += grid[i - 1][j];
        } else {
          grid[i][j] += Math.min(grid[i - 1][j], grid[i][j - 1]);
        }
      }
    }

    return grid[m - 1][n - 1];
  }

  /**
   * Largest square submatrix with all 1s.
   *
   * <p><b>LeetCode 221 (Medium)</b>
   *
   * <p><b>Example:</b>
   * <pre>
   * matrix = [['1','0','1'],['1','1','1'],['1','1','1']]
   * Output: 4 (2x2 square)
   * </pre>
   *
   * <p><b>Constraints:</b> m, n ≤ 300
   *
   * <p><b>Time:</b> O(m·n) <b>Space:</b> O(m·n)
   *
   * <p><b>Tricky:</b> dp[i][j] = min(top, left, diagonal) + 1. Side length = max dp value.
   *
   * @param matrix char matrix with '0' and '1'
   * @return area of largest square
   */
  public static int maximalSquare(char[][] matrix) {
    if (matrix == null || matrix.length == 0) {
      return 0;
    }

    int m = matrix.length;
    int n = matrix[0].length;
    int[][] dp = new int[m + 1][n + 1];
    int maxSide = 0;

    for (int i = 1; i <= m; i++) {
      for (int j = 1; j <= n; j++) {
        if (matrix[i - 1][j - 1] == '1') {
          dp[i][j] = Math.min(Math.min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1;
          maxSide = Math.max(maxSide, dp[i][j]);
        }
      }
    }

    return maxSide * maxSide;
  }

  // ===================== SECTION 7: SIMULATION =====================

  /**
   * Game of Life: simulate cells with birth/death rules.
   *
   * <p><b>LeetCode 289 (Medium)</b>
   *
   * <p><b>Rules:</b>
   * <ul>
   *   <li>Live cell, 2-3 neighbors: survives
   *   <li>Live cell, <2 or >3 neighbors: dies
   *   <li>Dead cell, exactly 3 neighbors: becomes alive
   * </ul>
   *
   * <p><b>Constraints:</b> m, n ≤ 25
   *
   * <p><b>Time:</b> O(m·n) <b>Space:</b> O(1) with encoding
   *
   * <p><b>Tricky:</b> Encode state: use bit 0 for current, bit 1 for next. -1 = live→dead,
   * 2 = dead→live.
   *
   * @param board board to update in-place
   */
  public static void gameOfLife(int[][] board) {
    if (board == null || board.length == 0) {
      return;
    }

    int m = board.length;
    int n = board[0].length;

    // Count neighbors and encode state
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        int liveNeighbors = 0;
        for (int[] dir : DIRECTIONS_8) {
          int newRow = i + dir[0];
          int newCol = j + dir[1];
          if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n) {
            liveNeighbors += board[newRow][newCol] & 1;
          }
        }

        if ((board[i][j] & 1) == ALIVE) {
          // Live cell
          if (liveNeighbors == 2 || liveNeighbors == 3) {
            board[i][j] = 3; // Stays alive
          }
        } else {
          // Dead cell
          if (liveNeighbors == 3) {
            board[i][j] = 2; // Becomes alive
          }
        }
      }
    }

    // Decode state
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        board[i][j] >>= 1;
      }
    }
  }

  /**
   * Main method demonstrating all matrix problems.
   *
   * @param args unused
   */
  public static void main(String[] args) {
    System.out.println("=== Matrix Problems ===\n");

    // Traversal
    System.out.println("1. Spiral Order:");
    int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    System.out.println(spiralOrder(matrix));

    System.out.println("\n2. Generate Spiral:");
    int[][] spiral = generateSpiralMatrix(3);
    for (int[] row : spiral) {
      System.out.println(java.util.Arrays.toString(row));
    }

    // Rotation
    System.out.println("\n3. Rotate Image:");
    int[][] rotate = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    rotateImage(rotate);
    for (int[] row : rotate) {
      System.out.println(java.util.Arrays.toString(row));
    }

    // Search
    System.out.println("\n4. Search Matrix:");
    int[][] searchMat = {{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}};
    System.out.println("Found 3: " + searchMatrix(searchMat, 3));

    // Islands
    System.out.println("\n5. Island Count:");
    char[][] grid = {{'1', '1', '0'}, {'1', '0', '0'}, {'0', '0', '1'}};
    System.out.println("Islands: " + numIslands(grid));

    // Paths
    System.out.println("\n6. Unique Paths (3x7):");
    System.out.println("Paths: " + uniquePaths(3, 7));

    // Squares
    System.out.println("\n7. Maximal Square:");
    char[][] sq = {{'1', '0', '1'}, {'1', '1', '1'}, {'1', '1', '1'}};
    System.out.println("Max square area: " + maximalSquare(sq));
  }
}
