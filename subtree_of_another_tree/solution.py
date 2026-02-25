from leetcode_py import TreeNode


class Solution:
    # Time: O(n * m): n is the number of nodes in the root tree, m is the number of nodes in the subRoot tree
    # Space: O(h): h is the height of the tree
    def is_subtree(
        self, root: TreeNode[int] | None, subRoot: TreeNode[int] | None
    ) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        return (
            self.is_same_tree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

    def is_same_tree(self, p: TreeNode[int] | None, q: TreeNode[int] | None) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        return (
            p.val == q.val
            and self.is_same_tree(p.left, q.left)
            and self.is_same_tree(p.right, q.right)
        )
