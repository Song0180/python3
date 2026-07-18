from leetcode_py import TreeNode


class Solution:
    # Time: O(h): h is the height of the tree
    # Space: O(h): h is the height of the tree
    def lowest_common_ancestor(
        self, root: TreeNode[int] | None, p: TreeNode[int], q: TreeNode[int]
    ) -> TreeNode[int] | None:
        if max(p.val, q.val) < root.val:
            return self.lowest_common_ancestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowest_common_ancestor(root.right, p, q)
        else:
            return root

    def lowest_common_ancestor_iterative(
        self, root: TreeNode[int] | None, p: TreeNode[int], q: TreeNode[int]
    ) -> TreeNode[int] | None:

        while root:
            if max(p.val, q.val) < root.val:
                root = root.left
            elif min(p.val, q.val) > root.val:
                root = root.right
            else:
                return root

        return None
