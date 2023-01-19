class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        """
        Given an integer array nums and an integer k,
        return the number of non-empty subarrays that have a sum divisible by k.

        A subarray is a contiguous part of an array.

        Input: nums = [4,5,0,-2,-3,1], k = 5
        Output: 7
        """
        res, prefix = 0, 0
        count = [1] + [0] * k

        for num in nums:
            prefix = (prefix + num) % k
            res += count[prefix]
            count[prefix] += 1

        return res
