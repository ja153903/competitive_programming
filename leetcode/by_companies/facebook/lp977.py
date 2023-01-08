class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)

        left, right = 0, len(nums) - 1

        idx = len(nums) - 1

        while left <= right:
            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2

            if left_sq > right_sq:
                result[idx] = left_sq
                left += 1
            else:
                result[idx] = right_sq
                right -= 1

            idx -= 1

        return result
