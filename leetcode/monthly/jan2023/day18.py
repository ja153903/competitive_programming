class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        """
        Given a circular integer array nums of length n,
        return the maximum possible sum of a non-empty subarray of nums

        There are two cases to consider here

        1. Maximum subarray exists within non-circular array
        2. Maximum subarray exists as circular array

        We can take advantage of Kadane here.

        If non-circular array, then we should just take advantage of Kadane.

        If circular array, then we should take advantage of:
            total - min_sum (this will give us the max subarray)
        """

        total, max_sum, cur_max, min_sum, cur_min = 0, nums[0], 0, nums[0], 0

        for num in nums:
            cur_max = max(num, cur_max + num)
            max_sum = max(max_sum, cur_max)
            cur_min = min(num, cur_min + num)
            min_sum = min(min_sum, cur_min)

            total += num

        if max_sum > 0:
            return max(max_sum, total - min_sum)

        return max_sum
