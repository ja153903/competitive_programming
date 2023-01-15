from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elem = 0
        digit = 0

        for num in nums:
            elem += num

            cur = 0

            while num > 0:
                cur += num % 10
                num //= 10

            digit += cur

        return abs(elem - digit)
