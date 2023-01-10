import pytest

from ..lp436 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "grid,expected",
    [
        ([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]], 16),
        ([[1]], 4),
        ([[1, 0]], 4),
        ([[1, 1], [1, 1]], 8),
    ],
)
def test_islandPerimeter(grid: list[list[int]], expected: int):
    assert solution.islandPerimeter(grid) == expected
