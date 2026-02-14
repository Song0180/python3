import pytest
from leetcode_py import logged_test

from .helpers import assert_max_sliding_window, run_max_sliding_window
from .solution import Solution


class TestTestSlidingWindowMaximum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
            ([1], 1, [1]),
            ([1, -1], 1, [1, -1]),
            ([9, 11], 2, [11]),
            ([4, -2], 2, [4]),
            ([1, 3, 1, 2, 0, 5], 3, [3, 3, 2, 5]),
            ([1, 2, 3, 4, 5], 2, [2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], 2, [5, 4, 3, 2]),
            ([1, 2, 3, 4, 5], 5, [5]),
            ([5, 4, 3, 2, 1], 5, [5]),
            ([7, 2, 4], 2, [7, 4]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, [3, 4, 5, 6, 7, 8, 9, 10]),
            ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 4, [10, 9, 8, 7, 6, 5, 4]),
            ([1, 1, 1, 1, 1], 2, [1, 1, 1, 1]),
            ([-1, -2, -3, -4], 2, [-1, -2, -3]),
        ],
    )
    def test_max_sliding_window(self, nums: list[int], k: int, expected: list[int]):
        result = run_max_sliding_window(Solution, nums, k)
        assert_max_sliding_window(result, expected)
