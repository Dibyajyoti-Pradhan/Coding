/// @file 17_Matrix.cpp
/// @brief Matrix algorithms: traversal, transformation, search, DFS/BFS,
///        shortest path, dynamic programming, and simulation.
///
/// Treat matrix as graph for DFS/BFS; flatten 2D index as `row*cols+col`;
/// 4-dir and 8-dir arrays as `constexpr`; Game of Life in-place encoding:
/// `-1`=live→dead, `2`=dead→live (so `abs(val)==1` means currently/was
/// alive).
///
/// Time/Space varies per algorithm (see individual functions).

#include <algorithm>
#include <climits>
#include <iostream>
#include <queue>
#include <vector>

namespace matrix_playground {

// Direction arrays for 4 and 8 directional movement
constexpr int kDirs4[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
constexpr int kDirs8[8][2] = {
    {0, 1}, {1, 0}, {0, -1}, {-1, 0},
    {1, 1}, {1, -1}, {-1, 1}, {-1, -1}
};

// ============================================================================
// PATTERN 1 — TRAVERSAL
// ============================================================================

/// @brief LC 54: Spiral order traversal.
/// @param matrix 2D grid of integers.
/// @return Elements in spiral order (clockwise, outside-in).
/// @details Example: [[1,2,3],[4,5,6],[7,8,9]] → [1,2,3,6,9,8,7,4,5].
/// @constraints Time: O(m*n), Space: O(1) (output not counted).
/// @note Tricky: 4 boundary pointers; collapse them inward.
[[nodiscard]] std::vector<int> SpiralOrder(
    const std::vector<std::vector<int>>& matrix) noexcept {
  std::vector<int> result;
  if (matrix.empty()) return result;

  int top = 0, bottom = matrix.size() - 1;
  int left = 0, right = matrix[0].size() - 1;

  while (top <= bottom && left <= right) {
    // Right
    for (int col = left; col <= right; ++col) {
      result.emplace_back(matrix[top][col]);
    }
    ++top;

    // Down
    for (int row = top; row <= bottom; ++row) {
      result.emplace_back(matrix[row][right]);
    }
    --right;

    // Left
    if (top <= bottom) {
      for (int col = right; col >= left; --col) {
        result.emplace_back(matrix[bottom][col]);
      }
      --bottom;
    }

    // Up
    if (left <= right) {
      for (int row = bottom; row >= top; --row) {
        result.emplace_back(matrix[row][left]);
      }
      ++left;
    }
  }

  return result;
}

/// @brief LC 59: Generate spiral matrix.
/// @param n Dimension (n×n).
/// @return Matrix filled 1→n² in spiral order.
/// @details Example: n=3 → [[1,2,3],[8,9,4],[7,6,5]].
/// @constraints Time: O(n²), Space: O(1) (output not counted).
[[nodiscard]] std::vector<std::vector<int>> GenerateSpiralMatrix(
    int n) noexcept {
  std::vector<std::vector<int>> result(n, std::vector<int>(n, 0));

  int top = 0, bottom = n - 1, left = 0, right = n - 1;
  int num = 1;

  while (top <= bottom && left <= right) {
    for (int col = left; col <= right; ++col) {
      result[top][col] = num++;
    }
    ++top;

    for (int row = top; row <= bottom; ++row) {
      result[row][right] = num++;
    }
    --right;

    if (top <= bottom) {
      for (int col = right; col >= left; --col) {
        result[bottom][col] = num++;
      }
      --bottom;
    }

    if (left <= right) {
      for (int row = bottom; row >= top; --row) {
        result[row][left] = num++;
      }
      ++left;
    }
  }

  return result;
}

/// @brief LC 498: Diagonal traverse.
/// @param matrix 2D grid.
/// @return Elements in diagonal order (alternating up/down).
/// @details Example: [[1,2,3],[4,5,6],[7,8,9]]
///          → [1,2,4,7,5,3,6,8,9].
/// @constraints Time: O(m*n), Space: O(1).
/// @note Tricky: direction flag; adjust start based on diagonal index.
[[nodiscard]] std::vector<int> DiagonalTraverse(
    const std::vector<std::vector<int>>& matrix) noexcept {
  if (matrix.empty()) return {};

  int m = matrix.size(), n = matrix[0].size();
  std::vector<int> result;
  bool up = true;

  for (int d = 0; d < m + n - 1; ++d) {
    if (up) {
      // Start from bottom-left, go top-right
      int row = std::min(d, m - 1);
      int col = d - row;
      while (row >= 0 && col < n) {
        result.emplace_back(matrix[row][col]);
        --row;
        ++col;
      }
    } else {
      // Start from top-left, go bottom-right
      int col = std::min(d, n - 1);
      int row = d - col;
      while (col >= 0 && row < m) {
        result.emplace_back(matrix[row][col]);
        ++row;
        --col;
      }
    }
    up = !up;
  }

  return result;
}

// ============================================================================
// PATTERN 2 — TRANSFORMATION
// ============================================================================

/// @brief LC 48: Rotate image 90° clockwise.
/// @param matrix n×n matrix (modified in-place).
/// @return void
/// @constraints Time: O(n²), Space: O(1).
/// @note Tricky: transpose then reverse each row.
void RotateImage(std::vector<std::vector<int>>& matrix) noexcept {
  int n = matrix.size();

  // Transpose
  for (int i = 0; i < n; ++i) {
    for (int j = i + 1; j < n; ++j) {
      std::swap(matrix[i][j], matrix[j][i]);
    }
  }

  // Reverse each row
  for (int i = 0; i < n; ++i) {
    std::reverse(matrix[i].begin(), matrix[i].end());
  }
}

/// @brief LC 73: Set matrix zeroes (in-place, O(1) space).
/// @param matrix 2D matrix (modified in-place).
/// @return void
/// @constraints Time: O(m*n), Space: O(1).
/// @note Tricky: use first row/col as markers; track if they need zeros.
void SetMatrixZeroes(std::vector<std::vector<int>>& matrix) noexcept {
  int m = matrix.size(), n = matrix[0].size();
  bool first_row_zero = false, first_col_zero = false;

  // Check if first row/col need zeros
  for (int j = 0; j < n; ++j) {
    if (matrix[0][j] == 0) {
      first_row_zero = true;
      break;
    }
  }
  for (int i = 0; i < m; ++i) {
    if (matrix[i][0] == 0) {
      first_col_zero = true;
      break;
    }
  }

  // Mark in first row/col
  for (int i = 1; i < m; ++i) {
    for (int j = 1; j < n; ++j) {
      if (matrix[i][j] == 0) {
        matrix[i][0] = 0;
        matrix[0][j] = 0;
      }
    }
  }

  // Set zeros
  for (int i = 1; i < m; ++i) {
    for (int j = 1; j < n; ++j) {
      if (matrix[i][0] == 0 || matrix[0][j] == 0) {
        matrix[i][j] = 0;
      }
    }
  }

  // Handle first row/col
  if (first_row_zero) {
    std::fill(matrix[0].begin(), matrix[0].end(), 0);
  }
  if (first_col_zero) {
    for (int i = 0; i < m; ++i) {
      matrix[i][0] = 0;
    }
  }
}

/// @brief LC 867: Transpose matrix.
/// @param matrix m×n matrix.
/// @return Transposed matrix (n×m).
/// @constraints Time: O(m*n), Space: O(m*n).
[[nodiscard]] std::vector<std::vector<int>> Transpose(
    const std::vector<std::vector<int>>& matrix) noexcept {
  if (matrix.empty()) return {};
  int m = matrix.size(), n = matrix[0].size();
  std::vector<std::vector<int>> result(n, std::vector<int>(m));

  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      result[j][i] = matrix[i][j];
    }
  }

