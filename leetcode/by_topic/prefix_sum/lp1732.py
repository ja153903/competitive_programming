class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        res = 0
        alt = 0

        for g in gain:
            alt += g
            res = max(res, alt)

        return res
