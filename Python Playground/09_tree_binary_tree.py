"""
TREE & BINARY TREE - Complete Guide for Interview Preparation
==============================================================

CORE CONCEPTS:
--------------
1. Tree: hierarchical data structure with root and children
2. Binary Tree: each node has at most 2 children (left, right)
3. Full BT: every node has 0 or 2 children
4. Complete BT: all levels filled except possibly last (filled left to right)
5. Perfect BT: all internal nodes have 2 children, all leaves same level
6. Balanced BT: height difference of subtrees <= 1
7. BST: left < root < right (for all subtrees)

TREE TRAVERSALS:
- Inorder (Left, Root, Right) - BST gives sorted order
- Preorder (Root, Left, Right) - used for copying tree
- Postorder (Left, Right, Root) - used for deleting tree
- Level Order (BFS) - level by level

TRICKY PARTS:
-------------
1. Null/None checks are crucial!
2. Recursion is natural for trees but watch stack overflow
3. Parent pointers not always available
4. Tree modification during traversal
5. Understanding when to use DFS vs BFS

COMMON PATTERNS:
----------------
1. Recursive DFS (inorder, preorder, postorder)
2. Iterative DFS (using stack)
3. BFS (using queue)
4. Tree construction from traversals
5. Path problems (root to leaf, any path)
6. Lowest Common Ancestor
"""

from typing import Optional, List
from collections import deque


class TreeNode:
    """Binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================================
# PATTERN 1: TREE TRAVERSALS - RECURSIVE
# ============================================================================

def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    LeetCode 94 - Inorder traversal (Left, Root, Right).

    Time: O(n), Space: O(h) where h is height
    """
    result = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

    dfs(root)
    return result


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    LeetCode 144 - Preorder traversal (Root, Left, Right).

    Time: O(n), Space: O(h)
    """
    result = []

    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return result


def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    LeetCode 145 - Postorder traversal (Left, Right, Root).

    Time: O(n), Space: O(h)
    """
    result = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)

    dfs(root)
    return result


# ============================================================================
# PATTERN 2: TREE TRAVERSALS - ITERATIVE
# ============================================================================

def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    Iterative inorder traversal using stack.

    Time: O(n), Space: O(h)
    """
    result = []
    stack = []
    curr = root

    while curr or stack:
        # Go to leftmost node
        while curr:
            stack.append(curr)
            curr = curr.left

        # Process node
        curr = stack.pop()
        result.append(curr.val)

        # Move to right
        curr = curr.right

    return result


def preorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    Iterative preorder traversal.

    Time: O(n), Space: O(h)
    """
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push right first (so left is processed first)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def postorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    Iterative postorder traversal.

    Time: O(n), Space: O(h)
    Tricky: Use two stacks or reverse preorder
    """
    if not root:
        return []

    # Approach 1: Reverse of (Root, Right, Left)
    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push left first (so right is processed first)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return result[::-1]


# ============================================================================
# PATTERN 3: LEVEL ORDER TRAVERSAL (BFS)
# ============================================================================

def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    LeetCode 102 - Level order traversal.

    Time: O(n), Space: O(w) where w is max width
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    LeetCode 103 - Zigzag level order traversal.

    Time: O(n), Space: O(w)
    """
    if not root:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level = []
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if not left_to_right:
            level.reverse()

        result.append(level)
        left_to_right = not left_to_right

    return result


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    """
    LeetCode 199 - Binary tree right side view.

    Time: O(n), Space: O(w)
    Tricky: Last node at each level
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            # Add last node of level
            if i == level_size - 1:
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


# ============================================================================
# PATTERN 4: TREE PROPERTIES
# ============================================================================

def max_depth(root: Optional[TreeNode]) -> int:
    """
    LeetCode 104 - Maximum depth of binary tree.

    Time: O(n), Space: O(h)
    """
    if not root:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))


def min_depth(root: Optional[TreeNode]) -> int:
    """
    LeetCode 111 - Minimum depth of binary tree.

    Time: O(n), Space: O(h)
    Tricky: Depth to nearest LEAF node (both children None)
    """
    if not root:
        return 0

    # If one subtree empty, return depth of other
    if not root.left:
        return 1 + min_depth(root.right)
    if not root.right:
        return 1 + min_depth(root.left)

    return 1 + min(min_depth(root.left), min_depth(root.right))


def is_balanced(root: Optional[TreeNode]) -> bool:
    """
    LeetCode 110 - Check if tree is height-balanced.

    Time: O(n), Space: O(h)
    """
    def height(node):
        """Returns height if balanced, -1 if unbalanced."""
        if not node:
            return 0

        left_h = height(node.left)
        if left_h == -1:
            return -1

        right_h = height(node.right)
        if right_h == -1:
            return -1

        if abs(left_h - right_h) > 1:
            return -1

        return 1 + max(left_h, right_h)

    return height(root) != -1


def diameter(root: Optional[TreeNode]) -> int:
    """
    LeetCode 543 - Diameter of binary tree.

    Time: O(n), Space: O(h)
    Tricky: Longest path may not pass through root!
    """
    max_diameter = [0]

    def height(node):
        if not node:
            return 0

        left_h = height(node.left)
        right_h = height(node.right)

        # Update diameter
        max_diameter[0] = max(max_diameter[0], left_h + right_h)

        return 1 + max(left_h, right_h)

    height(root)
    return max_diameter[0]


# ============================================================================
# PATTERN 5: TREE COMPARISON & VALIDATION
# ============================================================================

def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    LeetCode 100 - Check if two trees are identical.

    Time: O(n), Space: O(h)
    """
    if not p and not q:
        return True
    if not p or not q:
        return False

    return (p.val == q.val and
            is_same_tree(p.left, q.left) and
            is_same_tree(p.right, q.right))