  return result;
}

// ============================================================================
// PATTERN 3 — SEARCH
// ============================================================================

/// @brief LC 74: Search matrix (rows and cols sorted).
/// @param matrix m×n sorted matrix.
/// @param target Value to find.
/// @return true if target exists.
/// @constraints Time: O(log(m*n)), Space: O(1).
/// @note Tricky: treat 2D as 1D; mid/n and mid%n give row/col.
[[nodiscard]] bool SearchMatrix(
    const std::vector<std::vector<int>>& matrix, int target) noexcept {
  if (matrix.empty() || matrix[0].empty()) return false;

  int m = matrix.size(), n = matrix[0].size();
  int left = 0, right = m * n - 1;

  while (left <= right) {
    int mid = left + (right - left) / 2;
    int val = matrix[mid / n][mid % n];
    if (val == target) return true;
    if (val < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return false;
}

/// @brief LC 240: Search matrix II (staircase search).
/// @param matrix m×n matrix (rows and cols sorted).
/// @param target Value to find.
/// @return true if target exists.
/// @constraints Time: O(m+n), Space: O(1).
/// @note Tricky: start top-right or bottom-left; eliminate row or col each
///       step.
[[nodiscard]] bool SearchMatrixII(
    const std::vector<std::vector<int>>& matrix, int target) noexcept {
  if (matrix.empty() || matrix[0].empty()) return false;

  int row = 0, col = static_cast<int>(matrix[0].size()) - 1;

  while (row < static_cast<int>(matrix.size()) && col >= 0) {
    if (matrix[row][col] == target) return true;
    if (matrix[row][col] > target) {
      --col;
    } else {
      ++row;
    }
  }

  return false;
}

// ============================================================================
// PATTERN 4 — DFS/BFS ISLANDS
// ============================================================================

/// @brief DFS helper for island counting.
/// @param grid Grid to traverse.
/// @param r Current row.
/// @param c Current column.
/// @param m Grid height.
/// @param n Grid width.
/// @return void
static void DfsIslands(std::vector<std::vector<char>>& grid, int r, int c,
                       int m, int n) noexcept;

/// @brief LC 200: Number of islands.
/// @param grid m×n grid of '0' and '1'.
/// @return Count of connected components of '1'.
/// @constraints Time: O(m*n), Space: O(m*n) recursion stack.
/// @note Tricky: mark visited by modifying grid; DFS with 4 directions.
[[nodiscard]] int NumIslands(std::vector<std::vector<char>> grid) noexcept {
  if (grid.empty()) return 0;

  int m = grid.size(), n = grid[0].size();
  int count = 0;

  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      if (grid[i][j] == '1') {
        ++count;
        DfsIslands(grid, i, j, m, n);
      }
    }
  }

  return count;
}

