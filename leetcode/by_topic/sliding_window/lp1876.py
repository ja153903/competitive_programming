class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        """
        s = "xyzzaz"
        keep track of the number of unique characters as we go through substrings

        xyz, yzz, zza, zaz (only 1)
        """
        res = 0
        cnt = [0] * 26
        start = 0

        for end, ch in enumerate(s):
            cnt[ord(ch) - 97] += 1

            if end - start + 1 == 3:
                unique = 0
                for i in range(26):
                    if cnt[i] > 0:
                        unique += 1

                if unique == 3:
                    res += 1

                cnt[ord(s[start]) - 97] -= 1
                start += 1

        return res
