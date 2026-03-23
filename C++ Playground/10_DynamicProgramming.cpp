#include <algorithm>
#include <climits>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

namespace dp_playground {

/// DP — identify state, transition, base case; reduce 2D DP to 1D when
/// previous row suffices; tabulation (bottom-up) preferred over memoisation
/// for interviews (cleaner space analysis); common patterns: linear DP, grid
/// DP, knapsack, interval DP, string DP.

/// Climb stairs (LC 70 Easy).
/// n steps, can climb 1 or 2 steps per move. Fibonacci variant.
/// Time: O(n), Space: O(1).
[[nodiscard]] int ClimbStairs(int n) noexcept {
  if (n <= 2) return n;
  int prev1 = 1;
  int prev2 = 2;
  for (int i = 3; i <= n; ++i) {
    int curr = prev1 + prev2;
    prev1 = prev2;
    prev2 = curr;
  }
  return prev2;
}

/// House robber (LC 198 Med).
/// Rob houses without robbing adjacent ones. Maximize total.
/// Time: O(n), Space: O(1).
[[nodiscard]] int HouseRobber(const std::vector<int>& nums) noexcept {
  if (nums.empty()) return 0;
  if (nums.size() == 1) return nums[0];

  int prev2 = nums[0];
  int prev1 = std::max(nums[0], nums[1]);

  for (int i = 2; i < static_cast<int>(nums.size()); ++i) {
    int curr = std::max(prev1, prev2 + nums[i]);
    prev2 = prev1;
    prev1 = curr;
  }

  return prev1;
}

/// House robber II (LC 213 Med).
/// Houses arranged in circle. Cannot rob first and last together.
/// Time: O(n), Space: O(1).
[[nodiscard]] int HouseRobberII(const std::vector<int>& nums) noexcept {
  if (nums.empty()) return 0;
  if (nums.size() == 1) return nums[0];

  auto rob_linear = [](const std::vector<int>& houses, int start,
                       int end) -> int {
    if (start > end) return 0;

    int prev2 = 0;
    int prev1 = 0;
    for (int i = start; i <= end; ++i) {
      int curr = std::max(prev1, prev2 + houses[i]);
      prev2 = prev1;
      prev1 = curr;
    }
    return prev1;
  };

  return std::max(rob_linear(nums, 0, static_cast<int>(nums.size()) - 2),
                  rob_linear(nums, 1, static_cast<int>(nums.size()) - 1));
}

/// Coin change (LC 322 Med).
/// Minimum coins to make amount. Unbounded knapsack.
/// Time: O(n * amount), Space: O(amount).
[[nodiscard]] int CoinChange(const std::vector<int>& coins,
                            int amount) noexcept {
  std::vector<int> dp(amount + 1, INT_MAX);
  dp[0] = 0;

  for (int i = 1; i <= amount; ++i) {
    for (int coin : coins) {
      if (coin <= i && dp[i - coin] != INT_MAX) {
        dp[i] = std::min(dp[i], dp[i - coin] + 1);
      }
    }
  }

  return dp[amount] == INT_MAX ? -1 : dp[amount];
}

/// Coin change II (LC 518 Med).
/// Count combinations of coins that sum to amount.
/// Time: O(n * amount), Space: O(amount).
[[nodiscard]] int CoinChangeII(int amount,
                              const std::vector<int>& coins) noexcept {
  std::vector<int> dp(amount + 1, 0);
  dp[0] = 1;

  for (int coin : coins) {
    for (int i = coin; i <= amount; ++i) {
      dp[i] += dp[i - coin];
    }
  }

  return dp[amount];
}

/// Partition equal subset sum (LC 416 Med).
/// Check if array can be partitioned into two equal-sum subsets.
/// 0/1 knapsack with target = sum/2.
/// Time: O(n * sum), Space: O(sum).
[[nodiscard]] bool PartitionEqualSubset(const std::vector<int>& nums) noexcept {
  int total = 0;
  for (int num : nums) total += num;

  if (total % 2 != 0) return false;

  int target = total / 2;
  std::vector<bool> dp(target + 1, false);
  dp[0] = true;

  for (int num : nums) {
    for (int i = target; i >= num; --i) {
      dp[i] = dp[i] || dp[i - num];
    }
  }

  return dp[target];
}

/// Longest increasing subsequence (LC 300 Med).
/// O(n log n) using patience sorting with std::lower_bound.
/// Time: O(n log n), Space: O(n).
[[nodiscard]] int LengthOfLIS(const std::vector<int>& nums) noexcept {
  if (nums.empty()) return 0;

  std::vector<int> tails;
  for (int num : nums) {
    auto it = std::lower_bound(tails.begin(), tails.end(), num);
    if (it == tails.end()) {
      tails.emplace_back(num);
    } else {
      *it = num;
    }
  }

  return static_cast<int>(tails.size());
}

/// Longest common subsequence (LC 1143 Med).
/// DP with space optimization to 1D.
/// Time: O(m * n), Space: O(min(m, n)).
[[nodiscard]] int LongestCommonSubsequence(
    std::string_view text1, std::string_view text2) noexcept {
  const int m = static_cast<int>(text1.size());
  const int n = static_cast<int>(text2.size());

  std::vector<int> prev(n + 1, 0);
  std::vector<int> curr(n + 1, 0);

  for (int i = 1; i <= m; ++i) {
    for (int j = 1; j <= n; ++j) {
      if (text1[i - 1] == text2[j - 1]) {
        curr[j] = prev[j - 1] + 1;
      } else {
        curr[j] = std::max(prev[j], curr[j - 1]);
      }
    }
    std::swap(prev, curr);
  }

  return prev[n];
}

/// Edit distance / Levenshtein distance (LC 72 Hard).
/// Minimum edits (insert, delete, replace) to transform word1 to word2.
/// Time: O(m * n), Space: O(min(m, n)).
[[nodiscard]] int EditDistance(std::string_view word1,
                              std::string_view word2) noexcept {
  const int m = static_cast<int>(word1.size());
  const int n = static_cast<int>(word2.size());

  std::vector<int> prev(n + 1);
  std::vector<int> curr(n + 1);

  for (int j = 0; j <= n; ++j) prev[j] = j;

  for (int i = 1; i <= m; ++i) {
    curr[0] = i;
    for (int j = 1; j <= n; ++j) {
      if (word1[i - 1] == word2[j - 1]) {
        curr[j] = prev[j - 1];
      } else {
        curr[j] = 1 + std::min({prev[j], curr[j - 1], prev[j - 1]});
      }
    }
    std::swap(prev, curr);
  }

  return prev[n];
}

/// Word break (LC 139 Med).
/// Check if s can be segmented into dictionary words.
/// Time: O(n^2), Space: O(n).
[[nodiscard]] bool WordBreak(std::string_view s,
                            const std::vector<std::string>& word_dict) noexcept {
  std::unordered_set<std::string> dict(word_dict.begin(), word_dict.end());
  const int n = static_cast<int>(s.size());
  std::vector<bool> dp(n + 1, false);
  dp[0] = true;

  for (int i = 1; i <= n; ++i) {
    for (int j = 0; j < i; ++j) {
      if (dp[j] && dict.count(std::string(s.substr(j, i - j))) > 0) {
        dp[i] = true;
        break;
      }
    }
  }

  return dp[n];
}

/// Decode ways (LC 91 Med).
/// Count ways to decode string (1-26 = 'A'-'Z').
/// Time: O(n), Space: O(1).
[[nodiscard]] int DecodeWays(std::string_view s) noexcept {
  if (s.empty() || s[0] == '0') return 0;

  int prev2 = 1;
  int prev1 = 1;

  for (int i = 1; i < static_cast<int>(s.size()); ++i) {
    int curr = 0;

    if (s[i] != '0') {
      curr = prev1;
    }

    if (s[i - 1] == '1' || (s[i - 1] == '2' && s[i] <= '6')) {
      curr += prev2;
    }

    prev2 = prev1;
    prev1 = curr;
  }

  return prev1;
}

/// Longest palindromic subsequence (LC 516 Med).
/// LPS = LCS(s, reverse(s)).
/// Time: O(n^2), Space: O(n).
[[nodiscard]] int LongestPalindromicSubsequence(
    std::string_view s) noexcept {
  const int n = static_cast<int>(s.size());
  std::vector<int> prev(n + 1, 0);
  std::vector<int> curr(n + 1, 0);

  std::string rev_s(s.rbegin(), s.rend());

  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= n; ++j) {
      if (s[i - 1] == rev_s[j - 1]) {
        curr[j] = prev[j - 1] + 1;
      } else {
        curr[j] = std::max(prev[j], curr[j - 1]);
      }
    }
    std::swap(prev, curr);
  }

  return prev[n];
}

