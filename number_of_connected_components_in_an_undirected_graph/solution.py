from collections import deque


class Solution:
    # Time: O(V + E)
    # Space: O(V + E)
    def count_components_dfs(self, n: int, edges: list[list[int]]) -> int:
        adj_map = {i: [] for i in range(n)}

        for a, b in edges:
            # undirected graph, need to update both nodes
            adj_map[a].append(b)
            adj_map[b].append(a)

        visited = set()

        def dfs(node):
            visited.add(node)

            for nei in adj_map[node]:
                if nei not in visited:
                    dfs(nei)

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count

    # dfs, O(V + E)
    def count_components(self, n, edges):
        adj_map = {i: [] for i in range(n)}

        for a, b in edges:
            # undirected graph, need to update both nodes
            adj_map[a].append(b)
            adj_map[b].append(a)

        visited = set()

        def bfs(node):
            q = deque([node])

            while q:
                n = q.popleft()
                visited.add(n)
                for nei in adj_map[n]:
                    if nei not in visited:
                        q.append(nei)

        count = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                count += 1

        return count
