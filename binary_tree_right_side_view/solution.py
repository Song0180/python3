from leetcode_py import TreeNode
from collections import deque


class Solution:
    # Time: O(n): n is the number of nodes in the tree
    # Space: O(w + h): w: max width of the tree,  h: tree height. worst total: O(n)
    def right_side_view_bfs(self, root: TreeNode[int] | None) -> list[int]:
        ans = []
        q = deque([root])

        while q:
            num_nodes = len(q)
            level = []
            for _ in range(num_nodes):
                node = q.popleft()

                if node:
                    level.append(node.val)

                    q.append(node.left)
                    q.append(node.right)

            if level:
                ans.append(level[-1])

        return ans

    # dfs
    # time: O(n)
    # space: O(h)
    def right_side_view(self, root: TreeNode[int] | None) -> list[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return

            # this is the first node at this depth → append its value.
            if len(res) == depth:
                res.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res
