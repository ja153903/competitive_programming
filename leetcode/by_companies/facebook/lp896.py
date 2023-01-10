def _is_monotonic_increasing(nums: list[int]) -> bool:
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            return False

    return True


def _is_monotonic_decreasing(nums: list[int]) -> bool:
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            return False

    return True


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        return _is_monotonic_increasing(nums) or _is_monotonic_decreasing(nums)
