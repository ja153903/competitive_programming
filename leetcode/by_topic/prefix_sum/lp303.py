class NumArray:
    def __init__(self, nums: list[int]):
        self._prefix_sum = []

        for num in nums:
            if not self._prefix_sum:
                self._prefix_sum.append(num)
            else:
                self._prefix_sum.append(self._prefix_sum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self._prefix_sum[right]

        return self._prefix_sum[right] - self._prefix_sum[left - 1]
