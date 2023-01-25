class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        """
        Given an integer array nums, return the length of the longest strictly increasing subsequence.

        nums = [10,9,2,5,3,7,101,18]

        dp[i] ~ the length of the longest strictly increasing subsequence from i

        Our algorithm has us going through the various indices to choose a starting place
        From that point on, we look back on the appropriate places we can choose to increase from

        dp[i] = max(dp[i - k]) for all k in [0, i)
        """
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
