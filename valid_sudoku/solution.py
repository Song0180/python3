from ast import Set
from collections import defaultdict


class SolutionVerbose:
    # Time: O(n^2)
    # Space: O(n)
    def is_valid_sudoku(self, board: list[list[str]]) -> bool:
        col_sets: list[Set] = [set() for _ in range(9)]
        grid_sets: list[list[Set]] = [[set() for _ in range(3)] for _ in range(3)]

        for row_idx, row in enumerate(board):
            row_set = set()
            for col_idx, col in enumerate(row):
                if board[row_idx][col_idx] == ".":
                    continue

                # check col
                if col not in col_sets[col_idx]:
                    col_sets[col_idx].add(col)
                else:
                    return False

                # check row
                if col not in row_set:
                    row_set.add(col)
                else:
                    return False

                # check grid
                grid_idx_row = row_idx // 3
                grid_idx_col = col_idx // 3

                if col not in grid_sets[grid_idx_row][grid_idx_col]:
                    grid_sets[grid_idx_row][grid_idx_col].add(col)
                else:
                    return False
        return True


class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def is_valid_sudoku(self, board: list[list[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        grids = defaultdict(set)

        for row in range(9):
            for col in range(9):
                cur = board[row][col]

                if cur == ".":
                    continue

                if (
                    cur in cols[col]
                    or cur in rows[row]
                    or cur in grids[(row // 3, col // 3)]
                ):
                    return False

                cols[col].add(cur)
                rows[row].add(cur)
                grids[(row // 3, col // 3)].add(cur)

        return True
