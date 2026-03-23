#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

namespace essential_playground {

/// Greedy — make locally optimal choice, prove it leads to global optimum.
/// Backtracking — explore all choices, prune early, undo.
/// Bit manipulation — XOR for cancel-pairs, n & (n-1) removes lowest set bit,
/// n & (-n) isolates lowest set bit.

// ============================================================================
// GREEDY
// ============================================================================

/// Jump game (LC 55 Med).
/// Can reach last index by jumping at most nums[i] steps forward.
/// Track max reachable index.
/// Time: O(n), Space: O(1).
[[nodiscard]] bool JumpGame(const std::vector<int>& nums) noexcept {
  int max_reach = 0;
  for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
    if (i > max_reach) return false;
    max_reach = std::max(max_reach, i + nums[i]);
  }
  return true;
}

/// Jump game II (LC 45 Med).
/// Minimum jumps to reach last index.
/// Greedy BFS levels.
/// Time: O(n), Space: O(1).
[[nodiscard]] int JumpGameII(const std::vector<int>& nums) noexcept {
  if (nums.size() <= 1) return 0;

  int jumps = 0;
  int curr_reach = 0;
  int next_reach = 0;

  for (int i = 0; i < static_cast<int>(nums.size()) - 1; ++i) {
    next_reach = std::max(next_reach, i + nums[i]);

    if (i == curr_reach) {
      ++jumps;
      curr_reach = next_reach;
    }
  }

  return jumps;
}

/// Partition labels (LC 763 Med).
/// Partition string such that each letter appears in one partition.
/// Use last occurrence map.
/// Time: O(n), Space: O(1).
[[nodiscard]] std::vector<int> PartitionLabels(
    std::string_view s) noexcept {
  std::vector<int> last_idx(26, -1);

  for (int i = 0; i < static_cast<int>(s.size()); ++i) {
    last_idx[s[i] - 'a'] = i;
  }

  std::vector<int> result;
  int start = 0;
  int end = 0;

  for (int i = 0; i < static_cast<int>(s.size()); ++i) {
    end = std::max(end, last_idx[s[i] - 'a']);
    if (i == end) {
      result.emplace_back(end - start + 1);
      start = i + 1;
    }
  }

  return result;
}

/// Gas station (LC 134 Med).
/// Can complete circuit starting from some station.
/// Time: O(n), Space: O(1).
[[nodiscard]] int GasStation(const std::vector<int>& gas,
                            const std::vector<int>& cost) noexcept {
  int total_gas = 0;
  int total_cost = 0;
  int curr_gas = 0;
  int start = 0;

  for (int i = 0; i < static_cast<int>(gas.size()); ++i) {
    total_gas += gas[i];
    total_cost += cost[i];
    curr_gas += gas[i] - cost[i];

    if (curr_gas < 0) {
      start = i + 1;
      curr_gas = 0;
    }
  }

  return total_gas >= total_cost ? start : -1;
}

// ============================================================================
// BACKTRACKING
// ============================================================================

/// Permutations (LC 46 Med).
/// Generate all permutations of array.
/// Time: O(n!), Space: O(n).
[[nodiscard]] std::vector<std::vector<int>> Permutations(
    std::vector<int> nums) noexcept {
  std::vector<std::vector<int>> result;

  auto backtrack = [&result, &nums](int start, auto& fn) -> void {
    if (start == static_cast<int>(nums.size())) {
      result.emplace_back(nums);
      return;
    }

    for (int i = start; i < static_cast<int>(nums.size()); ++i) {
      std::swap(nums[start], nums[i]);
      fn(start + 1, fn);
      std::swap(nums[start], nums[i]);
    }
  };

  backtrack(0, backtrack);
  return result;
}

/// Subsets (LC 78 Med).
/// Generate all subsets (power set).
/// Time: O(2^n), Space: O(1).
[[nodiscard]] std::vector<std::vector<int>> Subsets(
    const std::vector<int>& nums) noexcept {
  std::vector<std::vector<int>> result;
  std::vector<int> subset;

  auto backtrack = [&result, &subset, &nums](int start, auto& fn) -> void {
    result.emplace_back(subset);

    for (int i = start; i < static_cast<int>(nums.size()); ++i) {
      subset.emplace_back(nums[i]);
      fn(i + 1, fn);
      subset.pop_back();
    }
  };

  backtrack(0, backtrack);
  return result;
}

