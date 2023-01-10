from utility.constants import ROMAN_TO_INTEGER


class Solution:
    def romanToInt(self, s: str) -> int:
        curr = ROMAN_TO_INTEGER[s[-1]]
        res = curr

        #
        for i in range(len(s) - 2, -1, -1):
            if ROMAN_TO_INTEGER[s[i]] < curr:
                res -= ROMAN_TO_INTEGER[s[i]]
            else:
                res += ROMAN_TO_INTEGER[s[i]]

            curr = ROMAN_TO_INTEGER[s[i]]

        return res
