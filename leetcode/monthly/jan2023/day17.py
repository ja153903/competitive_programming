class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        A binary string is monotone increasing if it consists
        of some number of 0s followed by some number of 1s

        You are given a binary string s. You can flip s[1]
        changing it from 0 to 1 or from 1 to 0

        Return the minimum number of flips to make s monotone increasing

        --------
        Solution
        --------

        For this solution, we need to consider the following cases.

        1. If the string contains all 1s or all 0s, then there's no need to flip anything
        2. The situation becomes more complicated when we have a combination of both

        To handle the second case, we should keep track of two things.

        If we see a 1, then we should update the count of 1s
        If we see a 0, then we should update the number of flips

        However, the number of flips is then re-evaluated to be
        the minimum between the number of 1s and the number of flips.

        Why does this work?
        If there is a smaller number of 1s than other flips we need to make, then
        we should just flip all the ones. Otherwise, we should just commit the flips.
        """

        flips, ones = 0, 0

        for ch in s:
            if ch == "1":
                ones += 1
            else:
                flips += 1

            flips = min(flips, ones)

        return flips