/// @brief DFS helper for island counting (implementation).
static void DfsIslands(std::vector<std::vector<char>>& grid, int r, int c,
                       int m, int n) noexcept {
  if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] != '1') return;
  grid[r][c] = '0';
  for (const auto& dir : kDirs4) {
    DfsIslands(grid, r + dir[0], c + dir[1], m, n);
  }
}

/// @brief DFS helper for area calculation.
/// @param grid Grid to traverse.
/// @param r Current row.
/// @param c Current column.
/// @param m Grid height.
/// @param n Grid width.
/// @return Area of island containing (r,c).
static int DfsAreaIsland(std::vector<std::vector<int>>& grid, int r, int c,
                         int m, int n) noexcept;

/// @brief LC 695: Max area island.
/// @param grid m×n grid of 0 and 1.
/// @return Largest island area.
/// @constraints Time: O(m*n), Space: O(m*n).
[[nodiscard]] int MaxAreaIsland(std::vector<std::vector<int>> grid) noexcept {
  if (grid.empty()) return 0;

  int m = grid.size(), n = grid[0].size();
  int max_area = 0;

  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      if (grid[i][j] == 1) {
        max_area = std::max(max_area, DfsAreaIsland(grid, i, j, m, n));
      }
    }
  }

  return max_area;
}

/// @brief DFS helper for area calculation (implementation).
static int DfsAreaIsland(std::vector<std::vector<int>>& grid, int r, int c,
                         int m, int n) noexcept {
  if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] != 1) return 0;
  grid[r][c] = 0;
  int area = 1;
  for (const auto& dir : kDirs4) {
    area += DfsAreaIsland(grid, r + dir[0], c + dir[1], m, n);
  }
  return area;
}

