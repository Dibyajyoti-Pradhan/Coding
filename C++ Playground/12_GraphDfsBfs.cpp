#include <algorithm>
#include <climits>
#include <functional>
#include <iostream>
#include <numeric>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>

namespace graph_playground {

/// Adjacency list via vector<vector<int>>.
/// BFS for shortest path (unweighted); DFS for connectivity.
/// Topological sort via Kahn's (BFS on in-degrees) or DFS post-order.
/// Dijkstra with priority_queue<pair<int,int>> for weighted graphs.

struct GraphNode {
  int val;
  std::vector<GraphNode*> neighbors;
  explicit GraphNode(int x) : val(x) {}
};

constexpr int kDirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

// ============================================================================
// DFS — ISLANDS
// ============================================================================

/// Number of islands (LC 200 Med).
/// Count connected components of '1' in grid.
/// Time: O(m * n), Space: O(m * n).
[[nodiscard]] int NumIslands(std::vector<std::vector<char>> grid) noexcept {
  if (grid.empty()) return 0;

  const int m = static_cast<int>(grid.size());
  const int n = static_cast<int>(grid[0].size());
  int count = 0;

  auto dfs = [&grid, m, n](int i, int j, auto& fn) -> void {
    if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == '0') return;
    grid[i][j] = '0';
    fn(i + 1, j, fn);
    fn(i - 1, j, fn);
    fn(i, j + 1, fn);
    fn(i, j - 1, fn);
  };

  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      if (grid[i][j] == '1') {
        dfs(i, j, dfs);
        ++count;
      }
    }
  }

  return count;
}

/// Max area island (LC 695 Med).
/// Find area of largest island.
/// Time: O(m * n), Space: O(m * n).
[[nodiscard]] int MaxAreaIsland(std::vector<std::vector<int>> grid) noexcept {
  if (grid.empty()) return 0;

  const int m = static_cast<int>(grid.size());
  const int n = static_cast<int>(grid[0].size());
  int max_area = 0;

  auto dfs = [&grid, m, n, &max_area](int i, int j, auto& fn) -> int {
    if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == 0) return 0;
    grid[i][j] = 0;
    int area = 1;
    area += fn(i + 1, j, fn);
    area += fn(i - 1, j, fn);
    area += fn(i, j + 1, fn);
    area += fn(i, j - 1, fn);
    return area;
  };

  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      if (grid[i][j] == 1) {
        max_area = std::max(max_area, dfs(i, j, dfs));
      }
    }
  }

  return max_area;
}

/// Surrounded regions (LC 130 Med).
/// Mark 'O' regions surrounded by 'X' as 'X'.
/// DFS from border 'O's to mark safe regions.
/// Time: O(m * n), Space: O(m * n).
void SurroundedRegions(std::vector<std::vector<char>>& board) noexcept {
  if (board.empty()) return;

  const int m = static_cast<int>(board.size());
  const int n = static_cast<int>(board[0].size());

  auto dfs = [&board, m, n](int i, int j, auto& fn) -> void {
    if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] != 'O') return;
    board[i][j] = 'T';
    fn(i + 1, j, fn);
    fn(i - 1, j, fn);
    fn(i, j + 1, fn);
    fn(i, j - 1, fn);
  };

  for (int i = 0; i < m; ++i) {
    if (board[i][0] == 'O') dfs(i, 0, dfs);
    if (board[i][n - 1] == 'O') dfs(i, n - 1, dfs);
  }

  for (int j = 0; j < n; ++j) {
    if (board[0][j] == 'O') dfs(0, j, dfs);
    if (board[m - 1][j] == 'O') dfs(m - 1, j, dfs);
  }

  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      if (board[i][j] == 'O') board[i][j] = 'X';
      else if (board[i][j] == 'T') board[i][j] = 'O';
    }
  }
}

// ============================================================================
// BFS — SHORTEST PATH
// ============================================================================

