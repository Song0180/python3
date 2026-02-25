from leetcode_py import TreeNode


class Solution:
    # Time: O(n): n is the number of nodes in the tree
    # Space: O(h): h is the height of the tree
    def is_same_tree(self, p: TreeNode[int] | None, q: TreeNode[int] | None) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
