from leetcode_py import TreeNode


class Codec:
    # Time: O(?)
    # Space: O(?)
    def __init__(self) -> None:
        # TODO: Initialize
        pass

    # Time: O(n): n is the number of nodes in the tree
    # Space: O(n): n is the number of nodes in the tree
    def serialize(self, root: TreeNode[int] | None) -> str:
        res = []

        def dfs(root):
            if not root:
                res.append("null")
                return

            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(res)

    # Time: O(n): n is the number of nodes in the tree
    # Space: O(n): n is the number of nodes in the tree
    def deserialize(self, data: str) -> TreeNode[int] | None:
        vals = data.split(",")

        i = 0

        def dfs():
            nonlocal i

            if i >= len(vals) or vals[i] == "null":
                i += 1
                return None

            root = TreeNode(int(vals[i]))
            i += 1
            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()