/// Shortest path in binary matrix (LC 1091 Med).
/// 8-directional BFS.
/// Time: O(m * n), Space: O(m * n).
[[nodiscard]] int ShortestPathBinaryMatrix(
    std::vector<std::vector<int>> grid) noexcept {
  if (grid.empty() || grid[0][0] == 1) return -1;

  const int m = static_cast<int>(grid.size());
  const int n = static_cast<int>(grid[0].size());

  std::queue<std::pair<int, int>> q;
  q.push({0, 0});
  grid[0][0] = 1;
  int dist = 1;

  constexpr int dirs[8][2] = {
    {0, 1}, {1, 0}, {0, -1}, {-1, 0}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}
  };

  while (!q.empty()) {
    int size = static_cast<int>(q.size());
    for (int i = 0; i < size; ++i) {
      auto [x, y] = q.front();
      q.pop();

      if (x == m - 1 && y == n - 1) return dist;

      for (const auto& dir : dirs) {
        int nx = x + dir[0];
        int ny = y + dir[1];
        if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 0) {
          grid[nx][ny] = 1;
          q.push({nx, ny});
        }
      }
    }
    ++dist;
  }

  return -1;
}

/// Rotting oranges (LC 994 Med).
/// Multi-source BFS.
/// Time: O(m * n), Space: O(m * n).
[[nodiscard]] int RottingOranges(std::vector<std::vector<int>> grid) noexcept {
  if (grid.empty()) return 0;

  const int m = static_cast<int>(grid.size());
  const int n = static_cast<int>(grid[0].size());

  std::queue<std::pair<int, int>> q;
  int fresh = 0;

  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      if (grid[i][j] == 2) q.push({i, j});
      else if (grid[i][j] == 1) ++fresh;
    }
  }

  if (fresh == 0) return 0;

  int minutes = 0;
  while (!q.empty()) {
    int size = static_cast<int>(q.size());
    for (int i = 0; i < size; ++i) {
      auto [x, y] = q.front();
      q.pop();

      for (const auto& dir : kDirs) {
        int nx = x + dir[0];
        int ny = y + dir[1];
        if (nx >= 0 && nx < m && ny >= 0 && ny < n &&
            grid[nx][ny] == 1) {
          grid[nx][ny] = 2;
          q.push({nx, ny});
          --fresh;
        }
      }
    }
    if (!q.empty()) ++minutes;
  }

  return fresh == 0 ? minutes : -1;
}

/// Word ladder (LC 127 Hard).
/// Shortest transformation sequence.
/// Time: O(n * w^2) where w = word length, Space: O(n).
[[nodiscard]] int WordLadder(std::string begin_word,
                            std::string end_word,
                            std::vector<std::string>& word_list) noexcept {
  std::unordered_set<std::string> dict(word_list.begin(), word_list.end());
  if (dict.find(end_word) == dict.end()) return 0;

  std::queue<std::pair<std::string, int>> q;
  q.push({begin_word, 1});

  while (!q.empty()) {
    auto [word, level] = q.front();
    q.pop();

    if (word == end_word) return level;

    for (int i = 0; i < static_cast<int>(word.size()); ++i) {
      char orig = word[i];
      for (char c = 'a'; c <= 'z'; ++c) {
        word[i] = c;
        if (dict.count(word) > 0) {
          dict.erase(word);
          q.push({word, level + 1});
        }
      }
      word[i] = orig;
    }
  }

  return 0;
}

// ============================================================================
// TOPOLOGICAL SORT
// ============================================================================

/// Can finish courses (LC 207 Med).
/// Kahn's algorithm (BFS topological sort).
/// Time: O(V + E), Space: O(V).
[[nodiscard]] bool CanFinish(int num_courses,
                            const std::vector<std::vector<int>>&
                            prerequisites) noexcept {
  std::vector<int> in_degree(num_courses, 0);
  std::vector<std::vector<int>> adj(num_courses);

  for (const auto& pre : prerequisites) {
    adj[pre[1]].emplace_back(pre[0]);
    ++in_degree[pre[0]];
  }

  std::queue<int> q;
  for (int i = 0; i < num_courses; ++i) {
    if (in_degree[i] == 0) q.push(i);
  }

  int count = 0;
  while (!q.empty()) {
    int u = q.front();
    q.pop();
    ++count;

    for (int v : adj[u]) {
      --in_degree[v];
      if (in_degree[v] == 0) q.push(v);
    }
  }

  return count == num_courses;
}