/// @brief DFS helper for surrounded regions.
/// @param board Board to traverse.
/// @param r Current row.
/// @param c Current column.
/// @param m Board height.
/// @param n Board width.
/// @return void
static void DfsSurrounded(std::vector<std::vector<char>>& board, int r, int c,
                          int m, int n) noexcept;

/// @brief LC 130: Surrounded regions (mark surrounded 'O' as 'X').
/// @param board m×n board with 'X' and 'O'.
/// @return void (modifies board in-place).
/// @constraints Time: O(m*n), Space: O(m*n).
/// @note Tricky: DFS from boundaries; mark reachable 'O' as safe; rest → 'X'.
void SurroundedRegions(std::vector<std::vector<char>>& board) noexcept {
  if (board.empty()) return;

  int m = board.size(), n = board[0].size();

  // DFS from boundaries
  for (int i = 0; i < m; ++i) {
    if (board[i][0] == 'O') DfsSurrounded(board, i, 0, m, n);
    if (board[i][n - 1] == 'O') DfsSurrounded(board, i, n - 1, m, n);
  }
  for (int j = 0; j < n; ++j) {
    if (board[0][j] == 'O') DfsSurrounded(board, 0, j, m, n);
    if (board[m - 1][j] == 'O') DfsSurrounded(board, m - 1, j, m, n);
  }

  // Restore and mark surrounded
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      if (board[i][j] == 'B') {
        board[i][j] = 'O';
      } else if (board[i][j] == 'O') {
        board[i][j] = 'X';
      }
    }
  }
}

/// @brief DFS helper for surrounded regions (implementation).
static void DfsSurrounded(std::vector<std::vector<char>>& board, int r, int c,
                          int m, int n) noexcept {
  if (r < 0 || r >= m || c < 0 || c >= n || board[r][c] != 'O') return;
  board[r][c] = 'B';  // Mark as safe
  for (const auto& dir : kDirs4) {
    DfsSurrounded(board, r + dir[0], c + dir[1], m, n);
  }
}

/// @brief DFS helper for waterflow.
/// @param heights Height grid.
/// @param visited Visited matrix for this ocean.
/// @param r Current row.
/// @param c Current column.
/// @param m Grid height.
/// @param n Grid width.
/// @param prev_height Previous height.
/// @return void
static void DfsPacAtl(const std::vector<std::vector<int>>& heights,
                      std::vector<std::vector<bool>>& visited, int r, int c,
                      int m, int n, int prev_height) noexcept;

/// @brief LC 417: Pacific Atlantic waterflow.
/// @param heights m×n grid of elevations.
/// @return Cells where water flows to both oceans.
/// @constraints Time: O(m*n), Space: O(m*n).
/// @note Tricky: reverse BFS from both borders; cell valid if reachable from
///       both.
[[nodiscard]] std::vector<std::vector<int>> PacificAtlantic(
    const std::vector<std::vector<int>>& heights) noexcept {
  if (heights.empty()) return {};

  int m = heights.size(), n = heights[0].size();
  std::vector<std::vector<bool>> pacific(m, std::vector<bool>(n, false));
  std::vector<std::vector<bool>> atlantic(m, std::vector<bool>(n, false));

  // BFS from Pacific (top, left)
  for (int i = 0; i < m; ++i) {
    DfsPacAtl(heights, pacific, i, 0, m, n, heights[i][0]);
  }
  for (int j = 0; j < n; ++j) {
    DfsPacAtl(heights, pacific, 0, j, m, n, heights[0][j]);
  }

  // BFS from Atlantic (bottom, right)
  for (int i = 0; i < m; ++i) {
    DfsPacAtl(heights, atlantic, i, n - 1, m, n, heights[i][n - 1]);
  }
  for (int j = 0; j < n; ++j) {
    DfsPacAtl(heights, atlantic, m - 1, j, m, n, heights[m - 1][j]);
  }

  std::vector<std::vector<int>> result;
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      if (pacific[i][j] && atlantic[i][j]) {
        result.push_back({i, j});
      }
    }
  }

  return result;
}

