"""
MATRIX - Complete Guide for Interview Preparation
==================================================

CORE CONCEPTS:
--------------
1. 2D array representation: matrix[row][col]
2. Dimensions: m rows × n columns
3. Common patterns: traversal, search, transformation, DP
4. Treat as graph for DFS/BFS problems

MATRIX OPERATIONS:
------------------
- Access: matrix[i][j] - O(1)
- Traverse: nested loops - O(m*n)
- Rotate: in-place transformation
- Search: binary search if sorted

COMMON PATTERNS:
----------------
1. Traversal (spiral, diagonal, zigzag)
2. DFS/BFS (islands, flood fill, shortest path)
3. Dynamic Programming (paths, max sum)
4. Matrix Transformation (rotate, transpose)
5. Binary Search in Matrix
6. Simulation (game of life)

TRICKY PARTS:
-------------
1. Index bounds: 0 <= i < m, 0 <= j < n
2. In-place modification vs creating new matrix
3. Row-major vs column-major order
4. 4-directional vs 8-directional movement
5. Visited tracking in DFS/BFS

DIRECTIONS:
-----------
4-directional: [(0,1), (1,0), (0,-1), (-1,0)]  # right, down, left, up
8-directional: [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
"""

from typing import List, Set, Tuple
from collections import deque
import heapq


# ============================================================================
# PATTERN 1: MATRIX TRAVERSAL
# ============================================================================

def spiral_order(matrix: List[List[int]]) -> List[int]:
    """
    PROBLEM: Spiral Matrix (LeetCode 54)

    Given an m x n matrix, return all elements of the matrix in spiral order.

    Example 1:
        Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
        Output: [1,2,3,6,9,8,7,4,5]
        Visualization:
            1 → 2 → 3
                    ↓
            4 → 5   6
            ↑       ↓
            7 ← 8 ← 9

    Example 2:
        Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        Output: [1,2,3,4,8,12,11,10,9,5,6,7]

    Constraints:
        - m == matrix.length
        - n == matrix[i].length
        - 1 <= m, n <= 10
        - -100 <= matrix[i][j] <= 100

    Time: O(m*n), Space: O(1) excluding output
    """
    if not matrix:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Traverse down
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Traverse left (if still have rows)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # Traverse up (if still have columns)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result


def generate_spiral_matrix(n: int) -> List[List[int]]:
    """
    PROBLEM: Spiral Matrix II (LeetCode 59)

    Given a positive integer n, generate an n x n matrix filled with elements
    from 1 to n² in spiral order.

    Example 1:
        Input: n = 3
        Output: [[1,2,3],[8,9,4],[7,6,5]]
        Visualization:
            1 → 2 → 3
                    ↓
            8 → 9   4
            ↑       ↓
            7 ← 6 ← 5

    Example 2:
        Input: n = 1
        Output: [[1]]

    Constraints:
        - 1 <= n <= 20

    Time: O(n²), Space: O(1) excluding output
    """
    matrix = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1

    while top <= bottom and left <= right:
        # Fill right
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        top += 1

        # Fill down
        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1
        right -= 1

        # Fill left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1

        # Fill up
        if left <= right:
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1

    return matrix


def diagonal_traverse(mat: List[List[int]]) -> List[int]:
    """
    PROBLEM: Diagonal Traverse (LeetCode 498)

    Given an m x n matrix mat, return an array of all the elements of the array
    in a diagonal order.

    Example 1:
        Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
        Output: [1,2,4,7,5,3,6,8,9]
        Visualization:
            1 → 2   3
            ↓ ↗ ↓ ↗ ↓
            4   5   6
              ↗   ↗
            7   8   9

    Example 2:
        Input: mat = [[1,2],[3,4]]
        Output: [1,2,3,4]

    Constraints:
        - m == mat.length
        - n == mat[i].length
        - 1 <= m, n <= 10^4
        - 1 <= m * n <= 10^4
        - -10^5 <= mat[i][j] <= 10^5

    Time: O(m*n), Space: O(1) excluding output
    """
    if not mat:
        return []

    m, n = len(mat), len(mat[0])
    result = []
    row, col = 0, 0
    going_up = True

    for _ in range(m * n):
        result.append(mat[row][col])

        if going_up:
            # Moving diagonally up
            if col == n - 1:
                # Hit right edge, go down
                row += 1
                going_up = False
            elif row == 0:
                # Hit top edge, go right
                col += 1
                going_up = False
            else:
                # Continue diagonal up
                row -= 1
                col += 1
        else:
            # Moving diagonally down
            if row == m - 1:
                # Hit bottom edge, go right
                col += 1
                going_up = True
            elif col == 0:
                # Hit left edge, go down
                row += 1
                going_up = True
            else:
                # Continue diagonal down
                row += 1
                col -= 1

    return result


