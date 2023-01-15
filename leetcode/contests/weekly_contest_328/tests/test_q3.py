import pytest

from ..q3 import Solution

solution = Solution()


@pytest.mark.parametrize("nums,k,expected", [([3, 1, 4, 3, 2, 2, 4], 2, 4)])
def test_q3(nums, k, expected):
    assert solution.countGood(nums, k) == expected
