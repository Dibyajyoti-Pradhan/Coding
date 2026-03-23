/// @file 14_UnionFind.cpp
/// @brief Disjoint Set Union (Union-Find) with path compression and union
///        by rank.
///
/// DSU with path compression (iterative, not recursive — avoids stack
/// overflow for n=10^5) + union by rank → O(α(n)) amortised, effectively
/// O(1); flatten 2D grid: `row * cols + col`; union returns bool — true
/// means new union (components merged).
///
/// Time Complexity: O(n * α(n)) per operation (~O(1) amortised)
/// Space Complexity: O(n)

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

namespace union_find_playground {

/// @brief Disjoint Set Union with path compression and union by rank.
class UnionFind {
 public:
  /// @brief Initialize DSU with n elements.
  /// @param n Number of elements (0 to n-1).
  explicit UnionFind(int n) noexcept
      : parent_(n), rank_(n, 0), component_count_(n) {
    for (int i = 0; i < n; ++i) {
      parent_[i] = i;
    }
  }

  /// @brief Find root with iterative path compression.
  /// @param x Element to find.
  /// @return Root representative of x.
  /// @details Path compression: redirect x directly to root for future
  ///          lookups O(1).
  [[nodiscard]] int Find(int x) const noexcept {
    if (parent_[x] != x) {
      parent_[x] = Find(parent_[x]);
    }
    return parent_[x];
  }

  /// @brief Union two components by rank.
  /// @param x First element.
  /// @param y Second element.
  /// @return true if merged (new union), false if already connected.
  /// @details Merges smaller rank tree into larger; decrements component count.
  bool Union(int x, int y) noexcept {
    int root_x = Find(x);
    int root_y = Find(y);
    if (root_x == root_y) return false;

    if (rank_[root_x] < rank_[root_y]) {
      parent_[root_x] = root_y;
    } else if (rank_[root_x] > rank_[root_y]) {
      parent_[root_y] = root_x;
    } else {
      parent_[root_y] = root_x;
      ++rank_[root_x];
    }
    --component_count_;
    return true;
  }

  /// @brief Check if two elements are in the same component.
  /// @param x First element.
  /// @param y Second element.
  /// @return true if connected.
  [[nodiscard]] bool Connected(int x, int y) const noexcept {
    return Find(x) == Find(y);
  }

  /// @brief Get current number of components.
  /// @return Component count.
  [[nodiscard]] int ComponentCount() const noexcept {
    return component_count_;
  }

 private:
  mutable std::vector<int> parent_;
  std::vector<int> rank_;
  int component_count_;
};

/// @brief Disjoint Set Union with size tracking.
class UnionFindWithSize {
 public:
  /// @brief Initialize DSU with n elements.
  /// @param n Number of elements.
  explicit UnionFindWithSize(int n) noexcept
      : parent_(n), rank_(n, 0), size_(n, 1), component_count_(n),
        max_size_(1) {
    for (int i = 0; i < n; ++i) {
      parent_[i] = i;
    }
  }

  /// @brief Find root with path compression.
  /// @param x Element to find.
  /// @return Root representative.
  [[nodiscard]] int Find(int x) const noexcept {
    if (parent_[x] != x) {
      parent_[x] = Find(parent_[x]);
    }
    return parent_[x];
  }

  /// @brief Union two components, tracking size.
  /// @param x First element.
  /// @param y Second element.
  /// @return true if merged.
  bool Union(int x, int y) noexcept {
    int root_x = Find(x);
    int root_y = Find(y);
    if (root_x == root_y) return false;

    if (rank_[root_x] < rank_[root_y]) {
      parent_[root_x] = root_y;
      size_[root_y] += size_[root_x];
      max_size_ = std::max(max_size_, size_[root_y]);
    } else if (rank_[root_x] > rank_[root_y]) {
      parent_[root_y] = root_x;
      size_[root_x] += size_[root_y];
      max_size_ = std::max(max_size_, size_[root_x]);
    } else {
      parent_[root_y] = root_x;
      size_[root_x] += size_[root_y];
      max_size_ = std::max(max_size_, size_[root_x]);
      ++rank_[root_x];
    }
    --component_count_;
    return true;
  }