/// Find course order (LC 210 Med).
/// Topological sort order.
/// Time: O(V + E), Space: O(V).
[[nodiscard]] std::vector<int> FindOrder(
    int num_courses,
    const std::vector<std::vector<int>>& prerequisites) noexcept {
  std::vector<int> result;
  std::vector<int> in_degree(num_courses, 0);
  std::vector<std::vector<int>> adj(num_courses);

  for (const auto& pre : prerequisites) {
    adj[pre[1]].emplace_back(pre[0]);
    ++in_degree[pre[0]];
  }

  std::queue<int> q;
  for (int i = 0; i < num_courses; ++i) {
    if (in_degree[i] == 0) q.push(i);
  }

  while (!q.empty()) {
    int u = q.front();
    q.pop();
    result.emplace_back(u);

    for (int v : adj[u]) {
      --in_degree[v];
      if (in_degree[v] == 0) q.push(v);
    }
  }

  return static_cast<int>(result.size()) == num_courses ? result
                                                          : std::vector<int>();
}

// ============================================================================
// CLONE
// ============================================================================

/// Clone graph (LC 133 Med).
/// BFS + map to clone nodes.
/// Time: O(V + E), Space: O(V).
[[nodiscard]] GraphNode* CloneGraph(GraphNode* node) noexcept {
  if (node == nullptr) return nullptr;

  std::unordered_map<GraphNode*, GraphNode*> cloned;
  std::queue<GraphNode*> q;

  q.push(node);
  cloned[node] = new GraphNode(node->val);

  while (!q.empty()) {
    GraphNode* curr = q.front();
    q.pop();

    for (GraphNode* neighbor : curr->neighbors) {
      if (cloned.find(neighbor) == cloned.end()) {
        cloned[neighbor] = new GraphNode(neighbor->val);
        q.push(neighbor);
      }
      cloned[curr]->neighbors.emplace_back(cloned[neighbor]);
    }
  }

  return cloned[node];
}

// ============================================================================
// UNION-FIND
// ============================================================================

/// Count connected components (Union-Find).
/// Time: O(n * α(n)), Space: O(n).
[[nodiscard]] int CountComponents(int n,
                                 const std::vector<std::vector<int>>&
                                 edges) noexcept {
  std::vector<int> parent(n);
  std::iota(parent.begin(), parent.end(), 0);

  std::function<int(int)> find = [&parent, &find](int x) -> int {
    if (parent[x] != x) parent[x] = find(parent[x]);
    return parent[x];
  };

  int count = n;
  for (const auto& edge : edges) {
    int px = find(edge[0]);
    int py = find(edge[1]);
    if (px != py) {
      parent[px] = py;
      --count;
    }
  }

  return count;
}

/// Find redundant connection (LC 684 Med).
/// Union-Find to detect cycle.
/// Time: O(n * α(n)), Space: O(n).
[[nodiscard]] std::vector<int> FindRedundantConnection(
    const std::vector<std::vector<int>>& edges) noexcept {
  std::vector<int> parent(edges.size() + 1);
  std::iota(parent.begin(), parent.end(), 0);

  std::function<int(int)> find = [&parent, &find](int x) -> int {
    if (parent[x] != x) parent[x] = find(parent[x]);
    return parent[x];
  };

  for (const auto& edge : edges) {
    int px = find(edge[0]);
    int py = find(edge[1]);
    if (px == py) return {edge[0], edge[1]};
    parent[px] = py;
  }

  return {};
}

// ============================================================================
// DIJKSTRA
// ============================================================================

/// Network delay time (LC 743 Med).
/// Dijkstra's shortest path.
/// Time: O((V + E) log V), Space: O(V).
[[nodiscard]] int NetworkDelayTime(
    const std::vector<std::vector<int>>& times, int n,
    int k) noexcept {
  std::vector<std::vector<std::pair<int, int>>> adj(n + 1);

  for (const auto& t : times) {
    adj[t[0]].emplace_back(t[1], t[2]);
  }

  std::vector<int> dist(n + 1, INT_MAX);
  std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>,
                      std::greater<std::pair<int, int>>>
      pq;

  dist[k] = 0;
  pq.push({0, k});

  while (!pq.empty()) {
    auto [d, u] = pq.top();
    pq.pop();

    if (d > dist[u]) continue;

    for (const auto& [v, w] : adj[u]) {
      if (dist[u] + w < dist[v]) {
        dist[v] = dist[u] + w;
        pq.push({dist[v], v});
      }
    }
  }

  int max_dist = 0;
  for (int i = 1; i <= n; ++i) {
    if (dist[i] == INT_MAX) return -1;
    max_dist = std::max(max_dist, dist[i]);
  }

  return max_dist;
}