/// Combination sum (LC 39 Med).
/// Find combinations that sum to target (unbounded).
/// Time: O(N^(T/M)), Space: O(T/M).
[[nodiscard]] std::vector<std::vector<int>> CombinationSum(
    std::vector<int> candidates, int target) noexcept {
  std::vector<std::vector<int>> result;
  std::vector<int> combo;

  auto backtrack = [&result, &combo, &candidates,
                    &target](int start, int remain, auto& fn) -> void {
    if (remain == 0) {
      result.emplace_back(combo);
      return;
    }
    if (remain < 0) return;

    for (int i = start; i < static_cast<int>(candidates.size()); ++i) {
      combo.emplace_back(candidates[i]);
      fn(i, remain - candidates[i], fn);
      combo.pop_back();
    }
  };

  backtrack(0, target, backtrack);
  return result;
}

/// N-Queens (LC 51 Hard).
/// Place n queens on n x n board; no two attack.
/// Time: O(N!), Space: O(N).
[[nodiscard]] std::vector<std::vector<std::string>> NQueens(int n) noexcept {
  std::vector<std::vector<std::string>> result;
  std::vector<std::string> board(n, std::string(n, '.'));

  std::unordered_set<int> cols, diag1, diag2;

  auto backtrack = [&result, &board, &cols, &diag1, &diag2, n](
                       int row, auto& fn) -> void {
    if (row == n) {
      result.emplace_back(board);
      return;
    }

    for (int col = 0; col < n; ++col) {
      int d1 = row - col;
      int d2 = row + col;

      if (cols.count(col) || diag1.count(d1) || diag2.count(d2)) {
        continue;
      }

      board[row][col] = 'Q';
      cols.insert(col);
      diag1.insert(d1);
      diag2.insert(d2);

      fn(row + 1, fn);

      board[row][col] = '.';
      cols.erase(col);
      diag1.erase(d1);
      diag2.erase(d2);
    }
  };

  backtrack(0, backtrack);
  return result;
}

/// Word search (LC 79 Med).
/// Search for word in 2D grid.
/// Time: O(m * n * 4^L) where L = word length, Space: O(L).
[[nodiscard]] bool WordSearch(std::vector<std::vector<char>>& board,
                             std::string_view word) noexcept {
  if (board.empty() || word.empty()) return false;

  const int m = static_cast<int>(board.size());
  const int n = static_cast<int>(board[0].size());

  auto dfs = [&board, &word, m, n](int i, int j, int idx,
                                     auto& fn) -> bool {
    if (idx == static_cast<int>(word.size())) return true;
    if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] == '#' ||
        board[i][j] != word[idx]) {
      return false;
    }

    char orig = board[i][j];
    board[i][j] = '#';

    bool found = fn(i + 1, j, idx + 1, fn) || fn(i - 1, j, idx + 1, fn) ||
                 fn(i, j + 1, idx + 1, fn) || fn(i, j - 1, idx + 1, fn);

    board[i][j] = orig;
    return found;
  };

  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      if (dfs(i, j, 0, dfs)) return true;
    }
  }

  return false;
}

// ============================================================================
// BIT MANIPULATION
// ============================================================================

/// Single number (LC 136 Easy).
/// Find element appearing once; others appear twice.
/// XOR all elements.
/// Time: O(n), Space: O(1).
[[nodiscard]] int SingleNumber(const std::vector<int>& nums) noexcept {
  int result = 0;
  for (int num : nums) result ^= num;
  return result;
}

/// Single number II (LC 137 Med).
/// Find element appearing once; others appear three times.
/// 32-bit count mod 3.
/// Time: O(n), Space: O(1).
[[nodiscard]] int SingleNumberII(const std::vector<int>& nums) noexcept {
  int ones = 0;
  int twos = 0;

  for (int num : nums) {
    twos |= ones & num;
    ones ^= num;
    int threes = ones & twos;
    ones &= ~threes;
    twos &= ~threes;
  }

  return ones;
}

/// Counting bits (LC 338 Easy).
/// For each i from 0 to n, count set bits in i.
/// Use DP: dp[i] = dp[i >> 1] + (i & 1).
/// Time: O(n), Space: O(n).
[[nodiscard]] std::vector<int> CountingBits(int n) noexcept {
  std::vector<int> dp(n + 1, 0);

  for (int i = 1; i <= n; ++i) {
    dp[i] = dp[i >> 1] + (i & 1);
  }

  return dp;
}

/// Reverse bits (LC 190 Easy).
/// Reverse bits of 32-bit unsigned integer.
/// Time: O(1), Space: O(1).
[[nodiscard]] uint32_t ReverseBits(uint32_t n) noexcept {
  uint32_t result = 0;

  for (int i = 0; i < 32; ++i) {
    result = (result << 1) | (n & 1);
    n >>= 1;
  }

  return result;
}