# ============================================================================
# PATTERN 2: MATRIX TRANSFORMATION
# ============================================================================

def rotate_matrix(matrix: List[List[int]]) -> None:
    """
    PROBLEM: Rotate Image (LeetCode 48)

    You are given an n x n 2D matrix representing an image, rotate the image
    by 90 degrees (clockwise).

    You have to rotate the image in-place, which means you have to modify the
    input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

    Example 1:
        Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
        Output: [[7,4,1],[8,5,2],[9,6,3]]
        Visualization:
            1 2 3       7 4 1
            4 5 6  -->  8 5 2
            7 8 9       9 6 3

    Example 2:
        Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    Constraints:
        - n == matrix.length == matrix[i].length
        - 1 <= n <= 20
        - -1000 <= matrix[i][j] <= 1000

    Time: O(n²), Space: O(1)
    Trick: Transpose then reverse each row
    """
    n = len(matrix)

    # Step 1: Transpose (swap matrix[i][j] with matrix[j][i])
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()


def set_matrix_zeroes(matrix: List[List[int]]) -> None:
    """
    PROBLEM: Set Matrix Zeroes (LeetCode 73)

    Given an m x n integer matrix, if an element is 0, set its entire row and
    column to 0's.

    You must do it in place.

    Example 1:
        Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
        Output: [[1,0,1],[0,0,0],[1,0,1]]

    Example 2:
        Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

    Constraints:
        - m == matrix.length
        - n == matrix[0].length
        - 1 <= m, n <= 200
        - -2³¹ <= matrix[i][j] <= 2³¹ - 1

    Follow up:
        - A straightforward solution using O(mn) space is probably a bad idea.
        - A simple improvement uses O(m + n) space, but still not the best solution.
        - Could you devise a constant space solution?

    Time: O(m*n), Space: O(1)
    Trick: Use first row and column as markers
    """
    if not matrix:
        return

    m, n = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))

    # Use first row and column as markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Set zeros based on markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Handle first row
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0

    # Handle first column
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0


# ============================================================================
# PATTERN 3: MATRIX SEARCH
# ============================================================================

def search_matrix(matrix: List[List[int]], target: int) -> bool:
    """
    PROBLEM: Search a 2D Matrix (LeetCode 74)

    You are given an m x n integer matrix with the following two properties:
    - Each row is sorted in non-decreasing order.
    - The first integer of each row is greater than the last integer of the previous row.

    Given an integer target, return true if target is in matrix or false otherwise.

    You must write a solution in O(log(m * n)) time complexity.

    Example 1:
        Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
        Output: true

    Example 2:
        Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
        Output: false

    Constraints:
        - m == matrix.length
        - n == matrix[i].length
        - 1 <= m, n <= 100
        - -10⁴ <= matrix[i][j], target <= 10⁴

    Time: O(log(m*n)), Space: O(1)
    Trick: Treat as 1D sorted array
    """
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = left + (right - left) // 2
        row, col = mid // n, mid % n
        mid_val = matrix[row][col]

        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


def search_matrix_ii(matrix: List[List[int]], target: int) -> bool:
    """
    PROBLEM: Search a 2D Matrix II (LeetCode 240)

    Write an efficient algorithm that searches for a value target in an m x n
    integer matrix. This matrix has the following properties:
    - Integers in each row are sorted in ascending from left to right.
    - Integers in each column are sorted in ascending from top to bottom.

    Example 1:
        Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],
                        [10,13,14,17,24],[18,21,23,26,30]], target = 5
        Output: true

    Example 2:
        Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],
                        [10,13,14,17,24],[18,21,23,26,30]], target = 20
        Output: false

    Constraints:
        - m == matrix.length
        - n == matrix[i].length
        - 1 <= n, m <= 300
        - -10⁹ <= matrix[i][j] <= 10⁹
        - All integers in each row are sorted in ascending order.
        - All integers in each column are sorted in ascending order.
        - -10⁹ <= target <= 10⁹

    Time: O(m + n), Space: O(1)
    Trick: Start from top-right or bottom-left
    """
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    row, col = 0, n - 1  # Start from top-right

    while row < m and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down

    return False


