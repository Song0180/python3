def run_max_sliding_window(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.max_sliding_window(nums, k)


def assert_max_sliding_window(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