/// Minimum cut palindrome (LC 132 Hard).
/// Minimum cuts to partition string into palindromes.
/// Precompute is_palindrome[i][j], then DP.
/// Time: O(n^2), Space: O(n^2).
[[nodiscard]] int MinCutPalindrome(std::string_view s) noexcept {
  const int n = static_cast<int>(s.size());
  std::vector<std::vector<bool>> is_pal(n, std::vector<bool>(n, false));

  for (int i = 0; i < n; ++i) {
    is_pal[i][i] = true;
  }

  for (int len = 2; len <= n; ++len) {
    for (int i = 0; i <= n - len; ++i) {
      int j = i + len - 1;
      if (s[i] == s[j]) {
        is_pal[i][j] = (len == 2) || is_pal[i + 1][j - 1];
      }
    }
  }

  std::vector<int> dp(n, INT_MAX);
  for (int i = 0; i < n; ++i) {
    if (is_pal[0][i]) {
      dp[i] = 0;
    } else {
      for (int j = 0; j < i; ++j) {
        if (is_pal[j + 1][i]) {
          dp[i] = std::min(dp[i], dp[j] + 1);
        }
      }
    }
  }

  return dp[n - 1];
}

/// Unique paths (LC 62 Med).
/// m x n grid, move down or right. Count paths.
/// Time: O(m * n), Space: O(n).
[[nodiscard]] int UniquePaths(int m, int n) noexcept {
  std::vector<int> dp(n, 1);

  for (int i = 1; i < m; ++i) {
    for (int j = 1; j < n; ++j) {
      dp[j] += dp[j - 1];
    }
  }

  return dp[n - 1];
}

