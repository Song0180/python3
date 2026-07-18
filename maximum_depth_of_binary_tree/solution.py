from collections import deque
from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(height), best/balanced: O(logn), worst/skewed: O(n)
    def max_depth_dfs(self, root: TreeNode[int] | None) -> int:
        if not root:
            return 0

        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)

        return 1 + max(left_depth, right_depth)

    # bfs
    def max_depth(self, root: TreeNode[int] | None) -> int:
        if not root:
            return 0

        depth = 0

        q = deque([root])
        while q:
            level_len = len(q)
            depth += 1
            # only pop out nodes from current level and add next level
            for _ in range(level_len):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return depth
