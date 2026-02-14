def run_min_cost_connect_points(solution_class: type, points: list[list[int]]):
    implementation = solution_class()
    return implementation.min_cost_connect_points(points)


def assert_min_cost_connect_points(result: int, expected: int) -> bool:
    assert result == expected
    return True
