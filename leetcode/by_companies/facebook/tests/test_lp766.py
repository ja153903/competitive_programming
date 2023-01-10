import pytest

from ..lp766 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "matrix,expected",
    [([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]], True), ([[1, 2], [2, 2]], False)],
)
def test_isToeplitzMatrix(matrix: list[list[int]], expected: bool):
    assert solution.isToeplitzMatrix(matrix) == expected