/// Minimum path sum (LC 64 Med).
/// m x n grid with costs. Find minimum sum path.
/// Time: O(m * n), Space: O(n).
[[nodiscard]] int MinPathSum(const std::vector<std::vector<int>>& grid) noexcept {
  if (grid.empty()) return 0;

  const int m = static_cast<int>(grid.size());
  const int n = static_cast<int>(grid[0].size());

  std::vector<int> dp(n, grid[0][0]);

  for (int j = 1; j < n; ++j) {
    dp[j] = dp[j - 1] + grid[0][j];
  }

  for (int i = 1; i < m; ++i) {
    dp[0] += grid[i][0];
    for (int j = 1; j < n; ++j) {
      dp[j] = grid[i][j] + std::min(dp[j], dp[j - 1]);
    }
  }

  return dp[n - 1];
}

/// Maximal square (LC 221 Med).
/// Largest square submatrix of 1's in binary matrix.
/// Time: O(m * n), Space: O(n).
[[nodiscard]] int MaximalSquare(
    const std::vector<std::vector<char>>& matrix) noexcept {
  if (matrix.empty()) return 0;

  const int m = static_cast<int>(matrix.size());
  const int n = static_cast<int>(matrix[0].size());

  std::vector<int> dp(n, 0);
  int max_side = 0;

  for (int i = 0; i < m; ++i) {
    int prev = 0;
    for (int j = 0; j < n; ++j) {
      int temp = dp[j];
      if (matrix[i][j] == '1') {
        dp[j] = 1 + std::min({dp[j], dp[j - 1 >= 0 ? j - 1 : 0], prev});
        if (j > 0) dp[j] = 1 + std::min({dp[j] - 1, dp[j - 1], prev});
        max_side = std::max(max_side, dp[j]);
      } else {
        dp[j] = 0;
      }
      prev = temp;
    }
  }

  return max_side * max_side;
}

/// Max profit I (LC 121 Easy).
/// One transaction allowed. Maximize profit.
/// Time: O(n), Space: O(1).
[[nodiscard]] int MaxProfitI(const std::vector<int>& prices) noexcept {
  if (prices.size() < 2) return 0;

  int min_price = prices[0];
  int max_profit = 0;

  for (int i = 1; i < static_cast<int>(prices.size()); ++i) {
    max_profit = std::max(max_profit, prices[i] - min_price);
    min_price = std::min(min_price, prices[i]);
  }

  return max_profit;
}

