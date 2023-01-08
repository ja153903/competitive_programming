import pytest

from ..week2 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "damage,armor,expected",
    [([2, 7, 4, 3], 4, 13), ([2, 5, 3, 4], 7, 10), ([3, 3, 3], 0, 10)],
)
def test_minimumHealth(damage: list[int], armor: int, expected: int):
    assert solution.minimumHealth(damage, armor) == expected
