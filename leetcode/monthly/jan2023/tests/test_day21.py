import pytest

from ..day21 import Solution


solution = Solution()


@pytest.mark.parametrize(
    "s,expected", [("25525511135", ["255.255.11.135", "255.255.111.35"])]
)
def test_restoreIpAddresses(s: str, expected: list[str]):
    assert solution.restoreIpAddresses(s) == expected
