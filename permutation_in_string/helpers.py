def run_check_inclusion(solution_class: type, s1: str, s2: str):
    implementation = solution_class()
    return implementation.check_inclusion(s1, s2)


def assert_check_inclusion(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
