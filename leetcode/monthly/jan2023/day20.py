class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        """
        Given an integer array nums, return all the different
        possible non-decreasing subsequences of the given array with
        at least two elements. You may return the answer in any order.

        Input: nums = [4,6,7,7]
        Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

        My initial intuition for this problem would be to implement some sort
        of backtracking algorithm.

        We'd want to keep items in a set to make sure that we know its unique
        """

        def _backtrack(idx: int, current: list[int]):
            if idx <= len(nums) and len(current) >= 2:
                res.append(list(current))

            used = {}

            for i in range(idx, len(nums)):
                if len(current) > 0 and current[-1] > nums[i]:
                    continue

                if nums[i] in used:
                    continue

                used[nums[i]] = True

                current.append(nums[i])

                _backtrack(i + 1, current)

                current.pop()

        res = []

        _backtrack(0, [])

        return res