/// Max profit II (LC 122 Med).
/// Unlimited transactions. Buy and sell to maximize profit.
/// Time: O(n), Space: O(1).
[[nodiscard]] int MaxProfitII(const std::vector<int>& prices) noexcept {
  int max_profit = 0;

  for (int i = 1; i < static_cast<int>(prices.size()); ++i) {
    if (prices[i] > prices[i - 1]) {
      max_profit += prices[i] - prices[i - 1];
    }
  }

  return max_profit;
}

/// Max profit with cooldown (LC 309 Med).
/// After sell, must cooldown one day before buying again.
/// States: hold, sold, cooldown.
/// Time: O(n), Space: O(1).
[[nodiscard]] int MaxProfitWithCooldown(
    const std::vector<int>& prices) noexcept {
  if (prices.size() < 2) return 0;

  int hold = -prices[0];
  int sold = 0;
  int cooldown = 0;

  for (int i = 1; i < static_cast<int>(prices.size()); ++i) {
    int new_hold = std::max(hold, cooldown - prices[i]);
    int new_sold = std::max(sold, hold + prices[i]);
    int new_cooldown = std::max(cooldown, sold);

    hold = new_hold;
    sold = new_sold;
    cooldown = new_cooldown;
  }

  return std::max(sold, cooldown);
}

}  // namespace dp_playground

/// Test driver demonstrating all DP functions.
int main() {
  using namespace dp_playground;

  std::cout << "=== Dynamic Programming Algorithms ===\n\n";

  std::cout << "Climb Stairs (n=5): " << ClimbStairs(5) << "\n";
  std::cout << "House Robber ([1,2,3,1]): "
            << HouseRobber({1, 2, 3, 1}) << "\n";
  std::cout << "House Robber II ([2,3,2]): "
            << HouseRobberII({2, 3, 2}) << "\n";

  std::cout << "Coin Change ([1,2,5], 5): "
            << CoinChange({1, 2, 5}, 5) << "\n";
  std::cout << "Coin Change II (5, [1,2,5]): "
            << CoinChangeII(5, {1, 2, 5}) << "\n";

  std::cout << "Partition Equal Subset ([1,5,11,5]): "
            << (PartitionEqualSubset({1, 5, 11, 5}) ? "true" : "false")
            << "\n";

  std::cout << "LIS ([10,9,2,5,3,7,101,18]): "
            << LengthOfLIS({10, 9, 2, 5, 3, 7, 101, 18}) << "\n";

  std::cout << "LCS ('abc', 'abc'): "
            << LongestCommonSubsequence("abc", "abc") << "\n";

  std::cout << "Edit Distance ('horse', 'ros'): "
            << EditDistance("horse", "ros") << "\n";

  std::cout << "Word Break ('catsandcatsdog', ['cat','cats','and','sand',"
               "'dog']): "
            << (WordBreak("catsandcatsdog", {"cat", "cats", "and", "sand",
                                             "dog"})
                    ? "true"
                    : "false")
            << "\n";

  std::cout << "Decode Ways ('226'): " << DecodeWays("226") << "\n";

  std::cout << "LPS ('bbbab'): "
            << LongestPalindromicSubsequence("bbbab") << "\n";

  std::cout << "Min Cut Palindrome ('nitin'): "
            << MinCutPalindrome("nitin") << "\n";

  std::cout << "Unique Paths (3, 2): "
            << UniquePaths(3, 2) << "\n";

  std::cout << "Min Path Sum ([[1,3,1],[1,5,1],[4,2,1]]): "
            << MinPathSum({{1, 3, 1}, {1, 5, 1}, {4, 2, 1}}) << "\n";

  std::cout << "Maximal Square ([['1','0','1'],['1','1','1'],['1','1',"
               "'1']]): "
            << MaximalSquare({{'1', '0', '1'}, {'1', '1', '1'},
                             {'1', '1', '1'}})
            << "\n";

  std::cout << "Max Profit I ([7,1,5,3,6,4]): "
            << MaxProfitI({7, 1, 5, 3, 6, 4}) << "\n";

  std::cout << "Max Profit II ([7,1,5,3,6,4]): "
            << MaxProfitII({7, 1, 5, 3, 6, 4}) << "\n";

  std::cout << "Max Profit With Cooldown ([1,2,3,0,2]): "
            << MaxProfitWithCooldown({1, 2, 3, 0, 2}) << "\n";

  std::cout << "\nAll DP tests passed!\n";
  return 0;
}