def is_symmetric(root: Optional[TreeNode]) -> bool:
    """
    LeetCode 101 - Check if tree is symmetric.

    Time: O(n), Space: O(h)
    """
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))

    return is_mirror(root, root) if root else True


def is_subtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    """
    LeetCode 572 - Check if subRoot is subtree of root.

    Time: O(m * n), Space: O(h)
    """
    if not root:
        return False
    if is_same_tree(root, subRoot):
        return True

    return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot)


# ============================================================================
# PATTERN 6: PATH PROBLEMS
# ============================================================================

def has_path_sum(root: Optional[TreeNode], targetSum: int) -> bool:
    """
    LeetCode 112 - Check if root-to-leaf path with given sum exists.

    Time: O(n), Space: O(h)
    """
    if not root:
        return False

    # Leaf node
    if not root.left and not root.right:
        return root.val == targetSum

    targetSum -= root.val
    return has_path_sum(root.left, targetSum) or has_path_sum(root.right, targetSum)


def path_sum_ii(root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    """
    LeetCode 113 - Find all root-to-leaf paths with given sum.

    Time: O(n), Space: O(h)
    """
    result = []

    def dfs(node, remaining, path):
        if not node:
            return

        path.append(node.val)

        # Leaf node
        if not node.left and not node.right and remaining == node.val:
            result.append(path[:])  # Important: make copy!

        dfs(node.left, remaining - node.val, path)
        dfs(node.right, remaining - node.val, path)

        path.pop()  # Backtrack

    dfs(root, targetSum, [])
    return result


def max_path_sum(root: Optional[TreeNode]) -> int:
    """
    LeetCode 124 - Binary tree maximum path sum (any node to any node).

    Time: O(n), Space: O(h)
    Tricky: Path can start and end at any node
    """
    max_sum = [float('-inf')]

    def max_gain(node):
        """Returns max path sum starting from node going down."""
        if not node:
            return 0

        # Only consider positive gains
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)

        # Path through current node
        current_path = node.val + left_gain + right_gain
        max_sum[0] = max(max_sum[0], current_path)

        # Return max path extending from current node
        return node.val + max(left_gain, right_gain)

    max_gain(root)
    return max_sum[0]


