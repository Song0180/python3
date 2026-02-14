import pytest
from leetcode_py import logged_test

from .helpers import assert_find_cheapest_price, run_find_cheapest_price
from .solution import Solution


class TestTestCheapestFlightsWithinKStops:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, flights, src, dst, k, expected",
        [
            (
                4,
                [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
                0,
                3,
                1,
                700,
            ),
            (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200),
            (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0, 500),
            (
                5,
                [
                    [0, 1, 100],
                    [0, 2, 500],
                    [1, 2, 100],
                    [1, 3, 600],
                    [2, 3, 200],
                    [3, 4, 100],
                ],
                0,
                4,
                2,
                800,
            ),
            (4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1, 6),
            (3, [[0, 1, 100], [1, 2, 100]], 0, 2, 0, -1),
            (2, [[0, 1, 100]], 0, 1, 0, 100),
            (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 2, 200),
            (4, [[0, 1, 100], [1, 2, 100], [2, 3, 100], [0, 3, 500]], 0, 3, 1, 500),
            (
                5,
                [[0, 1, 100], [1, 2, 100], [2, 3, 100], [3, 4, 100], [0, 4, 1000]],
                0,
                4,
                0,
                1000,
            ),
            (3, [[0, 1, 100], [1, 2, 100], [2, 0, 100]], 0, 2, 1, 200),
            (4, [[0, 1, 100], [1, 2, 100], [2, 3, 100]], 0, 3, 10, 300),
            (3, [[0, 1, 200], [1, 2, 200], [0, 2, 500]], 0, 2, 1, 400),
        ],
    )
    def test_find_cheapest_price(
        self,
        n: int,
        flights: list[list[int]],
        src: int,
        dst: int,
        k: int,
        expected: int,
    ):
        result = run_find_cheapest_price(Solution, n, flights, src, dst, k)
        assert_find_cheapest_price(result, expected)
