import pytest

from ..lp1047 import Solution

solution = Solution()


@pytest.mark.parametrize("s,expected", [("abbaca", "ca")])
def test_removeDuplicates(s: str, expected: str):
    assert solution.removeDuplicates(s) == expected
