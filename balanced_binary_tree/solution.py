from leetcode_py import TreeNode


class Solution:
    # Time: O(n): n is the number of nodes in the tree
    # Space: O(h): h is the height of the tree
    def is_balanced(self, root: TreeNode[int] | None) -> bool:
        ans = True

        def dfs(root):
            nonlocal ans

            if not root:
                return 0

            left_height = dfs(root.left)
            right_height = dfs(root.right)

            if abs(left_height - right_height) > 1:
                ans = False

            return 1 + max(left_height, right_height)

        dfs(root)
        return ans
