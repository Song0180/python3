import pytest
from leetcode_py import logged_test

from .helpers import assert_longest_increasing_path, run_longest_increasing_path
from .solution import Solution


class TestTestLongestIncreasingPathInAMatrix:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "matrix, expected",
        [
            ([[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4),
            ([[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4),
            ([[1]], 1),
            ([[1, 2]], 2),
            ([[2, 1]], 2),
            ([[1], [2]], 2),
            ([[1], [1], [1]], 1),
            ([[1, 2, 3]], 3),
            ([[3, 2, 1]], 3),
            ([[1, 2, 3], [6, 5, 4], [7, 8, 9]], 9),
            ([[9, 8, 7], [2, 1, 6], [3, 4, 5]], 9),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5),
            ([[9, 8, 7], [6, 5, 4], [3, 2, 1]], 5),
            ([[3, 4, 5], [3, 2, 6], [2, 2, 7]], 5),
        ],
    )
    def test_longest_increasing_path(self, matrix: list[list[int]], expected: int):
        result = run_longest_increasing_path(Solution, matrix)
        assert_longest_increasing_path(result, expected)
