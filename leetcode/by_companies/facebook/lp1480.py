class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        rs = [0] * len(nums)

        for i, num in enumerate(nums):
            if i > 0:
                rs[i] += rs[i - 1]

            rs[i] += num

        return rs
