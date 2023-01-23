class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        current = left

        ranges.sort(key=lambda arr: arr[1])

        for interval in ranges:
            start, end = interval

            while start <= current <= end:
                current += 1

        return current > right
