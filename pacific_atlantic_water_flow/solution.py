from collections import deque


class Solution:
    # Time: O(m * n)
    # Space: O(m * n)
    def pacific_atlantic_dfs(self, heights: list[list[int]]) -> list[list[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac, atl = set(), set()
        res = []

        def dfs(r, c, visited, prev_height):
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or (r, c) in visited
                or heights[r][c] < prev_height
            ):
                return

            visited.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # find top & bottom edges
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # find left & right edges
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res

    # Time: O(m * n)
    # Space: O(m * n)
    def pacific_atlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac, atl = set(), set()
        res = []

        def bfs(source, visited):
            q = deque(source)

            while q:
                r, c = q.popleft()
                visited.add((r, c))

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0
                        or nc < 0
                        or nr >= ROWS
                        or nc >= COLS
                        or (nr, nc) in visited
                        or heights[nr][nc] < heights[r][c]
                    ):
                        continue
                    q.append((nr, nc))

        pac_source = []
        atl_source = []

        # find top & bottom edges
        for c in range(COLS):
            pac_source.append((0, c))
            atl_source.append((ROWS - 1, c))

        # find left & right edges
        for r in range(ROWS):
            pac_source.append((r, 0))
            atl_source.append((r, COLS - 1))

        bfs(pac_source, pac)
        bfs(atl_source, atl)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