/// Hamming weight (LC 191 Easy).
/// Count set bits in 32-bit integer.
/// Brian Kernighan: n &= n-1 removes lowest set bit.
/// Time: O(1), Space: O(1).
[[nodiscard]] int HammingWeight(uint32_t n) noexcept {
  int count = 0;
  while (n > 0) {
    n &= n - 1;
    ++count;
  }
  return count;
}

// ============================================================================
// MATH
// ============================================================================

/// GCD using Euclidean algorithm.
/// Time: O(log(min(a,b))), Space: O(1).
[[nodiscard]] constexpr int Gcd(int a, int b) noexcept {
  while (b != 0) {
    int temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

/// Check if number is prime.
/// Time: O(sqrt(n)), Space: O(1).
[[nodiscard]] bool IsPrime(int n) noexcept {
  if (n < 2) return false;
  if (n == 2) return true;
  if (n % 2 == 0) return false;

  for (int i = 3; i * i <= n; i += 2) {
    if (n % i == 0) return false;
  }

  return true;
}

/// Sieve of Eratosthenes.
/// Find all primes up to n.
/// Time: O(n log log n), Space: O(n).
[[nodiscard]] std::vector<int> SieveOfEratosthenes(int n) noexcept {
  if (n < 2) return {};

  std::vector<bool> is_prime(n + 1, true);
  is_prime[0] = is_prime[1] = false;

  for (int i = 2; i * i <= n; ++i) {
    if (is_prime[i]) {
      for (int j = i * i; j <= n; j += i) {
        is_prime[j] = false;
      }
    }
  }

  std::vector<int> primes;
  for (int i = 2; i <= n; ++i) {
    if (is_prime[i]) primes.emplace_back(i);
  }

  return primes;
}

/// Fast exponentiation (LC 50 Med).
/// Compute x^n in O(log n).
/// Time: O(log n), Space: O(1).
[[nodiscard]] double PowFast(double x, long long n) noexcept {
  if (n == 0) return 1.0;

  double result = 1.0;
  double base = x;

  if (n < 0) {
    base = 1.0 / base;
    n = -n;
  }

  while (n > 0) {
    if ((n & 1) == 1) result *= base;
    base *= base;
    n >>= 1;
  }

  return result;
}

}  // namespace essential_playground

/// Test driver demonstrating all essential functions.
int main() {
  using namespace essential_playground;

  std::cout << "=== Essential Topics ===\n\n";

  std::cout << "Jump Game ([2,3,1,1,4]): "
            << (JumpGame({2, 3, 1, 1, 4}) ? "true" : "false") << "\n";

  std::cout << "Jump Game II ([2,3,1,1,4]): "
            << JumpGameII({2, 3, 1, 1, 4}) << "\n";

  std::cout << "Partition Labels ('ababcbacadefegdehijhklij'): ";
  auto parts = PartitionLabels("ababcbacadefegdehijhklij");
  for (int p : parts) std::cout << p << " ";
  std::cout << "\n";

  std::cout << "Gas Station ([1,2,3,4,5], [3,4,5,1,2]): "
            << GasStation({1, 2, 3, 4, 5}, {3, 4, 5, 1, 2}) << "\n";

  std::cout << "Single Number ([4,1,2,1,2]): "
            << SingleNumber({4, 1, 2, 1, 2}) << "\n";

  std::cout << "Single Number II ([2,2,3,2]): "
            << SingleNumberII({2, 2, 3, 2}) << "\n";

  std::cout << "Counting Bits (5): ";
  auto bits = CountingBits(5);
  for (int b : bits) std::cout << b << " ";
  std::cout << "\n";

  std::cout << "Reverse Bits (43261596): " << ReverseBits(43261596) << "\n";

  std::cout << "Hamming Weight (11): " << HammingWeight(11) << "\n";

  std::cout << "GCD (48, 18): " << Gcd(48, 18) << "\n";

  std::cout << "Is Prime (17): " << (IsPrime(17) ? "true" : "false") << "\n";

  std::cout << "Primes up to 20: ";
  auto primes = SieveOfEratosthenes(20);
  for (int p : primes) std::cout << p << " ";
  std::cout << "\n";

  std::cout << "Pow (2.0, 10): " << PowFast(2.0, 10) << "\n";
  std::cout << "Pow (2.0, -2): " << PowFast(2.0, -2) << "\n";

  std::cout << "\nAll essential topic tests passed!\n";
  return 0;
}
