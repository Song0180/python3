from leetcode_py import TreeNode


class Solution:
    # Time: O(n): n is the number of nodes in the tree
    # Space: O(h): h is the height of the tree
    def is_valid_bst(self, root: TreeNode[int] | None) -> bool:
        def dfs(root, min_val, max_val):
            if not root:
                return True

            if root.val <= min_val or root.val >= max_val:
                return False

            return dfs(root.left, min_val, root.val) and dfs(
                root.right, root.val, max_val
            )

        return dfs(root, float("-inf"), float("inf"))
