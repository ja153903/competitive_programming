class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        prefix_sum = []

        for num in nums:
            if not prefix_sum:
                prefix_sum.append(num)
            else:
                prefix_sum.append(prefix_sum[-1] + num)

        for i in range(len(prefix_sum)):
            left = 0 if i == 0 else prefix_sum[i - 1]
            right = prefix_sum[-1] - prefix_sum[i]

            if left == right:
                return i

        return -1
