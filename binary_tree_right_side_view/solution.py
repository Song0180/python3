from leetcode_py import TreeNode
from collections import deque


class Solution:
    # Time: O(n): n is the number of nodes in the tree
    # Space: O(d): d is the depth of the tree
    def right_side_view(self, root: TreeNode[int] | None) -> list[int]:
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
