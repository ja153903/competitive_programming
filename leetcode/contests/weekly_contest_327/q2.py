import heapq
import math


class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        score = 0
        nums = [-num for num in nums]

        heapq.heapify(nums)

        while k > 0:
            top = -heapq.heappop(nums)
            score += top

            heapq.heappush(nums, -math.ceil(top / 3))
            k -= 1

        return score
