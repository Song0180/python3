import collections
from leetcode_py import TreeNode


class Solution:
    # Time: O(n): n is the number of nodes in the tree
    # Space: O(n): n is the number of nodes in the tree
    def build_tree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        preorder_q = collections.deque(preorder)

        def dfs(l, r):
            if l > r:
                return None

            root_val = preorder_q.popleft()
            root = TreeNode(root_val)

            root.left = dfs(l, inorder_map[root_val] - 1)
            root.right = dfs(inorder_map[root_val] + 1, r)
            return root

        return dfs(0, len(inorder) - 1)
