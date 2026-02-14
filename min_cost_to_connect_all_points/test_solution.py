import pytest
from leetcode_py import logged_test

from .helpers import assert_min_cost_connect_points, run_min_cost_connect_points
from .solution import Solution


class TestTestMinCostToConnectAllPoints:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "points, expected",
        [
            ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20),
            ([[3, 12], [-2, 5], [-4, 1]], 18),
            ([[0, 0]], 0),
            ([[0, 0], [1, 1]], 2),
            ([[0, 0], [1, 1], [2, 2]], 4),
            ([[0, 0], [2, 2], [3, 10]], 13),
            ([[0, 0], [1, 1], [2, 2], [3, 3]], 6),
            ([[-1000000, -1000000], [1000000, 1000000]], 4000000),
            ([[0, 0], [1, 0], [2, 0], [3, 0]], 3),
            ([[0, 0], [0, 1], [0, 2], [0, 3]], 3),
            ([[0, 0], [3, 3], [6, 0]], 12),
            ([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], 8),
            ([[0, 0], [1, 1], [2, 0]], 4),
        ],
    )
    def test_min_cost_connect_points(self, points: list[list[int]], expected: int):
        result = run_min_cost_connect_points(Solution, points)
        assert_min_cost_connect_points(result, expected)
