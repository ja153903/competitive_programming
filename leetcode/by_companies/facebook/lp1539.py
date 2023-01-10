class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        unique = set(arr)
        max_value = max(arr) + k

        for i in range(1, max_value + 1):
            if i not in unique:
                k -= 1
                if k == 0:
                    return i

        return 0

    def findKthPositive_follow_up(self, arr: list[int], k: int) -> int:
        # Can we do this with binary search?
        pass