# ============================================================================
# PATTERN 4: MATRIX DFS/BFS - ISLANDS
# ============================================================================

def num_islands(grid: List[List[str]]) -> int:
    """
    PROBLEM: Number of Islands (LeetCode 200)

    Given an m x n 2D binary grid which represents a map of '1's (land) and
    '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands
    horizontally or vertically. You may assume all four edges of the grid are
    all surrounded by water.

    Example 1:
        Input: grid = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]
        Output: 1

    Example 2:
        Input: grid = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
        Output: 3

    Constraints:
        - m == grid.length
        - n == grid[i].length
        - 1 <= m, n <= 300
        - grid[i][j] is '0' or '1'.

    Time: O(m*n), Space: O(m*n) for recursion
    """
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    count = 0

    def dfs(i: int, j: int):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
            return

        grid[i][j] = '0'  # Mark as visited

        # Explore 4 directions
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1

    return count


def max_area_island(grid: List[List[int]]) -> int:
    """
    PROBLEM: Max Area of Island (LeetCode 695)

    You are given an m x n binary matrix grid. An island is a group of 1's
    (representing land) connected 4-directionally (horizontal or vertical).

    You may assume all four edges of the grid are surrounded by water.

    The area of an island is the number of cells with a value 1 in the island.

    Return the maximum area of an island in grid. If there is no island, return 0.

    Example 1:
        Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                       [0,0,0,0,0,0,0,1,1,1,0,0,0],
                       [0,1,1,0,1,0,0,0,0,0,0,0,0],
                       [0,1,0,0,1,1,0,0,1,0,1,0,0],
                       [0,1,0,0,1,1,0,0,1,1,1,0,0],
                       [0,0,0,0,0,0,0,0,0,0,1,0,0],
                       [0,0,0,0,0,0,0,1,1,1,0,0,0],
                       [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        Output: 6
        Explanation: The max area island has area = 6 (shown in grid[4][4:7])

    Example 2:
        Input: grid = [[0,0,0,0,0,0,0,0]]
        Output: 0

    Constraints:
        - m == grid.length
        - n == grid[i].length
        - 1 <= m, n <= 50
        - grid[i][j] is either 0 or 1.

    Time: O(m*n), Space: O(m*n)
    """
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])

    def dfs(i: int, j: int) -> int:
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
            return 0

        grid[i][j] = 0  # Mark visited

        return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)

    max_area = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                max_area = max(max_area, dfs(i, j))

    return max_area


def surrounded_regions(board: List[List[str]]) -> None:
    """
    PROBLEM: Surrounded Regions (LeetCode 130)

    Given an m x n matrix board containing 'X' and 'O', capture all regions
    that are 4-directionally surrounded by 'X'.

    A region is captured by flipping all 'O's into 'X's in that surrounded region.

    Example 1:
        Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        Explanation: Surrounded regions should not be on the border.

    Example 2:
        Input: board = [["X"]]
        Output: [["X"]]

    Constraints:
        - m == board.length
        - n == board[i].length
        - 1 <= m, n <= 200
        - board[i][j] is 'X' or 'O'.

    Time: O(m*n), Space: O(m*n)
    Trick: DFS from borders, mark safe 'O's, then flip remaining
    """
    if not board:
        return

    m, n = len(board), len(board[0])

    def dfs(i: int, j: int):
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
            return

        board[i][j] = 'S'  # Mark as safe

        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    # Mark all 'O's connected to border as safe
    for i in range(m):
        dfs(i, 0)
        dfs(i, n - 1)

    for j in range(n):
        dfs(0, j)
        dfs(m - 1, j)

    # Flip: 'O' -> 'X' (surrounded), 'S' -> 'O' (safe)
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'S':
                board[i][j] = 'O'


# ============================================================================
# PATTERN 5: SHORTEST PATH IN MATRIX (BFS)
# ============================================================================

