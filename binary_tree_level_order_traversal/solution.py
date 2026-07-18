from collections import deque
from leetcode_py import TreeNode


class Solution:
    # Time: O(?)
    # Space: O(?)
    def level_order(self, root: TreeNode[int] | None) -> list[list[int]]:
        res = []

        if not root:
            return res

        q = deque([root])

        while q:
            level_vals = []

            for _ in range(len(q)):
                node = q.popleft()

                level_vals.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level_vals)

        return res
