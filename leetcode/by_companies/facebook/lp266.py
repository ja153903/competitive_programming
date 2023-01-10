from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        s_cnt = Counter(s)

        num_odd = 0

        for value in s_cnt.values():
            if value % 2 == 1:
                num_odd += 1

        return num_odd <= 1
