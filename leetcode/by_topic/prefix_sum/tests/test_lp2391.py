import pytest


from ..lp2391 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "garbage,travel,expected",
    [
        (["G", "P", "GP", "GG"], [2, 4, 3], 21),
        (["MMM", "PGM", "GP"], [3, 10], 37),
        (["G", "M"], [1], 3),
    ],
)
def test_garbageCollection(garbage: list[str], travel: list[int], expected: int):
    assert solution.garbageCollection(garbage, travel) == expected
