from leetcode_py import TreeNode


class Solution:
    # Time: O(n): n is the number of nodes in the tree
    # Space: O(h): h is the height of the tree
    def kth_smallest(self, root: TreeNode[int] | None, k: int) -> int:
        count = 0
        ans = None

        def dfs(node):
            nonlocal count, ans
            if not node or ans != None:
                return

            dfs(node.left)
            if count == k - 1:
                ans = node.val
            count += 1
            dfs(node.right)

        dfs(root)
        return ans