/// @brief DFS helper for waterflow (implementation).
static void DfsPacAtl(const std::vector<std::vector<int>>& heights,
                      std::vector<std::vector<bool>>& visited, int r, int c,
                      int m, int n, int prev_height) noexcept {
  if (r < 0 || r >= m || c < 0 || c >= n || visited[r][c] ||
      heights[r][c] < prev_height) {
    return;
  }
  visited[r][c] = true;
  for (const auto& dir : kDirs4) {
    DfsPacAtl(heights, visited, r + dir[0], c + dir[1], m, n,
              heights[r][c]);
  }
}

// ============================================================================
// PATTERN 5 — SHORTEST PATH BFS
// ============================================================================

/// @brief LC 1091: Shortest path in binary matrix (8-directional).
/// @param grid m×n binary grid (0=walkable, 1=obstacle).
/// @return Shortest path length from [0,0] to [m-1,n-1], -1 if none.
/// @constraints Time: O(m*n), Space: O(m*n).
[[nodiscard]] int ShortestPathBinaryMatrix(
    std::vector<std::vector<int>> grid) noexcept {
  if (grid.empty() || grid[0][0] == 1) return -1;

  int m = grid.size(), n = grid[0].size();
  if (m == 1 && n == 1) return 1;

  std::queue<std::pair<int, int>> q;
  q.emplace(0, 0);
  grid[0][0] = 1;
  int dist = 1;

  while (!q.empty()) {
    int size = q.size();
    for (int i = 0; i < size; ++i) {
      auto [r, c] = q.front();
      q.pop();

      for (const auto& dir : kDirs8) {
        int nr = r + dir[0], nc = c + dir[1];
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 0) {
          if (nr == m - 1 && nc == n - 1) return dist + 1;
          grid[nr][nc] = 1;
          q.emplace(nr, nc);
        }
      }
    }
    ++dist;
  }

  return -1;
}

/// @brief LC 994: Rotting oranges (multi-source BFS).
/// @param grid m×n grid (0=empty, 1=fresh, 2=rotten).
/// @return Minutes until all fresh oranges rot, -1 if impossible.
/// @constraints Time: O(m*n), Space: O(m*n).
[[nodiscard]] int RottingOranges(std::vector<std::vector<int>> grid) noexcept {
  int m = grid.size(), n = grid[0].size();
  std::queue<std::pair<int, int>> q;
  int fresh = 0;

  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      if (grid[i][j] == 2) {
        q.emplace(i, j);
      } else if (grid[i][j] == 1) {
        ++fresh;
      }
    }
  }

  if (fresh == 0) return 0;

  int minutes = 0;
  while (!q.empty() && fresh > 0) {
    int size = q.size();
    for (int i = 0; i < size; ++i) {
      auto [r, c] = q.front();
      q.pop();

      for (const auto& dir : kDirs4) {
        int nr = r + dir[0], nc = c + dir[1];
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
          grid[nr][nc] = 2;
          q.emplace(nr, nc);
          --fresh;
        }
      }
    }
    ++minutes;
  }

  return fresh == 0 ? minutes : -1;
}

/// @brief LC 286: Walls and gates (multi-source BFS).
/// @param rooms m×n grid (0=gate, INT_MAX=empty, -1=wall).
/// @return void (modifies rooms to distance from nearest gate).
/// @constraints Time: O(m*n), Space: O(m*n).
void WallsAndGates(std::vector<std::vector<int>>& rooms) noexcept {
  if (rooms.empty()) return;

  int m = rooms.size(), n = rooms[0].size();
  std::queue<std::pair<int, int>> q;

  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      if (rooms[i][j] == 0) {
        q.emplace(i, j);
      }
    }
  }

  while (!q.empty()) {
    auto [r, c] = q.front();
    q.pop();

    for (const auto& dir : kDirs4) {
      int nr = r + dir[0], nc = c + dir[1];
      if (nr >= 0 && nr < m && nc >= 0 && nc < n &&
          rooms[nr][nc] == INT_MAX) {
        rooms[nr][nc] = rooms[r][c] + 1;
        q.emplace(nr, nc);
      }
    }
  }
}