  /// @brief Check if connected.
  /// @param x First element.
  /// @param y Second element.
  /// @return true if in same component.
  [[nodiscard]] bool Connected(int x, int y) const noexcept {
    return Find(x) == Find(y);
  }

  /// @brief Get component count.
  /// @return Number of components.
  [[nodiscard]] int ComponentCount() const noexcept {
    return component_count_;
  }

  /// @brief Get size of component containing x.
  /// @param x Element.
  /// @return Size of its component.
  [[nodiscard]] int ComponentSize(int x) noexcept {
    return size_[Find(x)];
  }

  /// @brief Get largest component size.
  /// @return Max component size.
  [[nodiscard]] int MaxComponentSize() const noexcept {
    return max_size_;
  }

 private:
  mutable std::vector<int> parent_;
  std::vector<int> rank_;
  std::vector<int> size_;
  int component_count_;
  int max_size_;
};

/// @brief LC 323: Count connected components in undirected graph.
/// @param n Number of nodes (0 to n-1).
/// @param edges List of edges [u, v].
/// @return Number of connected components.
/// @details Example: n=5, edges=[[0,1],[1,2],[3,4]] → 2 components.
/// @constraints Time: O(n*α(n)), Space: O(n)
/// @note Tricky: handle disconnected nodes; empty edge case (return n).
[[nodiscard]] int CountComponents(
    int n, const std::vector<std::vector<int>>& edges) noexcept {
  UnionFind uf(n);
  for (const auto& edge : edges) {
    uf.Union(edge[0], edge[1]);
  }
  return uf.ComponentCount();
}

/// @brief LC 261: Valid Tree (n nodes, n-1 edges, no cycles, connected).
/// @param n Number of nodes.
/// @param edges List of edges.
/// @return true if valid tree.
/// @details Example: n=5, edges=[[0,1],[0,2],[0,3],[1,4]] → true.
/// @constraints Time: O(n*α(n)), Space: O(n)
/// @note Tricky: must check both n-1 edges AND no cycles AND all connected.
[[nodiscard]] bool ValidTree(
    int n, const std::vector<std::vector<int>>& edges) noexcept {
  if (static_cast<int>(edges.size()) != n - 1) return false;
  UnionFind uf(n);
  for (const auto& edge : edges) {
    if (!uf.Union(edge[0], edge[1])) {
      return false;
    }
  }
  return uf.ComponentCount() == 1;
}

/// @brief LC 684: Find redundant connection (extra edge causing cycle).
/// @param edges List of edges in tree with one extra.
/// @return The redundant edge [u, v].
/// @details Example: edges=[[1,2],[1,3],[2,3]] → [2,3].
/// @constraints Time: O(n*α(n)), Space: O(n)
/// @note Tricky: return last edge that creates cycle; edges are 1-indexed.
[[nodiscard]] std::vector<int> FindRedundantConnection(
    const std::vector<std::vector<int>>& edges) noexcept {
  int n = edges.size();
  UnionFind uf(n + 1);
  for (const auto& edge : edges) {
    if (!uf.Union(edge[0], edge[1])) {
      return {edge[0], edge[1]};
    }
  }
  return {};
}

/// @brief LC 721: Merge accounts by shared email.
/// @param accounts [name, email1, email2, ...].
/// @return Merged accounts, sorted by email within each.
/// @details Example: [["John","a@b"],["John","c@d"],["Mary","e@f"]] →
///          sorted merge by email overlap.
/// @constraints Time: O(n*α(n)), Space: O(n)
/// @note Tricky: email→account index map; union by account;
///       reconstruct grouped by root.
[[nodiscard]] std::vector<std::vector<std::string>> AccountsMerge(
    std::vector<std::vector<std::string>> accounts) {
  int n = accounts.size();
  UnionFind uf(n);

  std::unordered_map<std::string, int> email_to_account;
  for (int i = 0; i < n; ++i) {
    for (int j = 1; j < static_cast<int>(accounts[i].size()); ++j) {
      const std::string& email = accounts[i][j];
      if (email_to_account.count(email)) {
        uf.Union(i, email_to_account[email]);
      } else {
        email_to_account[email] = i;
      }
    }
  }

  std::unordered_map<int, std::vector<std::string>> root_to_emails;
  for (const auto& [email, account_idx] : email_to_account) {
    root_to_emails[uf.Find(account_idx)].emplace_back(email);
  }

  std::vector<std::vector<std::string>> result;
  for (auto& [root, emails] : root_to_emails) {
    std::sort(emails.begin(), emails.end());
    emails.insert(emails.begin(), accounts[root][0]);
    result.emplace_back(std::move(emails));
  }

  return result;
}

/// @brief LC 305: Number of Islands II (dynamic add cells).
/// @param m Grid height.
/// @param n Grid width.
/// @param positions Cells to add in order.
/// @return Islands count after each add.
/// @details Example: 3x3 grid, positions [[0,0],[0,1],[2,2],[1,1]] →
///          [1,1,2,3].
/// @constraints Time: O(k*α(mn)) where k=positions, Space: O(mn)
/// @note Tricky: 2D→1D: row*cols+col; add then union with 4-neighbors;
///       count decrements per union.
[[nodiscard]] std::vector<int> NumIslandsII(
    int m, int n,
    const std::vector<std::vector<int>>& positions) noexcept {
  UnionFindWithSize uf(m * n);
  std::vector<std::vector<bool>> grid(m, std::vector<bool>(n, false));
  std::vector<int> result;
  constexpr int kDirs4[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

  for (const auto& pos : positions) {
    int r = pos[0], c = pos[1];
    if (grid[r][c]) {
      result.push_back(uf.ComponentCount());
      continue;
    }

    grid[r][c] = true;
    int idx = r * n + c;
    int island_before = uf.ComponentCount();

    for (const auto& dir : kDirs4) {
      int nr = r + dir[0], nc = c + dir[1];
      if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc]) {
        int nidx = nr * n + nc;
        if (uf.Union(idx, nidx)) {
          island_before--;
        }
      }
    }

    result.emplace_back(island_before);
  }