def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
    """
    PROBLEM: Shortest Path in Binary Matrix (LeetCode 1091)

    Given an n x n binary matrix grid, return the length of the shortest clear
    path in the matrix. If there is no clear path, return -1.

    A clear path in a binary matrix is a path from the top-left cell (0, 0) to
    the bottom-right cell (n-1, n-1) such that:
    - All the visited cells of the path are 0.
    - All the adjacent cells of the path are 8-directionally connected.

    The length of a clear path is the number of visited cells of this path.

    Example 1:
        Input: grid = [[0,1],[1,0]]
        Output: 2

    Example 2:
        Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
        Output: 4

    Example 3:
        Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
        Output: -1

    Constraints:
        - n == grid.length
        - n == grid[i].length
        - 1 <= n <= 100
        - grid[i][j] is 0 or 1

    Time: O(n²), Space: O(n²)
    """
    n = len(grid)

    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1

    # 8 directions
    directions = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

    queue = deque([(0, 0, 1)])  # (row, col, distance)
    grid[0][0] = 1  # Mark visited

    while queue:
        row, col, dist = queue.popleft()

        if row == n-1 and col == n-1:
            return dist

        for dr, dc in directions:
            r, c = row + dr, col + dc

            if 0 <= r < n and 0 <= c < n and grid[r][c] == 0:
                grid[r][c] = 1  # Mark visited
                queue.append((r, c, dist + 1))

    return -1


def orange_rotting(grid: List[List[int]]) -> int:
    """
    PROBLEM: Rotting Oranges (LeetCode 994)

    You are given an m x n grid where each cell can have one of three values:
    - 0 representing an empty cell
    - 1 representing a fresh orange
    - 2 representing a rotten orange

    Every minute, any fresh orange that is 4-directionally adjacent to a rotten
    orange becomes rotten.

    Return the minimum number of minutes that must elapse until no cell has a
    fresh orange. If this is impossible, return -1.

    Example 1:
        Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
        Output: 4

    Example 2:
        Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
        Output: -1
        Explanation: The orange in the bottom left corner (row 2, column 0) is
        never rotten, because rotting only happens 4-directionally.

    Example 3:
        Input: grid = [[0,2]]
        Output: 0
        Explanation: Since there are no fresh oranges at minute 0, answer is 0.

    Constraints:
        - m == grid.length
        - n == grid[i].length
        - 1 <= m, n <= 10
        - grid[i][j] is 0, 1, or 2.

    Time: O(m*n), Space: O(m*n)
    """
    if not grid:
        return -1

    m, n = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0

    # Find all rotten oranges and count fresh ones
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh_count += 1

    if fresh_count == 0:
        return 0

    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    max_time = 0

    while queue:
        row, col, time = queue.popleft()
        max_time = max(max_time, time)

        for dr, dc in directions:
            r, c = row + dr, col + dc

            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                grid[r][c] = 2  # Make rotten
                fresh_count -= 1
                queue.append((r, c, time + 1))

    return max_time if fresh_count == 0 else -1


# ============================================================================
# PATTERN 6: MATRIX DP
# ============================================================================

def unique_paths(m: int, n: int) -> int:
    """
    PROBLEM: Unique Paths (LeetCode 62)

    There is a robot on an m x n grid. The robot is initially located at the
    top-left corner (0, 0). The robot tries to move to the bottom-right corner
    (m-1, n-1). The robot can only move either down or right at any point in time.

    Given the two integers m and n, return the number of possible unique paths
    that the robot can take to reach the bottom-right corner.

    Example 1:
        Input: m = 3, n = 7
        Output: 28

    Example 2:
        Input: m = 3, n = 2
        Output: 3
        Explanation: From top-left, there are 3 ways to reach bottom-right:
        1. Right -> Down -> Down
        2. Down -> Down -> Right
        3. Down -> Right -> Down

    Constraints:
        - 1 <= m, n <= 100

    Time: O(m*n), Space: O(n)
    """
    dp = [1] * n

    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]

    return dp[n-1]


