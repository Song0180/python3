def run_find_cheapest_price(
    solution_class: type, n: int, flights: list[list[int]], src: int, dst: int, k: int
):
    implementation = solution_class()
    return implementation.find_cheapest_price(n, flights, src, dst, k)


def assert_find_cheapest_price(result: int, expected: int) -> bool:
    assert result == expected
    return True
