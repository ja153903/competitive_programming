import pytest

from ..lp1859 import Solution

solution = Solution()


@pytest.mark.parametrize('s,expected',
                         [("is2 sentence4 This1 a3", "This is a sentence"), ("Myself2 Me1 I4 and3", "Me Myself and I")])
def test_sortSentence(s: str, expected: str):
    assert solution.sortSentence(s) == expected
