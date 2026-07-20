from collections import deque


class Solution:
    # Time: O(m * n)
    # Space: O(m * n)
    def num_islands_dfs(self, grid: list[list[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != "1":
                return

            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1

        return count

    # time: O(m * n)
    # space: O(m * n)
    def num_islands(self, grid: list[list[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0

        def bfs(r, c):
            q = deque([(r, c)])

            while q:
                row, col = q.popleft()

                if (
                    row < 0
                    or col < 0
                    or row >= ROWS
                    or col >= COLS
                    or grid[row][col] != "1"
                ):
                    continue

                grid[row][col] = "0"
                for dr, dc in directions:
                    q.append((row + dr, col + dc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    count += 1

        return count
