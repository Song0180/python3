import pytest
from leetcode_py import logged_test

from .helpers import assert_check_inclusion, run_check_inclusion
from .solution import Solution


class TestTestPermutationInString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s1, s2, expected",
        [
            ("ab", "eidbaooo", True),
            ("ab", "eidboaoo", False),
            ("a", "a", True),
            ("ab", "ab", True),
            ("abc", "bbbca", True),
            ("abcd", "abc", False),
            ("hello", "ooolleoooleh", False),
            ("adc", "dcda", True),
            ("ab", "a", False),
            ("a", "b", False),
            ("abc", "ccccbbbbaaaa", False),
            ("abc", "babcabc", True),
            ("ky", "ainwkckifykxlribaypk", True),
            ("roxyz", "xyzro", True),
            ("abcdxabcd", "abcdxabcdabcdxabcd", True),
        ],
    )
    def test_check_inclusion(self, s1: str, s2: str, expected: bool):
        result = run_check_inclusion(Solution, s1, s2)
        assert_check_inclusion(result, expected)
