import pytest

from ..day18 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, -2, 3, -2], 3),
        ([5, -3, 5], 10),
        ([-3, -2, -3], -2),
        ([-2], -2),
        ([-5, 3, 5], 8),
    ],
)
def test_maxSubarraySumCircular(nums: list[int], expected: int):
    assert solution.maxSubarraySumCircular(nums) == expected
