class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        res = 0

        j = 0

        for i in range(1, len(nums) - 1):
            if (nums[j] < nums[i] and nums[i] > nums[i + 1]) or (
                nums[j] > nums[i] and nums[i] < nums[i + 1]
            ):
                res += 1
                # the idea here is that we're marking the previous valley or hill
                # that we've found.
                # this accounts for duplicate values that lie in the same hill or valley
                j = i

        return res
