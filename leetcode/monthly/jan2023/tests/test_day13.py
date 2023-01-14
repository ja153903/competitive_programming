import pytest

from ..day13 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "parent,s,expected",
    [
        ([-1, 0, 0, 1, 1, 2], "abacbe", 3),
        ([-1, 0, 0, 0], "aabc", 3),
        ([-1, 0, 1], "aab", 2),
    ],
)
def test_longestPath(parent: list[int], s: str, expected: int):
    assert solution.longestPath(parent, s) == expected