// ============================================================================
// PATTERN 6 — MATRIX DP
// ============================================================================

/// @brief LC 62: Unique paths (right/down only).
/// @param m Grid height.
/// @param n Grid width.
/// @return Number of distinct paths from [0,0] to [m-1,n-1].
/// @constraints Time: O(m*n), Space: O(n).
/// @note Tricky: 1D DP suffices; dp[j] += dp[j-1].
[[nodiscard]] int UniquePaths(int m, int n) noexcept {
  std::vector<int> dp(n, 1);
  for (int i = 1; i < m; ++i) {
    for (int j = 1; j < n; ++j) {
      dp[j] += dp[j - 1];
    }
  }
  return dp[n - 1];
}

/// @brief LC 64: Minimum path sum.
/// @param grid m×n grid of non-negative integers.
/// @return Minimum sum from [0,0] to [m-1,n-1].
/// @constraints Time: O(m*n), Space: O(n).
[[nodiscard]] int MinPathSum(
    const std::vector<std::vector<int>>& grid) noexcept {
  if (grid.empty()) return 0;
  int m = grid.size(), n = grid[0].size();
  std::vector<int> dp(n);
  dp[0] = grid[0][0];

  for (int j = 1; j < n; ++j) dp[j] = dp[j - 1] + grid[0][j];

  for (int i = 1; i < m; ++i) {
    dp[0] += grid[i][0];
    for (int j = 1; j < n; ++j) {
      dp[j] = grid[i][j] + std::min(dp[j], dp[j - 1]);
    }
  }

  return dp[n - 1];
}

/// @brief LC 221: Maximal square.
/// @param matrix m×n matrix of '0' and '1'.
/// @return Area of largest square of all '1's.
/// @constraints Time: O(m*n), Space: O(n).
/// @note Tricky: dp[j] = min(top, left, diag) + 1 if matrix[i][j]=='1'.
[[nodiscard]] int MaximalSquare(
    const std::vector<std::vector<char>>& matrix) noexcept {
  if (matrix.empty()) return 0;

  int m = matrix.size(), n = matrix[0].size();
  std::vector<int> dp(n, 0);
  int max_side = 0;

  for (int i = 0; i < m; ++i) {
    std::vector<int> new_dp(n, 0);
    for (int j = 0; j < n; ++j) {
      if (matrix[i][j] == '1') {
        if (j == 0) {
          new_dp[j] = 1;
        } else {
          new_dp[j] = std::min({dp[j], dp[j - 1], new_dp[j - 1]}) + 1;
        }
        max_side = std::max(max_side, new_dp[j]);
      }
    }
    dp = std::move(new_dp);
  }

  return max_side * max_side;
}

/// @brief Maximal sum rectangle in matrix (DP + Kadane).
/// @param matrix m×n grid of integers.
/// @return Maximum sum of any rectangle.
/// @constraints Time: O(m²*n), Space: O(n).
/// @note Tricky: fix left/right cols; Kadane on col sums.
[[nodiscard]] int MaxSumRectangle(
    const std::vector<std::vector<int>>& matrix) noexcept {
  if (matrix.empty()) return 0;

  int m = matrix.size(), n = matrix[0].size();
  int max_sum = INT_MIN;

  for (int left = 0; left < n; ++left) {
    std::vector<int> col_sum(m, 0);
    for (int right = left; right < n; ++right) {
      // Add right column to col_sum
      for (int i = 0; i < m; ++i) {
        col_sum[i] += matrix[i][right];
      }
      // Kadane on col_sum
      int current = 0;
      for (int i = 0; i < m; ++i) {
        current = std::max(col_sum[i], current + col_sum[i]);
        max_sum = std::max(max_sum, current);
      }
    }
  }

  return max_sum;
}

// ============================================================================
// PATTERN 7 — SIMULATION (Game of Life)
// ============================================================================

