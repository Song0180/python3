from collections import deque
from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h)
    # dfs
    def invert_tree_dfs(self, root: TreeNode[int] | None) -> TreeNode[int] | None:
        if not root:
            return None

        left_node = self.invert_tree(root.left)
        right_node = self.invert_tree(root.right)

        root.left = right_node
        root.right = left_node

        return root

    # bfs
    # t: O(n)
    # s: O(n)
    def invert_tree(self, root: TreeNode[int] | None) -> TreeNode[int] | None:
        if not root:
            return None

        q = deque([root])

        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return root
