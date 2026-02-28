from leetcode_py import TreeNode


class Solution:
    # Time: O(?)
    # Space: O(?)
    def max_path_sum(self, root: TreeNode[int] | None) -> int:
        ans = root.val

        def dfs(root):
            nonlocal ans

            if not root:
                return 0

            left_max = dfs(root.left)
            right_max = dfs(root.right)

            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            ans = max(ans, root.val + left_max + right_max)
            return root.val + max(left_max, right_max)

        dfs(root)
        return ans