/// @brief LC 289: Game of Life.
/// @param board m×n board of 0 and 1 (dead/alive).
/// @return void (modifies board with next generation).
/// @constraints Time: O(m*n), Space: O(1).
/// @note Tricky: -1=live→dead, 2=dead→live; abs==1 means
///       currently/was alive.
void GameOfLife(std::vector<std::vector<int>>& board) noexcept {
  if (board.empty()) return;

  int m = board.size(), n = board[0].size();

  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      int live_neighbors = 0;

      for (const auto& dir : kDirs8) {
        int ni = i + dir[0], nj = j + dir[1];
        if (ni >= 0 && ni < m && nj >= 0 && nj < n &&
            (board[ni][nj] == 1 || board[ni][nj] == -1)) {
          ++live_neighbors;
        }
      }

      if (board[i][j] == 1 && (live_neighbors < 2 || live_neighbors > 3)) {
        board[i][j] = -1;  // live → dead
      } else if (board[i][j] == 0 && live_neighbors == 3) {
        board[i][j] = 2;  // dead → live
      }
    }
  }

  // Restore encoding
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      if (board[i][j] == -1) {
        board[i][j] = 0;
      } else if (board[i][j] == 2) {
        board[i][j] = 1;
      }
    }
  }
}

}  // namespace matrix_playground

int main() {
  using namespace matrix_playground;
  std::cout << "=== Matrix Playground ===\n\n";

  std::cout << "--- Pattern 1: Traversal ---\n\n";

  std::cout << "Spiral Order (LC 54)\n";
  {
    auto result = SpiralOrder({{1, 2, 3}, {4, 5, 6}, {7, 8, 9}});
    std::cout << "Input: [[1,2,3],[4,5,6],[7,8,9]]\nOutput: [";
    for (int i = 0; i < static_cast<int>(result.size()); ++i) {
      if (i > 0) std::cout << ", ";
      std::cout << result[i];
    }
    std::cout << "]\n";
  }

  std::cout << "\nGenerate Spiral (LC 59)\n";
  {
    auto result = GenerateSpiralMatrix(3);
    std::cout << "n=3:\n";
    for (const auto& row : result) {
      for (int x : row) std::cout << x << " ";
      std::cout << "\n";
    }
  }

  std::cout << "\nDiagonal Traverse (LC 498)\n";
  {
    auto result = DiagonalTraverse({{1, 2, 3}, {4, 5, 6}, {7, 8, 9}});
    std::cout << "Output: [";
    for (int i = 0; i < static_cast<int>(result.size()); ++i) {
      if (i > 0) std::cout << ", ";
      std::cout << result[i];
    }
    std::cout << "]\n";
  }

  std::cout << "\n--- Pattern 2: Transformation ---\n\n";

  std::cout << "Rotate Image (LC 48)\n";
  {
    std::vector<std::vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    RotateImage(matrix);
    std::cout << "After 90° clockwise rotation:\n";
    for (const auto& row : matrix) {
      for (int x : row) std::cout << x << " ";
      std::cout << "\n";
    }
  }

  std::cout << "\n--- Pattern 3: Search ---\n\n";

  std::cout << "Search Matrix (LC 74)\n";
  {
    bool result = SearchMatrix({{1, 3, 5, 7}, {10, 11, 16, 20}}, 3);
    std::cout << "Search 3 in [[1,3,5,7],[10,11,16,20]]: "
              << (result ? "true" : "false") << "\n";
  }

  std::cout << "\n--- Pattern 6: Matrix DP ---\n\n";

  std::cout << "Unique Paths (LC 62)\n";
  {
    int result = UniquePaths(3, 2);
    std::cout << "Paths in 3x2 grid: " << result << "\n";
  }

  std::cout << "\nMin Path Sum (LC 64)\n";
  {
    std::vector<std::vector<int>> grid = {{1, 3, 1}, {1, 5, 1}, {4, 2, 1}};
    int result = MinPathSum(grid);
    std::cout << "Min sum [[1,3,1],[1,5,1],[4,2,1]]: " << result << "\n";
  }

  return 0;
}