/// Pacific Atlantic water flow (LC 417 Med).
/// Reverse BFS from both borders.
/// Time: O(m * n), Space: O(m * n).
[[nodiscard]] std::vector<std::vector<int>> PacificAtlantic(
    const std::vector<std::vector<int>>& heights) noexcept {
  if (heights.empty()) return {};

  const int m = static_cast<int>(heights.size());
  const int n = static_cast<int>(heights[0].size());

  std::vector<std::vector<bool>> pacific(m, std::vector<bool>(n, false));
  std::vector<std::vector<bool>> atlantic(m, std::vector<bool>(n, false));

  auto bfs = [&heights, m, n](std::vector<std::vector<bool>>& visited,
                               std::queue<std::pair<int, int>>& q) {
    while (!q.empty()) {
      auto [x, y] = q.front();
      q.pop();

      for (const auto& dir : kDirs) {
        int nx = x + dir[0];
        int ny = y + dir[1];
        if (nx >= 0 && nx < m && ny >= 0 && ny < n &&
            !visited[nx][ny] && heights[nx][ny] >= heights[x][y]) {
          visited[nx][ny] = true;
          q.push({nx, ny});
        }
      }
    }
  };

  std::queue<std::pair<int, int>> pac_q, atl_q;

  for (int i = 0; i < m; ++i) {
    pacific[i][0] = true;
    pac_q.push({i, 0});
    atlantic[i][n - 1] = true;
    atl_q.push({i, n - 1});
  }

  for (int j = 0; j < n; ++j) {
    pacific[0][j] = true;
    pac_q.push({0, j});
    atlantic[m - 1][j] = true;
    atl_q.push({m - 1, j});
  }

  bfs(pacific, pac_q);
  bfs(atlantic, atl_q);

  std::vector<std::vector<int>> result;
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      if (pacific[i][j] && atlantic[i][j]) {
        result.emplace_back(std::vector<int>{i, j});
      }
    }
  }

  return result;
}

}  // namespace graph_playground

/// Test driver demonstrating all graph functions.
int main() {
  using namespace graph_playground;

  std::cout << "=== Graph DFS/BFS Algorithms ===\n\n";

  std::vector<std::vector<char>> grid1 = {
    {'1', '1', '1', '1', '0'},
    {'1', '1', '0', '1', '0'},
    {'1', '1', '0', '0', '0'},
    {'0', '0', '0', '0', '0'}
  };
  std::cout << "Num Islands: " << NumIslands(grid1) << "\n";

  std::vector<std::vector<int>> grid2 = {
    {1, 1, 1},
    {1, 0, 1},
    {1, 1, 1}
  };
  std::cout << "Max Area Island: " << MaxAreaIsland(grid2) << "\n";

  std::cout << "Can Finish (2, [[1,0]]): "
            << (CanFinish(2, {{1, 0}}) ? "true" : "false") << "\n";

  std::cout << "Can Finish (2, [[1,0],[0,1]]): "
            << (CanFinish(2, {{1, 0}, {0, 1}}) ? "true" : "false")
            << "\n";

  std::cout << "Count Components (5, [[0,1],[1,2],[3,4]]): "
            << CountComponents(5, {{0, 1}, {1, 2}, {3, 4}}) << "\n";

  std::cout << "Find Redundant Connection ([[1,2],[1,3],[2,3]]): ";
  auto redund = FindRedundantConnection({{1, 2}, {1, 3}, {2, 3}});
  if (!redund.empty()) std::cout << "[" << redund[0] << "," << redund[1] << "]";
  std::cout << "\n";

  std::cout << "Network Delay Time ([[2,1,1],[2,3,1],[3,4,1]], 4, 2): "
            << NetworkDelayTime({{2, 1, 1}, {2, 3, 1}, {3, 4, 1}}, 4, 2)
            << "\n";

  std::cout << "\nAll graph tests passed!\n";
  return 0;
}