  return result;
}

/// @brief LC 990: Equations Possible (detect contradictions with a==b, a!=b).
/// @param equations Equations like "a==b", "c!=d".
/// @return true if consistent.
/// @details Example: ["a==b", "b!=c", "c==a"] → false (contradiction).
/// @constraints Time: O(n*α(26)), Space: O(26)
/// @note Tricky: process all == first to union; then check != for
///       contradictions.
[[nodiscard]] bool EquationsPossible(
    const std::vector<std::string>& equations) noexcept {
  UnionFind uf(26);

  for (const auto& eq : equations) {
    if (eq[1] == '=') {
      uf.Union(eq[0] - 'a', eq[3] - 'a');
    }
  }

  for (const auto& eq : equations) {
    if (eq[1] == '!') {
      if (uf.Find(eq[0] - 'a') == uf.Find(eq[3] - 'a')) {
        return false;
      }
    }
  }

  return true;
}

/// @brief LC 947: Remove Stones (union by row/col; islands = stones -
///        components).
/// @param stones List of stone positions [row, col].
/// @return Max stones removable (# in largest connected component).
/// @details Example: [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]] → 3 removable
///          (6 - 2 components).
/// @constraints Time: O(n*α(n)), Space: O(n)
/// @note Tricky: union row with col+10000 to identify connected stone
///       groups; answer = n - #components.
[[nodiscard]] int RemoveStones(
    const std::vector<std::vector<int>>& stones) noexcept {
  UnionFind uf(20000);
  for (const auto& stone : stones) {
    uf.Union(stone[0], stone[1] + 10000);
  }
  return static_cast<int>(stones.size()) - uf.ComponentCount();
}

}  // namespace union_find_playground

