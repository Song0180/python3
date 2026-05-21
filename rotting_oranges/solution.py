from collections import deque


class Solution:
    # Time: O(m * n)
    # Space: O(m * n)
    def oranges_rotting(self, grid: list[list[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ROWS = len(grid)
        COLS = len(grid[0])

        rotten = deque()
        fresh_count = 0
        minutes = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return minutes

        # bfs to rot the oranges
        # trick: consider fresh_count to skip when no fresh oranges left
        while rotten and fresh_count > 0:
            level_nodes = len(rotten)
            for _ in range(level_nodes):
                r, c = rotten.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS):
                        continue
                    if grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue

                    grid[nr][nc] = 2
                    rotten.append((nr, nc))
                    fresh_count -= 1

            minutes += 1

        if fresh_count > 0:
            return -1

        return minutes
