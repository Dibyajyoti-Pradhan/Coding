import java.util.ArrayList;
import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Stack;

/**
 * Binary Tree traversals, properties, and common patterns.
 *
 * Covers: DFS (inorder/preorder/postorder) recursively and iteratively, BFS
 * level-order (including zigzag), tree properties (height, balance, diameter),
 * path sums, BST operations (validation, LCA, kth smallest), and tree
 * construction from preorder+inorder or serialization/deserialization.
 *
 * KEY INSIGHTS:
 * - Recursion is natural for trees but watch stack depth on skewed trees
 * - Iterative traversals use explicit Stack or Deque
 * - DFS: O(n) time, O(h) space (recursion) or O(h) explicit stack
 * - BFS: O(n) time, O(w) space where w = max width
 * - All methods include defensive null checks; null root is valid (empty tree)
 */
public final class TreeBinaryTree {

  private TreeBinaryTree() {
    // Utility class; prevent instantiation
  }

  /**
   * Represents a node in a binary tree. Public access for LeetCode compatibility.
   */
  public static class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;

    /**
     * Constructs a TreeNode with the given value and no children.
     *
     * @param val the node value
     */
    public TreeNode(int val) {
      this.val = val;
    }

    /**
     * Constructs a TreeNode with value, left and right children.
     *
     * @param val the node value
     * @param left the left child (may be null)
     * @param right the right child (may be null)
     */
    public TreeNode(int val, TreeNode left, TreeNode right) {
      this.val = val;
      this.left = left;
      this.right = right;
    }
  }

  // ============================================================================
  // DFS TRAVERSALS (Recursive + Iterative)
  // ============================================================================

  /**
   * Inorder traversal (Left-Root-Right) using recursion.
   *
   * @param root the root of the tree (may be null)
   * @return List of node values in inorder sequence
   *
   * LeetCode 94, Easy. Example: [1,2,3] → [1,null,2,3] inorder = [1,3,2]
   *
   * Time: O(n), Space: O(h) recursion stack.
   */
  public static List<Integer> inorderTraversal(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    inorderHelper(root, result);
    return result;
  }

  private static void inorderHelper(TreeNode node, List<Integer> result) {
    if (node == null) {
      return;
    }
    inorderHelper(node.left, result);
    result.add(node.val);
    inorderHelper(node.right, result);
  }

  /**
   * Inorder traversal using explicit Stack (iterative).
   *
   * @param root the root of the tree (may be null)
   * @return List of node values in inorder sequence
   *
   * Time: O(n), Space: O(h) explicit stack.
   * Tricky: Go left as far as possible, pop & process, move right.
   */
  public static List<Integer> inorderTraversalIterative(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    Stack<TreeNode> stack = new Stack<>();
    TreeNode curr = root;

    while (curr != null || !stack.isEmpty()) {
      while (curr != null) {
        stack.push(curr);
        curr = curr.left;
      }
      curr = stack.pop();
      result.add(curr.val);
      curr = curr.right;
    }

    return result;
  }

  /**
   * Preorder traversal (Root-Left-Right) using recursion.
   *
   * @param root the root of the tree (may be null)
   * @return List of node values in preorder sequence
   *
   * LeetCode 144, Easy. Useful for tree construction and copying.
   * Time: O(n), Space: O(h) recursion stack.
   */
  public static List<Integer> preorderTraversal(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    preorderHelper(root, result);
    return result;
  }

  private static void preorderHelper(TreeNode node, List<Integer> result) {
    if (node == null) {
      return;
    }
    result.add(node.val);
    preorderHelper(node.left, result);
    preorderHelper(node.right, result);
  }

  /**
   * Preorder traversal using explicit Stack (iterative).
   *
   * @param root the root of the tree (may be null)
   * @return List of node values in preorder sequence
   *
   * Time: O(n), Space: O(h) explicit stack.
   */
  public static List<Integer> preorderTraversalIterative(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    if (root == null) {
      return result;
    }

    Stack<TreeNode> stack = new Stack<>();
    stack.push(root);

    while (!stack.isEmpty()) {
      TreeNode node = stack.pop();
      result.add(node.val);
      // Push right before left so left is processed first
      if (node.right != null) {
        stack.push(node.right);
      }
      if (node.left != null) {
        stack.push(node.left);
      }
    }

    return result;
  }

  /**
   * Postorder traversal (Left-Right-Root) using recursion.
   *
   * @param root the root of the tree (may be null)
   * @return List of node values in postorder sequence
   *
   * LeetCode 145, Easy. Useful for tree deletion (delete children first).
   * Time: O(n), Space: O(h) recursion stack.
   */
  public static List<Integer> postorderTraversal(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    postorderHelper(root, result);
    return result;
  }

  private static void postorderHelper(TreeNode node, List<Integer> result) {
    if (node == null) {
      return;
    }
    postorderHelper(node.left, result);
    postorderHelper(node.right, result);
    result.add(node.val);
  }

  /**
   * Postorder traversal using two Stacks (iterative).
   *
   * @param root the root of the tree (may be null)
   * @return List of node values in postorder sequence
   *
   * Time: O(n), Space: O(h).
   * Tricky: Use second stack to reverse; push right then left.
   */
  public static List<Integer> postorderTraversalIterative(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    if (root == null) {
      return result;
    }

    Stack<TreeNode> stack1 = new Stack<>();
    Stack<TreeNode> stack2 = new Stack<>();
    stack1.push(root);

    while (!stack1.isEmpty()) {
      TreeNode node = stack1.pop();
      stack2.push(node);
      if (node.left != null) {
        stack1.push(node.left);
      }
      if (node.right != null) {
        stack1.push(node.right);
      }
    }

    while (!stack2.isEmpty()) {
      result.add(stack2.pop().val);
    }

    return result;
  }

  // ============================================================================
  // BFS LEVEL ORDER
  // ============================================================================

  /**
   * Level-order traversal (BFS) with nodes grouped by level.
   *
   * @param root the root of the tree (may be null)
   * @return List of lists where each inner list is one level
   *
   * LeetCode 102, Medium. Example: [3,9,20,null,null,15,7] →
   * [[3],[9,20],[15,7]]
   *
   * Time: O(n), Space: O(w) where w = max width.
   */
  public static List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> result = new ArrayList<>();
    if (root == null) {
      return result;
    }

    Deque<TreeNode> queue = new LinkedList<>();
    queue.add(root);

    while (!queue.isEmpty()) {
      int levelSize = queue.size();
      List<Integer> level = new ArrayList<>();
      for (int i = 0; i < levelSize; i++) {
        TreeNode node = queue.removeFirst();
        level.add(node.val);
        if (node.left != null) {
          queue.add(node.left);
        }
        if (node.right != null) {
          queue.add(node.right);
        }
      }
      result.add(level);
    }

    return result;
  }

  /**
   * Zigzag level-order traversal (alternating left-to-right, right-to-left).
   *
   * @param root the root of the tree (may be null)
   * @return List of lists with alternating traversal direction per level
   *
   * LeetCode 103, Medium. Example: [3,9,20,null,null,15,7] →
   * [[3],[20,9],[15,7]]
   *
   * Time: O(n), Space: O(w).
   * Tricky: Use Deque; alternate addFirst/addLast and removeFirst/removeLast.
   */
  public static List<List<Integer>> zigzagLevelOrder(TreeNode root) {
    List<List<Integer>> result = new ArrayList<>();
    if (root == null) {
      return result;
    }

    Deque<TreeNode> queue = new LinkedList<>();
    queue.add(root);
    boolean leftToRight = true;

    while (!queue.isEmpty()) {
      int levelSize = queue.size();
      List<Integer> level = new ArrayList<>();

      for (int i = 0; i < levelSize; i++) {
        TreeNode node;
        if (leftToRight) {
          node = queue.removeFirst();
          if (node.left != null) {
            queue.addLast(node.left);
          }
          if (node.right != null) {
            queue.addLast(node.right);
          }
        } else {
          node = queue.removeLast();
          if (node.right != null) {
            queue.addFirst(node.right);
          }
          if (node.left != null) {
            queue.addFirst(node.left);
          }
        }
        level.add(node.val);
      }

      result.add(level);
      leftToRight = !leftToRight;
    }

    return result;
  }

  // ============================================================================
  // TREE PROPERTIES
  // ============================================================================

  /**
   * Maximum depth (height) of a binary tree.
   *
   * @param root the root of the tree (may be null)
   * @return maximum depth; 0 if root is null, 1 if leaf
   *
   * LeetCode 104, Easy. Example: [3,9,20,null,null,15,7] → 3
   *
   * Time: O(n), Space: O(h).
   */
  public static int maxDepth(TreeNode root) {
    if (root == null) {
      return 0;
    }
    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
  }

  /**
   * Check if a binary tree is balanced (height of subtrees differs by ≤1).
   *
   * @param root the root of the tree (may be null)
   * @return true if balanced, false otherwise
   *
   * LeetCode 110, Easy. Example: [3,9,20,null,null,15,7] → true
   *
   * Time: O(n), Space: O(h).
   * Tricky: Use helper that returns -1 if unbalanced, else height.
   */
  public static boolean isBalanced(TreeNode root) {
    return heightIfBalanced(root) != -1;
  }

  private static int heightIfBalanced(TreeNode node) {
    if (node == null) {
      return 0;
    }

    int leftHeight = heightIfBalanced(node.left);
    if (leftHeight == -1) {
      return -1;
    }

    int rightHeight = heightIfBalanced(node.right);
    if (rightHeight == -1) {
      return -1;
    }

    if (Math.abs(leftHeight - rightHeight) > 1) {
      return -1;
    }

    return 1 + Math.max(leftHeight, rightHeight);
  }

  /**
   * Diameter of binary tree (longest path between any two nodes).
   *
   * @param root the root of the tree (may be null)
   * @return the diameter (number of edges)
   *
   * LeetCode 543, Easy. Example: [1,2,3,4,5] → 3 (path 4→2→1→3)
   *
   * Time: O(n), Space: O(h).
   * Tricky: Diameter may not pass through root; track max globally.
   */
  public static int diameterOfBinaryTree(TreeNode root) {
    int[] maxDiameter = {0};
    diameterHelper(root, maxDiameter);
    return maxDiameter[0];
  }

  private static int diameterHelper(TreeNode node, int[] maxDiameter) {
    if (node == null) {
      return 0;
    }

    int leftHeight = diameterHelper(node.left, maxDiameter);
    int rightHeight = diameterHelper(node.right, maxDiameter);

    maxDiameter[0] = Math.max(maxDiameter[0], leftHeight + rightHeight);

    return 1 + Math.max(leftHeight, rightHeight);
  }

  // ============================================================================
  // PATH PROBLEMS
  // ============================================================================

  /**
   * Check if tree has a root-to-leaf path with given sum.
   *
   * @param root the root of the tree (may be null)
   * @param targetSum the target sum
   * @return true if such a path exists, false otherwise
   *
   * LeetCode 112, Easy. Example: [5,4,8,11,...] targetSum=22 → true
   *
   * Time: O(n), Space: O(h).
   */
  public static boolean hasPathSum(TreeNode root, int targetSum) {
    if (root == null) {
      return false;
    }
    if (root.left == null && root.right == null) {
      return root.val == targetSum;
    }
    return hasPathSum(root.left, targetSum - root.val)
        || hasPathSum(root.right, targetSum - root.val);
  }

  /**
   * Maximum path sum in a binary tree (any node to any node).
   *
   * @param root the root of the tree (may not be null)
   * @return maximum path sum
   *
   * LeetCode 124, Hard. Example: [-10,9,20,null,null,15,7] → 42 (15+20+7)
   *
   * Time: O(n), Space: O(h).
   * Tricky: Path can skip root; track global max. Negative paths excluded.
   */
  public static int maxPathSum(TreeNode root) {
    if (root == null) {
      throw new IllegalArgumentException("root cannot be null");
    }
    int[] maxSum = {Integer.MIN_VALUE};
    maxPathSumHelper(root, maxSum);
    return maxSum[0];
  }

  private static int maxPathSumHelper(TreeNode node, int[] maxSum) {
    if (node == null) {
      return 0;
    }

    int leftSum = Math.max(0, maxPathSumHelper(node.left, maxSum));
    int rightSum = Math.max(0, maxPathSumHelper(node.right, maxSum));

    int currentMax = leftSum + node.val + rightSum;
    maxSum[0] = Math.max(maxSum[0], currentMax);

    return node.val + Math.max(leftSum, rightSum);
  }

  // ============================================================================
  // BST OPERATIONS
  // ============================================================================

  /**
   * Validate if a tree is a valid BST.
   *
   * @param root the root of the tree (may be null)
   * @return true if valid BST, false otherwise
   *
   * LeetCode 98, Medium. Valid: left < node < right recursively.
   *
   * Time: O(n), Space: O(h).
   * Tricky: Check against bounds, not just immediate children.
   */
  public static boolean isValidBST(TreeNode root) {
    return isValidBSTHelper(root, Long.MIN_VALUE, Long.MAX_VALUE);
  }

  private static boolean isValidBSTHelper(
      TreeNode node, long minVal, long maxVal) {
    if (node == null) {
      return true;
    }
    if (node.val <= minVal || node.val >= maxVal) {
      return false;
    }
    return isValidBSTHelper(node.left, minVal, node.val)
        && isValidBSTHelper(node.right, node.val, maxVal);
  }

  /**
   * Find the lowest common ancestor (LCA) of two nodes in a BST.
   *
   * @param root the root of the BST (may not be null)
   * @param p first node (may not be null)
   * @param q second node (may not be null)
   * @return the LCA node
   *
   * LeetCode 236, Medium (general tree). Example: root=[6,2,8,0,4,7,9],
   * p=2, q=8 → 6
   *
   * Time: O(n) general tree / O(log n) BST, Space: O(h).
   * Tricky: LCA can be one of the nodes itself.
   */
  public static TreeNode lowestCommonAncestor(
      TreeNode root, TreeNode p, TreeNode q) {
    if (root == null || root == p || root == q) {
      return root;
    }

    TreeNode leftLCA = lowestCommonAncestor(root.left, p, q);
    TreeNode rightLCA = lowestCommonAncestor(root.right, p, q);

    if (leftLCA != null && rightLCA != null) {
      return root;
    }
    return leftLCA != null ? leftLCA : rightLCA;
  }

  /**
   * Find the kth smallest element in a BST.
   *
   * @param root the root of the BST (may not be null)
   * @param k the rank (1-indexed; k=1 is minimum)
   * @return the kth smallest value
   *
   * LeetCode 230, Medium. Example: [3,1,4,null,2], k=1 → 1
   *
   * Time: O(k) average, O(n) worst (skewed tree), Space: O(h).
   * Tricky: Inorder is ascending; stop after k elements.
   */
  public static int kthSmallest(TreeNode root, int k) {
    if (root == null || k <= 0) {
      throw new IllegalArgumentException("root must be non-null, k >= 1");
    }
    int[] count = {0};
    int[] result = {Integer.MIN_VALUE};
    kthSmallestHelper(root, k, count, result);
    return result[0];
  }

  private static void kthSmallestHelper(
      TreeNode node, int k, int[] count, int[] result) {
    if (node == null || count[0] >= k) {
      return;
    }

    kthSmallestHelper(node.left, k, count, result);

    count[0]++;
    if (count[0] == k) {
      result[0] = node.val;
      return;
    }

    kthSmallestHelper(node.right, k, count, result);
  }

  // ============================================================================
  // TREE CONSTRUCTION
  // ============================================================================

  /**
   * Construct a binary tree from preorder and inorder traversals.
   *
   * @param preorder the preorder traversal array (may not be null)
   * @param inorder the inorder traversal array (may not be null)
   * @return the root of the constructed tree
   *
   * LeetCode 105, Medium. Preorder: root first; inorder: root in middle.
   *
   * Time: O(n²) naive / O(n) with HashMap, Space: O(n).
   * Tricky: Use HashMap to map inorder values to indices for O(1) lookup.
   */
  public static TreeNode buildTree(int[] preorder, int[] inorder) {
    if (preorder == null || inorder == null || preorder.length == 0) {
      throw new IllegalArgumentException("arrays must be non-null and non-empty");
    }

    Map<Integer, Integer> inorderMap = new HashMap<>();
    for (int i = 0; i < inorder.length; i++) {
      inorderMap.put(inorder[i], i);
    }

    return buildTreeHelper(
        preorder, 0, preorder.length - 1,
        inorder, 0, inorder.length - 1,
        inorderMap);
  }

  private static TreeNode buildTreeHelper(
      int[] preorder, int preStart, int preEnd,
      int[] inorder, int inStart, int inEnd,
      Map<Integer, Integer> inorderMap) {
    if (preStart > preEnd || inStart > inEnd) {
      return null;
    }

    int rootVal = preorder[preStart];
    int rootInorderIdx = inorderMap.get(rootVal);

    int leftTreeSize = rootInorderIdx - inStart;

    TreeNode root = new TreeNode(rootVal);
    root.left = buildTreeHelper(
        preorder, preStart + 1, preStart + leftTreeSize,
        inorder, inStart, rootInorderIdx - 1,
        inorderMap);
    root.right = buildTreeHelper(
        preorder, preStart + leftTreeSize + 1, preEnd,
        inorder, rootInorderIdx + 1, inEnd,
        inorderMap);

    return root;
  }

  /**
   * Serialize a binary tree to a string.
   *
   * @param root the root of the tree (may be null)
   * @return a serialized string representation
   *
   * LeetCode 297, Hard. Format uses commas and '#' for null nodes.
   * Example: [1,2,3] → "1,2,#,#,3,#,#"
   *
   * Time: O(n), Space: O(n).
   */
  public static String serialize(TreeNode root) {
    StringBuilder sb = new StringBuilder();
    serializeHelper(root, sb);
    return sb.toString();
  }

  private static void serializeHelper(TreeNode node, StringBuilder sb) {
    if (node == null) {
      sb.append("#,");
      return;
    }

    sb.append(node.val).append(",");
    serializeHelper(node.left, sb);
    serializeHelper(node.right, sb);
  }

  /**
   * Deserialize a string back to a binary tree.
   *
   * @param data the serialized string (may not be null)
   * @return the root of the reconstructed tree
   *
   * Time: O(n), Space: O(n).
   */
  public static TreeNode deserialize(String data) {
    if (data == null || data.isEmpty()) {
      throw new IllegalArgumentException("data cannot be null or empty");
    }

    String[] values = data.split(",");
    Deque<String> queue = new LinkedList<>();
    for (String val : values) {
      queue.add(val);
    }

    return deserializeHelper(queue);
  }

  private static TreeNode deserializeHelper(Deque<String> queue) {
    String val = queue.removeFirst();

    if ("#".equals(val)) {
      return null;
    }

    TreeNode node = new TreeNode(Integer.parseInt(val));
    node.left = deserializeHelper(queue);
    node.right = deserializeHelper(queue);

    return node;
  }

  // ============================================================================
  // MAIN: Test cases for all methods
  // ============================================================================

  /**
   * Main method demonstrating all tree operations.
   *
   * @param args not used
   */
  public static void main(String[] args) {
    System.out.println("=== Binary Tree Operations ===\n");

    // Build a sample tree:     1
    //                         / \
    //                        2   3
    //                       / \
    //                      4   5
    TreeNode root = new TreeNode(1);
    root.left = new TreeNode(2);
    root.right = new TreeNode(3);
    root.left.left = new TreeNode(4);
    root.left.right = new TreeNode(5);

    System.out.println("Inorder (Recursive): " + inorderTraversal(root));
    System.out.println("Inorder (Iterative): " + inorderTraversalIterative(root));
    System.out.println("Preorder (Recursive): " + preorderTraversal(root));
    System.out.println("Preorder (Iterative): " + preorderTraversalIterative(root));
    System.out.println("Postorder (Recursive): " + postorderTraversal(root));
    System.out.println("Postorder (Iterative): " + postorderTraversalIterative(root));

    System.out.println("\nLevel Order: " + levelOrder(root));
    System.out.println("Zigzag Level Order: " + zigzagLevelOrder(root));

    System.out.println("\nMax Depth: " + maxDepth(root));
    System.out.println("Is Balanced: " + isBalanced(root));
    System.out.println("Diameter: " + diameterOfBinaryTree(root));

    System.out.println("\nHas Path Sum (8): " + hasPathSum(root, 8));
    System.out.println("Has Path Sum (10): " + hasPathSum(root, 10));

    System.out.println("\nMax Path Sum: " + maxPathSum(root));

    // BST test: [4,2,6,1,3,5,7]
    TreeNode bst = new TreeNode(4);
    bst.left = new TreeNode(2);
    bst.right = new TreeNode(6);
    bst.left.left = new TreeNode(1);
    bst.left.right = new TreeNode(3);
    bst.right.left = new TreeNode(5);
    bst.right.right = new TreeNode(7);

    System.out.println("\nIs Valid BST: " + isValidBST(bst));
    System.out.println("LCA(1, 3): " + lowestCommonAncestor(bst, bst.left.left,
        bst.left.right).val);
    System.out.println("Kth Smallest (k=3): " + kthSmallest(bst, 3));

    // Build from preorder/inorder
    int[] preorder = {3, 9, 20, 15, 7};
    int[] inorder = {9, 3, 15, 20, 7};
    TreeNode built = buildTree(preorder, inorder);
    System.out.println("Built tree inorder: " + inorderTraversal(built));

    // Serialize/deserialize
    String serialized = serialize(root);
    System.out.println("\nSerialized: " + serialized);
    TreeNode deserialized = deserialize(serialized);
    System.out.println("Deserialized inorder: " + inorderTraversal(deserialized));
  }
}