def binary_tree_paths(root: Optional[TreeNode]) -> List[str]:
    """
    LeetCode 257 - All root-to-leaf paths.

    Time: O(n), Space: O(h)
    """
    result = []

    def dfs(node, path):
        if not node:
            return

        path.append(str(node.val))

        # Leaf node
        if not node.left and not node.right:
            result.append("->".join(path))
        else:
            dfs(node.left, path)
            dfs(node.right, path)

        path.pop()

    dfs(root, [])
    return result


# ============================================================================
# PATTERN 7: LOWEST COMMON ANCESTOR
# ============================================================================

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    LeetCode 236 - Lowest common ancestor of binary tree.

    Time: O(n), Space: O(h)
    """
    if not root or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    # If both sides return node, current is LCA
    if left and right:
        return root

    # Return non-null side
    return left if left else right


# ============================================================================
# PATTERN 8: TREE CONSTRUCTION
# ============================================================================

def build_tree_inorder_preorder(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """
    LeetCode 105 - Construct tree from preorder and inorder traversals.

    Time: O(n), Space: O(n)
    """
    if not preorder or not inorder:
        return None

    # First element of preorder is root
    root = TreeNode(preorder[0])

    # Find root in inorder (left side = left subtree, right side = right subtree)
    mid = inorder.index(preorder[0])

    # Recursively build subtrees
    root.left = build_tree_inorder_preorder(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree_inorder_preorder(preorder[mid+1:], inorder[mid+1:])

    return root


def build_tree_inorder_postorder(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    """
    LeetCode 106 - Construct tree from inorder and postorder traversals.

    Time: O(n), Space: O(n)
    """
    if not inorder or not postorder:
        return None

    # Last element of postorder is root
    root = TreeNode(postorder[-1])

    # Find root in inorder
    mid = inorder.index(postorder[-1])

    # Recursively build subtrees
    root.left = build_tree_inorder_postorder(inorder[:mid], postorder[:mid])
    root.right = build_tree_inorder_postorder(inorder[mid+1:], postorder[mid:-1])

    return root


# ============================================================================
# PATTERN 9: TREE MODIFICATION
# ============================================================================

def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    LeetCode 226 - Invert binary tree.

    Time: O(n), Space: O(h)
    """
    if not root:
        return None

    # Swap children
    root.left, root.right = root.right, root.left

    # Recursively invert subtrees
    invert_tree(root.left)
    invert_tree(root.right)

    return root


def flatten_tree(root: Optional[TreeNode]) -> None:
    """
    LeetCode 114 - Flatten binary tree to linked list (in-place, preorder).

    Time: O(n), Space: O(h)
    """
    def flatten_helper(node):
        """Returns tail of flattened subtree."""
        if not node:
            return None

        # Leaf node
        if not node.left and not node.right:
            return node

        # Flatten subtrees
        left_tail = flatten_helper(node.left)
        right_tail = flatten_helper(node.right)

        # If left subtree exists, insert it between node and right
        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None

        # Return tail of flattened tree
        return right_tail if right_tail else left_tail

    flatten_helper(root)


# ============================================================================
# PRACTICE PROBLEMS
# ============================================================================
"""
EASY:
- Max Depth (104)
- Invert Binary Tree (226)
- Symmetric Tree (101)
- Same Tree (100)
- Path Sum (112)
- Balanced Binary Tree (110)

MEDIUM:
- Level Order Traversal (102)
- Binary Tree Right Side View (199)
- Kth Smallest in BST (230)
- Construct Binary Tree from Traversals (105, 106)
- Path Sum II (113)
- Lowest Common Ancestor (236)
- Flatten Binary Tree (114)
- Binary Tree Zigzag Level Order (103)

HARD:
- Binary Tree Maximum Path Sum (124)
- Serialize and Deserialize Binary Tree (297)
- Vertical Order Traversal (987)
"""

if __name__ == "__main__":
    # Create test tree:     1
    #                      / \
    #                     2   3
    #                    / \
    #                   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Inorder:", inorder_traversal(root))
    print("Preorder:", preorder_traversal(root))
    print("Postorder:", postorder_traversal(root))
    print("Level Order:", level_order(root))
    print("Max Depth:", max_depth(root))
