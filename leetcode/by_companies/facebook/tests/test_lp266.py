import pytest

from ..lp266 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "s,expected", [("aa", True), ("code", False), ("aab", True), ("carerac", True)]
)
def test_canPermutePalindrome(s: str, expected: bool):
    assert solution.canPermutePalindrome(s) == expected
