import pytest

from ..math import gcd, lcm


@pytest.mark.parametrize('a,b,expected', [
    (3, 2, 1), (6, 2, 2), (18, 15, 3)
])
def test_gcd(a: int, b: int, expected: int):
    assert gcd(a, b) == expected


@pytest.mark.parametrize('a,b,expected', [
    (24, 60, 120), (3, 12, 12), (0, 1, 0)
])
def test_lcm(a: int, b: int, expected: int):
    assert lcm(a, b) == expected