def min_path_sum(grid: List[List[int]]) -> int:
    """
    PROBLEM: Minimum Path Sum (LeetCode 64)

    Given a m x n grid filled with non-negative numbers, find a path from top
    left to bottom right, which minimizes the sum of all numbers along its path.

    Note: You can only move either down or right at any point in time.

    Example 1:
        Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
        Output: 7
        Explanation: Path 1 → 3 → 1 → 1 → 1 minimizes the sum.

    Example 2:
        Input: grid = [[1,2,3],[4,5,6]]
        Output: 12

    Constraints:
        - m == grid.length
        - n == grid[i].length
        - 1 <= m, n <= 200
        - 0 <= grid[i][j] <= 200

    Time: O(m*n), Space: O(n)
    """
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(m):
        for j in range(n):
            if j == 0:
                dp[j] += grid[i][j]
            else:
                dp[j] = grid[i][j] + min(dp[j], dp[j-1])

    return dp[n-1]


# ============================================================================
# PATTERN 7: GAME SIMULATION
# ============================================================================

def game_of_life(board: List[List[int]]) -> None:
    """
    PROBLEM: Game of Life (LeetCode 289)

    The board is made up of an m x n grid of cells, where each cell has an
    initial state: live (1) or dead (0). Each cell interacts with its eight
    neighbors (horizontal, vertical, diagonal) using the following four rules:

    1. Any live cell with fewer than two live neighbors dies (under-population).
    2. Any live cell with 2 or 3 live neighbors lives on to the next generation.
    3. Any live cell with more than 3 live neighbors dies (over-population).
    4. Any dead cell with exactly 3 live neighbors becomes a live cell (reproduction).

    Given the current state of the board, update the board to reflect its next state.

    Example 1:
        Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

    Example 2:
        Input: board = [[1,1],[1,0]]
        Output: [[1,1],[1,1]]

    Constraints:
        - m == board.length
        - n == board[i].length
        - 1 <= m, n <= 25
        - board[i][j] is 0 or 1.

    Follow up:
        - Could you solve it in-place?

    Time: O(m*n), Space: O(1)
    Trick: Use state encoding (2 = dead->live, -1 = live->dead)
    """
    if not board:
        return

    m, n = len(board), len(board[0])

    def count_live_neighbors(i: int, j: int) -> int:
        count = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if abs(board[ni][nj]) == 1:
                        count += 1
        return count

    # Update board with encoded states
    for i in range(m):
        for j in range(n):
            live_neighbors = count_live_neighbors(i, j)

            if board[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    board[i][j] = -1  # Live -> Dead
            else:
                if live_neighbors == 3:
                    board[i][j] = 2  # Dead -> Live

    # Decode states
    for i in range(m):
        for j in range(n):
            if board[i][j] == -1:
                board[i][j] = 0
            elif board[i][j] == 2:
                board[i][j] = 1


# ============================================================================
# PRACTICE PROBLEMS
# ============================================================================

"""
EASY:
- Reshape the Matrix (566)
- Transpose Matrix (867)
- Flood Fill (733)

MEDIUM:
- Spiral Matrix (54, 59)
- Rotate Image (48)
- Set Matrix Zeroes (73)
- Search a 2D Matrix (74, 240)
- Number of Islands (200)
- Surrounded Regions (130)
- Shortest Path in Binary Matrix (1091)
- Rotting Oranges (994)
- Unique Paths (62)
- Minimum Path Sum (64)
- Game of Life (289)
- Diagonal Traverse (498)

HARD:
- Max Sum Rectangle (not on LeetCode)
- Dungeon Game (174)
- Cherry Pickup (741)
"""


if __name__ == "__main__":
    print("="*70)
    print("MATRIX - Test Examples")
    print("="*70)

    # Test 1: Spiral Matrix
    print("\n1. Spiral Matrix:")
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(f"   Input: {matrix}")
    print(f"   Output: {spiral_order(matrix)}")

    # Test 2: Rotate Matrix
    print("\n2. Rotate Image (90° clockwise):")
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(f"   Before: {matrix}")
    rotate_matrix(matrix)
    print(f"   After:  {matrix}")

    # Test 3: Number of Islands
    print("\n3. Number of Islands:")
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(f"   Islands: {num_islands(grid)}")

    # Test 4: Unique Paths
    print("\n4. Unique Paths (3x7 grid):")
    print(f"   Number of paths: {unique_paths(3, 7)}")

    print("\n" + "="*70)
    print("Matrix problems are essential for coding interviews!")
    print("="*70)