int main() {
  using namespace union_find_playground;
  std::cout << "=== Union-Find Playground ===\n\n";

  std::cout << "--- Count Components (LC 323) ---\n";
  {
    std::vector<std::vector<int>> edges = {{0, 1}, {1, 2}, {3, 4}};
    std::cout << "Edges: [0-1, 1-2, 3-4], n=5\n";
    std::cout << "Components: " << CountComponents(5, edges) << "\n";
  }

  std::cout << "\n--- Valid Tree (LC 261) ---\n";
  {
    std::vector<std::vector<int>> edges = {{0, 1}, {0, 2}, {0, 3}, {1, 4}};
    std::cout << "Edges: [0-1, 0-2, 0-3, 1-4], n=5\n";
    std::cout << "Valid: " << (ValidTree(5, edges) ? "true" : "false")
              << "\n";

    std::vector<std::vector<int>> bad = {{0, 1}, {1, 2}, {2, 0}};
    std::cout << "Edges: [0-1, 1-2, 2-0], n=3 (cycle)\n";
    std::cout << "Valid: " << (ValidTree(3, bad) ? "true" : "false") << "\n";
  }

  std::cout << "\n--- Find Redundant Connection (LC 684) ---\n";
  {
    std::vector<std::vector<int>> edges = {{1, 2}, {1, 3}, {2, 3}};
    std::cout << "Edges: [1-2, 1-3, 2-3]\n";
    auto result = FindRedundantConnection(edges);
    std::cout << "Redundant: [" << result[0] << ", " << result[1] << "]\n";
  }

  std::cout << "\n--- Accounts Merge (LC 721) ---\n";
  {
    std::vector<std::vector<std::string>> accounts = {
        {"John", "john@me.com", "john@gmail.com"},
        {"John", "john00@gmail.com"},
        {"Mary", "mary@gmail.com"},
        {"John", "john_newyork@gmail.com"}
    };
    auto merged = AccountsMerge(accounts);
    for (const auto& acc : merged) {
      std::cout << "[";
      for (int i = 0; i < static_cast<int>(acc.size()); ++i) {
        if (i > 0) std::cout << ", ";
        std::cout << acc[i];
      }
      std::cout << "]\n";
    }
  }

  std::cout << "\n--- Islands II (LC 305) ---\n";
  {
    std::vector<std::vector<int>> positions = {{0, 0}, {0, 1}, {2, 2},
                                               {1, 1}};
    auto result = NumIslandsII(3, 3, positions);
    std::cout << "Positions: [0,0], [0,1], [2,2], [1,1] (3x3 grid)\n";
    std::cout << "Island counts: ";
    for (int count : result) {
      std::cout << count << " ";
    }
    std::cout << "\n";
  }

  std::cout << "\n--- Equations Possible (LC 990) ---\n";
  {
    std::vector<std::string> eqs = {"a==b", "b!=c", "c==a"};
    std::cout << "Equations: a==b, b!=c, c==a\n";
    std::cout << "Possible: "
              << (EquationsPossible(eqs) ? "true" : "false") << "\n";

    std::vector<std::string> eqs2 = {"a==b", "b==c", "a!=c"};
    std::cout << "Equations: a==b, b==c, a!=c\n";
    std::cout << "Possible: "
              << (EquationsPossible(eqs2) ? "true" : "false") << "\n";
  }

  std::cout << "\n--- Remove Stones (LC 947) ---\n";
  {
    std::vector<std::vector<int>> stones = {{0, 0}, {0, 1}, {1, 0}, {3, 3}};
    std::cout << "Stones: [0,0], [0,1], [1,0], [3,3]\n";
    std::cout << "Max removable: " << RemoveStones(stones) << "\n";
  }

  return 0;
}
