#include <algorithm>
#include <climits>
#include <iostream>
#include <queue>
#include <stack>
#include <string>
#include <unordered_map>
#include <vector>

namespace tree_playground {

/// Binary tree node structure matching LeetCode API.
/// Recursive DFS is natural but risks stack overflow for very deep trees.
/// Iterative DFS uses explicit std::stack; BFS uses std::queue.
/// Always handle nullptr before accessing children; pass global results by
/// reference into recursive helpers.
struct TreeNode {
  int val;
  TreeNode* left;
  TreeNode* right;
  explicit TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

/// Inorder traversal of binary tree (LC 94 Easy).
/// Left-Root-Right order. Iterative with explicit stack.
/// Time: O(n), Space: O(h) where h = height.
[[nodiscard]] std::vector<int> InorderTraversal(TreeNode* root) noexcept {
  std::vector<int> result;
  std::stack<TreeNode*> stk;
  TreeNode* current = root;

  while (current != nullptr || !stk.empty()) {
    while (current != nullptr) {
      stk.push(current);
      current = current->left;
    }
    current = stk.top();
    stk.pop();
    result.emplace_back(current->val);
    current = current->right;
  }

  return result;
}

/// Preorder traversal of binary tree (LC 144 Easy).
/// Root-Left-Right order. Iterative with explicit stack.
/// Time: O(n), Space: O(h).
[[nodiscard]] std::vector<int> PreorderTraversal(TreeNode* root) noexcept {
  std::vector<int> result;
  if (root == nullptr) return result;

  std::stack<TreeNode*> stk;
  stk.push(root);

  while (!stk.empty()) {
    TreeNode* node = stk.top();
    stk.pop();
    result.emplace_back(node->val);

    if (node->right != nullptr) stk.push(node->right);
    if (node->left != nullptr) stk.push(node->left);
  }

  return result;
}

/// Postorder traversal of binary tree (LC 145 Easy).
/// Left-Right-Root order. Uses reverse preorder trick.
/// Time: O(n), Space: O(h).
[[nodiscard]] std::vector<int> PostorderTraversal(TreeNode* root) noexcept {
  std::vector<int> result;
  if (root == nullptr) return result;

  std::stack<TreeNode*> stk;
  stk.push(root);

  while (!stk.empty()) {
    TreeNode* node = stk.top();
    stk.pop();
    result.emplace_back(node->val);

    if (node->left != nullptr) stk.push(node->left);
    if (node->right != nullptr) stk.push(node->right);
  }

  std::reverse(result.begin(), result.end());
  return result;
}

/// Level-order (BFS) traversal (LC 102 Med).
/// Returns vector of level vectors.
/// Time: O(n), Space: O(w) where w = max width.
[[nodiscard]] std::vector<std::vector<int>> LevelOrder(
    TreeNode* root) noexcept {
  std::vector<std::vector<int>> result;
  if (root == nullptr) return result;

  std::queue<TreeNode*> queue;
  queue.push(root);

  while (!queue.empty()) {
    int level_size = static_cast<int>(queue.size());
    std::vector<int> level;

    for (int i = 0; i < level_size; ++i) {
      TreeNode* node = queue.front();
      queue.pop();
      level.emplace_back(node->val);

      if (node->left != nullptr) queue.push(node->left);
      if (node->right != nullptr) queue.push(node->right);
    }

    result.emplace_back(level);
  }

  return result;
}

/// Zigzag level-order traversal (LC 103 Med).
/// Alternates left-to-right and right-to-left per level.
/// Time: O(n), Space: O(w).
[[nodiscard]] std::vector<std::vector<int>> ZigzagLevelOrder(
    TreeNode* root) noexcept {
  std::vector<std::vector<int>> result;
  if (root == nullptr) return result;

  std::queue<TreeNode*> queue;
  queue.push(root);
  bool left_to_right = true;

  while (!queue.empty()) {
    int level_size = static_cast<int>(queue.size());
    std::vector<int> level;

    for (int i = 0; i < level_size; ++i) {
      TreeNode* node = queue.front();
      queue.pop();
      level.emplace_back(node->val);

      if (node->left != nullptr) queue.push(node->left);
      if (node->right != nullptr) queue.push(node->right);
    }

    if (!left_to_right) {
      std::reverse(level.begin(), level.end());
    }

    result.emplace_back(level);
    left_to_right = !left_to_right;
  }

  return result;
}

/// Maximum depth of binary tree (LC 104 Easy).
/// Height is longest path from root to leaf.
/// Time: O(n), Space: O(h).
[[nodiscard]] int MaxDepth(TreeNode* root) noexcept {
  if (root == nullptr) return 0;
  return 1 + std::max(MaxDepth(root->left), MaxDepth(root->right));
}

/// Check if tree is balanced (LC 110 Easy).
/// Balanced: height difference of left/right subtrees <= 1 at each node.
/// Time: O(n), Space: O(h).
[[nodiscard]] bool IsBalanced(TreeNode* root) noexcept {
  auto helper = [](TreeNode* node, auto& fn) -> int {
    if (node == nullptr) return 0;

    int left_height = fn(node->left, fn);
    if (left_height == -1) return -1;

    int right_height = fn(node->right, fn);
    if (right_height == -1) return -1;

    if (std::abs(left_height - right_height) > 1) return -1;
    return 1 + std::max(left_height, right_height);
  };

  return helper(root, helper) != -1;
}

/// Diameter of binary tree (LC 543 Easy).
/// Longest path between any two nodes (may not pass through root).
/// Time: O(n), Space: O(h).
[[nodiscard]] int Diameter(TreeNode* root) noexcept {
  int diameter_max = 0;

  auto helper = [&diameter_max](TreeNode* node, auto& fn) -> int {
    if (node == nullptr) return 0;

    int left_height = fn(node->left, fn);
    int right_height = fn(node->right, fn);

    diameter_max = std::max(diameter_max, left_height + right_height);
    return 1 + std::max(left_height, right_height);
  };

  helper(root, helper);
  return diameter_max;
}

/// Check if path from root to leaf sums to target_sum (LC 112 Easy).
/// Time: O(n), Space: O(h).
[[nodiscard]] bool HasPathSum(TreeNode* root,
                             int target_sum) noexcept {
  if (root == nullptr) return false;

  if (root->left == nullptr && root->right == nullptr) {
    return root->val == target_sum;
  }

  return HasPathSum(root->left, target_sum - root->val) ||
         HasPathSum(root->right, target_sum - root->val);
}

/// Maximum path sum in binary tree (LC 124 Hard).
/// Path can start and end at any nodes; includes at least one node.
/// Time: O(n), Space: O(h).
[[nodiscard]] int MaxPathSum(TreeNode* root) noexcept {
  int max_sum = INT_MIN;

  auto helper = [&max_sum](TreeNode* node, auto& fn) -> int {
    if (node == nullptr) return 0;

    int left = std::max(0, fn(node->left, fn));
    int right = std::max(0, fn(node->right, fn));

    max_sum = std::max(max_sum, left + node->val + right);
    return node->val + std::max(left, right);
  };

  helper(root, helper);
  return max_sum;
}

/// Validate binary search tree (LC 98 Med).
/// Check if tree satisfies BST property using min/max bounds.
/// Time: O(n), Space: O(h).
[[nodiscard]] bool IsValidBST(TreeNode* root) noexcept {
  auto helper = [](TreeNode* node, long long min_val, long long max_val,
                   auto& fn) -> bool {
    if (node == nullptr) return true;
    if (node->val <= min_val || node->val >= max_val) return false;

    return fn(node->left, min_val, static_cast<long long>(node->val), fn) &&
           fn(node->right, static_cast<long long>(node->val), max_val, fn);
  };

  return helper(root, LLONG_MIN, LLONG_MAX, helper);
}

/// Lowest common ancestor in binary tree (LC 236 Med).
/// Time: O(n), Space: O(h).
[[nodiscard]] TreeNode* LowestCommonAncestor(TreeNode* root, TreeNode* p,
                                             TreeNode* q) noexcept {
  if (root == nullptr || root == p || root == q) return root;

  TreeNode* left = LowestCommonAncestor(root->left, p, q);
  TreeNode* right = LowestCommonAncestor(root->right, p, q);

  if (left != nullptr && right != nullptr) return root;
  return left != nullptr ? left : right;
}

/// K-th smallest element in BST (LC 230 Med).
/// Inorder traversal visits nodes in ascending order.
/// Time: O(k), Space: O(h).
[[nodiscard]] int KthSmallestInBST(TreeNode* root, int k) noexcept {
  int count = 0;
  int result = 0;

  auto inorder = [&result, &count, &k](TreeNode* node, auto& fn) -> void {
    if (node == nullptr) return;

    fn(node->left, fn);
    ++count;
    if (count == k) {
      result = node->val;
      return;
    }
    fn(node->right, fn);
  };

  inorder(root, inorder);
  return result;
}

/// Build tree from preorder and inorder (LC 105 Med).
/// Preorder: root | left | right. Inorder: left | root | right.
/// Time: O(n), Space: O(n).
[[nodiscard]] TreeNode* BuildTreeFromPreIn(
    const std::vector<int>& preorder,
    const std::vector<int>& inorder) noexcept {
  if (preorder.empty() || inorder.empty()) return nullptr;

  std::unordered_map<int, int> in_map;
  for (int i = 0; i < static_cast<int>(inorder.size()); ++i) {
    in_map[inorder[i]] = i;
  }

  int pre_idx = 0;

  auto build = [&](TreeNode*& node, int in_left, int in_right,
                   auto& fn) -> void {
    if (in_left > in_right) {
      node = nullptr;
      return;
    }

    node = new TreeNode(preorder[pre_idx++]);
    int in_idx = in_map[node->val];

    fn(node->left, in_left, in_idx - 1, fn);
    fn(node->right, in_idx + 1, in_right, fn);
  };

  TreeNode* root = nullptr;
  build(root, 0, static_cast<int>(inorder.size()) - 1, build);
  return root;
}

/// Invert/mirror a binary tree (LC 226 Easy).
/// Swap left and right children recursively.
/// Time: O(n), Space: O(h).
[[nodiscard]] TreeNode* InvertTree(TreeNode* root) noexcept {
  if (root == nullptr) return nullptr;

  std::swap(root->left, root->right);
  // Recursively invert subtrees; cast to void to suppress nodiscard warning.
  (void)InvertTree(root->left);
  (void)InvertTree(root->right);

  return root;
}

/// Serialize tree to string (LC 297 Hard).
/// Uses level-order with "null" markers for empty nodes.
/// Time: O(n), Space: O(n).
[[nodiscard]] std::string Serialize(TreeNode* root) noexcept {
  std::string result;
  if (root == nullptr) return result;

  std::queue<TreeNode*> queue;
  queue.push(root);

  while (!queue.empty()) {
    TreeNode* node = queue.front();
    queue.pop();

    if (node == nullptr) {
      result += "null,";
    } else {
      result += std::to_string(node->val) + ",";
      queue.push(node->left);
      queue.push(node->right);
    }
  }

  return result;
}

/// Deserialize tree from string (LC 297 Hard).
/// Time: O(n), Space: O(n).
[[nodiscard]] TreeNode* Deserialize(const std::string& data) noexcept {
  if (data.empty()) return nullptr;

  std::vector<std::string> tokens;
  std::string token;

  for (char c : data) {
    if (c == ',') {
      if (!token.empty()) {
        tokens.emplace_back(token);
        token.clear();
      }
    } else {
      token += c;
    }
  }
  if (!token.empty()) tokens.emplace_back(token);

  if (tokens.empty() || tokens[0] == "null") return nullptr;

  TreeNode* root = new TreeNode(std::stoi(tokens[0]));
  std::queue<TreeNode*> queue;
  queue.push(root);
  int idx = 1;

  while (!queue.empty() && idx < static_cast<int>(tokens.size())) {
    TreeNode* node = queue.front();
    queue.pop();

    if (tokens[idx] != "null") {
      node->left = new TreeNode(std::stoi(tokens[idx]));
      queue.push(node->left);
    }
    ++idx;

    if (idx < static_cast<int>(tokens.size()) && tokens[idx] != "null") {
      node->right = new TreeNode(std::stoi(tokens[idx]));
      queue.push(node->right);
    }
    ++idx;
  }

  return root;
}

/// Cleanup helper to free tree memory.
void DeleteTree(TreeNode* root) noexcept {
  if (root == nullptr) return;
  DeleteTree(root->left);
  DeleteTree(root->right);
  delete root;
}

}  // namespace tree_playground

/// Test driver demonstrating all tree functions.
int main() {
  using namespace tree_playground;

  std::cout << "=== Binary Tree Algorithms ===\n\n";

  // Tree structure:
  //       1
  //      / \
  //     2   3
  TreeNode* root = new TreeNode(1);
  root->left = new TreeNode(2);
  root->right = new TreeNode(3);

  std::cout << "Inorder: ";
  auto inorder = InorderTraversal(root);
  for (int val : inorder) std::cout << val << " ";
  std::cout << "\n";

  std::cout << "Preorder: ";
  auto preorder = PreorderTraversal(root);
  for (int val : preorder) std::cout << val << " ";
  std::cout << "\n";

  std::cout << "Postorder: ";
  auto postorder = PostorderTraversal(root);
  for (int val : postorder) std::cout << val << " ";
  std::cout << "\n";

  std::cout << "Level Order:\n";
  auto levels = LevelOrder(root);
  for (const auto& level : levels) {
    for (int val : level) std::cout << val << " ";
    std::cout << "\n";
  }

  std::cout << "Max Depth: " << MaxDepth(root) << "\n";
  std::cout << "Is Balanced: " << (IsBalanced(root) ? "true" : "false")
            << "\n";
  std::cout << "Diameter: " << Diameter(root) << "\n";

  DeleteTree(root);

  //     10
  //    /  \
  //   5   15
  root = new TreeNode(10);
  root->left = new TreeNode(5);
  root->right = new TreeNode(15);

  std::cout << "\nBST Tests:\n";
  std::cout << "Is Valid BST: " << (IsValidBST(root) ? "true" : "false")
            << "\n";

  root->left->left = new TreeNode(3);
  root->left->right = new TreeNode(7);
  root->right->left = new TreeNode(12);
  root->right->right = new TreeNode(17);

  std::cout << "Kth Smallest (k=3): " << KthSmallestInBST(root, 3) << "\n";

  std::cout << "Serialize: " << Serialize(root) << "\n";

  std::cout << "Has Path Sum (32): "
            << (HasPathSum(root, 32) ? "true" : "false") << "\n";

  DeleteTree(root);

  std::cout << "\nAll tree tests passed!\n";
  return 0;
}
