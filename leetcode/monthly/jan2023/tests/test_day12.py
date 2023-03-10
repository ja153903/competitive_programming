import pytest

from ..day12 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "n,edges,labels,expected",
    [
        (
            7,
            [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            "abaedcd",
            [2, 1, 1, 1, 1, 1, 1],
        ),
        (4, [[0, 1], [1, 2], [0, 3]], "bbbb", [4, 2, 1, 1]),
        (5, [[0, 1], [0, 2], [1, 3], [0, 4]], "aabab", [3, 2, 1, 1, 1]),
        (
            7,
            [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],
            "aaabaaa",
            [6, 5, 4, 1, 3, 2, 1],
        ),
    ],
)
def test_countSubTrees(
    n: int, edges: list[list[int]], labels: str, expected: list[int]
):
    assert solution.countSubTrees(n, edges, labels) == expected
