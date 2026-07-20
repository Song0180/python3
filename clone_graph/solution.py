from collections import deque
from leetcode_py import GraphNode


class Solution:
    # Time: O(V + E)
    # Space: O(V)
    def clone_graph_dfs(self, node: GraphNode | None) -> GraphNode | None:
        if not node:
            return None

        old_new_map: dict[int, GraphNode] = {}

        def dfs(cur: GraphNode) -> GraphNode:
            node_id = id(cur)
            if node_id in old_new_map:
                return old_new_map[node_id]

            copy = GraphNode(cur.val)
            old_new_map[node_id] = copy

            for nei in cur.neighbors:
                nei_node = dfs(nei)
                copy.neighbors.append(nei_node)

            return copy

        return dfs(node)

    def clone_graph(self, node: GraphNode | None) -> GraphNode | None:
        if not node:
            return None

        old_new_map: dict[int, GraphNode] = {id(node): GraphNode(node.val)}
        q = deque([node])

        while q:
            cur = q.popleft()

            for nei in cur.neighbors:
                if id(nei) not in old_new_map:
                    old_new_map[id(nei)] = GraphNode(nei.val)
                    q.append(nei)
                old_new_map[id(cur)].neighbors.append(old_new_map[id(nei)])

        return old_new_map[id(node)]
