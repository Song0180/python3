def run_longest_increasing_path(solution_class: type, matrix: list[list[int]]):
    implementation = solution_class()
    return implementation.longest_increasing_path(matrix)


def assert_longest_increasing_path(result: int, expected: int) -> bool:
    assert result == expected
    return True
