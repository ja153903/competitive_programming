from collections import Counter
from math import comb


class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        """
        Ideal sliding window solution
        """
        res, i = 0, 0
        count = Counter()

        for num in nums:
            k -= count[num]
            count[num] += 1
            while k <= 0:
                count[nums[i]] -= 1
                k += count[nums[i]]
                i += 1
            res += i

        return res

    def get_number_of_pairs_in_window(self, counter) -> int:
        pairs_in_window = [comb(value, 2) for value in counter.values() if value > 0]
        return sum(value for value in pairs_in_window if value > 0)

    # This solution works but it TLEs because of the above method
    # to count the number of pairs
    def countGood_tle(self, nums: list[int], k: int) -> int:
        counter = Counter()

        res, start = 0, 0

        for i, num in enumerate(nums):
            counter[num] += 1

            # for each number in the window, this will give us the number of pairs we can construct
            # with the current count in the counter
            pairs_in_window = self.get_number_of_pairs_in_window(counter)

            while start < len(nums) and pairs_in_window >= k:
                if pairs_in_window >= k:
                    res += 1 + len(nums) - i - 1

                counter[nums[start]] -= 1
                start += 1

                pairs_in_window = self.get_number_of_pairs_in_window(counter)

        return res
