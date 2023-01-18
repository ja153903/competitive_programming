import pytest

from ..lp953 import Solution


solution = Solution()


@pytest.mark.parametrize(
    "words,order,expected",
    [
        (["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
        (["word", "world", "row"], "worldabcefghijkmnpqstuvxyz", False),
        (["apple", "app"], "abcdefghijklmnopqrstuvwxyz", False),
    ],
)
def test_isAlienSorted(words: list[str], order: str, expected: bool):
    assert solution.isAlienSorted(words, order) == expected
