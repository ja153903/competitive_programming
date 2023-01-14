from typing import List

import pytest

from ..lp253 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "intervals,expected",
    [
        ([[9, 16], [6, 16], [1, 9], [3, 15]], 3),
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[7, 10], [2, 4]], 1),
        ([[2, 11], [6, 16], [11, 16]], 2),
    ],
)
def test_minMeetingRooms(intervals: List[List[int]], expected: int):
    assert solution.minMeetingRooms(intervals) == expected
