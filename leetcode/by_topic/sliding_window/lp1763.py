def _is_nice(chars: list[str]) -> bool:
    as_set = set(chars)

    for ch in as_set:
        if ch.swapcase() not in as_set:
            return False

    return True


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        """
        A string s is nice if, for every letter of the alphabet that s contains,
        it appears both in uppercase and lowercase.
        For example, "abABB" is nice because 'A' and 'a' appear,
        and 'B' and 'b' appear.
        However, "abA" is not because 'b' appears, but 'B' does not.

        Given a string s, return the longest substring of s that is nice.
        If there are multiple, return the substring of the earliest occurrence.
        If there are none, return an empty string.

        Observations:
        * if the length is less than or equal to 1, then we know there are no
          nice substrings
        * since the constraints are rather small, the best way to solve this problem
          is by using brute force
        """
        if len(s) <= 1:
            return ""

        longest_nice_substr, longest_nice_substr_len = [], 0

        for i in range(len(s)):
            nice_substr = []
            for j in range(i, len(s)):
                nice_substr.append(s[j])

                if len(nice_substr) > 1 and _is_nice(nice_substr):
                    if longest_nice_substr_len < len(nice_substr):
                        longest_nice_substr_len = len(nice_substr)
                        longest_nice_substr = list(nice_substr)

        return "".join(longest_nice_substr)
