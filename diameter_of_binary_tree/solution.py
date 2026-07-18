from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h): O(logn) ~ O(n)
    def diameter_of_binary_tree(self, root: TreeNode[int] | None) -> int:
        max_dia = 0

        def dfs(node):
            nonlocal max_dia

            if not node:
                return 0

            left_d = dfs(node.left)
            right_d = dfs(node.right)

            # at any given node, diameter = left depth + right depth
            max_dia = max(max_dia, left_d + right_d)

            return 1 + max(left_d, right_d)

        dfs(root)
        return max_dia
