from collections import deque
from leetcode_py import TreeNode


class Solution:
    # Time: O(n): n is the number of nodes in the tree
    # Space: O(h): h is the height of the tree
    def is_valid_bst_dfs(self, root: TreeNode[int] | None) -> bool:
        def dfs(root, min_val, max_val):
            if not root:
                return True

            if root.val <= min_val or root.val >= max_val:
                return False

            return dfs(root.left, min_val, root.val) and dfs(
                root.right, root.val, max_val
            )

        return dfs(root, float("-inf"), float("inf"))

    # bfs
    # time: O(n)
    # space: O(w) q length -> worst O(n) balanced tree, n/2; best: O(1), skewed tree
    def is_valid_bst(self, root: TreeNode[int] | None) -> bool:
        if not root:
            return True

        q = deque([(root, float("-inf"), float("inf"))])
        while q:
            node, lower, upper = q.popleft()

            if node.val <= lower or node.val >= upper:
                return False

            if node.left:
                q.append((node.left, lower, node.val))
            if node.right:
                q.append((node.right, node.val, upper))

        return True
